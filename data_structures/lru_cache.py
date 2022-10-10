"""
A set of classes to implement an LRU (Least Recently Used) Cache.

An LRU Cache stores a limited capacity of key-value pairs, where keys must be
hashable and values can be any literal or object. In order to add a new item to
a cache that is at capacity, the least recently 'used' item is evicted to make
room for the new item. In this API, an item, k, is 'used' when `get(k)` or
`set(k, val)` is called.

The LRU_Cache class is the API to implement an LRU Cache.

Example
-------
from data_structures.lru_cache import LRU_Cache

lru = LRU_Cache(3)  # capacity = 3
lru.set(1, 'a')
lru.set(2, 'b')
lru.set(3, 'c')
print(lru)          # [(1, 'a'), (2, 'b'), (3, 'c')]
                    # ^ least recently used        ^ most recently used

lru.set(4, 'd')     # key 1 is evicted to add 4 to the end
print(lru)          # [(2, 'b'), (3, 'c'), (4, 'd')]

lru.get(2)          # returns 'b', and moves key 2 to end
print(lru)          # [(3, 'c'), (4, 'd'), (2, 'b')]

lru.set(5, 'e')     # key 3 is evicted to add 5 to the end
print(lru)          # [(4, 'd'), (2, 'b'), (5, 'e')]
"""

from typing import Hashable


class Node:
    """Represent a node of a doubly-linked list"""

    def __init__(self, key: Hashable, value: object):
        """Initialize a new node with empty pointers"""

        # Check that key is hashable
        try:
            hash(key)
        except TypeError:
            raise TypeError(f"Key must be a hashable type not {type(key)}.")

        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str((self.key, self.value))

    def __repr__(self):
        return str(self)


class DoublyLinkedList:
    """Represent a doubly-linked list"""

    def __init__(self):
        """Initialize an empty doubly-linked list"""

        # Use sentinal nodes to access actual head and tail nodes
        self._sentinal_head = Node("sentinal_head", 0)
        self._sentinal_tail = Node("sentinal_tail", 0)

        # Initialize sentinal nodes to point to eachother
        self._sentinal_head.next = self._sentinal_tail
        self._sentinal_tail.prev = self._sentinal_head

        self.size = 0

    def __str__(self):
        return str(self.as_list())

    def __repr__(self):
        return str(self)

    @property
    def head(self):
        """Return the actual head node of the list"""
        if self.size > 0:
            return self._sentinal_head.next
        raise IndexError("Empty doubly-linked list has no head")

    @property
    def tail(self):
        """Return the actual tail node of the list"""
        if self.size > 0:
            return self._sentinal_tail.prev
        raise IndexError("Empty doubly-linked list has no tail")

    def insert_end(self, key: Hashable, value: object) -> Node:
        """Insert new item as the tail and return its Node object"""

        # Create new node and set pointers
        new_node = Node(key, value)
        new_node.next = self._sentinal_tail
        new_node.prev = self._sentinal_tail.prev

        # Insert at end of list
        self._sentinal_tail.prev.next = new_node
        self._sentinal_tail.prev = new_node
        self.size += 1

        return new_node

    def move_to_end(self, node: Node) -> int:
        """
        Move `node` from its current position in the list to the tail.
        Returns 1 if successful or -1 if unsucessful.

        This method is not meant to be called with a node that is not already
        in the list. Doing so can break the doubly-linked list by inserting
        `node` without incrementing `size`.

        The user must ensure that `node` is a list member.
        """

        # Simple check to prevent some cases where node is not in the list:
        # - all nodes in the list have both next and prev pointers set.
        # In order to maintain O(1), this is not a comprehensive check
        if node.next is None or node.prev is None:
            return -1

        # Remove node from its current position
        node.next.prev = node.prev
        node.prev.next = node.next

        # Insert at end of list
        node.next = self._sentinal_tail
        node.prev = self._sentinal_tail.prev
        self._sentinal_tail.prev.next = node
        self._sentinal_tail.prev = node

        return 1

    def remove_front(self) -> Node:
        """Remove and return the head node of the list"""

        # Check for empty list
        if self.size == 0:
            raise IndexError("Cannot remove from empty doubly-linked list")

        # Remove node from list
        removed_node = self._sentinal_head.next
        self._sentinal_head.next = removed_node.next
        removed_node.next.prev = self._sentinal_head

        self.size -= 1
        return removed_node

    def as_list(self):
        """Return node keys/values as list of tuples with head first"""
        out = []
        cur = self._sentinal_head.next
        while cur.next:
            out.append((cur.key, cur.value))
            cur = cur.next
        return out


class LRU_Cache:
    """An API for an LRU (Least Recently Used) Cache"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = DoublyLinkedList()
        self.key_to_node_map = {}

    @property
    def size(self):
        """The number of items currently stored in the cache"""
        return self.cache.size

    def __str__(self):
        return str(self.as_list())

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.cache.size

    def __contains__(self, key):
        return key in self.key_to_node_map

    def set(self, key, value):
        """Add or update a key-value, making it the most recently used item"""
        if key in self.key_to_node_map:
            node = self.key_to_node_map[key]
            node.value = value
            self.cache.move_to_end(node)
        else:
            if self.cache.size == self.capacity:
                evicted_node = self.cache.remove_front()
                del self.key_to_node_map[evicted_node.key]
            new_node = self.cache.insert_end(key, value)
            self.key_to_node_map[key] = new_node

    def get(self, key):
        """Return the value of key and make it the most recently used item"""
        if key in self.key_to_node_map:
            node = self.key_to_node_map[key]
            self.cache.move_to_end(node)
            return node.value

    def as_list(self):
        """Return cached values as list with least recently used item first"""
        return self.cache.as_list()
