# This program will load the graph from a sample DOT file and store the result in two variables.
from graph import City, load_graph

# The load_graph inherits parameters from the graph.py file.
nodes, graph = load_graph("roadmap.dot", City.from_dict)
print(f"\n{nodes['chester']}")
print(f"\n{graph}\n")
    

# The method neighbors() identifies the neighboring cities
for neighbor in graph.neighbors(nodes["chester"]):
    print(neighbor.name)
print("")

# in this program output, the map display a digits that represent the distance
for neighbor, weights in graph[nodes["chester"]].items():
    print(weights["distance"], neighbor.name)
print("")

# Defined a function that returns a list of neighbors and their weights

def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

# This reveals the neighboring nodes without the possible weights of the connecting edges, such as distances or the estimated travel times
for neighbor, weights in sort_by(graph[nodes["chester"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")