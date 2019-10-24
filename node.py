import path_finder

class Node:
    def advertise(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)

    def has_neighbor(self, node):
        return node in self.neighbors

    def __repr__(self):
        return str(self.id)

    def print(self):
        print(f'Node{self.id}: ', end='')
        for node in self.neighbors:
            print(f'{str(node)}, ', end='')
        print()

    def __init__(self, id, network_interface):
        self.neighbors = []
        self.id = id
        self.network_interface = network_interface
        self.messages = []
        
    def send_message(self, message):
        path = message.header
        next_hop = path.pop()
        if self.has_neighbor(next_hop):
            self.network_interface.send(self, next_hop, message)
        else:
            print(f"Warning: {str(self)} tried sending a message to a node not its neighbor: {next_hop}") #TODO implement logging

    def receive(self, message):
        self.messages.append(message)
        if len(message.header) > 0:
            self.send_message(message)

    def invoke_broadcast(self):
        pass
      #  path = path_finder.find_all_paths(self)
       # print(path_finder.print_path(path))

