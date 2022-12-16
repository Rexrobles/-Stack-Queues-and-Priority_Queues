# Depth-First Search Using a LIFO Queue

import networkx as nx
from graph import City, load_graph

# This def function argument will returning a value that are being considered between the 20th century.
def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
for node in nx.dfs_tree(graph, nodes["edinburgh"]):
    print("📌", node.name)
    if is_twentieth_century(node.year):
        print("\n✔️  Found:", node.name, node.year,"\n")
        break
else:
    print("\n 🛑 Not found \n")