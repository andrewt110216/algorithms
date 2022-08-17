# 203 - Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

from data_structures.class_linked_list import ListNode, list_to_ll


class Solution:

    # list the methods to be run against the test cases
    implementations = ["remove_elements"]

    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        """
        Traverse the list using a pointer to the previous node, and if
        the current node (prev.next) has value `val`, remove it from the list
        by setting prev.next to prev.next.next

        We must add a sentinal node before head, to handle the case where the
        head node needs to be removed

        Time: O(n) (traverse the list once)
        Space: O(1) (constant additional space is used)
        """

        # check for empty input
        if head is None:
            return head

        # create a sentinal node for ease of traversal, in case the head node
        # needs to be removed
        prehead = ListNode(val=0, next=head)
        prev = prehead

        # traverse the list until the current node (prev.next) is null
        while prev.next:

            # if current node == val, remove it from the list
            if prev.next.val == val:
                prev.next = prev.next.next

            # otherwise, move to the next node
            else:
                prev = prev.next

        # return head of updated list
        return prehead.next


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        [
            "Example 1",
            [list_to_ll([1, 2, 6, 3, 4, 5, 6]), 6],
            list_to_ll([1, 2, 3, 4, 5]),
        ],
        ["Example 2", [list_to_ll([]), 1], None],
        ["Example 3", [list_to_ll([7, 7, 7, 7]), 7], None],
        [
            "Every Other Val",
            [list_to_ll([5, 2, 5, 7, 5, 4, 5]), 5],
            list_to_ll([2, 7, 4]),
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
