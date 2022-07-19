# Leetcode Problem #617
# Merge Two Binary Trees

# CATEGORY
# DFS / BFS

# PROBLEM DESCRIPTION
# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other, some nodes of the 
# two trees are overlapped while the others are not. You need to merge the two 
# trees into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of the new tree.
# Return the merged tree.
# Note: The merging process must start from the root nodes of both trees.

# Example 1:
#     1        2               3
#    / \      / \             / \
#   3   2    1   3   === >   4   5
#  /          \   \         / \   \
# 5            4   7       5   4   7
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]

# Example 2:
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]

# Constraints
# The number of nodes in both trees is in the range [0, 2000].
# -10^4 <= Node.val <= 10^4

# AT NOTES
# With solution1, I assumed that the inputs were provided as lists representing
# binary trees...if only. They are actually provided as LC TreeNodes.
# So for the real solution, I will use a breadth-first-search through both 
# trees, simultaneously

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """Pre-order traversal of both trees, recursive"""
    def recurse(root1, root2):
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root3 = TreeNode(root1.val + root2.val)
        root3.left = recurse(root1.left, root2.left)
        root3.right = recurse(root1.right, root2.right)
        return root3
    return recurse(root1, root2)

# Test helper functions to convert between arrays and trees
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


# =============================== DRIVER CODE ================================

if __name__ == '__main__':

    # ------------------------------------------------------------------------
    # Set to true to see debugging print statements, if any
    debug = False

    tests = 0
    failed_tests = 0
    divider_width = 78

# Decorator Function for Testing Output --------------------------------------


    def test_decorator(func):
        """Decorator function to wrap around the solution"""
        def wrapper(expected, description, *args, **kwargs):
            global tests, failed_tests, divider_width
            tests += 1
            print(f" TEST CASE: {description} ".center(divider_width, "-"))
            print('Input:', *args, **kwargs)
            args = [array_to_tree(arg) for arg in args]
            result = tree_to_array(func(*args, **kwargs))
            print('Output:', result)

            if result == expected:
                print("\n > Test Result: **PASS!**\n")
            else:
                print("\n > Test Result: **FAIL.**\n")
                print(f"\t > Expected Result: {expected_result}\n")
                failed_tests += 1

        return wrapper

    solution = test_decorator(solution)

# ADD TEST CASES HERE--------------------------------------------------------

    # Test Case Block
    test_case_description = 'Example 1'
    args = [[1,3,2,5], [2,1,3,None,4,None,7]]
    kwargs = {}
    expected_result = [3,4,5,5,4,None,7]
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = [[1], [1,2]]
    kwargs = {}
    expected_result = [2,2]
    solution(expected_result, test_case_description, *args, **kwargs)

# SUMMARY ====================================================================

    print(f" ALL RESULTS ".center(divider_width, "="))
    print(f"\nTOTAL TESTS RUN: {tests}")
    print("\nOVERALL RESULT:\n")
    if failed_tests:
        print(f"\t{failed_tests} test(s) failed.\n")
        print("\t===========")
        print("\t|| FAIL. ||")
        print("\t===========")
    else:
        print(f"\tAll tests passed! Niceee.\n")
        print("\t===========")
        print("\t|| PASS! ||")
        print("\t===========")
    print("".center(divider_width, '='))
