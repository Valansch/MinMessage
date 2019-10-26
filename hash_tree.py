
class HashTree:
    """
        Minimal implementation of a hash tree.
        This allows "in" and element subtree access in O(1).
        Add complexity in O(log(n)).
    """



    def __init__(self, data, parent=None):
        """
            Constructs a new HashTree

            Parameters
            ---------
            data: Any
                The data to be stored in the root node of the tree

            parent: HashTree (Optional)
                The parent in case this tree is a subtree of parent

            Returns
            -------
            self: HashTree
                The newly constructed HashTree
        """
        self.parent = parent
        self.children = []
        self.data = data
        self.entries = set()
        self.entries.add(self)

    def __contains__(self, data):
        # avg O(1) because entries is collision free for type Node
        return HashTree(data) in self.entries

    def add(self, data):
        """
            Adds another entry as a child

            Parameters
            ---------
            data: Any
                The data to be stored in the child tree

            Returns
            -------
            child: HashTree
                The child that was added to self
        """
        child = HashTree(data, self)
        self.children.append(child)
        self.add_descendant(child)
        return child

    def add_descendant(self, tree):
        """
            Add new subtree to all descendants hashtable

            Parameters
            ---------
            tree: HashTree
        """
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
