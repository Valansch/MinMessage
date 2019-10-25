from hash_tree import HashTree

def extract_minimal_spanning_tree(root):
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
