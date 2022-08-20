import pytest
from data_structures.heap import Heap


# Fixtures
@pytest.fixture
def new_heap():
    return Heap()


@pytest.fixture
def list_ten():
    return [9, 10, 7, 8, 6, 5, 3, 4, 1, 2]


@pytest.fixture
def heap_ten(new_heap, list_ten):
    new_heap.heapify(list_ten)
    return new_heap


@pytest.fixture
def heap_ten_expected_items():
    return [1, 2, 5, 4, 3, 9, 6, 10, 7, 8]


# Tests
def test_create_heap(new_heap):
    assert new_heap.size == 0
    assert new_heap._items == []
    assert new_heap.is_empty()


def test_insert_into_heap(new_heap):
    new_heap.insert(4)
    assert new_heap.size == 1
    assert new_heap._items[0] == 4


def test_heapify_on_new_heap(new_heap, list_ten, heap_ten_expected_items):
    new_heap.heapify(list_ten)
    assert new_heap.size == 10
    assert new_heap._items == heap_ten_expected_items


def test_check_heap_invariant_true(heap_ten):
    assert heap_ten.check_invariant()


def test_check_heap_invariant_false_end(heap_ten, heap_ten_expected_items):
    heap_ten._items.append(0)
    heap_ten.size += 1
    assert heap_ten._items == heap_ten_expected_items + [0]
    assert not heap_ten.check_invariant()


def test_check_heap_invariant_false_start(heap_ten, heap_ten_expected_items):
    heap_ten._items.insert(0, 3)
    heap_ten.size += 1
    assert heap_ten._items == [3] + heap_ten_expected_items
    assert not heap_ten.check_invariant()


def test_heap_equality(heap_ten, list_ten):
    heap_ten2 = Heap()
    heap_ten2.heapify(list_ten)
    assert id(heap_ten) != id(heap_ten2)
    assert heap_ten == heap_ten2


def test_heap_inequality(heap_ten):
    heap_ten2 = Heap()
    heap_ten2.heapify([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert heap_ten != heap_ten2


def test_extract_min(heap_ten):
    assert heap_ten.extract_min() == 1


def test_extract_min_until_empty(heap_ten):
    for i in range(1, 11):
        extracted_min = heap_ten.extract_min()
        assert extracted_min == i
        assert heap_ten.check_invariant()
    assert heap_ten.is_empty()


def test_copy_heap(heap_ten):
    heap_copy = heap_ten.copy()
    assert id(heap_copy) != id(heap_ten)
    assert heap_copy == heap_ten


def test_heap_sort_empty(heap_ten, list_ten):
    sorted = heap_ten.heap_sort(empty=True)
    list_ten.sort()
    assert sorted == list_ten
    assert heap_ten.is_empty()


def test_heap_sort_do_not_empty(heap_ten, list_ten, heap_ten_expected_items):
    sorted = heap_ten.heap_sort(empty=False)
    list_ten.sort()
    assert sorted == list_ten
    assert heap_ten._items == heap_ten_expected_items


def test_heapify_into_existing_heap(heap_ten):
    heap_ten.heapify([0, -5, 12, 5, -2, 8, 14])
    assert heap_ten.size == 17
    assert heap_ten.check_invariant()


def test_swap_method(heap_ten):
    item0 = heap_ten.get_value(0)
    item5 = heap_ten.get_value(5)
    heap_ten._swap(0, 5)
    assert heap_ten.get_value(0) == item5
    assert heap_ten.get_value(5) == item0


def test_get_children_methods(heap_ten):
    assert heap_ten.get_left_child(0) == 1
    assert heap_ten.get_right_child(0) == 2
    assert heap_ten.get_left_child(1) == 3
    assert heap_ten.get_right_child(1) == 4
    assert heap_ten.get_left_child(2) == 5
    assert heap_ten.get_right_child(2) == 6
    assert heap_ten.get_left_child(10) is None
    assert heap_ten.get_right_child(10) is None


def test_get_parent_method(heap_ten):
    assert heap_ten.get_parent(0) is None
    assert heap_ten.get_parent(1) == 0
    assert heap_ten.get_parent(2) == 0
    assert heap_ten.get_parent(3) == 1
    assert heap_ten.get_parent(4) == 1
    assert heap_ten.get_parent(10) == 4


def test_bubble_up(heap_ten):
    heap_ten._items.append(0)
    heap_ten.size += 1
    heap_ten._bubble_up()
    assert heap_ten.check_invariant()
    assert heap_ten.get_value(0) == 0


def test_bubble_down(heap_ten):
    heap_ten._items.insert(0, 12)
    heap_ten.size += 1
    heap_ten._bubble_down()
    assert heap_ten.check_invariant()


def test_str_and_repr(heap_ten):
    assert str(heap_ten) == "<Heap [1, 2, 5, 4, 3, 9, 6, 10, 7, 8]>"
    assert repr(heap_ten) == "<Heap [1, 2, 5, 4, 3, 9, 6, 10, 7, 8]>"
