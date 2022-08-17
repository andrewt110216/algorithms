# 619 - Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/

from data_structures.class_binary_tree import TreeNode, array_to_tree


class Solution:

    # list the methods to be run against the test cases
    implementations = ["merge_trees"]

    def merge_trees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        Pre-order traversal of both trees, recursive

        Time: O()
        Space: O()
        """

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


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        [
            "Example 1",
            [
                array_to_tree([1, 3, 2, 5]),
                array_to_tree([2, 1, 3, None, 4, None, 7]),
            ],
            array_to_tree([3, 4, 5, 5, 4, None, 7]),
        ],
        [
            "Example 2",
            [array_to_tree([1]), array_to_tree([1, 2])],
            array_to_tree([2, 2]),
        ],
        [
            "Empty Input",
            [array_to_tree([]), array_to_tree([])],
            array_to_tree([]),
        ],
        [
            "All Overlap",
            [
                array_to_tree([10, 20, 30, 40, 50]),
                array_to_tree([1, 2, 3, 4, 5]),
            ],
            array_to_tree([11, 22, 33, 44, 55]),
        ],
        [
            "No Overlap",
            [
                array_to_tree([0, 1, None, 3, 4]),
                array_to_tree([0, None, 2, None, None, 5, 6]),
            ],
            array_to_tree([0, 1, 2, 3, 4, 5, 6]),
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
