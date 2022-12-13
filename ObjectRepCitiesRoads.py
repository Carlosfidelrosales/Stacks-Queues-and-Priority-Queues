# import networkx as nx
# print(nx.nx_agraph.read_dot("roadmap.dot"))

#oxford string maps
import networkx as nx
graph = nx.nx_agraph.read_dot("roadmap.dot")
print(graph.nodes["oxford"])