
from network import Network
import network_factory

from network_interface import NetworkInterface
from message import Message

from minimal_spanning_tree_builder import build_minimal_spanning_tree

random_speed = 624352
network_size = 100
edge_factor = 2
network = None

def setup_module():
    global network
    network = network_factory.create_random_network(random_speed, network_size, edge_factor)
    network_factory.connect_loose_ends(network, network.nodes)


def test_send_one_message():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()

    network.connect(node0, node1)

    network.inject_network_interfaces()
    
    msp = build_minimal_spanning_tree(network, node0)

    node0.invoke_broadcast("Content")

    assert network.total_messages == 1 and node1.messages[0].body =="Content"

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
    assert node1.messages[0].body =="Content"
    assert node2.messages[0].body =="Content"

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
    assert node1.messages[0].body =="Content"
    assert node2.messages[0].body =="Content"

    
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
    assert node1.messages[0].body =="Content"
    assert node2.messages[0].body =="Content"
    assert node3.messages[0].body =="Content"


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
    assert node1.messages[0].body =="Content"
    assert node2.messages[0].body =="Content"
    assert node3.messages[0].body =="Content"