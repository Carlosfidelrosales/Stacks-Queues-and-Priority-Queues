from collections import deque
from heapq import heappop, heappush

class PriorityQueue:
    def __init__(catalog):
        catalog._elements = []

    def enqueue_with_priority(catalog, priority, value):
        heappush(catalog._elements, (priority, value))

    def dequeue(catalog):
        return heappop(catalog._elements)



