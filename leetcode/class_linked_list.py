class ListNode:
    """Represent a node of a linked list"""

    def __init__(self, val=0, next=None):
        """Initialize the node value and next pointer"""
        self.val = val
        self.next = next

    def __repr__(self):
        """Represent the ListNode with a list of each node value"""
        return "<ListNode " + str(ll_to_list(self)) + ">"

    def __eq__(self, other):
        """
        Two ListNodes are equal if their list representations are equal

        Examples:
        <ListNode [1, 2, 3]> == <ListNode [1, 2, 3]>
        <ListNode [1, 2]> != <ListNode [1, 2, 3]>
        <ListNode [1, 2]> != <ListNode [1, 3]>
        """
        if not isinstance(other, ListNode):
            return NotImplemented

        return ll_to_list(self) == ll_to_list(other)


def ll_to_list(head):
    """Convert a linked list to a traditional list"""
    array = []
    if head:
        cur = head
        while cur and cur.next:
            array.append(cur.val)
            cur = cur.next
        array.append(cur.val)
    return array


def list_to_ll(array):
    """Convert a traditional list to a linked list"""
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


if __name__ == "__main__":

    # Display a few demonstrations of the ListNode class and related functions
    print()
    print(' Demonstrations of ListNode and Related Functions '.center(78, '='))
    print()

    # Demonstrate how to create a linked list from the ListNode class
    print(' Create a linked list from ListNodes '.center(78, '-'))
    print()

    # create nodes
    head = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    # connect them
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # print the head node to see the entire linked list
    print('> My linked list:', head)
    assert head.__repr__() == '<ListNode [0, 1, 2, 3, 4]>'
    print()

    # Demonstrate how to convert a linked list to a traditional list
    print(' Convert a linked list to a traditional list '.center(78, '-'))
    print()

    my_list = ll_to_list(head)
    print('> My linked list converted to a traditional list:', my_list)
    assert my_list == [0, 1, 2, 3, 4]
    print()

    # Demonstrate how to convert traditional list to a linked list
    print(' Convert a traditional list to a linked list '.center(78, '-'))
    print()

    my_list = [10, 9, 8, 7, 6]
    print('> My traditonal list is:', my_list)
    my_linked_list = list_to_ll(my_list)
    print('> My traditional list converted to a linked list:', my_linked_list)
    assert my_linked_list == list_to_ll([10, 9, 8, 7, 6])
    print()

    # Demonstrate comparison of linked lists
    print(' Compare two ListNodes '.center(78, '-'))
    print()

    linked_list_1 = list_to_ll([1, 2])
    linked_list_2 = list_to_ll([1, 2, 3])
    print('> linked_list_1:', linked_list_1)
    print('> linked_list_2:', linked_list_2)
    print('> Run Comparison: `linked_list_1 == linked_list_2`')
    print('  > Return:', linked_list_1 == linked_list_2)
    print()

    linked_list_1 = list_to_ll([1, 2, 3])
    print('> linked_list_1:', linked_list_1)
    print('> linked_list_2:', linked_list_2)
    print('> Run Comparison: `linked_list_1 == linked_list_2`')
    print('  > Return:', linked_list_1 == linked_list_2)
    print()

    print("".center(78, "="))
    print()
