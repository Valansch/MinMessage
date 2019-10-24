class NetworkInterface:
    
    def __init__(self, network):
        self.network = network

    def send(self, sender, target, message):
        if sender.has_neighbor(target):
            self.network.total_messages += 1
            target.receive(message)