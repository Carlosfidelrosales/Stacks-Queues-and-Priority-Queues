import networkx as nx
from Graph import (
    City,
    load_graph,
    depth_first_traverse,
    depth_first_search as dfs
)


# def is_twentieth_century(year):
#     return year and 1901 <= year <= 2000

# nodes, graph = load_graph("roadmap.dot", City.from_dict)
# for node in nx.dfs_tree(graph, nodes["oxford"]):
#     print("->", node.name)
#     if is_twentieth_century(node.year):
#         print("\n\nFound:", node.name, node.year)
#         break
#     else:
#         print("Not found")


def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
city = dfs(graph, nodes["edinburgh"], is_twentieth_century)
city.name


for city in depth_first_traverse(graph, nodes["edinburgh"]):
    print(city.name)