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
    print(heap_ten)
    for i in range(1, 11):
        extracted_min = heap_ten.extract_min()
        print(i, extracted_min, heap_ten)
        assert extracted_min == i
        assert heap_ten.check_invariant()
    assert heap_ten.is_empty()


# TODO: Add tests for the following
# - copy heap
# - heap sort
# - insert multiple items at once into heap
# - swap method
# - bubble up and bubble down methods
# - get left child, right, child and parent methods
# - after tests are successful, consider deleting the in-file tests...
