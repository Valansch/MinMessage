import copy

class Message:
    def __init__(self, header, body):
        self.header = header
        self.body = body

    def clone(self):
        return Message(copy.copy(self.header), copy.copy(self.body))