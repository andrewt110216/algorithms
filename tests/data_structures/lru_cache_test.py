import pytest
from data_structures.lru_cache import Node, DoublyLinkedList, LRU_Cache


class TestNode:
    """Tests for Node class"""

    def test_node_init(self):
        node = Node(1, "a")
        assert node.key == 1
        assert node.value == "a"
        assert node.prev is None
        assert node.next is None

    def test_node_str(self):
        assert str(Node(1, "a")) == "(1, 'a')"

    def test_node_repr(self):
        node = Node(1, "a")
        assert repr(node) == str(node)

    def test_node_unhashable_key(self):
        with pytest.raises(TypeError, match="must be a hashable type"):
            Node([1], "a")


class TestDoublyLinkedList:
    """Tests for DoublyLinkedList class"""

    # === Fixtures ===
    @pytest.fixture
    def new3(self):
        dll = DoublyLinkedList()
        dll.insert_end(1, "a")
        dll.insert_end(2, "b")
        dll.insert_end(3, "c")
        return dll

    @pytest.fixture
    def new3_list(self):
        return [(1, "a"), (2, "b"), (3, "c")]

    # === Tests ===
    def test_dll_init(self):
        dll = DoublyLinkedList()
        assert dll.size == 0

        assert dll._sentinal_head.key == "sentinal_head"
        assert dll._sentinal_head.value == 0
        assert dll._sentinal_head.next == dll._sentinal_tail

        assert dll._sentinal_tail.key == "sentinal_tail"
        assert dll._sentinal_tail.value == 0
        assert dll._sentinal_tail.prev == dll._sentinal_head

    def test_dll_str(self, new3, new3_list):
        assert str(new3) == str(new3_list)

    def test_dll_repr(self, new3):
        assert repr(new3) == str(new3)

    def test_dll_head(self, new3):
        head_node = new3.head
        assert head_node.key == 1
        assert head_node.value == "a"
        assert new3.size == 3

    def test_dll_tail(self, new3):
        tail_node = new3.tail
        assert tail_node.key == 3
        assert tail_node.value == "c"
        assert new3.size == 3

    def test_dll_insert_end(self, new3, new3_list):
        # Test with new
        dll = DoublyLinkedList()
        dll.insert_end(1, "a")
        assert dll.size == 1
        assert dll.head.key == 1
        assert dll.head.value == "a"
        assert dll.tail.key == 1
        assert dll.tail.value == "a"

        # Test with existing
        new3.insert_end(4, "d")
        assert new3.tail.key == 4
        assert new3.tail.value == "d"
        assert new3.size == 4
        assert new3.as_list() == new3_list + [(4, "d")]

    def test_dll_move_to_end(self, new3):
        # Move middle node
        node = new3.head.next
        new3.move_to_end(node)
        assert new3.tail.key == 2
        assert new3.tail.value == "b"
        assert new3.size == 3
        assert new3.as_list() == [(1, "a"), (3, "c"), (2, "b")]

        # Move head node
        node = new3.head
        new3.move_to_end(node)
        assert new3.tail.key == 1
        assert new3.tail.value == "a"
        assert new3.size == 3
        assert new3.as_list() == [(3, "c"), (2, "b"), (1, "a")]

        # Move tail node (no change)
        node = new3.tail
        new3.move_to_end(node)
        assert new3.tail.key == 1
        assert new3.tail.value == "a"
        assert new3.size == 3
        assert new3.as_list() == [(3, "c"), (2, "b"), (1, "a")]

    def test_dll_move_to_end_node_not_in_list(self, new3, new3_list):
        new_node = Node(5, "e")
        success = new3.move_to_end(new_node)
        assert success == -1
        assert new3.size == 3
        assert new3.as_list() == new3_list

    def test_dll_remove_front(self, new3):
        removed = new3.remove_front()
        assert removed.key == 1
        assert new3.size == 2
        assert new3.head.key == 2
        assert new3.tail.key == 3

        removed = new3.remove_front()
        assert removed.key == 2
        assert new3.size == 1
        assert new3.head.key == 3
        assert new3.tail.key == 3

        # Remove final node
        removed = new3.remove_front()
        assert removed.key == 3
        assert new3.size == 0
        assert new3._sentinal_head.next == new3._sentinal_tail
        assert new3._sentinal_tail.prev == new3._sentinal_head

        # Attempt to remove from empty list
        with pytest.raises(IndexError, match="remove from empty"):
            new3.remove_front()

    def test_dll_as_list(self, new3, new3_list):
        # Test empty
        dll = DoublyLinkedList()
        assert dll.as_list() == []

        # Test length 1
        dll.insert_end(1, "a")
        assert dll.as_list() == [(1, "a")]

        # Test existing
        assert new3.as_list() == new3_list


