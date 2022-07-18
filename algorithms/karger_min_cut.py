# Learning Algorithms
# Randomized Contraction - Karger Minimum Cut
# Andrew Tracey
# May 17, 2022

# Stanford Algorithms Specialization
# Class 1 - Week 4 - Programming Assignment

# DESCRIPTION
# Goal: Given a graph G with 200 vertices, calculate the minimum cut.
# More specifically, in dividing G into two subgraphs A and B, calculate the 
# cut(A, B) with the minimum number of edges crossing from A to B, and return
# the number of edges in that minimum cut.
# Method:
# Using the Randomized Contraction (aka Karger Minimum Cut) algorithm.
# 1. Randomly select two nodes of G, u and v.
# 2. Merge (or contract) u and v into a single super node in G.
# 3. Remove any self loops (e.g. nodes connecting u and v, now irrelevant)
# Repeat these steps until there are only 2 nodes (or super nodes) remaining.
# These two nodes represent the cut of G: that is, all of the nodes that were
# collapsed into one super node represent one set (A), while the nodes collapsed
# into the other super node represent the second set B.
# The number of edges between the super nodes is the min cut value.
# HOWEVER, this algorithm doesn't really guarantee a minimum cut. In fact, there
# is just 1 / n^2 (or 1/200^2 in this case) probability that it returns a cut 
# that is a minimum cut. If we run the algorith n^2 * ln(n) times, then the
# probability that we get the min cut in one of those trials is (1 - 1/n), or
# in this case (1 - 1/200) = 99.5%. Therefore, we need to run the algorithm
# 200^2 * ln(200) ~ 212,000 times. We'll actually do this twice to increase our
# odds of success from 99.5% to 99.9975%.

# ============================== IMPLEMENTATION ==============================
import math
import numpy as np
import random
from datetime import datetime
import copy

def load_graph_from_file(filepath: str) -> list[list[int]]:
    graph = {}
    with open(filepath) as f:
        lines = f.readlines()
    for line in lines:
        row_str = line.strip().split('\t')
        row = list(map(int, row_str))
        graph[row[0]] = row[1:]
    return graph

def karger(graph):
    """Karger randomized contraction algorithm"""

    # helper function from Karger algorithm
    def contract():
        """Given nodes u and v of the graph, contract them into a single node"""
        # Merge v into u in the set of remaining nodes
        for node in v:
            u.append(node)
        remaining_nodes.remove(v)

        # Copy all edges of v into u
        for edge in graph[v[0]]:
                graph[u[0]].append(edge)
        
        # Remove self-loops from u
        for node in u:
            while graph[u[0]].count(node) > 0:
                graph[u[0]].remove(node)

    remaining_nodes = [[node] for node in graph.keys()]
    while len(remaining_nodes) > 2:
        u, v = random.sample(remaining_nodes, 2)
        contract()
    num_edges = len(graph[remaining_nodes[0][0]])
    return num_edges

def min_cut(graph, trials):
    """Calculate the number of crossing edges of a minimum cut of a graph"""
    minimum_edges = math.inf
    checkpoints = list(map(int, np.linspace(trials*0.01, trials, 100)))
    checkpoint = 0
    start = end = datetime.now()
    print(f'Beginning Trial 1 of {trials:,} at {start}'.ljust(100, '-'))
    for trial in range(1, trials+1):
        random.seed()
        crossing_edges = karger(copy.deepcopy(graph))
        minimum_edges = min(minimum_edges, crossing_edges)
        if trial == checkpoints[checkpoint]:
            print(f' > {(checkpoint+1)}% complete ({trial:,} trials).'.ljust(32),
                  f'Trial Time: {datetime.now() - end}.',
                  f'Total Time: {datetime.now() - start}.',
                  f'Current Minimum: {minimum_edges}')
            end = datetime.now()
            checkpoint += 1
    print(f'Trials complete. Time elapsed: {datetime.now() - start}')
    return minimum_edges

# ================================ DRIVER CODE ================================

if __name__ == '__main__':

    print(f"START OF NEW EXECUTION".center(100, "="))

    graph_input_path = 'algorithms/input-files/karger_min_cut_input.txt'
    graph_input = load_graph_from_file(graph_input_path)
    expected_result = 17  # Per Stanford Algorithms course assignment

    # TEST INPUT - Uncomment to use
    # graph_input = {1: [3, 5, 7],
    #                     2: [3, 4],
    #                     3: [2, 1, 4, 5],
    #                     4: [3, 2],
    #                     5: [3, 1, 7, 6],
    #                     6: [5, 7],
    #                     7: [1, 5, 6]}
    # expected_result = 2

    n = len(graph_input)
    trials = int(round(n**2 * math.log(n), 0))
    result = min_cut(graph_input, trials)
    print('\nFINAL OUTPUT:', result)
    
    if result == expected_result:
        print('\nCORRECT!')
    else:
        print(f'\nIncorrect. The correct answer is {expected_result}')
