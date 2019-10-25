class NetworkInterface:
    def __init__(self, network):
        self.network = network

    def send(self, sender, target, message):
        if sender.has_neighbor(target):
            self.network.global_message_buffer.append((target, message))
