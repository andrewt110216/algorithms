"""
An API to represent a Singly-Linked List of integers and provide basic
operations, including insert, delete, search, and sort
"""

from __future__ import annotations


# TODO: handle errors that would be caused by a list with a cycle


class ListNode:
    """Represent a node of a singly-linked list"""

    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return (
            f"<ListNode {self.val} -> "
            f"({self.next.val if self.next else 'None'})>"
        )

    def __str__(self):
        return self.__repr__()


class LinkedList:
    """Represent a singly-linked list"""

    def __init__(self, node_values: list[int] = []):
        self._prehead = ListNode()
        self._tail = None
        self._length = 0
        if node_values:
            self.from_array(node_values)

    def __len__(self):
        return self._length

    def __eq__(self, list2):
        """Compare self to another linked list for equality"""
        if type(list2) != LinkedList:
            return False
        cur1 = self.get_head()
        cur2 = list2.get_head()
        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        if cur1 or cur2:
            return False
        return True

    def is_empty(self):
        """Return self._length == 0"""
        return self._length == 0

    def get_head(self):
        """Return head node"""
        return self._prehead.next

    def get_tail(self):
        """Return tail node"""
        return self._tail

    def insert(self, index: int, value: int):
        """Insert a new node at index"""
        n = self._length
        if index < 0 or index > n:
            raise IndexError
        cur = 0
        prev = self._prehead
        while cur <= n and prev:
            if cur == index:
                new_node = ListNode(value)
                tmp = prev.next
                prev.next = new_node
                new_node.next = tmp
                self._length += 1
                if cur == self._length - 1:
                    self._tail = new_node
                break
            prev = prev.next
            cur += 1

    def from_array(self, items: list[int]):
        """Add items from array to end of list"""
        prev = self._tail if self._tail else self._prehead
        for item in items:
            new_node = ListNode(item)
            prev.next = new_node
            prev = new_node
        self._length += len(items)
        self._tail = prev

    def get_value(self, index: int) -> int:
        """Return value of node at index"""
        if not 0 <= index < self._length:
            raise IndexError
        cur = self.get_head()
        for _ in range(index):
            cur = cur.next
        return cur.val

    def find_value(self, target: int) -> int:
        """Return index of first occurence of target value in self"""
        cur_idx = 0
        cur = self.get_head()
        while cur:
            if cur.val == target:
                return cur_idx
            cur = cur.next
            cur_idx += 1
        raise ValueError

    def count(self, target: int) -> int:
        """Count number of ocurrences of target value in self"""
        count = 0
        cur = self.get_head()
        while cur:
            if cur.val == target:
                count += 1
            cur = cur.next
        return count

    # TODO
    def find_all(self, target: int) -> list:
        """Return indices of all occurences of target value in self"""
        pass

    def pop(self) -> int:
        """Delete tail node and return its value"""
        pass

    def pop_left(self) -> int:
        """Delete head node and return its value"""
        pass

    def push(self) -> None:
        """Push a new node to end of list"""
        pass

    def push_left(self) -> None:
        """Push a new node to front of list"""
        pass

    def to_array(self) -> list:
        """Return a traditional list representation of self"""
        pass

    def show(self) -> None:
        """Print items of self as a traditional list"""
        print(self.to_array())

    def delete(self, target: int) -> None:
        """Delete first occurence of target value from self"""
        pass

    def delete_index(self, index: int) -> None:
        """Delete node at index from self"""
        pass

    def copy(self) -> LinkedList:
        """Return a copy of self"""
        pass

    def reverse(self) -> None:
        """Reverse elements of self"""
        pass

    def sort(self, descending: bool = False) -> None:
        """Sort list nodes by value"""
        pass

    def sorted(self, descending: bool = False) -> LinkedList:
        """Return a copy of list with nodes sorted by value"""
        pass

    def has_cycle(self) -> bool:
        """Check if self has a cycle, using Floyd's cycle-finding algorithm"""
        pass
