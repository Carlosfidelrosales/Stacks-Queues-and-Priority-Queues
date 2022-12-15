import argparse
import asyncio
import sys
from collections import Counter
from typing import NamedTuple
from urllib.parse import urljoin
import aiohttp
from bs4 import BeautifulSoup


class Job(NamedTuple):
    url: str
    depth: int = 1

    def __lt__(self, other):
        if isinstance(other, Job):
            return len(self.url) < len(other.url)

async def main(args):
    session = aiohttp.ClientSession()
    try:
        links = Counter()
        queue = asyncio.Queue()
        # queue = asyncio.LifoQueue()
        # queue = asyncio.PriorityQueue()
        tasks = [
            asyncio.create_task(
                worker(
                    f"Worker-{i + 1}",
                    session,
                    queue,
                    links,
                    args.max_depth,
                )
            )
            for i in range(args.num_workers)
        ]

        await queue.put(Job(args.url))
        await queue.join()

        for task in tasks:
            task.cancel()

        await asyncio.gather(*tasks, return_exceptions=True)

        display(links)
    finally:
        await session.close()


async def worker(worker_id, session, queue, links, max_depth):
    print(f"[{worker_id} starting]", file=sys.stderr)
    while True:
        url, depth = await queue.get()
        links[url] += 1
        try:
            if depth <= max_depth:
                print(f"[{worker_id} {depth=} {url=}]", file=sys.stderr)
                if html := await fetch_html(session, url):
                    for link_url in parse_links(url, html):
                        await queue.put(Job(link_url, depth + 1))
        except aiohttp.ClientError:
            print(f"[{worker_id} failed at {url=}]", file=sys.stderr)
        finally:
            queue.task_done()
