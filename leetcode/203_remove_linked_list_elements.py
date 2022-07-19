# Leetcode Problem #203
# Remove Linked List Elements

# CATEGORY
# Linked Lists

# PROBLEM DESCRIPTION
# Given the head of a linked list and an integer val, remove all the nodes of
# the linked list that has Node.val == val, and return the new head. 

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# Constraints
# The number of nodes in the list is in the range [0, 10^4].
# 1 <= Node.val <= 50
# 0 <= val <= 50


debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

# ADDED FUNCTIONS TO CONVERT BETWEEN LINKED LIST AND ARRAY FOR TESTING
def to_array(head):
    """Turn the list into an array"""
    if head is None:
        return []
    array = []
    cur_node = head
    while cur_node.next:
        array.append(cur_node.val)
        cur_node = cur_node.next
    array.append(cur_node.val)
    return array

def from_array(array):
    """Build a Linked List from an array"""
    n = len(array)
    if n == 0:
        return None
    if n == 1:
        return ListNode(array[0])
    else:
        head = ListNode(array[0])
        prev = head
        i = 1
        while i < n:
            new_node = ListNode(array[i])
            prev.next = new_node
            prev = prev.next
            i += 1
    return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(head, val):
    """Remove each occurence of val from the list starting at head"""
    if head is None:
        return head
    prehead = ListNode(val=0, next=head)
    prev = prehead
    while prev.next is not None:
        if prev.next.val == val:
            prev.next = prev.next.next
        else:
            prev = prev.next
    return prehead.next


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
            print('Input:', to_array(args[0]), args[1])
            result = to_array(func(*args, **kwargs))
            print('Output:', result)

            if result == expected:
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
    args = [from_array([1,2,6,3,4,5,6]), 6]
    kwargs = {}
    expected_result = [1,2,3,4,5]
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    args = [from_array([]), 1]
    kwargs = {}
    expected_result = []
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 3'
    args = [from_array([7,7,7,7]), 7]
    kwargs = {}
    expected_result = []
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
