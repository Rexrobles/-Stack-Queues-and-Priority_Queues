# Creating a custom data type for conveniently viewing graphs in cities and road maps.

from typing import NamedTuple

# Adding data class for future use, such as the networkx need.
class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float
    
    # extending a named tuple to ensure that your node objects are hashable, which is required by networkx.
    @classmethod
    def from_dict(cls, attributes):
        return cls(
            name = attributes["xlabel"],
            country = attributes["country"],
            year = int(attributes["year"]) or None,
            latitude = float(attributes["latitude"]),
            longitude = float(attributes["longitude"]),
        )