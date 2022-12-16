# Using Thread-Safe Queues

# Importing the necessary module and queue classes into the global namespace.
import argparse
from queue import LifoQueue, PriorityQueue, Queue

QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}
