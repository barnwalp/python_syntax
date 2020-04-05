class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}

        """
        __graph_dict is textually replaced with _Graph__graph_dict
        where Graph is the current class. this is intended to give
        classes and easy way to define private instance variables &
        methods
        """
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []