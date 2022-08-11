# Learning Algorithms
# Single-Source Shortest Path with Weighted Edges
# Dijkstra's Algorithm
# August 10, 2022

# Stanford Algorithms Specialization
# Class 2 - Week 2 - Programming Assignment

# DESCRIPTION
# Goal:
# Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1
# (the first vertex) as the source vertex, and to compute the shortest-path
# distances between 1 and every other vertex of the graph.
# If there is no path between a vertex vv and vertex 1, we'll define the
# shortest-path distance between 1 and vv to be 1_000_000.

# You should report the shortest-path distances to the following ten vertices,
# in order: 7,37,59,82,99,115,133,165,188,197.
# You should encode the distances as a comma-separated string of integers.

# Method:
# Dijkstra's Algorithm
# Create a set, X, of explored vertices, initialized with the source vertex.
#
# Create an array, A, of length n, where A[i] represents the length of the
# shortest path from s to i. Initialize A[s] = 0 and all other A[i] = 1_000_000
#
# Iterate n - 1 times, each time adding one new vertex to X, so that when the
# loop completes X == V. In each iteration:
# 1. Scan all available edges (u, v) where u is in X and v is not, and for each
#    edge, calculate a greedy score: A[u] + weight(u, v)
# 2. Choose the edge from step 1 with the smallest greedy score, add it to X,
#    and update A[v] to its greedy score

# ============================== IMPLEMENTATION ==============================
import math


def read_graph(filepath: str, n: int) -> list[list[tuple[int]]]:
    """
    Read the edges of the graph from file

    :param str filepath: path to txt file containing edge information as:
        row i: [tail_vertex] [head_vertex],[weight] [head_vertex][weight] ...
    :param int n: the number of edges in the graph, labeled 1 through n
    :return: a list representing the edges of the graph as follows:
        edges[i] = [(v, 100), (w, 50)]
            -> vertex u = i + 1: weight(u, v) = 100, weight(u, w) = 50
    """

    # save each line of the txt file in a list
    with open(filepath) as f:
        lines = f.readlines()

    # initalize output list, E, where E[i] represents edges out of vertex i
    edges = [[] for _ in range(n)]

    # process one line at a time
    for line in lines:
        contents = line.split()
        tail = int(contents[0])
        # iterate over each edge out of tail
        for edge in contents[1:]:
            head, weight = map(int, edge.split(","))
            edges[tail - 1].append((head, weight))

    return edges


def dijkstra(E: list[list[tuple[int]]], n: int) -> list[int]:
    """
    Run Dijsktra's algorithm on graph with vertices 1 to n and edges E

    :param lst E: E[i] = [(v, 100), (w, 50)] -> vertex i + 1 = u, has edges
                  to vertex v with length 100 and to vertex w with length 50
    :param int n: the number of edges in the graph, labeled 1 through n
    :return lst:  A[i] is the length of the shortest path from 1 to (i+1)
    """

    X = {1}  # set of explored nodes
    A = [0] + [1_000_000] * (n - 1)  # shortest path distances from 1 to i+1

    # outer loop will run n - 1 times, adding a new node to X in each iteration
    for _ in range(n - 1):

        # choose vertex in V - X with smallest greedy score from vertex in X
        chosen_score = math.inf
        for tail in X:
            for head, weight in E[tail - 1]:
                if head not in X:
                    score = A[tail - 1] + weight
                    if score < chosen_score:
                        chosen_vertex = head
                        chosen_score = score

        # update A and X for the chosen vertex
        A[chosen_vertex - 1] = chosen_score
        X.add(chosen_vertex)

    return A


def print_solution(A: list[int]) -> None:
    nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    n = len(nodes)
    for i, node in enumerate(nodes):
        try:
            print(A[node - 1], end="")
        except KeyError:
            print(f"Node {node} is out of bounds for the input list.")
            raise KeyError
        if i < n - 1:
            print(",", end="")
    print()


# =============================== DRIVER CODE =================================

if __name__ == "__main__":
    E = read_graph("algorithms/input-files/dijkstra_input.txt", 200)
    result = dijkstra(E, 200)
    print(result)
    print_solution(result)
