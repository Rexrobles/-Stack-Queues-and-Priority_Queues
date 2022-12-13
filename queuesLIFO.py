# LIFO Queues Python File
# Building a Queue Data Type

# Importing the Queues module 
from collections import deque
# importing queues for testing FIFO queue.
# from queues import Queue

# Class variables for the implementation of enqueue and dequeue.
class Queue:
    def __init__(self, * element):
        self._elements = deque() # The leading underscore in the attribute’s name indicates an internal bit of implementation, which only the class should access and modify.

    def __len__(self):
        return len(self._elements)
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
    
    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
    

# function for testing FIFO queue
fifo = Queue()
fifo.enqueue('First')
fifo.enqueue('Second')
fifo.enqueue('Third')

print(f"\n{len(fifo)} - before to iteration (elements have not yet been dequeued)\n")

for element in fifo:
    print(element) # adding print function to print fifo queue 
    
print(f"\n{len(fifo)} - after iteration (element have been dequeued)")
