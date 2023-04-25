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
        # to ensure that deleted vertex is left out from further deletion
        if vertex in neighbors:
            neighbors.remove(vertex)
        print(f'adjacent vertiecs to {vertex} are: {neighbors}')
        print(f'graph after deleting vertex {vertex} is: {self}')
        for vertices in neighbors:
            for value in self.__graph_dict[vertices]:
                if value is vertex:
                    self.__graph_dict[vertices].remove(vertex)
            # print(f'neighbour vertices are: {self.__graph_dict[vertices]}')

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        # print(f'{vertex1} --> {vertex2}')
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
            self.__graph_dict[vertex2].append(vertex1)
        else:
            # since vertex1 is not in the graph, it should be added first
            self.add_vertex(vertex1)
            self.__graph_dict[vertex1].append(vertex2)
            self.add_vertex(vertex2)
            self.__graph_dict[vertex2].append(vertex1)
            # print(f'{vertex1} --> {self.__graph_dict[vertex1]}')

    def remove_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex2 in self.__graph_dict[vertex1]:
            self.__graph_dict[vertex1].remove(vertex2)
        if vertex1 in self.__graph_dict[vertex2]:
            self.__graph_dict[vertex2].remove(vertex1)

    def __generate_edges(self):
        edges = []
        print('---------------------')
        for vertex, value in self.__graph_dict.items():
            print(f'{vertex} --> {value}')
            for neighbour in value:
                print(f'{neighbour} --> {vertex}')
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

    # print(f'Neighbors vertices of "a" are: {graph.neighbour_vertices("a")}')

    print(f'\n{graph}')
    graph.remove_vertex("a")
    print(f'\ngraph after removing vertex a is: \n{graph}')

    print('\nremoving edge (b, c)')
    graph.remove_edge({'b', 'c'})
    print(f'\n{graph}')

    print(graph.edges())
