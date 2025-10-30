class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []  # Lista de aristas (Edge)

class Edge:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def connect(self, origin_name, destination_name):
        origin = self.nodes[origin_name]
        destination = self.nodes[destination_name]
        edge = Edge(origin, destination)
        origin.edges.append(edge)