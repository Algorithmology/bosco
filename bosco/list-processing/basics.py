"""Basic python functions for benchmarking the bosco tool."""

import random
from typing import List, Any

def get_first_item(lst: List[Any]) -> Any:
    """Returns the first item of the list if it exists, otherwise returns None."""
    return lst[0] if lst else None

def get_last_item(lst: List[Any]) -> Any:
    """Returns the last item of the list if it exists, otherwise returns None."""
    return lst[-1] if lst else None

def get_list_length(lst: List[Any]) -> int:
    """Returns the length of the list."""
    return len(lst)

def reverse_list(lst: List[Any]) -> List[Any]:
    """Returns a new list that is the reverse of the input list."""
    return lst[::-1]

def sort_list(lst: List[Any]) -> List[Any]:
    """Returns a new list that is the sorted version of the input list."""
    return sorted(lst)

def append_item(lst: List[Any], item: Any) -> List[Any]:
    """Appends an item to the end of the list and returns the list."""
    lst.append(item)
    return lst

def remove_item(lst: List[Any], item: Any) -> List[Any]:
    """Removes an item from the list if it exists and returns the list."""
    if item in lst:
        lst.remove(item)
    return lst

def count_item(lst: List[Any], item: Any) -> int:
    """Returns the count of an item in the list."""
    return lst.count(item)

def clear_list(lst: List[Any]) -> List[Any]:
    """Clears all items from the list and returns the list."""
    lst.clear()
    return lst

def insert_item(lst: List[Any], index: int, item: Any) -> List[Any]:
    """Inserts an item at a specific index in the list and returns the list."""
    lst.insert(index, item)
    return lst

def delete_random_item(lst: List[Any]) -> List[Any]:
    """Deletes a random item from the list and returns the list."""
    if lst:
        del lst[random.randint(0, len(lst) - 1)]
    return lst

def copy_list(lst: List[Any]) -> List[Any]:
    """Returns a copy of the input list."""
    return lst.copy()

def list_in(lst: List[Any], item: Any) -> bool:
    """Returns True if the item is in the list, False otherwise."""
    return item in lst

def extend(lst1: List[Any], lst2: List[Any]) -> List[Any]:
    """Extends lst1 with the items in lst2 and returns the extended list."""
    lst1.extend(lst2)
    return lst1

def index(lst: List[Any], item: Any) -> int:
    """Returns the index of the first occurrence of an item in the list."""
    return lst.index(item)

def pop(lst: List[Any], index: int = -1) -> Any:
    """Removes and returns the item at the given index from the list."""
    return lst.pop(index)

def min(lst: List[Any]) -> Any:
    """Returns the smallest item in the list."""
    return min(lst)

def max(lst: List[Any]) -> Any:
    """Returns the largest item in the list."""
    return max(lst)

def filter_list(lst: List[Any], condition: callable) -> List[Any]:
    """Returns a new list containing only the items that satisfy the given condition."""
    return [item for item in lst if condition(item)]

def map_list(lst: List[Any], function: callable) -> List[Any]:
    """Applies a function to each item in the list and returns a new list with the results."""
    return [function(item) for item in lst]

def reduce_list(lst: List[Any], function: callable, initial: Any) -> Any:
    """Applies a function of two arguments cumulatively to the items of the list, from left to right, so as to reduce the list to a single output."""
    result = initial
    for item in lst:
        result = function(result, item)
    return result

def zip_lists(lst1: List[Any], lst2: List[Any]) -> List[tuple]:
    """Returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument lists."""
    return list(zip(lst1, lst2))

def flatten_list(lst: List[List[Any]]) -> List[Any]:
    """Flattens a list of lists into a single list."""
    return [item for sublist in lst for item in sublist]