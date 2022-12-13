from Graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# print("Prints the nodes of the selected " + str(nodes["oxford"]))
# print(graph)


#list of places/cities near oxford
print("Places that can be found near Oxford are: \n")
for neighbor in graph.neighbors(nodes["oxford"]):
    print(neighbor.name)

