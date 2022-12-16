# Priority Queues Python File

# Importing the required Python module for the priority queues
from collections import deque 
from itertools import count
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from typing import Any


# added mixin class
class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
            
            
# Class Inheritance from the queuesFIFO.py file (added the mixin class)
class Queue(IterableMixin):
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
    

class PriorityQueue(IterableMixin):
    # Init function for the Priority Queues 
    def __init__(self):
        self._elements = []
        self._counter = count()
        
        
    # adding an element into the Priority Queue.
    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    # Heappop for dequeueing elements from the Priority Queue.
    def dequeue(self):
        return heappop(self._elements)[-1]

#priority level: critical, important, and neutral.    
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

print("\nThese are the results:\n")
print(f"\t 1 -", messages.dequeue())
print(f"\t 2 -", messages.dequeue())
print(f"\t 3 -", messages.dequeue())
print(f"\t 4 -", messages.dequeue())

@dataclass(order=True)
class Element:
    priority: float
    count: int
    value: Any

class MutableMinHeap(IterableMixin):
    def __init__(self):
        super().__init__()
        self._elements_by_value = {}
        self._elements = []
        self._counter = count()

    def __setitem__(self, unique_value, priority):
        if unique_value in self._elements_by_value:
            self._elements_by_value[unique_value].priority = priority
            heapify(self._elements)
        else:
            element = Element(priority, next(self._counter), unique_value)
            self._elements_by_value[unique_value] = element
            heappush(self._elements, element)

    def __getitem__(self, unique_value):
        return self._elements_by_value[unique_value].priority

    def dequeue(self):
        return heappop(self._elements).value