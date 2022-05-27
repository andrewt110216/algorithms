# Learning Algorithms
# Depth-First-Search (DFS) - Preorder Traversal (Recursive & Iterative)
# Andrew Tracey
# May 26, 2022

class TreeNode:
    """Node of a binary tree"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# RECURSIVE APPROACH
def preorder_recursive(root):

    def recurse(node, traversal):
        if node:
            traversal.append(node.val)
            recurse(node.left, traversal)
            recurse(node.right, traversal)
    
    traversal = []
    recurse(root, traversal)
    return traversal

# ITERATIVE APPROACH
def preorder_iterative(root):
    traversal = []
    cur = root
    stack = []
    while cur or stack:
        if cur:
            traversal.append(cur.val)
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
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
    funcs = [preorder_iterative, preorder_recursive]
    func_names = ['Iterative', 'Recursive']
    inputs = [[1, 2, 5, 3, 4, 6, 7],
              [],
              [4, 2, 5, None, 3]
              ]
    results = [[1, 2, 3, 4, 5, 6, 7],
               [],
               [4, 2, 3, 5]
               ]
    
    # TEST RESULTS
    i = 0
    for input, result in zip(inputs, results):
        i += 1
        print(f'TEST #{i}'.center(79, '='))
        print(' Input:', input)
        for j, func in enumerate(funcs):
            print(f'-{func_names[j]} Solution'.ljust(70, '-'))
            tree = array_to_tree(input)
            output = func(tree)
            print('  > Output:', output)
            if output == result:
                print('## Correct! ##'.center(70))
            else:
                print('## WRONG :( ##'.center(70))
                print('      > Expected:', result)
    print('-'*79)
