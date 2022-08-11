class Heap:
    """Represent a min heap"""

    def __init__(self, items: iter = []):
        self.size = 0
        self.items = []
        if items:
            self.heapify(items)

    def __repr__(self):
        return f"<Heap {str(self.items[:self.size])}>"

    def __eq__(self, heap2):
        """Compare two heaps for equality of both items and heap size"""
        if self.size != heap2.size:
            return False
        if self.items[: self.size] != heap2.items[: heap2.size]:
            return False
        return True

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def get_parent(self, child_index: int) -> int:
        """Return the index of the parent node of a given node index"""
        if child_index > 0:
            return (child_index + 1) // 2 - 1
        return None

    def has_left_child(self, parent_index: int) -> bool:
        """Check if a node index has a left child"""
        if 2 * parent_index + 1 < self.size:
            return True
        return False

    def has_right_child(self, parent_index: int) -> bool:
        """Check if a node index has a right child"""
        if 2 * parent_index + 2 < self.size:
            return True
        return False

    def get_left_child(self, parent_index: int) -> int:
        """Get the index of the left child of a given node index"""
        if self.has_left_child(parent_index):
            return 2 * parent_index + 1
        return None

    def get_right_child(self, parent_index: int) -> int:
        """Get the index of the right child of a given node index"""
        if self.has_right_child(parent_index):
            return 2 * parent_index + 2
        return None

    def insert(self, new_item: object) -> None:
        """Insert a new node to the heap"""
        self.items.append(new_item)
        self.size += 1
        self.heapify_up()

    def extract_min(self) -> object:
        min_val = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return min_val

    def swap(self, index1: int, index2: int) -> None:
        """Swap items at index1 and index2"""
        temp = self.items[index1]
        self.items[index1] = self.items[index2]
        self.items[index2] = temp

    def heapify(self, new_items):
        """Insert new items into the heap, naively"""
        for new_item in new_items:
            self.insert(new_item)

    def heapify_up(self) -> None:
        index = self.size - 1
        while index > 0:
            parent_index = self.get_parent(index)
            if self.items[parent_index] > self.items[index]:
                self.swap(index, parent_index)
                index = parent_index
            else:
                return

    def heapify_down(self) -> None:
        index = 0
        while self.has_left_child(index):
            smaller_child = self.get_left_child(index)
            if self.has_right_child(index):
                right_child = self.get_right_child(index)
                if self.items[right_child] < self.items[smaller_child]:
                    smaller_child = right_child
            self.swap(index, smaller_child)
            index = smaller_child


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

    print("".center(78, "="))
    print()
