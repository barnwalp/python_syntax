# function to generate all edges
def generate_edges(graph):
    edge_collection = []
    # key and value of the dictionary will be returned
    for key, value in graph.items():
        # get individual edges from the value list
        for edge in value:
            # key, value is under () so that it adds as a tuple
            edge_collection.append((key, edge))
    return edge_collection


def find_isolated_nodes(graph):
    isolated_nodes = []
    for key, value in graph.items():
        if not graph[key]:
            isolated_nodes.append(key)
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

print(f'Edge lists are:  {generate_edges(graph)}')
print(f'Isolated nodes are: {find_isolated_nodes(graph)}')
