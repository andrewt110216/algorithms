# Learning Algorithms
# Depth-First-Search (DFS) - Inorder Traversal (Recursive & Iterative)
# Andrew Tracey
# May 26, 2022

class TreeNode:
    """Node of a binary tree"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# RECURSIVE APPROACH
def inorder_recursive(root):

    def recurse(node, traversal):
        if node:
            recurse(node.left, traversal)
            traversal.append(node.val)
            recurse(node.right, traversal)

    traversal = []
    recurse(root, traversal)
    return traversal

# ITERATIVE APPROACH
def inorder_iterative(root):
    traversal = []
    stack = []
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            traversal.append(cur.val)
            cur = cur.right
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
    funcs = [inorder_iterative, inorder_recursive]
    inputs = [[4, 2, 5, 1, 3],
              [],
              [4, 2, 5, None, 3]
              ]
    results = [[1, 2, 3, 4, 5],
               [],
               [2, 3, 4, 5]
               ]
    
    # TEST RESULTS
    i = 0
    for input, result in zip(inputs, results):
        i += 1
        print(f'TEST #{i}'.center(79, '='))
        print(' Input:', input)
        for func in funcs:
            if func == inorder_iterative:
                print('-Iterative Solution'.ljust(70, '-'))
            else:
                print('-Recursive Solution'.ljust(70, '-'))
            tree = array_to_tree(input)
            output = func(tree)
            print('  > Output:', output)
            if output == result:
                print('## Correct! ##'.center(70))
            else:
                print('## WRONG :( ##'.center(70))
                print('      > Expected:', result)
    print('-'*79)
