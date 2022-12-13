# Priority Queues Python File

# The purpose of a heap is not so much to sort elements as it is to store 
# them in a certain relationship to allow for fast lookup.
# importing heappush
from heapq import heappush
# importing heappop
from heapq import heappop

fruit = [] # empty list fruit variable

heappush(fruit, "strawberry")
heappush(fruit, "mango")
heappush(fruit, "pineapple")
heappush(fruit, "orange")
heappush(fruit, "apple")

# when using heappop function, you’ll always get the first one
# And the remaining variable might shuffle a bit.
print(heappop(fruit)) # print function for the output of the program
print("\nThese are the remaining elements:\n\t",fruit)