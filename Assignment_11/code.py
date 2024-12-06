import sys
from copy import deepcopy

INFINITY = sys.maxsize

network_topology = {
    'A': {'B': 1, 'C': 1, 'E': 1, 'F': 1},
    'B': {'A': 1, 'C': 1},
    'C': {'A': 1, 'B': 1, 'D': 1},
    'D': {'C': 1, 'G': 1},
    'E': {'A': 1},
    'F': {'A': 1, 'G': 1},
    'G': {'D': 1, 'F': 1},
}


def initialize_routing_table(node):
    return {neighbor: network_topology[node].get(neighbor, INFINITY) for neighbor in network_topology}


routing_tables = {node: initialize_routing_table(node) for node in network_topology}


def distance_vector_round():
    global routing_tables
    updated = False
    new_tables = deepcopy(routing_tables)

    for node in network_topology:
        if node == 'A':
            print("Distance Vectors received by A:",
                  {neighbor: new_tables[neighbor] for neighbor in network_topology['A']})
        for neighbor in network_topology[node]:
            for dest, neighbor_cost in routing_tables[neighbor].items():
                if dest == node:
                    continue
                new_cost = network_topology[node][neighbor] + neighbor_cost
                if new_cost < new_tables[node].get(dest, INFINITY):
                    new_tables[node][dest] = new_cost
                    updated = True

        routing_tables = new_tables
    return updated


def run_distance_vector_protocol():
    print("Initial Distance Vector of A:", routing_tables['A'])

    round_counter = 1
    while True:
        print(f"\nRound {round_counter}")
        updated = distance_vector_round()

        print("Updated Distance Vector of A:", routing_tables['A'])

        if not updated:
            break
        round_counter += 1

    print("\nFinal Distance Vector of A:", routing_tables['A'])


run_distance_vector_protocol()