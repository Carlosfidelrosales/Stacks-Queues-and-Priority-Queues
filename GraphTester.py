from Graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

print("Prints the nodes of the selected " + str(nodes["oxford"]))
print(graph)


#list of places/cities near oxford
print("Places that can be found near Oxford are: \n")
for neighbor in graph.neighbors(nodes["oxford"]):
    print(neighbor.name)

#list of places/cities near oxford and its distance
for neighbor, interval in graph[nodes["oxford"]].items():
    print(interval["distance"], neighbor.name)


#sorted the nearest and farthest place near oxford using the sort_by and by_distance def functions.
def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(interval):
    return float(interval["distance"])

for neighbor, interval in sort_by(graph[nodes["oxford"]], by_distance):
    print(f"{interval['distance']:>3} miles, {neighbor.name}")