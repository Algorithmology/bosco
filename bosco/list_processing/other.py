"""Other List Algorithms."""

from typing import List, Any, Union, Tuple


def is_subset(first_list: List[Any], second_list: List[Any]) -> bool:
    """Determine if one set is a subset of another set."""
    for element_one in first_list:
        matched = False
        for element_two in second_list:
            if element_one == element_two:
                matched = True
                break
        if not matched:
            return False
    return True


def list_intersection(list1: List[Any], list2: List[Any]) -> List[Any]:
    """Make a new list containing only the elements that are common to both input lists."""
    return [x for x in list1 if x in list2]


def list_symmetric_difference(list1: List[Any], list2: List[Any]) -> List[Any]:
    """Make a new list containing elements that are present in only one of the input lists"""
    return [x for x in list1 + list2 if (x not in list1) or (x not in list2)]


def list_concatenation(
    list1: List[Union[int, float, str]], list2: List[Union[int, float, str]]
) -> List[Union[int, float, str]]:
    """Concatenates two lists into a single list."""
    return list1 + list2


def list_elementwise_addition(
    list1: List[Union[int, float]], list2: List[Union[int, float]]
) -> List[Union[int, float]]:
    """Performs element-wise addition of two lists of numbers."""
    return [x + y for x, y in zip(list1, list2)]


def list_pairwise_multiplication(
    list1: List[Union[int, float]], list2: List[Union[int, float]]
) -> List[Union[int, float]]:
    """Performs pairwise multiplication of two lists of numbers."""
    return [x * y for x, y in zip(list1, list2)]
