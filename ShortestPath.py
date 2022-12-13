import networkx as nx
from Graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

city1 = nodes["oxford"]
city2 = nodes["preston"]

for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path))