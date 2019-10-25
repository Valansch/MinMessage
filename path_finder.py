import copy
from path import Path
from traversable_path import Path

def find_path(node, destination, path):
    path.append(node)
    if node == destination:
        return path
    else:
        for neighbor in node.neighbors:
            if neighbor in path:
                continue
            pass
            try:
                path = find_path(neighbor, destination, copy.copy(path))
            except LookupError:
                continue # node not found in this subpath
            return path
    raise LookupError("Destination unreachable.")
                 

def find_all_paths(network, node):
    paths = []
    for destination in network.nodes:
        if destination != node:
            paths.append(find_path(node, destination, Path()))
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
