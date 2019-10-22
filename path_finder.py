import copy

def find_path(node, destination, inpath):
    path = None
    if inpath is None:
        path = []
    else:
        path = copy.copy(inpath)

    path.append(node)
    if node == destination:
        return path

    unseen_neighbors = [neighbor for neighbor in node.neighbors if neighbor not in path]
    if len(unseen_neighbors) == 0:
        return None # No path found
    for neighbor in unseen_neighbors:
        new_path = find_path(neighbor, destination, path)
        if new_path is not None:
            return new_path
    return None


def find_all_paths(network, node):
    paths = []
    for destination in network.nodes:
        if destination != node:
            paths.append(find_path(node, destination, []))
    return paths


def remove_subpaths(paths, network_size):
    paths.sort(key = len)
    paths.reverse()

    duplicates = []

    for x in range (0, len(paths) - 1): 
        for y in range(x + 1, len(paths) - 1):
            if (set(paths[x]) > set(paths[y])):
                duplicates.append(y)

    print_path(paths)
    
    return "exclusives"

def print_path(paths):
    for path in paths:
        if path is None: continue
        for node in path:
            print(node.id, end=",")
