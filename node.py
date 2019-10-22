import path_finder

class Node:
    def advertise(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)

    def has_neighbor(self, node):
        return node in self.neighbors

    def __str__(self):
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
        
    def send_message(self, target, message):
        self.network_interface.send(self, target, message)

    def receive(self, source, message):
        self.messages.append(message)

    def invoke_broadcast(self):
        pass
      #  path = path_finder.find_all_paths(self)
       # print(path_finder.print_path(path))

