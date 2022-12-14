import networkx as nx
from Graph import (
    City,
    load_graph,
    breadth_first_traverse,
    breadth_first_search as bfs,
)


def twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# #for loop that will scan if a city has been granted to a place from 20th century.
# print("\n>> Finding the declared city stating from 20th Century.\n\n")
# for node in nx.bfs_tree(graph, nodes["oxford"]):
#     print(">>", node.name)
#     if twentieth_century(node.year):
#         print("\n\nFound:", node.name, node.year)
#         break
#     else:
#         print("Not found")

# #for loop that will scan if a city is from 20th century and it has the highest latitude among all the others.
# print("\n// Finding the City that is from 20th Century and it has highest value of latitude.\n\n")
# def order(neighbors):
#     def by_latitude(city):
#         return city.latitude
#     return iter(sorted(neighbors, key=by_latitude, reverse=True))

# for node in nx.bfs_tree(graph, nodes["oxford"], order):
#     print("//", node.name)
#     if twentieth_century(node.year):
#         print("\n\nFound:", node.name, node.year, node.latitude)
#         break
#     else:
#         print("Not found")

    
from Graph import (
    City,
    load_graph,
    breadth_first_traverse,
    breadth_first_search as bfs,
)

def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
city = bfs(graph, nodes["edinburgh"], is_twentieth_century)
city.name


for city in breadth_first_traverse(graph, nodes["edinburgh"]):
    print(city.name)
