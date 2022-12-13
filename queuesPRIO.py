# Priority Queues Python File

# Importing the required Python module for the priority queues
from collections import deque 
from heapq import heappop, heappush

class PriorityQueue:
    # Init function for the Priority Queues 
    def __init__(self):
        self._elements = []