from Graph import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

print("Prints the nodes of the selected " + str(nodes["oxford"]))
print(graph)
