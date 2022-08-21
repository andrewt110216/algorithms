import pytest
from data_structures.linked_list import ListNode, LinkedList


class TestNode:
    """Tests for ListNode class"""

    # Fixtures
    @pytest.fixture
    def new_node(self):
        return ListNode()

    # Tests
    def test_create_node(self):
        node = ListNode()
        assert node.val == 0
        assert node.next is None
        assert str(node) == repr(node) == "<ListNode 0 -> (None)>"

    def test_update_value(self, new_node):
        new_node.val = 10
        assert new_node.val == 10
        assert str(new_node) == "<ListNode 10 -> (None)>"

    def test_add_next(self, new_node):
        new_node.val = 10
        new_node.next = ListNode(1)
        assert str(new_node) == "<ListNode 10 -> (1)>"
        assert str(new_node.next) == "<ListNode 1 -> (None)>"


class TestLinkedList:
    """Tests for LinkedList class"""

    # Fixtures
    @pytest.fixture
    def new_list(self):
        return LinkedList()

    @pytest.fixture
    def list_two(self, new_list):
        new_list.insert(0, 1)
        new_list.insert(1, 2)
        return new_list

    @pytest.fixture
    def array_ten(self):
        return [5, 8, 3, 4, 9, 10, 2, 1, 7, 6]

    @pytest.fixture
    def list_ten(self, new_list, array_ten):
        new_list.from_array(array_ten)
        return new_list

    # Tests

    # Initialization
    def test_create_new_list(self):
        my_list = LinkedList()
        assert my_list._prehead.val == 0
        assert my_list._prehead.next is None
        assert my_list._tail is None
        assert my_list._length == 0

    # Linked list length
    def test_len(self, new_list):
        assert len(new_list) == 0

    def test_len_ten(self, list_ten):
        assert len(list_ten) == 10

    def test_is_empty(self, new_list):
        assert new_list.is_empty()

    def test_is_empty_false(self, list_two):
        assert not list_two.is_empty()

    # Insert
    def test_insert_into_new_successful(self, new_list):
        new_list.insert(0, 2)
        assert len(new_list) == 1
        assert new_list.get_head().val == 2
        assert new_list.get_tail().val == 2

    def test_insert_into_new_error(self, new_list):
        for i in [-1, 1, 2]:
            with pytest.raises(IndexError):
                new_list.insert(i, 2)

    def test_insert_at_head(self, list_two):
        list_two.insert(0, -1)
        assert list_two.get_head().val == -1
        assert len(list_two) == 3
        assert list_two.get_tail().val == 2

    def test_insert_at_tail(self, list_two):
        list_two.insert(2, 3)
        assert list_two.get_head().val == 1
        assert len(list_two) == 3
        assert list_two.get_tail().val == 3

    # Insert from array
    def test_from_array_new_one(self, new_list):
        new_list.from_array([1])
        assert new_list.get_head().val == 1
        assert new_list.get_tail().val == 1
        assert len(new_list) == 1

    def test_from_array_new_two(self, new_list):
        new_list.from_array([1, 2])
        assert new_list.get_head().val == 1
        assert new_list.get_tail().val == 2
        assert len(new_list) == 2

    def test_from_array_new_ten(self, new_list, array_ten):
        new_list.from_array(array_ten)
        assert len(new_list) == 10
        head = new_list.get_head()
        assert head.val == 5
        assert head.next.next.val == 3
        assert head.next.next.next.next.val == 9
        assert new_list.get_tail().val == 6

    def test_create_new_list_with_array(self, array_ten, list_ten):
        my_list = LinkedList(array_ten)
        assert my_list == list_ten
        assert id(my_list) != id(list_ten)

    # Get value by position
    def test_get_head_none(self, new_list):
        assert len(new_list) == 0
        assert new_list.get_head() is None

    def test_get_head_ten(self, list_ten):
        assert len(list_ten) == 10
        assert list_ten.get_head().val == 5

    def test_get_tail_none(self, new_list):
        assert len(new_list) == 0
        assert new_list.get_tail() is None

    def test_get_tail_ten(self, list_ten):
        assert len(list_ten) == 10
        assert list_ten.get_tail().val == 6

    def test_get_value(self, list_ten, array_ten):
        for idx, num in enumerate(array_ten):
            assert list_ten.get_value(idx) == num

    def test_get_value_error(self, list_ten):
        for index in [-1, 10, 11]:
            with pytest.raises(IndexError):
                list_ten.get_value(index)

    # Find value
    def test_find_value(self, list_ten, array_ten):
        for idx, num in enumerate(array_ten):
            assert list_ten.find_value(num) == idx

    def test_find_value_error(self, list_ten):
        for target in [-1, 3.5, 11]:
            with pytest.raises(ValueError):
                list_ten.find_value(target)

    def test_find_value_error_empty(self, new_list):
        with pytest.raises(ValueError):
            new_list.find_value(1)

    # Count
    def test_count_empty(self, new_list):
        for target in [-1, 0, 1, 10]:
            assert new_list.count(target) == 0

    def test_count_none(self, list_ten):
        for target in [-1, 3.5, 11]:
            assert list_ten.count(target) == 0

    def test_count_one(self, list_ten, array_ten):
        for target in array_ten:
            assert list_ten.count(target) == 1

    def test_count_multiple(self):
        my_list = LinkedList([2, 2, 2, 2])
        assert my_list.count(2) == 4

    # Equality
    def test_eq_empty(self, new_list):
        list2 = LinkedList()
        assert new_list == list2
        assert id(new_list) != id(list2)

    def test_eq_ten(self, list_ten, array_ten):
        list2 = LinkedList(array_ten)
        assert list_ten == list2
        assert id(list_ten) != id(list2)

    def test_eq_same_size_not_equal(self, list_ten):
        list2 = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        assert list_ten != list2

    # TODO
    # - find all
    # - pop
    # - pop_left
    # - push
    # - push_left
    # - to_array
    # - show
    # - delete
    # - delete_index
    # - copy
    # - reverse
    # - sort
    # - sorted
    # - has cycle
