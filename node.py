from message import Message
from minimal_spanning_tree_builder import extract_minimal_spanning_tree


class Node:
    def advertise(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)

    def has_neighbor(self, node):
        return node in self.neighbors

    def __repr__(self):
        return str(self.id)

    def print(self):
        print(f"Node{self.id}: ", end="")
        for node in self.neighbors:
            print(f"{str(node)}, ", end="")
        print()

    def __init__(self, id, network_interface):
        self.neighbors = []
        self.id = id
        self.network_interface = network_interface
        self.minimal_spanning_tree = None
        self.messages = []

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __hash__(self):
        # ID is unique for nodes created by network.create_node
        # ==> __hash__ is collision free and faster than calling super().hash()
        return self.id

    def send_message(self, message):
        path_tree = message.header["path_tree"]
        next_hop = path_tree.data
        if self.has_neighbor(next_hop):
            self.network_interface.send(self, next_hop, message)
        else:
            print(f"Warning: {str(self)} tried sending a message to a node not its neighbor: {next_hop}")

    def receive(self, message):
        self.messages.append(message.body)
        path_tree = message.header["path_tree"]
        for child_tree in path_tree.children:
            new_message = message.clone()
            new_message.header["path_tree"] = child_tree
            self.send_message(new_message)
        message = None

    def invoke_broadcast(self, content):
        if self.minimal_spanning_tree is None:
            self.minimal_spanning_tree = extract_minimal_spanning_tree(self)
        message = Message(self.minimal_spanning_tree, content)
        self.receive(message) # Call receive to drop "message zero" into the root nodes in port

        network = self.network_interface.network
        # Simulate network activity
        while len(network.global_message_buffer) > 0:
            network.network_tick()
