from message import Message
from minimal_spanning_tree_builder import extract_minimal_spanning_tree


class Node:
    """
        A network Node
    """

    def advertise(self, node):
        """
            Adds a new node to neighbor

            Parameters
            ----------
                node: Node
                    The new neighbor
        """
        if node not in self.neighbors:
            self.neighbors.append(node)

    def has_neighbor(self, node):
        return node in self.neighbors

    def __repr__(self):
        return str(self.id)

    def __init__(self, id, network_interface):
        self.neighbors = []
        self.id = id
        self.network_interface = network_interface
        self.minimal_spanning_tree = None
        self.messages = []

    def __hash__(self):
        # ID is unique for nodes created by network.create_node
        # ==> __hash__ is collision free and faster than calling super().hash()
        return self.id

    def send_message(self, message):
        """
            Sends a message if the next hop in the messages path is a neighbor

            Parameters
            ----------
                message: Message
                    The message to send
        """
        path_tree = message.header["path_tree"]
        next_hop = path_tree.data
        if self.has_neighbor(next_hop):
            self.network_interface.send(self, next_hop, message)
        else:
            print(
                f"Warning: {str(self)} tried sending a message to a node not its neighbor: {next_hop}"
            )

    def receive(self, message):
        """
            Callback for when a message is received by this node

            Parameters
            ----------
                message: Message
                    The message received
        """
        self.messages.append(message.body)
        path_tree = message.header["path_tree"]
        for child_tree in path_tree.children:
            new_message = message.clone()
            new_message.header["path_tree"] = child_tree
            self.send_message(new_message)
        message = None

    def invoke_broadcast(self, content):
        """
            Invokes a broadcast to all nodes reachable
            If this is the first broadcast send by this node,
            then a minimal spanning tree, containing all nodes reachable,
            will be constructed first. The complexity for this initial call
            is therefore in O(n*log(n)). All calls after that are in O(n)

            Parameters
            ----------
                content: Any
                    The content of the message to send
        """
        if self.minimal_spanning_tree is None:
            print("Creating MST...")
            self.minimal_spanning_tree = extract_minimal_spanning_tree(self)
            print("MST created")
        message = Message(self.minimal_spanning_tree, content)
        self.receive(message) # Call receive to drop "message zero" into the root nodes in port

        network = self.network_interface.network
        # Simulate network activity
        network.start()
