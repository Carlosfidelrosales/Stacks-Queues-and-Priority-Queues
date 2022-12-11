from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

fifo = Queue()
fifo.enqueue("First in Line")
fifo.enqueue("Second in Line")
fifo.enqueue("Third in Line")



print(fifo.dequeue())

print(fifo.dequeue())

print(fifo.dequeue())
