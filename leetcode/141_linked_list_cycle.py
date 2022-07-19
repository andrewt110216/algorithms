# Leetcode Problem #141
# Linked List Cycle

# CATEGORY
# Linked Lists, Two Pointers

# PROBLEM DESCRIPTION
# Given head, the head of a linked list, determine if the linked list has a
# cycle in it. There is a cycle in a linked list if there is some node in the
# list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next
# pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects
# to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects
# to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Constraints
# The number of the nodes in the list is in the range [0, 104].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.

# Follow Up
# Can you solve it using O(1) (i.e. constant) memory?

# AT NOTES
# Traverse the linked list, saving each node in a dictionary. At each
# new node, check to see if node.next is in the dict. If we get to a
# Null node.next, then there is no cycle (return False).

debug = False  # DO NOT CHANGE HERE. False for file import. Change below.

# ================================= SOLUTION =================================

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return f'({self.val})'

def solution(head: ListNode) -> bool:
    """Use a fast and slow pointer. Space O(1)."""
    if head is not None:
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
    return False

def solution1(head: ListNode) -> bool:
    """Traverse the list, tracking visited nodes in a set. Space O(n)"""
    if head is None:
        return False
    current = head
    visited = {head}
    while current.next is not None:
        if current.next in visited:
            return True
        else:
            visited.add(current.next)
            current = current.next
    return False


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
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    args = [head]
    kwargs = {}
    expected_result = True
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 2'
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    args = [head]
    kwargs = {}
    expected_result = True
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Example 3'
    head = ListNode(1)
    args = [head]
    kwargs = {}
    expected_result = False
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Empty'
    head = None
    args = [head]
    kwargs = {}
    expected_result = False
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Longer List Without Cycle'
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = ListNode(5)
    args = [head]
    kwargs = {}
    expected_result = False
    solution(expected_result, test_case_description, *args, **kwargs)

    # Test Case Block
    test_case_description = 'Two Elements'
    head = ListNode(1)
    head.next = ListNode(2)
    args = [head]
    kwargs = {}
    expected_result = False
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
