
from node import Node
from network_interface import NetworkInterface
from minimal_spanning_tree_builder import build_minimal_spanning_tree

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
        node = Node(len(self.nodes))
        self.nodes.append(node)
        return node

    def inject_network_interfaces(self):
        for node in self.nodes:
            msp = build_minimal_spanning_tree(self, node)
            network_interface = NetworkInterface(self, msp)
            node.network_interface = network_interface

    def get_size(self):
        return len(self.nodes)

    def print(self):
        for node in self.nodes:
            node.print()