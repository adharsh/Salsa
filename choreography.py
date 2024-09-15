#!/usr/bin/env python3
import argparse
import random
import networkx as nx
from networkx.drawing.nx_pydot import read_dot

def load_graph(dot_file):
    return nx.DiGraph(read_dot(dot_file))

def traverse_graph(graph, steps, skip_guapea):
    current_node = "Guapea"
    traversed = [current_node]
    step_count = 0
    while step_count < steps:
        neighbors = list(graph.successors(current_node))
        if not neighbors:
            print(f"ERROR! Should not happen. Dead end reached at {current_node}. Restarting from Guapea.")
            current_node = "Guapea"
            continue
        next_node = random.choice(neighbors)
        traversed.append(next_node)
        if not (skip_guapea and next_node == "Guapea"):
            step_count += 1
        current_node = next_node
    return traversed

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Traverse a salsa dance moves graph.")
    parser.add_argument("--steps", default=10, type=int, help="Number of steps to traverse")
    parser.add_argument("--dot-file", default="social.dot", help="Path to the DOT file containing the graph (default: social.dot)")
    parser.add_argument("--skip-guapea", default=True, action="store_true", help="Don't increment counter when moving to Guapea (default: True)")
    args = parser.parse_args()

    graph = load_graph(args.dot_file)
    traversed = traverse_graph(graph, args.steps, args.skip_guapea)
    
    print(f"Total nodes visited: {len(traversed)}")
    print("\n".join(traversed))
