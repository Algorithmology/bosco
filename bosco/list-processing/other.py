"""List sorting algorithms."""

from typing import List, Any

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
