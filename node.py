from message import Message


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

    def __init__(self, id):
        self.neighbors = []
        self.id = id
        self.network_interface = None
        self.messages = []

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __hash__(self):
        # ID is unique for nodes created by network.create_node ==> __hash__ is collision free and faster than calling super().hash()
        return self.id

    def send_message(self, message):
        path_tree = message.header["path_tree"]
        next_hop = path_tree.data
        if self.has_neighbor(next_hop):
            self.network_interface.send(self, next_hop, message)
        else:
            print(f"Warning: {str(self)} tried sending a message to a node not its neighbor: {next_hop}") #TODO implement logging

    def receive(self, message):
        self.messages.append(message)
        path_tree = message.header["path_tree"]
        for child_tree in path_tree.children:
            new_message = message.clone()
            new_message.header["path_tree"] = child_tree
            self.send_message(new_message)

    def invoke_broadcast(self, content):
        minimal_spanning_tree = self.network_interface.minimal_spanning_tree
        message = Message(minimal_spanning_tree, content)
        self.receive(message)
