"""List Combining Algorithms."""
from typing import List, Any, Tuple


def concatenate_lists(*lists: List[Any]) -> List[Any]:
    """Concatenate any number of list you give it."""
    result = []
    for lst in lists:
        result.extend(lst)
    return result


def zip_lists(*lists: List[Any]) -> Tuple[Any]:
    """Combine multiple lists into a single list of tuples,
    where each tuple contains elements from the corresponding positions of the lists."""
    return list(zip(*lists))


def merge_lists(list1: List[Any], list2: List[Any]) -> List[Any]:
    """Combine two lists in a way that the elements are typically interleaved or merged according to a specific criterion."""
    result = []
    for i in range(max(len(list1), len(list2))):
        if i < len(list1):
            result.append(list1[i])
        if i < len(list2):
            result.append(list2[i])
    return result
