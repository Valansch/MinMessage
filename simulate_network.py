import argparse
import sys
import time

import network_factory


def run_network_simulation(network_size, avg_edges_per_node):

    start = time.time()

    print(f"Creating random network of size {str(network_size)}...")
    network = network_factory.create_random_network(network_size, avg_edges_per_node)

    print("Invoking broadcast...")
    network.nodes[0].invoke_broadcast("Content")

    print(
        f"Broadcast finished. Total messages send: {str(network.total_messages)}" +
        f"seconds passed: {str(int(100 * (time.time() - start)) / 100)}s"
    )


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Simulates broadcasting a message with minimum number of messages required"
    )
    parser.add_argument(
        "network_size",
        metavar="<Network size>",
        type=int,
        help="The size of the network to simulate.",
    )
    parser.add_argument(
        "avg_edges_per_node",
        metavar="<Avg edges per node>",
        default=8,
        choices=range(1, 20),
        type=int,
        help="The average number of edges per node",
    )
    return vars(parser.parse_args())


def validate_arguments(arguments):
    if arguments["network_size"] <= 0:
        sys.exit(1)
        print("Network size must be a number greater 0.")


if __name__ == "__main__":
    arguments = parse_arguments()
    validate_arguments(arguments)
    run_network_simulation(arguments["network_size"], arguments["avg_edges_per_node"])
