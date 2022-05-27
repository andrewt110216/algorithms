# Learning Algorithms
# Breadth-First-Search (BFS) - Level Order Traversal
# Andrew Tracey
# May 26, 2022

from collections import deque

class TreeNode:
    """Node of a binary tree"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    
    if root is None:
        return []

    traversal = []
    q = deque()
    q.append(root)
    while q:
        cur = q.popleft()
        traversal.append(cur.val)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)

    return traversal


# DRIVER CODE =================================================================
if __name__ == '__main__':

    # helper function
    def array_to_tree(array: list) -> TreeNode:
        """Convert a list to a binary tree"""
        if len(array) == 0:
            return None
        def recurse(i=0):
            if i > len(array) - 1 or array[i] is None:
                return None
            node = TreeNode(array[i])
            node.left = recurse(2 * i + 1)
            node.right = recurse(2 * i + 2)
            return node
        return recurse()

    # TEST INPUTS
    inputs = [[1, 2, 3, 4, 5, 6, 7],
              [],
              [4, 2, 5, None, 3]
              ]
    results = [[1, 2, 3, 4, 5, 6, 7],
               [],
               [4, 2, 5, 3]
               ]
    
    # TEST RESULTS
    i = 0
    for input, result in zip(inputs, results):
        i += 1
        print(f'TEST #{i}'.center(79, '='))
        print(' Input:', input)
        tree = array_to_tree(input)
        output = level_order(tree)
        print('  > Output:', output)
        if output == result:
            print('## Correct! ##'.center(70))
        else:
            print('## WRONG :( ##'.center(70))
            print('      > Expected:', result)
    print('-'*79)
