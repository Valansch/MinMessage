class NetworkInterface:
    
    def __init__(self, network, minimal_spanning_tree):
        self.network = network
        self.minimal_spanning_tree = minimal_spanning_tree

    def send(self, sender, target, message):
        if sender.has_neighbor(target):
            self.network.total_messages += 1
            target.receive(message)