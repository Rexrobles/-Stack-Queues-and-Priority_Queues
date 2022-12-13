# Priority Queues Python File

# Importing the required Python module for the priority queues
from collections import deque 
from heapq import heappop, heappush

class PriorityQueue:
    # Init function for the Priority Queues 
    def __init__(self):
        self.elements = []
        
    # adding an element into the Priority Queue.
    def enqueue_with_priority(self, priority, value):
        heappush(self.elements, (priority, value))

    # Heappop for dequeueing elements from the Priority Queue.
    def dequeue(self):
        return heappop(self.elements)
    
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

messages.dequeue()