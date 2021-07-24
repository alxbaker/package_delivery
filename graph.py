# The Graph class is used to store adjacent addresses and the distances between them
class Graph:
    def __init__(self):
        # The adjacency_list dictionary contains addresses (vertexes) adjacent to a specific address
        self.adjacency_list = {}
        # The edge_weights dictionary contains distances between adjacent addresses (vertex)
        self.edge_weights = {}

    # This function adds a new vertex to the list
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    # This function adds a directed edge, or distance, between two vertexes
    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    # This function applies the add_directed_edge function twice
    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    # This function retrieves the distance between two vertexes
    def get_directed_edge(self, from_vertex, to_vertex):
        return self.edge_weights[(from_vertex, to_vertex)]
