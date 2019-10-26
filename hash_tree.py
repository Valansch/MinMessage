class HashTree:
    def __init__(self, data, parent=None):
        self.parent = parent
        self.children = []
        self.data = data
        self.entries = set()
        self.entries.add(self)

    def __contains__(self, data):
        # avg O(1) because entries is collision free for type Node
        return HashTree(data) in self.entries

    def add(self, data):
        child = HashTree(data, self)
        self.children.append(child)
        self.add_descendant(child)
        return child

    def add_descendant(self, tree):
        parent = self
        while parent is not None:
            parent.entries.add(tree)
            parent = parent.parent

    def __eq__(self, other):
        return self.data.id == other.data.id

    def __hash__(self):
        if type(self.data).__name__ == "Node":
            return self.data.id
        else:
            return hash(self.data)

    def __len__(self):
        return len(self.entries)
