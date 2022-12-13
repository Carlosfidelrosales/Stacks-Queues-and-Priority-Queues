import networkx as nx
from Graph import City, load_graph

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)

#for loop that will scan if a city has been granted to a place from 20th century.
# print("\nFinding the declared city stating from 20th Century.\n\n")
# for node in nx.bfs_tree(graph, nodes["oxford"]):
#     print(">>", node.name, node.year)
#     if is_twentieth_century(node.year):
#         print("\n\nFound:", node.name, node.year)
#         break
# else:
#     print("Not found")

#for loop that will scan if a city is from 20th century and it has the highest latitude among all the others.
print("\nFinding the City that is from 20th Century and it has highest value of latitude.\n\n")
def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude, reverse=True))

for node in nx.bfs_tree(graph, nodes["oxford"], sort_neighbors=order):
    print(">>", node.name, node.year, node.latitude)
    if is_twentieth_century(node.year):
        print("\n\nFound:", node.name, node.year, node.latitude)
        break
else:
    print("Not found")