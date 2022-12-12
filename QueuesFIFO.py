from collections import deque

class IterableMixin:
    def __len__(catalog):
        return len(catalog._elements)

    def __iter__(catalog):
        while len(catalog) > 0:
            yield catalog.dequeue()

class Queue (IterableMixin):
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

FIFO = Queue("First in Line", "Second in Line", "Third in Line")
print(len(FIFO))


for element in FIFO:
    print(element)

print(len(FIFO))   


