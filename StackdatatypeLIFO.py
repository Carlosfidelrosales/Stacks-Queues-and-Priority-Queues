from collections import deque
from heapq import heappush, heappop, heapify
from itertools import count
from dataclasses import dataclass
from itertools import count
from typing import Any

class IterableMixin:
    def __len__(catalog):
        return len(catalog._elements)

    def __iter__(catalog):
        while len(catalog) > 0:
            yield catalog.dequeue()

class Queue(IterableMixin):
    def __init__(catalog, *elements):
        catalog._elements = deque(elements)

    # def __len__(catalog):
    #     return len(catalog._elements)

    # def __iter__(catalog):
    #     while len(catalog) > 0:
    #         yield catalog.dequeue()

    def enqueue(catalog, element):
        catalog._elements.append(element)

    def dequeue(catalog):
        return catalog._elements.popleft()

class Stack(Queue):
    def dequeue(catalog):
        return catalog._elements.pop()

@dataclass(order=True)
class Element:
    priority: float
    count : int
    value : Any
class MutableMinHeap(IterableMixin):
    def __init__(catalog):
        super().__init__()
        catalog._elements_by_value = {}
        catalog._elements = []
        catalog._counter = count()

    def __setitem__(catalog, unique_value, priority):
        if unique_value in catalog._elements_by_value:
            catalog._elements_by_value[unique_value].priority = priority
            heapify(catalog._elements)
        else:
            element = Element(priority, next(catalog._counter), unique_value)
            catalog._elements_by_value[unique_value] = element
            heappush(catalog._elements, element)

    def __getitem__(catalog, unique_value):
        return catalog._elements_by_value[unique_value].priority

    def dequeue(catalog):
        return heappop(catalog._elements).value



print("\n(1) List of Kitchen Utensils when washing the dishes. Using LAST IN FIRST OUT QUEUE. \n")
LIFO = Stack("- Plate\n\n", "- Spoon", "- Fork", "- Glass", "- Saucer")

for element in LIFO:
    print(element)


# This can be also a way on printing the items in reverse order
LIFO = []

LIFO.append("- Plate")
LIFO.append("- Spoon")
LIFO.append("- Fork")
LIFO.append("- Glass")
LIFO.append("- Saucer")


# print("\n(2) List of Kitchen Utensils when washing the dishes. Using LAST IN FIRST OUT QUEUE. \n")
# print(LIFO.pop())
# print(LIFO.pop())
# print(LIFO.pop())
# print(LIFO.pop())
# print(LIFO.pop())