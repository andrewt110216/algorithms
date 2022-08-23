from __future__ import annotations


class Heap:
    """
    An API to represent a Heap of integers and provide basic Heap operations,
    including heapify, insert, and extract_min
    """

    def __init__(self, items: list[int] = []):
        self.size = 0
        self._items = []
        if items:
            self.heapify(items)

    def __repr__(self):
        return f"<Heap {str(self._items[:self.size])}>"

    def __str__(self):
        return f"<Heap {str(self._items[:self.size])}>"

    def __eq__(self, heap2: Heap):
        """Return self.items[:self.size] == heap2._items[:heap2.size]"""
        return self._items[: self.size] == heap2._items[: heap2.size]

    def is_empty(self) -> bool:
        """Return self.size == 0"""
        return self.size == 0

    def get_items(self) -> list:
        """Return a copy of the items of the heap"""
        return self._items.copy()

    def get_value(self, i: int) -> int:
        """Return the value at index i in the heap"""
        return self._items[i]

    def get_index(self, value: int) -> int:
        """Return the index of the first occurrence of value in Heap"""
        return self._items.index(value)

    def get_parent(self, index: int) -> int:
        """Get the parent index of an index, if it exists"""
        if index > 0 & index < self.size:
            return (index + 1) // 2 - 1
        return None

    def has_left_child(self, index: int) -> bool:
        """Check if an index has a left child"""
        return index >= 0 and (2 * index + 1 < self.size)

    def has_right_child(self, index: int) -> bool:
        """Check if an index has a right child"""
        return index >= 0 and (2 * index + 2 < self.size)

    def get_left_child(self, index: int) -> int:
        """Get the left child index of an index, if it exists"""
        if self.has_left_child(index):
            return 2 * index + 1
        return None

    def get_right_child(self, index: int) -> int:
        """Get the right child index of an index, if it exists"""
        if self.has_right_child(index):
            return 2 * index + 2
        return None

    def count_value(self, value: int) -> int:
        """Count the number of occurrences of value in Heap"""
        return self._items.count(value)

    def insert(self, value: int) -> None:
        """Insert a new node, maintaining the heap invariant"""
        self._items.append(value)
        self.size += 1
        self._bubble_up()

    def extract_min(self) -> int:
        """Extract and return min val from heap, maintaining heap invariant"""
        extracted_min = self._items[0]
        self._items[0] = self._items[self.size - 1]
        self._items.pop()
        self.size -= 1
        self._bubble_down()
        return extracted_min

    def _swap(self, i1: int, i2: int) -> None:
        """
        Swap items at two indexes

        This method is inteded for use by _bubble_up and _bubble_down.
        It is discouraged to use _swap directly as it does not force the heap
        invariant to be maintained.
        """
        self._items[i1], self._items[i2] = self._items[i2], self._items[i1]

    def heapify(self, new_items: list[int] = []) -> None:
        """Insert new items into the heap, one at a time"""
        for new_item in new_items:
            self.insert(new_item)

    def copy(self) -> Heap:
        """Return a copy of the heap"""
        new_heap = Heap()
        new_heap.size = self.size
        new_heap._items = self._items.copy()
        return new_heap

    def heap_sort(self, empty=True) -> list:
        """
        Return a sorted list of the heap elements

        If 'empty' is True (default), this will leave the heap empty
        Set to False to preserve the heap, as is, by using a copy for sorting
        """
        sorted = []
        if empty:
            while not self.is_empty():
                sorted.append(self.extract_min())
        else:
            heap_copy = self.copy()
            while not heap_copy.is_empty():
                sorted.append(heap_copy.extract_min())
        return sorted

    def _bubble_up(self) -> None:
        """
        Bubble last item of heap up to maintain heap invariant

        This method is intended for use by insert method
        """
        index = self.size - 1
        while index > 0:
            parent_index = self.get_parent(index)
            if self._items[parent_index] > self._items[index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                return

    def _bubble_down(self) -> None:
        """
        Bubble first item of heap down to maintain heap invariant

        This method is intended for use by extract_min method
        """
        index = 0
        while self.has_left_child(index):
            smaller_child = self.get_left_child(index)
            if self.has_right_child(index):
                right_child = self.get_right_child(index)
                if self.get_value(right_child) < self.get_value(smaller_child):
                    smaller_child = right_child
            if self.get_value(index) > self.get_value(smaller_child):
                self._swap(index, smaller_child)
                index = smaller_child
            else:
                break

    def check_invariant(self) -> bool:
        """Check if the heap is currently holding the heap invariant"""
        if self.size > 1:
            for idx, val in enumerate(self._items):
                if self.has_left_child(idx):
                    if val > self.get_value(self.get_left_child(idx)):
                        return False
                if self.has_right_child(idx):
                    if val > self.get_value(self.get_right_child(idx)):
                        return False
        return True
