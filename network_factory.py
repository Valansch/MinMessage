import random

from network import Network


def create_random_network(network_size, edge_factor, seed = None):
    if seed is not None:
        random.seed(seed)
    network = Network()
    for _ in range(network_size):
        network.create_new_node()

    for _ in range(1, edge_factor):
        for nodeA in network.nodes:
            nodeB = network.nodes[random.randint(1, network_size - 1)]
            if nodeA != nodeB:
                network.connect(nodeA, nodeB)
    return network


def connect_loose_ends(network, nodes):

    visisted = []
    stack = [nodes[0]]
    while len(stack) > 0:
        node = stack.pop()
        if node in visisted:
            continue  # Loop detected
        stack += node.neighbors
        visisted.append(node)
    complement = [node for node in nodes if node not in visisted]

    if len(complement) > 0:
        # This returns is always a connected graph, therefore connecting a connected graph creates another connected graph
        connect_loose_ends(network, complement)

        random_index = random.randint(1, (len(visisted))) - 1
        network.connect(complement[0], visisted[random_index])