class Graph(object):
    # if no dictionary is given, an empty dictionary will be used
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}

        """
        names with a leading underscore are to indicate that the attrubute or
        method is intended to be private. from M import * does not import objects
        whose name starts with an underscore.

        Any identifier of the form __spam with at least two leading underscores,
        at most one trailing underscore is textually replaced with _classname__spam
        so it can be used to define class-private instances and class variables

        """
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []


g = {'a': ['d'],
     'b': ['c'],
     'c': ['b', 'c', 'd', 'e'],
     'd': ['a', 'c'],
     'e': ['c'],
     'f': []
     }

graph = Graph(g)
print(f'vertices of graph: {graph.vertices()}')
