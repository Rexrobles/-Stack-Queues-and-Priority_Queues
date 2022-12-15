# Creating a custom data type for conveniently viewing graphs in cities and road maps.

from typing import NamedTuple
import networkx as nx
from queuesFIFO import Queue

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
    return nodes, nx.Graph(
        (nodes[name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges(data=True)
    )
    
def breadth_first_traverse(graph, source):
    queue = Queue(source)
    visited = {source}
    while queue:
        yield (node := queue.dequeue())
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

def breadth_first_search(graph, source, predicate):
    for node in breadth_first_traverse(graph, source):
        if predicate(node):
            return node