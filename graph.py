# Creating a custom data type for conveniently viewing graphs in cities and road maps.

from typing import NamedTuple

class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float