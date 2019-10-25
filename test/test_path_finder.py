from network import Network
import path_finder
from path import Path
import pytest

def test_transitive_path():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()

    network.connect(node0, node1)
    network.connect(node1, node2)

    is_path = path_finder.find_path(node0, node2, Path())
    should_path = Path()
    should_path.append(node0)
    should_path.append(node1)
    should_path.append(node2)
    assert is_path == should_path


def test_path_not_found():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()

    network.connect(node0, node1)

    with pytest.raises(LookupError):
        path_finder.find_path(node0, node2, Path())

def test_path_split():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()
    node3 = network.create_new_node()

    network.connect(node0, node1)
    network.connect(node1, node2)
    network.connect(node1, node3)

    is_path = path_finder.find_path(node0, node3, Path())
    should_path = Path()
    should_path.append(node0)
    should_path.append(node1)
    should_path.append(node3)
    assert is_path == should_path

def test_path_and_join():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()
    node3 = network.create_new_node()

    network.connect(node0, node2)
    network.connect(node0, node1)
    network.connect(node1, node3)
    network.connect(node2, node3)

    is_path = path_finder.find_path(node0, node3, Path())
    optional_pathA = Path()
    optional_pathA.append(node0)
    optional_pathA.append(node1)
    optional_pathA.append(node3)
    optional_pathB = Path()
    optional_pathB.append(node0)
    optional_pathB.append(node2)
    optional_pathB.append(node3)
    assert is_path == optional_pathA or is_path == optional_pathB

def test_find_all_paths():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()
    node3 = network.create_new_node()

    network.connect(node0, node1)
    network.connect(node1, node2)
    network.connect(node1, node3)

    is_paths = path_finder.find_all_paths(network, node0)
    should_paths = set()
    path_to_1 = Path()
    path_to_2 = Path()
    path_to_3 = Path()
    path_to_1.append(node0)
    path_to_1.append(node1)
    path_to_2.append(node0)
    path_to_2.append(node1)
    path_to_2.append(node2)
    path_to_3.append(node0)
    path_to_3.append(node1)
    path_to_3.append(node3)
    should_paths.add(path_to_1)
    should_paths.add(path_to_2)
    should_paths.add(path_to_3)
    assert set(is_paths) == should_paths

def test_path_comparison():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()

    pathA = Path()
    pathB = Path()
    pathA.append(node0)
    pathA.append(node1)
    pathB.append(node1)
    pathB.append(node0)
    
    assert pathA < pathB

def test_path_sorting():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()
    node3 = network.create_new_node()
    node4 = network.create_new_node()

    pathA = Path()
    pathB = Path()
    pathC = Path()
    pathA.append(node0)
    pathA.append(node1)
    pathB.append(node0)
    pathB.append(node2)
    pathB.append(node3)
    pathC.append(node0)
    pathC.append(node2)
    pathC.append(node4)

    paths_is = [pathC, pathB, pathA]
    paths_should = [pathA, pathB, pathC]

    paths_is.sort()
    assert paths_is == paths_should