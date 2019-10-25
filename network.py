from network_interface import NetworkInterface
from node import Node


class Network:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.total_messages = 0

    def connect(self, nodeA, nodeB):
        self.edges.append((nodeA, nodeB))
        self.edges.append((nodeB, nodeA))
        nodeA.advertise(nodeB)
        nodeB.advertise(nodeA)

    def create_new_node(self):
        node = Node(len(self.nodes), NetworkInterface(self))
        self.nodes.append(node)
        return node

    def get_size(self):
        return len(self.nodes)

    def print(self):
        for node in self.nodes:
            node.print()
