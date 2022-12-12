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
        return len(self.__elements)
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
    
    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
    

# function for testing FIFO queue
fifo = Queue()
fifo.enqueue('1st')
fifo.enqueue('2nd')
fifo.enqueue('3rd')

print(fifo.dequeue())