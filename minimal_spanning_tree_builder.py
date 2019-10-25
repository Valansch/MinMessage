from hash_tree import HashTree
from node import Node


def build_minimal_spanning_tree(network, root: Node):
    tree = HashTree(root)
    subtrees = []
    current_subtree = tree
    while True:
        for neighbor in current_subtree.data.neighbors:
            if not tree.contains(neighbor):  # O(1)
                new_subtree = current_subtree.add(neighbor)  # 0(log(n))
                subtrees.append(new_subtree)  # O(1)
        try:
            current_subtree = subtrees.pop()
        except IndexError:
            break
    return tree
