import copy

class Message:
    def __init__(self, path_tree, body):
        self.header = dict()
        self.header["path_tree"] = path_tree
        self.body = body

    def clone(self):
        return Message(copy.copy(self.header), copy.copy(self.body))