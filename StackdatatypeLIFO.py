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

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()


print("\nList of Kitchen Utensils when washing the dishes. Using LAST IN FIRST OUT QUEUE. \n")
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


print("\nList of Kitchen Utensils when washing the dishes. Using LAST IN FIRST OUT QUEUE. \n")
print(LIFO.pop())
print(LIFO.pop())
print(LIFO.pop())
print(LIFO.pop())
print(LIFO.pop())

    