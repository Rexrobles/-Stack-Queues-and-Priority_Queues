# This program will load the graph from a sample DOT file and store the result in two variables.
from graph import City, load_graph

# The load_graph inherits parameters from the graph.py file.
nodes, graph = load_graph("roadmap.dot", City.from_dict)
print(f"\n{nodes['chester']}")
print(f"\n{graph}\n")
    
def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

for neighbor, weights in sort_by(graph[nodes["chester"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")