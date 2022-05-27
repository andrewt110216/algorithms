"""
A set of classes and functions to convert between linked lists and lists.

These are useful for testing LeetCode solutions, allowing linked-lists to be
input as lists, and to convert linked-list outputs back to a list in order
to verify the result.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode " + str(linked_list_to_array(self))

def linked_list_to_array(head):
    """Convert a linked list to an array"""
    array = []
    if head:
        cur = head
        while cur and cur.next:
            array.append(cur.val)
            cur = cur.next
        array.append(cur.val)
    return array

def array_to_linked_list(array):
    """Convert an array to a linked list"""
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
    return head

# Tests
if __name__ == '__main__':

    def test(in_lst):
        """Test conversion functions: list -> linked list -> list"""
        print('New Test'.center(79, '-'))
        print('Input List:', in_lst, type(in_lst))
        out_ll = array_to_linked_list(in_lst)
        print('> Convert to Linked List:', out_ll, type(out_ll))
        out_lst = linked_list_to_array(out_ll)
        print('> Convert Back to List:', out_lst, type(out_lst))
        if out_lst == in_lst:
            print('  > SUCCESS! The end list matches the input list.')
        else:
            print('  > FAILURE. The end list does not match the input list.')
            print('  > FAILURE. The end list does not match the input list.')

    test1 = [1, 2, 3]
    test(test1)
    
    test2 = [1]
    test(test2)

    test3 = []
    test(test3)
