class HashTree():
    def __init__(self, data, parent = None):
        self.parent = parent
        self.children = []
        self.data = data
        self.entries = set()
        self.entries.add(self)

    def contains(self, data):
        return HashTree(data) in self.entries # avg O(1) because entries is collision free for type Node

    def add(self, data):
        child = HashTree(data, self)
        self.children.append(child)
        self.entries.add(child)
        return child

    def __eq__(self, other):
        return self.data.id == other.data.id

    def __hash__(self):
        return self.data.id


