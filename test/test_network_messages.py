import network_factory
from network import Network

random_seed = 624352
network_size = 100
edge_factor = 2


def test_send_one_message():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()

    network.connect(node0, node1)

    network.inject_network_interfaces()

    node0.invoke_broadcast("Content")

    assert network.total_messages == 1 and node1.messages[0].body == "Content"


def test_send_transitive_message():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()

    network.connect(node0, node1)
    network.connect(node1, node2)

    network.inject_network_interfaces()

    node0.invoke_broadcast("Content")

    assert network.total_messages == 2
    assert node1.messages[0].body == "Content"
    assert node2.messages[0].body == "Content"


def test_split_message():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()

    network.connect(node0, node1)
    network.connect(node0, node2)

    network.inject_network_interfaces()

    node0.invoke_broadcast("Content")

    assert network.total_messages == 2
    assert node1.messages[0].body == "Content"
    assert node2.messages[0].body == "Content"


def test_transitive_and_split_message():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()
    node3 = network.create_new_node()

    network.connect(node0, node1)
    network.connect(node1, node2)
    network.connect(node1, node3)

    network.inject_network_interfaces()

    node0.invoke_broadcast("Content")

    assert network.total_messages == 3
    assert node1.messages[0].body == "Content"
    assert node2.messages[0].body == "Content"
    assert node3.messages[0].body == "Content"


def test_split_and_join_message():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()
    node3 = network.create_new_node()

    network.connect(node0, node1)
    network.connect(node1, node2)
    network.connect(node1, node3)

    network.inject_network_interfaces()

    node0.invoke_broadcast("Content")

    assert network.total_messages == 3
    assert node1.messages[0].body == "Content"
    assert node2.messages[0].body == "Content"
    assert node3.messages[0].body == "Content"


def test_minimal_number_messages():
    network = network_factory.create_random_network(network_size, edge_factor, random_seed)
    network_factory.connect_loose_ends(network, network.nodes)

    network.inject_network_interfaces()

    network.nodes[0].invoke_broadcast("Content")

    assert network.total_messages == network_size - 1
    for node in network.nodes:
        if node.id > 0:
            assert len(node.messages) == 1 and node.messages[0].body == "Content"
