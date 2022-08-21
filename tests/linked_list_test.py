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
    def array_twos(self):
        return [2, 2, 2, 2]

    @pytest.fixture
    def list_ten(self, array_ten):
        return LinkedList(array_ten)

    @pytest.fixture
    def list_twos(self, array_twos):
        return LinkedList(array_twos)

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
        assert head.val == array_ten[0]
        assert head.next.next.val == array_ten[2]
        assert head.next.next.next.next.val == array_ten[4]
        assert new_list.get_tail().val == array_ten[-1]

    def test_create_new_list_with_array(self, array_ten, list_ten):
        my_list = LinkedList(array_ten)
        assert my_list == list_ten
        assert id(my_list) != id(list_ten)

    # Get value by position
    def test_get_head_none(self, new_list):
        with pytest.raises(IndexError, match='not get head'):
            new_list.get_head()

    def test_get_head_ten(self, list_ten, array_ten):
        assert len(list_ten) == 10
        assert list_ten.get_head().val == array_ten[0]

    def test_get_tail_none(self, new_list):
        with pytest.raises(IndexError, match='not get tail'):
            new_list.get_tail()

    def test_get_tail_ten(self, list_ten, array_ten):
        assert len(list_ten) == 10
        assert list_ten.get_tail().val == array_ten[-1]

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

    def test_find_all_empty(self, new_list):
        assert new_list.find_all(1) == []

    def test_find_all_one(self, list_ten, array_ten):
        assert list_ten.find_all(5) == [array_ten.index(5)]
        assert list_ten.find_all(9) == [array_ten.index(9)]
        assert list_ten.find_all(6) == [array_ten.index(6)]

    def test_find_all_three(self):
        my_list = LinkedList([0, 5, 0, 5, 5, 0])
        assert my_list.find_all(0) == [0, 2, 5]
        assert my_list.find_all(5) == [1, 3, 4]

    def test_find_all_every(self, array_twos):
        my_list = LinkedList(array_twos)
        assert my_list.find_all(2) == [0, 1, 2, 3]

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

    def test_count_multiple(self, array_twos):
        my_list = LinkedList(array_twos)
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

    # Pop
    def test_pop_error(self, new_list):
        with pytest.raises(IndexError, match="not pop from empty"):
            new_list.pop()

    def test_pop_left_error(self, new_list):
        with pytest.raises(IndexError, match="not pop from empty"):
            new_list.pop_left()

    def test_pop_ten(self, list_ten, array_ten):
        for i in range(10):
            assert list_ten.pop() == array_ten[9 - i]
            assert len(list_ten) == 9 - i
        assert list_ten.is_empty()

    def test_pop_left_ten(self, list_ten, array_ten):
        for i in range(10):
            assert list_ten.pop_left() == array_ten[i]
            assert len(list_ten) == 9 - i
        assert list_ten.is_empty()

    def test_pop_one(self):
        my_list = LinkedList([1])
        assert len(my_list) == 1
        assert my_list.pop() == 1
        assert my_list.is_empty()

    def test_pop_left_one(self):
        my_list = LinkedList([1])
        assert len(my_list) == 1
        assert my_list.pop_left() == 1
        assert my_list.is_empty()

    # To array
    def test_to_array_empty(self, new_list, capsys):
        assert new_list.to_array() == []
        new_list.show()
        assert capsys.readouterr().out == "[]\n"

    def test_to_array_ten(self, list_ten, array_ten, capsys):
        assert list_ten.to_array() == array_ten
        list_ten.show()
        assert capsys.readouterr().out == str(array_ten) + "\n"

    def test_to_array_twos(self, list_twos, array_twos, capsys):
        assert list_twos.to_array() == array_twos
        list_twos.show()
        assert capsys.readouterr().out == str(array_twos) + "\n"

    def test_to_array_one(self, capsys):
        my_list = LinkedList([4])
        assert my_list.to_array() == [4]
        my_list.show()
        assert capsys.readouterr().out == "[4]\n"

    # Push
    def test_push_empty(self, new_list):
        new_list.push(1)
        new_list.push(2)
        new_list.push(3)
        assert len(new_list) == 3
        assert new_list.get_head().val == 1
        assert new_list.get_tail().val == 3
        assert new_list.to_array() == [1, 2, 3]

    def test_push_left_empty(self, new_list):
        new_list.push_left(1)
        new_list.push_left(2)
        new_list.push_left(3)
        assert len(new_list) == 3
        assert new_list.get_head().val == 3
        assert new_list.get_tail().val == 1
        assert new_list.to_array() == [3, 2, 1]

    def test_push_ten(self, list_ten):
        list_ten.push(15)
        assert list_ten.get_tail().val == 15
        assert len(list_ten) == 11

    def test_push_left_ten(self, list_ten):
        list_ten.push_left(-15)
        assert list_ten.get_head().val == -15
        assert len(list_ten) == 11

    # TODO
    # - delete
    # - delete_index
    # - copy
    # - reverse
    # - sort
    # - sorted
    # - has cycle
