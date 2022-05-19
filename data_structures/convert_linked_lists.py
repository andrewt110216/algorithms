"""
A set of classes and functions to convert between linked lists and lists.

These can be useful for testing LeetCode solutions, allowing for easy creation
of linked list inputs and easy evaluation of linked list outputs.
"""

class ListNode:
    def __init__(self, val=0, next=None):
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

def linked_list_to_array(head):
    """Convert a ListNode object (linked list) to an array"""
    if head is None:
        return []
    array = []
    cur_node = head
    while cur_node.next:
        array.append(cur_node.val)
        cur_node = cur_node.next
    array.append(cur_node.val)
    return array

def array_to_linked_list(array):
    """Convert an array to a ListNode object (linked list)"""
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
