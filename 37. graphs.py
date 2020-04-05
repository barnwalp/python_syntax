# function to generate all edges
def generate_edges(graph):
    edge_collection = []
    # only key will be returned as vertex
    for vertex in graph:
        # get value from the dictionary using vertex key
        for edge in graph[vertex]:
            # vertex, edge is under () so that it adds as a tuple
            edge_collection.append((vertex, edge))
    return edge_collection


def find_isolated_nodes(graph):
    isolated_nodes = []
    for vertex in graph:
        if not graph[vertex]:
            isolated_nodes.append(vertex)
    return isolated_nodes


# representation of graph using dictionary
graph = {
    "a": ["c"],
    "b": ["c", "e"],
    "c": ["a", "b", "d", "e"],
    "d": ["c"],
    "e": ["c", "b"],
    "f": [],
    "g": []
}

print("Edge lists are: " + str(generate_edges(graph)))
print("Isolated nodes are: " + str(find_isolated_nodes(graph)))
