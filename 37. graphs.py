# function to generate all edges
def generate_edges(graph):
    edge_collection = []
    for vertex in graph:
        print("vertex is: " + str(vertex))
        # get value from the dictionary using vertex key
        for edge in graph[vertex]:
            print("Edge is: " + str(edge))
            # vertex, edge is under () so that it adds as a tuple
            edge_collection.append((vertex, edge))
    return edge_collection


# representation of graph using dictionary
graph = {
    "a": ["c"],
    "b": ["c", "e"],
    "c": ["a", "b", "d", "e"],
    "d": ["c"],
    "e": ["c", "b"],
    "f": [],
}

print(generate_edges(graph))
