from algorithms.kosaraju import kosaraju


def compute_and_compare(nodes, edges, expected):
    "Compute SCCs and compare to expected SCCs by sorting"
    out = kosaraju(nodes, edges)
    to_be_sorted = [out, expected]
    for sccs in to_be_sorted:
        for scc in sccs:
            scc.sort()
        sccs.sort()
    for scc_out, scc_exp in zip(out, expected):
        assert scc_out == scc_exp


def test_path_graph():
    "1 -> 2 -> 3 -> 4"
    nodes = [1, 2, 3, 4]
    edges = [[1, 2], [2, 3], [3, 4]]
    expected = [[1], [2], [3], [4]]
    compute_and_compare(nodes, edges, expected)


def test_complete_graph():
    "Every node has a node to every other node"
    nodes = [1, 2, 3, 4, 5]
    edges = [
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 1],
        [2, 3],
        [2, 4],
        [2, 5],
        [3, 1],
        [3, 2],
        [3, 4],
        [3, 5],
        [4, 1],
        [4, 2],
        [4, 3],
        [4, 5],
        [5, 1],
        [5, 2],
        [5, 3],
        [5, 4],
    ]
    expected = [[1, 2, 3, 4, 5]]
    compute_and_compare(nodes, edges, expected)


def test_empty_graph():
    "A graph with no edges"
    nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    edges = []
    expected = [[node] for node in nodes]
    compute_and_compare(nodes, edges, expected)


def test_cyclic_graph():
    """A graph that contains a cycle
    1 → 2 → 3 → 6
        ↓    ↖ ↙
    5 → 4     7
    """
    nodes = [1, 2, 3, 4, 5, 6, 7]
    edges = [[1, 2], [2, 3], [2, 4], [4, 5], [3, 6], [6, 7], [7, 3]]
    expected = [[1], [2], [3, 6, 7], [4], [5]]
    compute_and_compare(nodes, edges, expected)


def test_basic_scc_example():
    """A textbook example of a graph with 11 nodes and 4 SCCs
    Graph                   SCCs
    1 → 3 → 11 → 6          1, 3, 5
     ↖ ↙     ↘  ↗ ↘         11
      5       8 ← 10        6, 10, 8
      ↓ ↘   ↗    ↗          2, 4, 7, 9
      7 → 9  → 2
        ↖ ↓  ↙
          4
    """
    nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    edges = [
        [1, 3],
        [2, 4],
        [2, 10],
        [3, 5],
        [3, 11],
        [4, 7],
        [5, 1],
        [5, 7],
        [5, 9],
        [6, 10],
        [7, 9],
        [8, 6],
        [9, 2],
        [9, 4],
        [9, 8],
        [10, 8],
        [11, 6],
        [11, 8],
    ]
    expected = [[1, 3, 5], [11], [6, 10, 8], [2, 4, 7, 9]]
    compute_and_compare(nodes, edges, expected)


def test_directed_acyclic_graph():
    """The meta-graph constructed from SCCs is a DAG
       2
      ↗ ↘
    1     4
      ↘ ↗
       3
    """
    nodes = [1, 2, 3, 4]
    edges = [[1, 2], [1, 3], [2, 4], [3, 4]]
    expected = [[1], [2], [3], [4]]
    compute_and_compare(nodes, edges, expected)


def test_large_random_graph():
    """Generate a few large random graphs with varying density and make sure
    the algorithm computes quickly. Kosaraju is limited by recursion depth"""
    import random

    for i in range(5):
        n = 1_000
        nodes = [random.randint(-n, n) for _ in range(n)]
        m = int(n * (i + 2 / 5))
        edges = [
            [random.choice(nodes), random.choice(nodes)] for _ in range(m)
        ]
        kosaraju(nodes, edges)
