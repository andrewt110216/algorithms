# Leetcode Problem #148
# Sort List

# Given the head of a linked list, return the list after sorting it in 
#  ascending order.

# Example:
# Input: head = (4)->(2)->(1)->(3)
# Output: (1)->(2)->(3)->(4)
#
# Input: head = []
# Output: []

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        output = "(" + str(self.val) + ")"
        if self.next:
            output += "->" + str(self.next)
        return output

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base Case: return head if head = None or head.next = None
        if not head or not head.next:
            return head

        # Split the list into two parts
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        if debug:
            print('left:', left)
            print('right:', right)

        # Sort the two parts and merge them
        return self.merge(self.sortList(left), self.sortList(right))

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
        cur = prev_to_merged = ListNode()
        if debug:
            print('\tlist1:', list1)
            print('\tlist2:', list2)
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
        if debug: print('\treturning:', prev_to_merged.next)
        return prev_to_merged.next

# ================================ TEST CASES ================================

if __name__ == '__main__':

# ----------------------------------------------------------------------------
# Set to true to see debugging print statements, if any, from execution
    debug = False
# ----------------------------------------------------------------------------

    tests = 0
    failed_tests = 0
    divider_width = 78

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Base ".center(divider_width, "-"))
    tests += 1
    test_input = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print('Input:', test_input)
    sol = Solution()
    result = sol.sortList(test_input)
    print('Output:', result)

    expected_result = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    if str(result) == str(expected_result):
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Null Input ".center(divider_width, "-"))
    tests += 1
    test_input = []
    print('Input:', test_input)
    sol = Solution()
    result = sol.sortList(test_input)
    print('Output:', result)

    expected_result = []
    if str(result) == str(expected_result):
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Add Negatives & Zeroes ".center(divider_width, "-"))
    tests += 1
    test_input = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    print('Input:', test_input)
    sol = Solution()
    result = sol.sortList(test_input)
    print('Output:', result)

    expected_result = ListNode(-1, ListNode(0, ListNode(3, ListNode(4, ListNode(5)))))
    if str(result) == str(expected_result):
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        failed_tests += 1

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
