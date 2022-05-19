"""
A set of classes and functions to convert between binary trees and lists.

These can be useful for testing LeetCode solutions, allowing for easy creation
of binary tree inputs and easy evaluation of binary tree outputs.
"""

# Note the following properties of binary trees when represented as lists
# Let i represent the counting position, starting from 1 (i.e. index + 1),
# and n represent the length of the list
# 1. Parent Node
#      a. if i == 1, then node i has no parent node (it is the root)
#      b. if i > 1, then the parent node of i is node (i // 2)
# 2. Left Child Node
#      a. if 2i > n, then node i has no left child
#      b. if 2i <= n, then the left child of node i is node 2i
# 3. Right Child Node
#      a. if 2i + 1 > n, then node i has no right child
#      b. if 2i + 1 <= n, then the right child of node i is node 2i
# 4. Left Sibling
#      a. if i > 1 is odd, then the left sibling of node i is node i - 1
# 5. Right Sibling
#      a. if i < n is even, then the right sibling of node i is node i + 1
# 6. Level of a Node
#      a. the root node is level 1
#      b. the level of node i = floor( log2(i) ) + 1

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print(self):
        print(f'--- Visual representation of TreeNode from left to right ---')
        def recurse(self, space):
            if self == None:
                return
            space += 10
            recurse(self.right, space)
            print()
            for i in range(10, space):
                print(end = " ")
            print(self.val)
            recurse(self.left, space)
        recurse(self, 0)
        print('-'*60)
        return

    def __repr__(self):
        left = right = None
        if self.left:
            left = self.left.val
        if self.right:
            right = self.right.val
        return f"({self.val} -> l:{str(left)}, r: {str(right)})"

def array_to_tree(array: list) -> TreeNode:
    """Convert a list to a TreeNode object (binary tree)"""
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

def tree_to_array(root: TreeNode) -> list:
    """Convert a binary tree (given the root node) to a list"""
    array = []
    if root:
        import queue
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            cur = q.get()
            if cur:
                array.append(cur.val)
                q.put(cur.left)
                q.put(cur.right)
            else:
                array.append(None)
    # Clean up trailing None's
    while array[-1] is None:
        array.pop()
    return array


# Test the printed representations of a Tree
# tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3,
#         TreeNode(6), TreeNode(7)))
# print(tree1)
# tree1.print()

root1 = array_to_tree([2,1,3,None,4,None,7])
root1.print()
list1 = tree_to_array(root1)
print(list1)