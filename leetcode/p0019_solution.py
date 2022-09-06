# 19 - Remove Nth Node From End of Linked List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from data_structures.linked_list_node import ListNode, list_to_ll


class Solution:

    # list the methods to be run against the test cases
    implementations = ["two_pass", "two_pointer"]

    def two_pass(self, head: ListNode, n: int) -> ListNode:
        """
        Traverse the list to determine the length.
        Then, traverse the list again, stopping prior to the target node.

        Time: O(2 * length) = O(length)
        Space: O(1)
        """

        # Set up a sentinal node
        prehead = ListNode(0, head)

        # Traverse the list to find the length
        length = 0
        cur = prehead
        while cur.next:
            cur = cur.next
            length += 1

        # Take (length - n) steps from prehead to find target's predecessor
        cur = prehead
        for _ in range(length - n):
            cur = cur.next

        # Remove target node
        cur.next = cur.next.next

        # Return head of list using sentinal node
        return prehead.next

    def two_pointer(self, head: ListNode, n: int) -> ListNode:
        """
        Use two pointers, fast and slow, both starting at a sentinal prehead.
        Advance the fast pointer n times, so it is n steps ahead of slow.
        Now, advance both pointers one step at a time until fast.next = None.
        The slow pointer is now the predecessor to the target node.

        Time: O(length * 2) = O(length)
        Space: O(1)
        """

        # Set up a sentinal node and pointers
        prehead = ListNode(0, head)
        slow = fast = prehead

        # Start the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Advance both pointers until the fast pointer is the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove target node from linked list
        slow.next = slow.next.next

        # Return head of list
        return prehead.next


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    import sys
    import random
    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        [
            "Example 1",
            [list_to_ll([1, 2, 3, 4, 5]), 2],
            list_to_ll([1, 2, 3, 5]),
        ],
        ["Example 2", [list_to_ll([1]), 1], list_to_ll([])],
        ["Example 3", [list_to_ll([1, 2]), 1], list_to_ll([1])],
    ]

    # Add a large test case in order to compare runtime of two algorithms
    size = 3_000
    sys.setrecursionlimit(size * 10)
    lst = [random.randint(1, size + 1) for _ in range(size)]
    n = random.randint(0, size - 1)
    expected = lst.copy()
    expected.pop(size - n)
    large_test = ["Large Input", [list_to_ll(lst), n], list_to_ll(expected)]
    test_cases.append(large_test)

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
