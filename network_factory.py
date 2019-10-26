import copy
import random

import numpy as np

from network import Network


def create_random_network(network_size, edge_factor, seed=None):
    """
        Creates a random jointed network
        
        Parameters
        ---------
            network_size: int
                Number of nodes in the network

            edge_factor: int
                Number of edges in relation to network size
                Also: Average number of edges per node
            
            seed: int (optional)
                The seed for the random number generater

        Returns
        -------
            network: Network
                The created jointed network
        """

    edge_factor = edge_factor - 2 if edge_factor > 3 else 1
    if seed is not None:
        random.seed(seed)
    network = Network()
    for _ in range(network_size):
        network.create_new_node() # Create all nodes

    # Connect random nodes
    for _ in range(1, edge_factor - 1):
        for nodeA in network.nodes:
            nodeB = network.nodes[random.randint(1, network_size - 1)]
            if nodeA != nodeB:
                network.connect(nodeA, nodeB)

    # Connect it all
    connect_disjointed_network(network, network_size, edge_factor)

    return network


def connect_disjointed_network(network, size, avg_edges):
    """
        Joints a networking using a minimum spanning tree

    Parameters
    ---------
        network: Network
            The network to joint
        size: int
            Network size
        avg_edges: int
            The average number of edges per node

    Returns
    -------
        network: Network
            A jointed network
    """
    nodes = copy.copy(network.nodes)
    current_level = [nodes.pop()]

    # Using a poisson distribution for the number of edges to ensure sufficient randomness
    # This means there will there will be a normal distribution of nodes with 1,2 or more edges
    # Equally there will be a normal distribution of paths containing nodes only having 2 neighbors
    generator = [abs(x - 1) for x in (np.random.poisson(2, size))]
    while True:  # size / k / avg_edges times ==> O(n)
        next_level = []
        for node in current_level:  # k times
            n_children = generator.pop()
            for _ in range(0, n_children):  # 2 times on average
                new_node = nodes.pop()
                network.connect(node, new_node)
                next_level.append(new_node)
                if len(nodes) == 0:
                    return network
        if len(next_level) == 0:
            # If by chance we did not create any new nodes on this level, backtrack
            next_level = current_level
        current_level = next_level
