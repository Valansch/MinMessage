import network_factory

random_seed = 624352
network_size = 100
edge_factor = 2


def test_create_random_network_size():
    network = network_factory.create_random_network(network_size, edge_factor, random_seed)
    assert network.get_size() == network_size


def network_connected(network):
    visisted = []
    stack = [network.nodes[0]]
    while len(stack) > 0:
        node = stack.pop()
        if node in visisted:
            continue  # Loop detected
        stack += node.neighbors
        visisted.append(node)

    return network_size == len(visisted)


def test_network_not_connected():
    network = network_factory.create_random_network(network_size, edge_factor, random_seed)
    assert not network_connected(network)


def test_connect_loose_ends():
    network = network_factory.create_random_network(network_size, edge_factor, random_seed)
    network_factory.connect_loose_ends(network, network.nodes)

    assert network_connected(network)
