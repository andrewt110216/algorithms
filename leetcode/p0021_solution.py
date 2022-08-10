# 020 - Merge Two Sorted (Linked) Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

from class_linked_list import ListNode, list_to_ll


class Solution:

    # list the methods to be run against the test cases
    implementations = ["merge_lists_recursive", "merge_lists_iterative"]

    def merge_lists_recursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Build the merged list recursively. Create a new `merged` list and set
        the value of the head node to the smaller of l1.val and l2.val. Advance
        the pointers for l1 or l2, and repeat recursively on `merged.next` to
        build the rest of the merged list

        Time: O(n + m) (one recursive call per element in each list)
        Space: O(n + m) (the call stack)
        """

        def recurse(l1, l2):

            # base case: one or both nodes are null

            # if l1 is null, the rest of l2 needs to be merged
            # or, in the case that l2 is also null, we set the next pointer of
            # the final node of merged to null (l2)
            if l1 is None:
                return l2

            # if l2 is null, the rest of l1 needs to be merged
            if l2 is None:
                return l1

            # `head` is the head of the output list and `merged` is the pointer
            head = ListNode()
            merged = head

            # set the value of merged to the smaller of l1 and l2 and advance
            # that list to the next node
            if l1.val < l2.val:
                merged.val = l1.val
                l1 = l1.next
            else:
                merged.val = l2.val
                l2 = l2.next

            # set merged.next by recursing on the rest of l1 and l2
            merged.next = recurse(l1, l2)

            # return the head of our output list
            return head

        return recurse(l1, l2)

    def merge_lists_iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        This is the merge subroutine of the merge-sort algorithm

        Traverse l1 and l2, copying the smaller node into merged, then advance
        that list and merged. When one of l1 or l2 is exhausted, copy over the
        remaining nodes from the other list

        Time: O(n + m) (one recursive call per element in each list)
        Space: O(1) (no additional data strucutre or call stack needed)
        """

        # check for empty input
        if l1 is None and l2 is None:
            return None

        # `head` is the head of the output list and `merged` is the pointer
        head = ListNode()
        merged = head

        # traverse both lists, copying smaller node into `merged`
        while l1 and l2:
            if l1.val < l2.val:
                merged.val = l1.val
                l1 = l1.next
            else:
                merged.val = l2.val
                l2 = l2.next

            # advance merged to next node, if necessary
            if l1 or l2:
                merged.next = ListNode()
                merged = merged.next

        # copy remaining nodes from l1 or l2 into merged
        while l1:
            merged.val = l1.val
            l1 = l1.next
            if l1:
                merged.next = ListNode()
                merged = merged.next
        while l2:
            merged.val = l2.val
            l2 = l2.next
            if l2:
                merged.next = ListNode()
                merged = merged.next

        return head


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    case1 = [
        "Example 1",
        list(map(list_to_ll, [[1, 2, 4], [1, 3, 4]])),
        list_to_ll([1, 1, 2, 3, 4, 4]),
    ]
    case2 = ["Example 2", list(map(list_to_ll, [[], []])), list_to_ll([])]
    case3 = ["Example 3", list(map(list_to_ll, [[], [0]])), list_to_ll([0])]
    case4 = [
        "Add Duplicates and Negatives",
        list(map(list_to_ll, [[-2, 0, 1, 4, 4], [-8, -2, -1, 0, 3]])),
        list_to_ll([-8, -2, -2, -1, 0, 0, 1, 3, 4, 4]),
    ]
    test_cases = [case1, case2, case3, case4]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
