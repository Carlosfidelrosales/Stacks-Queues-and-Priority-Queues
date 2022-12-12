from collections import deque
from heapq import heappop, heappush
from itertools import count

# The most straightforward way of representing the arrival time in a priority queue is perhaps a monotonically increasing counter count().

class PriorityQueue:
    def __init__(catalog):
        catalog._elements = []
        catalog._counter = count()

    def enqueue_with_priority(catalog, priority, value):
        element = (-priority, next(catalog._counter), value)
        heappush(catalog._elements, element)

    def dequeue(catalog):
        return heappop(catalog._elements)[-1]



