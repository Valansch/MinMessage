import time

import network_factory


def run_network_simulation(network_size, avg_edges_per_node):

    print("========================================================================================")
    start = time.time()

    print(f"Creating random network of size {str(network_size)}...")
    network = network_factory.create_random_network(network_size, avg_edges_per_node)

    print("Invoking broadcast...")
    network.nodes[0].invoke_broadcast("Content")

    print(f"Broadcast finished. Total messages send: {str(network.total_messages)} seconds passed: {str(int(100 * (time.time() - start)) / 100)}s") 

if __name__ == "__main__":
    run_network_simulation(100, 5)
    run_network_simulation(500, 5)
    run_network_simulation(1000, 5)
    run_network_simulation(5000, 5)
    run_network_simulation(10000, 5)
    run_network_simulation(30000, 5)
