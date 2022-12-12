# LIFO Queues Python File
# Building a Queue Data Type

# Importing the Queues module 
from collections import deque

# Class variables for the implementation of enqueue and dequeue.
class Queue:
    def __init__(self):
        self._elements = deque() 