class TestLRUCache:
    """Tests for LRU_Cache class"""

    # === Fixtures ===
    @pytest.fixture
    def new3(self):
        lru = LRU_Cache(3)
        lru.set(1, "a")
        lru.set(2, "b")
        lru.set(3, "c")
        return lru

    @pytest.fixture
    def new3_list(self):
        return [(1, "a"), (2, "b"), (3, "c")]

    # === Tests ===
    def test_lru_basic_examples(self, new3):
        # Should evict key 1 to add key 4 as tail
        new3.set(4, "d")
        assert new3.as_list() == [(2, "b"), (3, "c"), (4, "d")]

        # Should return 'b' and move key 2 to tail
        out = new3.get(2)
        assert out == "b"
        assert new3.as_list() == [(3, "c"), (4, "d"), (2, "b")]

        # Should evict key 3 to add key 5 as tail
        new3.set(5, "e")
        assert new3.as_list() == [(4, "d"), (2, "b"), (5, "e")]

    def test_lru_init(self):
        lru = LRU_Cache(10)
        assert lru.capacity == 10
        assert isinstance(lru.cache, DoublyLinkedList)
        assert lru.cache.size == 0
        assert lru.key_to_node_map == {}

    def test_lru_str(self, new3, new3_list):
        assert str(new3) == str(new3_list)

    def test_lru_repr(self, new3):
        assert repr(new3) == str(new3)

    def test_lru_size(self, new3):
        # Test with empty
        lru = LRU_Cache(10)
        assert lru.size == 0

        # Test with existing
        assert new3.size == 3

    def test_lru_set_new(self):
        lru = LRU_Cache(3)
        lru.set(1, "a")
        assert lru.size == 1
        assert 1 in lru
        assert lru.get(1) == "a"
        assert lru.as_list() == [(1, "a")]

        # Add another item
        lru.set(2, "b")
        assert lru.size == 2
        assert 2 in lru
        assert lru.get(2) == "b"
        assert lru.as_list() == [(1, "a"), (2, "b")]

    def test_lru_set_existing(self, new3):
        # Overwrite the value of an existing key
        new3.set(1, "z")
        assert new3.size == 3  # no change in size
        assert new3.get(1) == "z"
        assert new3.cache.tail.key == 1  # most recently used
        assert new3.cache.head.key == 2  # least recently used
        assert new3.as_list() == [(2, "b"), (3, "c"), (1, "z")]

        # Add a new key to a list at capacity, evicting key 2
        new3.set(4, "d")
        assert new3.size == 3  # no change in size
        assert new3.get(4) == "d"
        assert 2 not in new3
        assert new3.cache.tail.key == 4  # most recently used
        assert new3.cache.head.key == 3  # least recently used
        assert new3.as_list() == [(3, "c"), (1, "z"), (4, "d")]

    def test_lru_get(self, new3):
        # Not in cache
        assert new3.get(4) is None

        # In cache, moving key to tail
        assert new3.get(1) == "a"
        assert new3.cache.tail.key == 1

    def test_as_list(self, new3, new3_list):
        # Test empty
        lru = LRU_Cache(3)
        assert lru.as_list() == []

        # Test length 1
        lru.set(1, "a")
        assert lru.as_list() == [(1, "a")]

        # Test existing
        assert new3.as_list() == new3_list
