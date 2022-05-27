# Learning Algorithms
# Floyd's Cycle Finding Algorithm
# Andrew Tracey
# May 27, 2022

# DESCRIPTION
# Goal: Determine if a given linked list has a cycle in it, using O(1) space
#  complexity. The naive approach stores seen nodes in a set, using O(n) space.
# Method: Floyd's Cycle Finding Algorithm
# Use a fast and slow pointer to traverse the list, where the fast pointer moves
# two steps to the slow pointers one step. If fast reaches the end, there is
# no cycle. If there is a cycle, fast will eventually catch up to slow and they
# will be equal 

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ============================== IMPLEMENTATION ==============================

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def array_to_linked_list(array, pos=-1):
    """
    Convert an array to a linked list, with an optional cylce
    
    :param array: list of node values
    :param pos: index of node to which 'end' node points (creating a cycle)
    :return: head node of a linked list
    """
    n = len(array)
    if n == 0:
        return None
    head = ListNode(array[0])
    prev = head
    i = 1
    while i < n:
        new_node = ListNode(array[i])
        prev.next = new_node
        prev = prev.next
        i += 1
    if pos >= 0:
        tmp = head
        for _ in range(pos):
            tmp = tmp.next
        prev.next = tmp
    return head

def algorithm(head):
    """Determine if a linked list has a cycle in it"""
    # APPROACH: Floyd's Cycle Finding Algorithm (Fast & Slow Pointers)
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    # We reached the end, therefore there is not a cycle from the end
    return False

# ================================ TEST CASES ================================

if __name__ == '__main__':
    from datetime import datetime

# ----------------------------------------------------------------------------
# Set to true to see debugging print statements, if any, from execution
    debug = False
# ----------------------------------------------------------------------------

    tests = 0
    failed_tests = 0
    divider_width = 78

# Decorator Function for Testing Output --------------------------------------

    def test_decorator(func):
        """Decorator function to wrap around the algorithm"""
        def wrapper(expected, description, *args, **kwargs):
            global tests, failed_tests, divider_width
            tests += 1
            print(f" TEST CASE: {description} ".center(divider_width, "-"))
            print('Input:', *args, **kwargs)
            start = datetime.now()
            args = [array_to_linked_list(*args)]
            result = func(*args, **kwargs)
            print('Output:', result)
            print('Time:', datetime.now() - start)

            if result == expected:
                print("\n > Test Result: **PASS!**\n")
            else:
                print("\n > Test Result: **FAIL.**\n")
                print(f"\t > Expected Output: {expected_result}\n")
                failed_tests += 1

        return wrapper

    # For testing, decorate the algorithm function
    algorithm = test_decorator(algorithm)

# ADD TEST CASES HERE--------------------------------------------------------

    # Test Case Block
    test_case_description = 'Example 1'
    args = [[3,2,0,-4], 1]
    kwargs = {}
    expected_result = True
    algorithm(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = [[1,2], 0]
    kwargs = {}
    expected_result = True
    algorithm(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 3'
    args = [[1], -1]
    kwargs = {}
    expected_result = False
    algorithm(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 4'
    args = [[1, 2, 3, 4, 5, 6, 7], 5]
    kwargs = {}
    expected_result = True
    algorithm(expected_result, test_case_description, *args, **kwargs)
    
    # Test Case Block
    test_case_description = 'Example 5'
    args = [[1, 2, 3, 4, 5, 6, 7, 8], 5]
    kwargs = {}
    expected_result = True
    algorithm(expected_result, test_case_description, *args, **kwargs)

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
