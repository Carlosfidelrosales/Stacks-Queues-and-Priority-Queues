from collections import deque
from heapq import heappop, heappush

# Enqueue_with_priority() method takes two arguments, a priority and a corresponding value, which it then wraps in a tuple and pushes onto the heap using the heapq module. 

class PriorityQueue:
    def __init__(catalog):
        catalog._elements = []

    def enqueue_with_priority(catalog, priority, value):
        heappush(catalog._elements, (priority, value))

    def dequeue(catalog):
        return heappop(catalog._elements)

# Defined three priority levels: critical, important, and neutral. Next, instantiated a priority queue and used it to enqueue a few messages with those priorities. However, instead of dequeuing the message with the highest priority, it got a tuple corresponding to the message with the lowest priority.

CRITICAL = 1
IMPORTANT = 2
NEUTRAL = 3

alert = PriorityQueue()
alert.enqueue_with_priority(IMPORTANT, "Flesh Wound Injury")
alert.enqueue_with_priority(NEUTRAL, "Minor Injury")
alert.enqueue_with_priority(CRITICAL, "Acute Danger")
alert.enqueue_with_priority(IMPORTANT, "Dislocation on the bones")

# print(alert.dequeue())
# print("------------------------------------------------------------\n")

class PriorityQueue:
    def __init__(catalog):
        catalog._elements = []

    def enqueue_with_priority(catalog, priority, value):
        heappush(catalog._elements, (-priority, value))

    def dequeue(catalog):
        return heappop(catalog._elements)[1]

# push critical messages ahead of important and neutral ones
print(alert.dequeue())
print(alert.dequeue())
print(alert.dequeue())
print(alert.dequeue())



