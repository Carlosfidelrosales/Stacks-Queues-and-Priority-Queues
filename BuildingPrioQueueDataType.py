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

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

alert = PriorityQueue()
alert.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
alert.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
alert.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
alert.enqueue_with_priority(CRITICAL, "Hazard lights turned on")

print(alert.dequeue())



