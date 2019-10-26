from hash_tree import HashTree


def extract_minimal_spanning_tree(root):
    """
        Constructs a minimal spanning tree by traversing 
        a network starting from a given root node

        Parameters
        ----------
        root: Node

        Returns
        ---------
        HashTree: The minimal spanning tree
    """
    tree = HashTree(root)
    subtrees = []
    current_subtree = tree
    while True:
        for neighbor in current_subtree.data.neighbors:  # O(n * log(n))
            if neighbor not in tree:  # O(1)
                new_subtree = current_subtree.add(neighbor)  # 0(log(n))

                # O(1) (Will be O(k) O(log(n) times)
                # Since every k <= n: The sum of these calls are o(n * log(n)) <= O(n * log(n))
                subtrees.append(new_subtree)
        try:
            current_subtree = subtrees.pop()
        except IndexError:
            break
    return tree
