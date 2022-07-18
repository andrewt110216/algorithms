# Learning Algorithms
# Calculating Strongly Connected Components (SCC's) of a Graph
# Andrew Tracey
# July 7-18, 2022

# Stanford Algorithms Specialization
# Class 2 - Week 1 - Programming Assignment

# DESCRIPTION
# Your task is to compute the strongly connected components (SCCs) in the graph,
# as provided by the input text file, listing all the edges of the graph, which
# has nodes numbered from 1 to 875,714.

# You should output the sizes of the 5 largest SCCs in the given graph, in
# decreasing order of sizes, separated by commas (avoid any spaces).
# So if your algorithm computes the sizes of the five largest SCCs to be 500,
# 400, 300, 200 and 100, then your answer should be "500,400,300,200,100"
# (without the quotes). If your algorithm finds less than 5 SCCs, then write 0
# for the remaining terms.

# Method:
# Kosaraju's Algorithm
# 1. Let G' = G with all edges reveresed.
#    - Perform a DFS loop over all nodes, computing the 'finishing position' of
#      each node, defined as the order at which the node completes its own DFS.
# 2. Perform a 2nd DFS loop over all nodes, with the outer loop processing nodes
#    in the reverse order of their finishing positions (e.g. starting with the 
#    nth finishing node, down to the 1st finishing node).
#    - Each DFS initiated from the for loop will reveal a new SCC.

# NOTES
# 1. Given the size of the input, we will not be able to implement DFS using
#    recursion; the call stack will exceed the maximum recursion depth.
#    Therefore, we will need to use an iterative algorithm.
# 2. We must come up with a way to efficiently access all edges out AND in (for
#    the reversed graph) of a given node. For the input size, we do not want to
#    wait to do this by traversing the list of edges for each node. Instead, we
#    will create lists of length n + 1 (ignoring list index 0, since the nodes
#    start counting from 1), where index i is a list of all nodes accessbile
#    from node i. We will have a list for G and G'. While this is time consuming
#    since we have to traverse the edges 2 times, it is strictly an O(m) step,
#    which does not hurt our overall Big O run time ( O(m + n) ).

# ============================== IMPLEMENTATION ==============================
from collections import deque

class Kosaraju():
    """Use Kosaraju's algorithm to calculate Strongly Connected Components"""

    def __init__(self, filename, n):
        """
        Initialize graph data from input file and execute Kosaraju's algorithm
        to calculate a list of the SCC's
        
        :param str filename: the relative path to a text file containing the
            edges of the graph, with an edge on each line as: 'tail head'
        """
        # node labels start at 1, so add 1 to align list indexes to node labels
        self._lst_len = n + 1
        self._read_graph(filename)
        self._get_finishing_order()
        self._get_sccs()

    def _read_graph(self, filename):
        """Read edges from file and generate adjacency lists for G and G' """
        with open('algorithms/' + filename) as f:
            lines = f.readlines()
        # g[1] = [2, 3] => the edges out of node 1 are (1, 2) and (1, 3)
        self.g = [[] for _ in range(self._lst_len)]
        self.g_rev = [[] for _ in range(self._lst_len)]
        for line in lines:
            tail, head = map(int, line.strip().split())
            self.g[tail].append(head)
            self.g_rev[head].append(tail)

    def _get_finishing_order(self):
        """Run DFS loop over g_rev and calculate the finishing orders"""
        # order[0] = 6 => node 6 finished first
        self.finishing_order = []
        explored = [False] * self._lst_len
        finished = [False] * self._lst_len
        for node in range(self._lst_len - 1, 0, -1):
            if not explored[node]:
                stack = deque([node])
                while stack:
                    cur = stack.pop()
                    if not explored[cur]:
                        explored[cur] = True
                        stack.append(cur)
                        for neighbor in self.g_rev[cur]:
                            if not explored[neighbor]:
                                stack.append(neighbor)
                    else:
                        if not finished[cur]:
                            self.finishing_order.append(cur)
                            finished[cur] = True

    def _get_sccs(self):
        """Discover SCC's using the previously calculated finishing orders"""
        all_scc = []
        explored = [False] * self._lst_len
        for node in reversed(self.finishing_order):
            if not explored[node]:
                cur_scc = []
                stack = deque([node])
                while stack:
                    cur = stack.pop()
                    if not explored[cur]:
                        cur_scc.append(cur)
                        explored[cur] = True
                        stack.append(cur)
                        for neighbor in self.g[cur]:
                            if not explored[neighbor]:
                                stack.append(neighbor)
                all_scc.append(cur_scc)
        self.all_scc = all_scc

    def get_top_5_scc_sizes(self):
        top_5 = sorted(self.all_scc, key=lambda scc: -len(scc))[:5]
        return [len(top_5[i]) if i < len(top_5) else 0 for i in range(5)]

# ================================ DRIVER CODE ================================

if __name__ == '__main__':

    # ----- Run Test Cases & Optionally Add The Assignment Case -----
    add_assignment = True
    filename_base = 'kosaraju-inputs/kosaraju_scc_input'
    cases_failed = 0
    # cases[i - 1] = [graph size, expected result]
    cases = [
        [9, [3, 3, 3, 0, 0]],
        [8, [3, 3, 2, 0, 0]],
        [8, [3, 3, 1, 1, 0]],
        [8, [7, 1, 0, 0, 0]],
        [12, [6, 3, 2, 1, 0]],
        [4, [1,1,1,1,0]],
    ]
    if add_assignment:
        cases.append([875714, [434821, 968, 459, 313, 211]])

    print('\n--- RUNNING CASES ---')
    for i, case in enumerate(cases):
        graph_size, expected_result = case
        if graph_size == 875714:
            print('Solution to Assignment:')
            filename = f'{filename_base}.txt'
        else:
            print(f'Test Case #{i + 1}:')
            filename = f'{filename_base}_test{i+1}.txt'
        kosaraju = Kosaraju(filename, graph_size)
        result = kosaraju.get_top_5_scc_sizes()
        print(' > Result:', result)
        if expected_result == result:
            print('   > Passed')
        else:
            cases_failed += 1
            print('   > Failed')
            print('   - Expected:', expected_result)

# Summarize results
print('\n--- SUMMARY ---')
print(f'Ran {len(cases)} cases and failed {cases_failed} case(s).')
print(f'*** RESULT:', ['PASS', 'FAIL'][cases_failed > 0], '***\n')
