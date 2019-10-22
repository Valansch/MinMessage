class Path:
    def __init__(self, nodeA, nodeB):
        self.edges = []
    
    def append(self, nodeA, nodeB):
        last_node = self.edges[len(self.edges) - 1]
        if 