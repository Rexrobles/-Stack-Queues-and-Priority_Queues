# LIFO Queues Python File
# Building a Queue Data Type

# Importing the Queues module 
from collections import deque

# Class variables for the implementation of enqueue and dequeue.
class Queue:
    def __init__(self):
        self._elements = deque() # The leading underscore in the attribute’s name indicates an internal bit of implementation, which only the class should access and modify.

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()