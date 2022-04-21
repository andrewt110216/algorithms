# Leetcode Problem #21
# Merge Two Sorted Lists
# Andrew Tracey
# April 7, 2022

# https://leetcode.com/problems/merge-two-sorted-lists/

# PROBLEM DESCRIPTION
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by
#  splicing together the nodes of the first two lists.
# Return the *head* of the merged linked list.

# Example:
# Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]
#  where the above "lists" actually represent Node objects

# ================================= SOLUTION =================================

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val='?', next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		nodes = []
		cur_node = self
		while cur_node.next:
			nodes.append(str(cur_node.val))
			cur_node = cur_node.next
		nodes.append(str(cur_node.val))
		return "ListNode [" + ", ".join(nodes) + "]"


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    	if not list1 and not list2:
    		return None
    	merged_list_head = ListNode()
    	merged_list = merged_list_head
    	iterations = 0
    	while list1 and list2:
    		iterations += 1
    		if debug:
	    		print(f"Iteration {iterations}------")
	    		print(f'  list1.val =', list1.val)
	    		print(f'  list2.val =', list2.val)
    		if list1.val <= list2.val:
    			merged_list.val = list1.val
    			list1 = list1.next
    		else:
    			merged_list.val = list2.val
    			list2 = list2.next
    		if list1 or list2:
	    		new_node = ListNode()
	    		merged_list.next = new_node
	    		merged_list = merged_list.next
    		if debug: print(f'  merged_list_head =', merged_list_head)

    	# Copy remaining nodes in list1 or list2
    	if debug: print(f'Copying over remaining nodes...')
    	while list1:
    		if debug: print(f'  list1.val =', list1.val)
    		merged_list.val = list1.val
    		list1 = list1.next
    		if list1:
    			new_node = ListNode()
    			merged_list.next = new_node
    			merged_list = merged_list.next
    		if debug: print(f'  merged_list_head =', merged_list_head)
    	while list2:
    		if debug: print(f'  list2.val =', list2.val)
    		merged_list.val = list2.val
    		list2 = list2.next
    		if list2:
    			new_node = ListNode()
    			merged_list.next = new_node
    			merged_list = merged_list.next
    		if debug: print(f'  merged_list_head =', merged_list_head)

    	return merged_list_head


# ================================ TEST CASES ================================

# ----------------------------------------------------------------------------
# Set to true to see debugging print statements, if any, from execution
debug = True
# ----------------------------------------------------------------------------

if __name__ == '__main__':

    tests = 0
    failed_tests = 0
    divider_width = 78

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Base ".center(divider_width, "-"))
    tests += 1
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    print('Input:', list1, list2)
    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)
    print('Output:', result)

    expected_result = ListNode(1, ListNode(1, ListNode(2, ListNode(3, 
    	ListNode(4, ListNode(4))))))
    if str(result) == str(expected_result):
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        failed_tests += 1


# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Add Duplicates and Negatives ".center(divider_width, "-"))
    tests += 1
    list1 = ListNode(-2, ListNode(0, ListNode(1, ListNode(4, ListNode(4)))))
    list2 = ListNode(-8, ListNode(-2, ListNode(-1, ListNode(0, ListNode(3)))))
    print('Input:', list1, list2)
    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)
    print('Output:', result)

    expected_result = ListNode(-8, ListNode(-2, ListNode(-2, ListNode(-1, 
    	ListNode(0, ListNode(0, ListNode(1, ListNode(3, ListNode(4, 
    		ListNode(4))))))))))
    if str(result) == str(expected_result):
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"    > Expected Result was: {expected_result}")
        failed_tests += 1

# New Test Case --------------------------------------------------------------

    print(f" TEST CASE: Empty Inputs ".center(divider_width, "-"))
    tests += 1
    list1 = None
    list2 = None
    print('Input:', list1, list2)
    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)
    print('Output:', result)

    expected_result = None
    if str(result) == str(expected_result):
        print("\n > Test Result: **PASS!**\n")
    else:
        print("\n > Test Result: **FAIL.**\n")
        print(f"    > Expected Result was: {expected_result}")
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
