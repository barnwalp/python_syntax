class Graph(object):
    # if no dictionary is given, an empty dictionary will be used
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}

        """
        names with a leading underscore are to indicate that the attrubute or
        method is intended to be private. from M import * does not import
        objects whose name starts with an underscore.

        Any identifier of the form __spam with at least two leading
        underscores, at most one trailing underscore is textually replaced
        with _classname__spam so it can be used to define class-private
        instances and class variables.

        """
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def remove_vertex(self, vertex):
        neighbors = self.__graph_dict[vertex]
        del self.__graph_dict[vertex]
        print(neighbors)
        for vertices in neighbors:
            print(f'neighbour vertices are: {self.__graph_dict[vertices]}')

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        # print(f'{vertex1} --> {vertex2}')
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            # since vertex1 is not in the graph, it should be added first
            self.add_vertex(vertex1)
            self.__graph_dict[vertex1].append(vertex2)
            # print(f'{vertex1} --> {self.__graph_dict[vertex1]}')

    def __generate_edges(self):
        edges = []
        for vertex, value in self.__graph_dict.items():
            for neighbour in value:
                # {} will ensure that orientation of edges
                # does not matter
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def adjacent_edge(self, vertex1, vertex2):
        if {vertex1, vertex2} in self.__generate_edges():
            return True
        else:
            return False

    def neighbour_vertices(self, vertex):
        return self.__graph_dict[vertex]

    def __repr__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def __str__(self):
        output = "graph is: \n"
        for key, value in self.__graph_dict.items():
            # print(f'{key} --> {value}')
            output += str(key) + ' --> ' + str(value) + "\n"
        return output


if __name__ == "__main__":
    g = {'a': ['d'],
         'b': ['c'],
         'c': ['b', 'c', 'd', 'e'],
         'd': ['a', 'c'],
         'e': ['c'],
         'f': []
         }

    graph = Graph(g)
    # print(f'vertices of graph: {graph.vertices()}')
    # print(f'edges of graph: {graph.edges()}')

    print(f'\nAdd Vertex: "z"')
    graph.add_vertex("z")

    print(f'\n{graph}')

    print(f'\nadd an edge: (a,z)')
    graph.add_edge({'a', 'z'})

    print(f'\n{graph}')

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x", "y"})

    # print(f'\n{graph}')
    #
    # print(f'Is vertex a adjacent to b: {graph.adjacent_edge("a", "b")}')
    # print(f'Is vertex c adjacent to d: {graph.adjacent_edge("c", "d")}')

    print(f'Neighbors vertices of "a" are: {graph.neighbour_vertices("a")}')

    print(f'\n{graph}')
    graph.remove_vertex("a")
    print(f'\n{graph}')