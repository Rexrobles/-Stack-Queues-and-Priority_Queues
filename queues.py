# LIFO Queues Python File
# Building a Queue Data Type

# Importing the Queues module 
from collections import deque
# importing queues for testing FIFO queue.
from queues import Queue

# Class variables for the implementation of enqueue and dequeue.
class Queue:
    def __init__(self):
        self.elements = deque() # The leading underscore in the attribute’s name indicates an internal bit of implementation, which only the class should access and modify.

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        return self.elements.popleft()