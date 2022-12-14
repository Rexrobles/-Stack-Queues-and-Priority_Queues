# Creating a custom data type for conveniently viewing graphs in cities and road maps.

from typing import NamedTuple
import networkx as nx

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

# This function import the file for node object    
def load_graph(filename, node_factory):
    graph = nx.nx_agraph.read_dot(filename)
    nodes = {
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data = True)
    }