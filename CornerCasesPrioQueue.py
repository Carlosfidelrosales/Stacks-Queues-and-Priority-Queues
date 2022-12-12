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

CRITICAL = 3
IMPORTANT = 2 
NEUTRAL = 1 
    
alert = PriorityQueue()
alert.enqueue_with_priority(IMPORTANT, "Flesh Wound Injury")
alert.enqueue_with_priority(NEUTRAL, "Minor Injury")
alert.enqueue_with_priority(CRITICAL, "Acute Danger")
alert.enqueue_with_priority(IMPORTANT, "Dislocation on the bones")

print("This is the list of priorities that will be needed for the hospitals.")
print("\nFirst is " + alert.dequeue())
print("Second is " + alert.dequeue())
print("Third is " + alert.dequeue())
print("Fourth is " + alert.dequeue())
