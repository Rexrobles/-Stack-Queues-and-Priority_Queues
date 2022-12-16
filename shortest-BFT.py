# importing networkx to reveal all the shortest paths between two cities, which will have the same minimal length
import networkx as nx
from graph import City, load_graph
# From graph.py import file path
from graph import shortest_path
from graph import connected

nodes, graph = load_graph("roadmap.dot", City.from_dict)

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path))
    
print(" → ".join(city.name for city in shortest_path(graph, city1, city2)), "\n")

def by_latitude(city):
    return -city.latitude

print(" → ".join(
    city.name
    for city in shortest_path(graph, city1, city2, by_latitude)), "\n")

print(connected(graph, nodes["belfast"], nodes["glasgow"]), "\n")

print(connected(graph, nodes["belfast"], nodes["derry"]))
