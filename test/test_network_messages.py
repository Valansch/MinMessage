
from network import Network
import network_factory
from path import Path
from traversable_path import TraversablePath

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

    path = Path()
    path.append(nodeB)

    message = Message(TraversablePath(path), "Content")
    nodeA.send_message(message)

    assert simple_network.total_messages == 1 and nodeB.messages[0].body =="Content"

def test_send_transitive_message():
    simple_network = Network()
    nodeA = simple_network.create_new_node()
    nodeB = simple_network.create_new_node()
    nodeC = simple_network.create_new_node()
    simple_network.connect(nodeA, nodeB)
    simple_network.connect(nodeB, nodeC)

    path = Path()
    path.append(nodeB)
    path.append(nodeC)

    message = Message(TraversablePath(path), "Content")
    nodeA.send_message(message)

    assert simple_network.total_messages == 2 
    assert nodeB.messages[0].body =="Content"
    assert nodeC.messages[0].body =="Content"

