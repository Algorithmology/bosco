"""List searching algorithms."""

from typing import List, Optional
import math


def compute_iterative_binary_search(values: List[int], target: int) -> bool:
    """Search a list using iterative binary search."""
    end = len(values) - 1
    start = 0
    while start <= end:
        mid = (start + end) // 2
        if values[mid] == target:
            return True
        elif values[mid] < target:
            start = mid + 1
        elif values[mid] > target:
            end = mid - 1
    return False


def compute_recursive_binary_search(
    values: List[int], target: int, start: int = 0, end: Optional[int] = None
) -> bool:
    """Search a list using recursive binary search."""
    if end is None:
        end = len(values) - 1
    if start > end:
        return False
    mid = (start + end) // 2
    if values[mid] == target:
        return True
    elif values[mid] < target:
        return compute_recursive_binary_search(values, target, mid + 1, end)
    elif values[mid] > target:
        return compute_recursive_binary_search(values, target, start, mid - 1)


def compute_jump_search(search_list: List[int], x: int) -> int:
    """Search a list using jump search function."""
    n = len(search_list)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while search_list[min(step, n) - 1] < x:
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            return -1
    while search_list[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    if search_list[prev] == x:
        return prev
    return -1


def compute_interpolation_search(search_list: List[int], x: int) -> int:
    """Find indices of two corners."""
    lo = 0
    n = len(search_list)
    hi = n - 1
    while lo <= hi and x >= search_list[lo] and x <= search_list[hi]:
        if lo == hi:
            if search_list[lo] == x:
                return lo
            return -1
        pos = lo + int(
            (
                (float(hi - lo) / (search_list[hi] - search_list[lo]))
                * (x - search_list[lo])
            )
        )
        if search_list[pos] == x:
            return pos
        if list[pos] < x:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1


def compute_linear_search(search_list: List[int], x: int) -> int:
    """Search a list using linear search function."""
    for i in range(len(search_list)):
        if search_list[i] == x:
            return i
    return -1


def compute_exponential_search(search_list: List[int], x: int) -> int:
    """Return the position of first occurrence of x in array."""
    n = len(search_list) - 1
    if search_list[0] == x:
        return 0
    i = 1
    while i < n and search_list[i] <= x:
        i = i * 2
    return compute_recursive_binary_search(search_list, x, i / 2, min(i, n))
