from hash_tree import HashTree
from node import Node
def build_minimal_spanning_tree(network, root: Node):
    tree = HashTree(root)
    nodes = []
    current_node = root
    while True:
        for neighbor in current_node.neighbors:
            if not tree.contains(neighbor): # O(1)
                nodes.append(neighbor)
                tree.add(neighbor) # O(log(1))
        try:
            current_node = nodes.pop()
        except IndexError:
            break
    return tree

from network import Network
