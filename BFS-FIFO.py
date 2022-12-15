# Breadth-First Search Using a FIFO Queue
# it look for a node that satisfies a particular condition by exploring the graph in concentric layers or levels.
# Using chosen source node unless the graph is a tree data structure, in which case you typically start at the root node of that tree. 

import networkx as nx
from graph import City, load_graph

# This def function argument will returning a value that are being considered between the 20th century.
def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
for node in nx.bfs_tree(graph, nodes["edinburgh"]):
    print("📌", node.name)
    if is_twentieth_century(node.year):
        print("\n✔️  Found:", node.name, node.year,"\n")
        break
else:
    print("\n 🛑 Not found \n")
    
def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude, reverse=True))

for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
    print("📌", node.name)
    if is_twentieth_century(node.year):
        print("\n✔️  Found:", node.name, node.year,"\n")
        break
else:
    print("\n 🛑 Not found \n")