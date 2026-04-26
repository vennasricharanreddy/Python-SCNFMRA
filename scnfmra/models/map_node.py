class MapNode:
    def __init__(self, node_id, coordinates):
        self.node_id = node_id
        self.coordinates = coordinates
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)