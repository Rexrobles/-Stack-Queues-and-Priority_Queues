# Handling Corner Cases (HCC) Priority Queues Python File

# Imported data class module 
from dataclasses import dataclass

# class to represent messages in the queue.
@dataclass
class message:
    event: str