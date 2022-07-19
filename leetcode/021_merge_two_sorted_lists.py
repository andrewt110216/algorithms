# Leetcode Problem #21
# Merge Two Sorted Lists

# CATEGORY
# Linked Lists, Recursion

# PROBLEM DESCRIPTION
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by
#  splicing together the nodes of the first two lists.
# Return the *head* of the merged linked list.


# Example 1:
# Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]
#  where the above "lists" actually represent Node objects

# Example 2:
#

# Constraints
#

# Follow Up
#

# AT NOTES
# 

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

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


def solution(list1: ListNode, list2: ListNode) -> ListNode:
    """Recursive solution"""

    def recurse(list1, list2):

        # Base Case
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        # Identify smaller head node, recurse to merge remainder
        head = ListNode()
        merged = head
        if list1.val < list2.val:
            merged.val = list1.val
            list1 = list1.next
        else:
            merged.val = list2.val
            list2 = list2.next
        merged.next = recurse(list1, list2)
        return head

    return recurse(list1, list2)

def solution1(list1: ListNode, list2: ListNode) -> ListNode:
    """Iterative solution"""
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
            result = func(*args, **kwargs)
            print('Output:', result)

            if str(result) == str(expected):
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
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    args = [list1, list2]
    kwargs = {}
    expected_result = ListNode(1, ListNode(1, ListNode(2, ListNode(3, 
        ListNode(4, ListNode(4))))))
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = ' Add Duplicates and Negatives'
    list1 = ListNode(-2, ListNode(0, ListNode(1, ListNode(4, ListNode(4)))))
    list2 = ListNode(-8, ListNode(-2, ListNode(-1, ListNode(0, ListNode(3)))))
    args = [list1, list2]
    kwargs = {}
    expected_result = ListNode(-8, ListNode(-2, ListNode(-2, ListNode(-1, 
        ListNode(0, ListNode(0, ListNode(1, ListNode(3, ListNode(4, 
            ListNode(4))))))))))
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    list1 = None
    list2 = None
    args = [list1, list2]
    kwargs = {}
    expected_result = None
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 3'
    list1 = None
    list2 = ListNode(0)
    args = [list1, list2]
    kwargs = {}
    expected_result = ListNode(0)
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
