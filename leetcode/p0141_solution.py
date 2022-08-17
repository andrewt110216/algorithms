# 141 - Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

from data_structures.class_linked_list import ListNode, list_to_ll


class Solution:

    # list the methods to be run against the test cases
    implementations = ["has_cycle_floyds", "has_cycle_dict"]

    def has_cycle_floyds(self, head: ListNode) -> bool:
        """
        Use a fast and slow pointer, known as Floyd's Cycle Finding Algorithm

        If there is a cycle in the list, eventually the fast pointer will catch
        up to the slow pointer. If there is not a cycle, then we will
        eventually find a final node with a null next pointer

        Time: O(n) (one pass through the linked list)
        Space: O(1) (all steps use constant time)
        """

        # check for empty input (which would not have a cycle in it)
        if not head:
            return False

        # set pointers
        slow = head
        fast = head.next

        # advance slow one node at a time, and fast two nodes at a time
        #  if fast catches up to slow, there is a cycle
        # we cannot directly compare slow and fast using my ListNode class
        #  since list may have a cycle. Instead, compare their memory addresses
        while slow is not fast:

            # if fast is at the end of the list, there must not be a cycle
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next  # we can do this bc we know fast.next exists

        # fast caught up to slow, therefore there was a cycle
        return True

    def has_cycle_dict(self, head: ListNode) -> bool:
        """
        Traverse head, storing previously seen nodes in a set. If we encounter
        a previously seen node before the end of the list, then there's a cycle

        Time: O(n) (one pass through the linked list)
        Space: O(n) (max size of set)
        """

        # store seen nodes in a hash set
        # since my implementation of ListNode is not hashable, I will store the
        # id's of the nodes in seen, instead of the node objects themselves
        seen = set()

        # traverse list looking for end (None) or previously seen nodes (cycle)
        while head and head.next:
            if id(head) in seen:
                return True
            seen.add(id(head))
            head = head.next

        # we reached the end of the list, therefore there was not a cycle
        return False


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]

    # case 1 and 2 have a cycle in them
    head1 = list_to_ll([3, 2, 0, -4])
    head1.next.next.next.next = head1.next
    head1.has_cycle = True  # prevent infinite recursion in __repr__

    head2 = list_to_ll([1, 2])
    head2.next.next = head2
    head2.has_cycle = True  # prevent infinite recursion in __repr__

    case1 = ["Example 1", [head1], True]
    case2 = ["Example 2", [head2], True]
    case3 = ["Example 3", [ListNode(1)], False]
    case4 = ["Empty Input", [None], False]
    case5 = ["Two Nodes, No Cycle", [list_to_ll([1, 2])], False]
    case6 = ["Longer List, No Cylce", [list_to_ll([1, 2, 0, 4, 5, 8])], False]
    test_cases = [case1, case2, case3, case4, case5, case6]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
