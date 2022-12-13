# Priority Queues Python File

# Importing the required Python module for the priority queues
from collections import deque 
from heapq import heappop, heappush
from queues import PriorityQueue

class PriorityQueue:
    # Init function for the Priority Queues 
    def __init__(self):
        self._elements = []
        
    # adding an element into the Priority Queue.
    def enqueue_with_priority(self, priority, value):
        heappush(self.elements, (priority, value))

    # Heappop for dequeueing elements from the Priority Queue.
    def dequeue(self):
        return heappop(self.elements)