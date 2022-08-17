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
        """Extract and return min value from heap, maintaining heap invariant"""
        extracted_min = self._items[0]
        self._items[0] = self._items[self.size - 1]
        self.size -= 1
        self._bubble_down()
        return extracted_min

    def swap(self, i1: int, i2: int) -> None:
        """Swap items at two indexes"""
        self._items[i1], self._items[i2] = self._items[i2], self._items[i1]

    def heapify(self, new_items: list[int] = []) -> None:
        """Insert new items into the heap, one at a time"""
        for new_item in new_items:
            self.insert(new_item)

    def _bubble_up(self) -> None:
        """
        Bubble last item of heap up to maintain heap invariant
        
        This method is intended for use by insert method
        """
        index = self.size - 1
        while index > 0:
            parent_index = self.get_parent(index)
            if self._items[parent_index] > self._items[index]:
                self.swap(index, parent_index)
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
            self.swap(index, smaller_child)
            index = smaller_child

    def check_invariant(self) -> bool:
        """Check if the heap is currently holding the heap invariant"""
        for idx, val in enumerate(self._items):
            if self.has_left_child(idx):
                if val > self.get_value(self.get_left_child(idx)):
                    return False
            if self.has_right_child(idx):
                if val > self.get_value(self.get_right_child(idx)):
                    return False
        return True

if __name__ == "__main__":

    # Display a few demonstrations of the Heap class
    print()
    print(" Demonstrations of the Heap Class ".center(78, "="))
    print()

    # Demonstrate how to heapify a traditional list
    print(" Heapify a traditional list ".center(78, "-"))
    print()
    my_list = [10, 16, 8, 11, 9, 4, 5, 13, 22, 7]
    print("> My traditonal list is:", my_list)
    my_heap = Heap(my_list)
    print("> My heap is:", my_heap)
    print()

    # Demonstrate inserting into a heap
    print(" Insert into a heap ".center(78, "-"))
    print()
    new_item = 2
    print("> The value to be inserted is:", new_item)
    my_heap.insert(new_item)
    print("> My updated heap is:", my_heap)
    print()

    # Demonstrate adding multiple new items to an existing heap
    print(" Add multiple new items to an existing heap ".center(78, "-"))
    print()
    new_items = [6, 1, 23, 12]
    print("> The new items to add are:", new_items)
    my_heap.heapify(new_items)
    print("> My updated heap is:", my_heap)
    print()

    # Demonstrate extracting the minimum value from a heap
    print(" Extract the min value from a heap ".center(78, "-"))
    print()
    print("> The min value from the heap was:", my_heap.extract_min())
    print("> My updated heap is:", my_heap)
    print("\n> Let's do it again!...")
    print("> The min value from the heap was:", my_heap.extract_min())
    print("> My updated heap is:", my_heap)
    print("\n> Heck, let's extract min until we can no more!...")
    while not my_heap.is_empty():
        print(f" > Extracted min: {my_heap.extract_min()}")
    print("> My updated heap is:", my_heap)
    print("> Wow, looks like we just sorted our items in O(nlogn) time! ;)")
    print()

    # Demonstrate comparison of heaps
    print(" Compare Two Heaps For Equality ".center(78, "-"))
    print()

    heap_1 = Heap([5, 4, 3, 2, 1])
    heap_2 = Heap([5, 4, 3, 2, 1])
    print("> heap_1:", heap_1)
    print("> heap_2:", heap_2)
    print("> Run Comparison: `heap_1 == heap_2`")
    print("  > Return:", heap_1 == heap_2)
    print("> Prove that heap_1 is not the SAME heap as heap_2:")
    print(f"  > ID(heap_1): {id(heap_1)}, ID(heap_2): {id(heap_2)}")
    assert heap_1 == heap_2
    assert id(heap_1) != id(heap_2)
    print()

    heap_1 = Heap([1, 2, 3, 4])
    heap_2 = Heap([1, 2, 3])
    print("> heap_1:", heap_1)
    print("> heap_2:", heap_2)
    print("> Run Comparison: `heap_1 == heap_2`")
    print("  > Return:", heap_1 == heap_2)
    assert heap_1 != heap_2
    print()

    # Demonstrate checking the heap invariant
    print(" Confirm that the heap invariant is maintained".center(78, "-"))
    print()

    my_heap = Heap([5, 4, 3, 2, 1])
    print("> my_heap:", my_heap)
    print("> Check Invariant: `my_heap.check_invariant()")
    print("  > Return:", my_heap.check_invariant())
    assert my_heap.check_invariant()
    print()

    # Demonstrate why the programmer should not modify the heap items directly
    print(" A programmer should NOT modify heap._items ".center(78, "-"))
    print()

    print("> IMPROPERLY modify the heap items by: `my_heap._items.append(0)`")
    my_heap._items.append(0)
    print("> Then, IMPROPERLY increase the heap size by: `my_heap.size += 1`")
    my_heap.size += 1
    print("> my_heap is now invalid:", my_heap)
    print("> Check Invariant: `my_heap.check_invariant()")
    print("  > Return:", my_heap.check_invariant())
    assert not my_heap.check_invariant()
    print()

    print("".center(78, "="))
    print()
