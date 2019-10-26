
class HashTree:
    """
        Minimal implementation of a hash tree.
        This allows "in" and element subtree access in O(1).
        Add complexity in O(log(n)).
    """



    def __init__(self, data, parent=None, entries = None):
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
        if entries is None:
            self.entries = set()
        else:
            self.entries = entries
        self.entries.add(self)

    def __contains__(self, data):
        if self.parent is not None:
            raise NotImplementedError(
                "HashTree:__contains__ is only implemented for root trees " +
                f"tree {str(self)} with value {str(self.data)} with parent: " +
                f"{str(self.parent)} and value {str(self.parent.data)}"
            )   
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
        child = HashTree(data, self, self.entries)
        self.children.append(child)
        self.entries.add(child)
        return child

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        if type(self.data).__name__ == "Node":
            return self.data.id
        else:
            return hash(self.data)

    def __len__(self):
        return len(self.entries)
