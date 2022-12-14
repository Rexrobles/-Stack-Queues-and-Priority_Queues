# Handling Corner Cases (HCC) Priority Queues Python File

# Imported data class module 
from dataclasses import dataclass

# class to represent messages in the queue.
@dataclass
class message:
    event: str
    
# class variable for implementation that have same a same priority
wipers = message("Windshield wipers turned on")
hazard_lights = message("Hazard lights turned on")

wipers < hazard_lights
