from network_interface import NetworkInterface
from node import Node


class Network:
    """
        An abstraction of a simulated network containing all nodes and edges.
    """

    def __init__(self):
        """
            Constructs an empty network

            Returns
            -------
                network: Network
        """
        self.nodes = []
        self.edges = []
        self.total_messages = 0
        # "Magic" global message buffer, that is used to simulate every message floating through the network
        self.global_message_buffer = []

    def connect(self, nodeA, nodeB):
        """
            Connects two nodes and advertises the nodes to each other

            Parameters
            ----------
                nodeA: Node
                nodeB: Node
        """
        if nodeA not in nodeB.neighbors:
            self.edges.append((nodeA, nodeB))
            self.edges.append((nodeB, nodeA))
            nodeA.advertise(nodeB)
            nodeB.advertise(nodeA)

    def create_new_node(self):
        """
            Creates a unique disjointed node and adds to the network

            Returns
            -------
                node: Node
                    The newly created node
        """
        node = Node(len(self.nodes), NetworkInterface(self))
        self.nodes.append(node)
        return node

    def get_size(self):
        return len(self.nodes)

    def start(self):
        """
            Simulates network activity until no more messages are to be send
        """

        target = None
        message = None
        while len(self.global_message_buffer) > 0:
            try:
                target, message = self.global_message_buffer.pop()
            except IndexError:
                break

            self.total_messages += 1
            target.receive(message)
