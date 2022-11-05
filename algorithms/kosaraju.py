# Kosaraju's Algorithm for Computing Strongly Connected Components (SCCs)
# Discovers the strongly connected components of a directed graph using DFS

# Analysis
#  Case     TC        SC    Comments
#  ----     --        --    --------
#  Worst    O(n + m)  O(n)
#  Average  O(n + m)  O(n)
#  Best     O(n + m)  O(n)

# n := the number of nodes in the graph
# m := the number of edges in the graph

from collections import defaultdict


def kosaraju(nodes, edges):
    """Returns a list representing the strongly connected components of a graph

    :nodes list: node objects
    :edges list: directed edges [u, v] (u -> v)
    :return set: groups node objects into SCCs
    """

    # 1. Process input into graph using integer id's for nodes
    node_id_map = {}  # node -> node_id (index in nodes)
    for i, node in enumerate(nodes):
        node_id_map[node] = i

    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    for head_node, tail_node in edges:
        head_id = node_id_map[head_node]
        tail_id = node_id_map[tail_node]
        adj[head_id].append(tail_id)
        rev_adj[tail_id].append(head_id)

    # 2. DFS on reversed graph to find topological ordering of nodes
    visited = [False] * len(nodes)
    topological_orders = [0] * len(nodes)
    cur_position = len(nodes) - 1

    def _dfs_topological(node_id):
        """Uses DFS to find topological ordering of graph nodes"""
        visited[node_id] = True
        for tail_id in rev_adj[node_id]:
            if not visited[tail_id]:
                _dfs_topological(tail_id)
        nonlocal cur_position
        topological_orders[cur_position] = node_id
        cur_position -= 1

    for node in nodes:
        node_id = node_id_map[node]
        if not visited[node_id]:
            _dfs_topological(node_id)

    # 3. DFS on graph in topological order of reversed graph
    visited = [False] * len(nodes)
    sccs = []

    def _dfs_scc(node_id, source_node_id, scc):
        """Uses DFS to discover all nodes in SCC led by source vertex"""
        visited[node_id] = True
        scc.append(nodes[node_id])
        for tail_id in adj[node_id]:
            if not visited[tail_id]:
                _dfs_scc(tail_id, source_node_id, scc)

    for node_id in topological_orders:
        if not visited[node_id]:
            scc = []
            _dfs_scc(node_id, node_id, scc)
            sccs.append(scc)

    return sccs


if __name__ == "__main__":

    """
    Example Graph           SCCs
    -------------           ----
    1 → 3 → 11 → 6          1, 3, 5
     ↖ ↙     ↘  ↗ ↘         11
      5       8 ← 10        6, 10, 8
      ↓ ↘   ↗    ↗          2, 4, 7, 9
      7 → 9  → 2
        ↖ ↓  ↙
          4
    """

    # List of nodes and edges of graph
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

    sccs = kosaraju(nodes, edges)
    print(sccs)
