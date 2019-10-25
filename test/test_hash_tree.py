from minimal_spanning_tree_builder import build_minimal_spanning_tree
from network import Network


def test_minimal_tree():
    network = Network()
    node = network.create_new_node()

    msp = build_minimal_spanning_tree(node)

    assert len(msp) == 1 and len(msp.children) == 0 and msp.data == node


def test_single_edge():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()

    network.connect(node0, node1)

    msp = build_minimal_spanning_tree(node0)

    assert len(msp) == 2 and len(msp.children) == 1 and msp.children[0].data == node1


def test_transitive_tree():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()

    network.connect(node0, node1)
    network.connect(node1, node2)

    msp = build_minimal_spanning_tree(node0)

    assert len(msp) == 3 and msp.children[0].children[0].data == node2


def test_split_tree():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()

    network.connect(node0, node1)
    network.connect(node0, node2)

    msp = build_minimal_spanning_tree(node0)

    assert (
        len(msp) == 3
        and len(msp.children) == 2
        and msp.children[0].data == node1
        and msp.children[1].data == node2
    )


def test_split_and_join_tree():
    network = Network()
    node0 = network.create_new_node()
    node1 = network.create_new_node()
    node2 = network.create_new_node()
    node3 = network.create_new_node()

    network.connect(node0, node1)
    network.connect(node0, node2)
    network.connect(node1, node3)
    network.connect(node2, node3)

    msp = build_minimal_spanning_tree(node0)

    child_0_children = msp.children[0].children
    child_1_children = msp.children[1].children
    # Either node1 or node2 has child node3
    assert (
        (
            len(child_0_children) == 1 and child_0_children[0].data == node3
        ) or (
            len(child_1_children) == 1 and child_1_children[0].data == node3
        )
    )
