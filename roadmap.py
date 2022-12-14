# Creating Road Map of the Unkited Kingdom using Python Program

# importing networkx
import networkx as nx 

# try print one map string from roadmap.dot if it will correspond to the dictionary keyvalue
graph = nx.nx_agraph.read_dot("roadmap.dot")
print(f"\n{graph}")
print(f"{graph.nodes['chester']}\n")