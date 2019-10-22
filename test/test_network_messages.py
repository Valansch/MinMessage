
from network import Network
import network_factory

from network_interface import NetworkInterface
from message import Message

import path_finder

random_speed = 624352
network_size = 100
edge_factor = 2
network = None

def setup_module():
    global network
    network = network_factory.create_random_network(random_speed, network_size, edge_factor)
    network_factory.connect_loose_ends(network, network.nodes)


def test_send_one_message():
    simple_network = Network()
    nodeA = simple_network.create_new_node()
    nodeB = simple_network.create_new_node()
    simple_network.connect(nodeA, nodeB)

    message = Message([], "Content")
    nodeA.send_message(nodeB, message)

    assert simple_network.total_messages == 1 and nodeB.messages[0].body =="Content"

def test_send_transitive_message():
    simple_network = Network()
    node0 = simple_network.create_new_node()
    node1 = simple_network.create_new_node()
    node2 = simple_network.create_new_node()
    simple_network.connect(node0, node1)
    simple_network.connect(node0, node2)

    message = Message([], "Content")
    #nodeA.send_message(nodeC, message)
    
    network = network_factory.create_random_network(random_speed, network_size, edge_factor)
    network_factory.connect_loose_ends(network, network.nodes)
    path_finder.remove_subpaths(path_finder.find_all_paths(network, network.nodes[0]), network_size)
    
    assert simple_network.total_messages == 1 and nodeB.messages[0].body =="Content"
