# 148 - Sort (Linked) List
# https://leetcode.com/problems/sort-list/

from data_structures.class_linked_list import ListNode, list_to_ll


class Solution:

    # list the methods to be run against the test cases
    implementations = ["sort_list"]

    def sort_list(self, head: ListNode) -> ListNode:
        """
        Use merge sort algorithm

        Time: O(n logn)
        Space: O()
        """

        # base case
        if not head or not head.next:
            return head

        # split the list into two parts
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        # sort the two parts and merge them
        return self.merge(self.sort_list(left), self.sort_list(right))

    def getMid(self, head):
        """Return the middle node of a linked list"""
        half = head
        full = head.next
        while full and full.next:
            half = half.next
            full = full.next.next
        return half

    def merge(self, list1, list2):
        """Merge two sorted linked lists"""
        cur = pre_head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:  # list2.val <= list1.val
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return pre_head.next


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    case1 = ["Example 1", [None], None]

    linked_list2 = list_to_ll([-1, 5, 3, 4, 0])
    expected_result2 = list_to_ll([-1, 0, 3, 4, 5])
    case2 = ["Example 2", [linked_list2], expected_result2]

    linked_list3 = list_to_ll([10, -2, 9, 7, 5, 4, 0, -2, -5, 8])
    expected_result3 = list_to_ll([-5, -2, -2, 0, 4, 5, 7, 8, 9, 10])
    case3 = ["Longer List", [linked_list3], expected_result3]

    test_cases = [case1, case2, case3]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
