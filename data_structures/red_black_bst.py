"""
A set of classes to implement a Red-Black BST (Binary Search Tree).

The RedBlackBST class is the API to implement a Red-Black BST.

A Red-Black BST is a self-balancing BST that ensures the height of the tree is
always O(logn), where n is the number of nodes in the tree. More precisely, the
height of the tree bounded above by 2log(n + 1).

As a result, it provides worst-case runtime of O(logn) for lookup, insertion,
and deletion.

Time Complexity
Operation |  Worst  | Average |  Best 
--------------------------------------
Find         O(logn)  O(logn)    O(1)
Insert       O(logn)  O(logn)    O(1)
Delete       O(logn)  O(logn)    O(1)
Print        O(n)     O(n)       O(n)

Example
-------
from data_structures.red_black_bst import RedBlackBST



"""
from collections import deque


class Node:
    "Represent a Node of a Red-Black BST"

    def __init__(self, key, val=None, color=0):
        """
        Initialize a new node for a Red-Black BST to store a key-value pair

        The BST will be sorted bassed on key.
        A node has pointers to its parent and its left and right children.
        A node is colored Red or Black, represented by 1 or 0, respectively.
        """
        self.key = key
        self.val = val
        self.parent: Node = None
        self.left: Node = None
        self.right: Node = None
        self.color = color  # 1 = Red, 0 = Black


class RedBlackBST:
    """
    An API for a Red-Black Binary Search Tree (BST)

    Duplicate keys are not allowed. Inserting a duplicate key will update the
    value for that key.
    """

    colors = ['b', 'r']

    def __init__(self):
        "Initialize a new, empty Red-Black BST"
        self.NIL = Node('x', color = 0)  # universal NIL node
        self.root = self.NIL
        self.size = 0

    def __str__(self):
        levels, max_len = self._level_order()
        depth = len(levels)
        line_width = 2**depth * (max_len + 2)  # FIGURE OUT SPACING
        out = ''
        CRED = '\033[91m'
        CEND = '\033[0m'
        for i, level in enumerate(levels):
            line = ''
            space = (depth - i)  # FIGURE OUT SPACING
            extra_color_chars = 0
            for key, color in level:
                if color:
                    line += CRED
                    extra_color_chars += 9
                line += f"{key}".center(max_len + 1)
                if color:
                    line += CEND
                line += " " * space
            line = line.center(line_width + extra_color_chars)
            out += line + '\n'
        return out[:-2]

    def _level_order(self):
        """Return the level-order traversal of the tree including NIL nodes as
        a list of lists AND returns the max str-length of any key"""
        levels = []
        queue = deque([self.root])
        max_len = 0
        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    level.append((curr.key, curr.color))
                    max_len = max(max_len, len(str(curr.key)))
                    queue.append(curr.left)
                    queue.append(curr.right)
            levels.append(level)
        return levels, max_len

    def insert(self, key, value = None):
        "Insert a new key-value pair or update the value for an existing key"

        # 1. Insert just as in standard BST, coloring new node Red
        self.root = self._insert(key, value, self.root)

    def _insert(self, key, value, root):
        "Helper function for recursive insertion"

        # if root is NIL, we want to insert new node in its place
        if root == self.NIL:
            new_node = Node(key, value)
            new_node.color = 1  # insert as Red node
            new_node.left = new_node.right = self.NIL  # set children as NIL
            return new_node

        # since we do not allow duplicate keys, if root has same key, then just
        # update its value and return it
        if root.key == key:
            root.val = value
            return root

        # otherwise, search left or right for key
        if key < root.key:
            root.left = self._insert(key, value, root.left)
        else:
            root.right = self._insert(key, value, root.right)

        return root

    def delete(self, key):
        pass

    def find(self, value):
        pass


if __name__ == "__main__":

    # Initialize a new BST with some initial data
    bst = RedBlackBST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(6)
    bst.insert(10)
    print(bst)
