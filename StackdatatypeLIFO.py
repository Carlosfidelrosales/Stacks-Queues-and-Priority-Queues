from collections import deque

class Queue:
    def __init__(catalog, *elements):
        catalog._elements = deque(elements)

    def __len__(catalog):
        return len(catalog._elements)

    def __iter__(catalog):
        while len(catalog) > 0:
            yield catalog.dequeue()

    def enqueue(catalog, element):
        catalog._elements.append(element)

    def dequeue(catalog):
        return catalog._elements.popleft()


    