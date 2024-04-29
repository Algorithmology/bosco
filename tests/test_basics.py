import pytest
import random

# Assuming your functions are in a file named list_functions.py
from bosco.list_processing.basics import (get_first_item, get_last_item, get_list_length,
                            reverse_list, sort_list, append_item, remove_item,
                            count_item, clear_list, insert_item, delete_random_item,
                            copy_list, list_in, extend, index, pop, minimum, maximum,
                            filter_list, map_list, reduce_list, zip_lists, flatten_list)

def test_get_first_item():
    assert get_first_item([1, 2, 3]) == 1
    assert get_first_item([]) is None

def test_get_last_item():
    assert get_last_item([1, 2, 3]) == 3
    assert get_last_item([]) is None

def test_get_list_length():
    assert get_list_length([1, 2, 3]) == 3
    assert get_list_length([]) == 0

def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([]) == []

def test_sort_list():
    assert sort_list([3, 1, 2]) == [1, 2, 3]
    assert sort_list([]) == []

def test_append_item():
    lst = [1, 2]
    assert append_item(lst, 3) == [1, 2, 3]

def test_remove_item():
    assert remove_item([1, 2, 3, 2], 2) == [1, 3, 2]
    assert remove_item([1, 2, 3], 4) == [1, 2, 3]  # Item not in list

def test_count_item():
    assert count_item([1, 1, 2, 3, 1], 1) == 3
    assert count_item([], 1) == 0

def test_clear_list():
    assert clear_list([1, 2, 3]) == []

def test_insert_item():
    assert insert_item([1, 3], 1, 2) == [1, 2, 3]

def test_delete_random_item():
    lst = [1, 2, 3]
    random.seed(0)  # Setting seed for reproducibility in test
    assert delete_random_item(lst) == [1, 3]

def test_copy_list():
    lst = [1, 2, 3]
    assert copy_list(lst) == lst

def test_list_in():
    assert list_in([1, 2, 3], 1) is True
    assert list_in([1, 2, 3], 4) is False

def test_extend():
    assert extend([1, 2], [3, 4]) == [1, 2, 3, 4]

def test_index():
    assert index([1, 2, 3], 3) == 2
    with pytest.raises(ValueError):
        index([1, 2, 3], 4)

def test_pop():
    lst = [1, 2, 3]
    assert pop(lst) == 3
    assert pop(lst, 0) == 1

def test_min():
    assert minimum([1, 2, 3]) == 1

def test_max():
    assert maximum([1, 2, 3]) == 3

def test_filter_list():
    assert filter_list([1, 2, 3, 4], lambda x: x > 2) == [3, 4]

def test_map_list():
    assert map_list([1, 2, 3], lambda x: x * x) == [1, 4, 9]

def test_reduce_list():
    assert reduce_list([1, 2, 3, 4], lambda x, y: x + y, 0) == 10

def test_zip_lists():
    assert zip_lists([1, 2], [3, 4]) == [(1, 3), (2, 4)]

def test_flatten_list():
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
