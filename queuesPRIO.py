# Priority Queues Python File

# The purpose of a heap is not so much to sort elements as it is to store 
# them in a certain relationship to allow for fast lookup.
# importing heappush
from heapq import heappush

fruit = [] # empty list fruit variable

heappush(fruit, "strawberry")
heappush(fruit, "mango")
heappush(fruit, "pineapple")
heappush(fruit, "orange")
heappush(fruit, "apple")

print("\nElements being sorted as:\n\n", fruit)