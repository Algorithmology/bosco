"""Conduct doubling experiments for provided algorithms that perform list sorting."""

import os
import sys
from timeit import repeat
from typing import List, Tuple


def run_sorting_algorithm(
    file_path: str, algorithm: str, array: List[int]
) -> Tuple[float, float, float]:
    """Run a sorting algorithm and profile it with the timeit package."""
    directory, file_name = os.path.split(file_path)
    module_name = os.path.splitext(file_name)[0]

    if directory:
        sys.path.append(directory)

    try:
        module = __import__(module_name)
        algorithm_func = getattr(module, algorithm)
    except (ImportError, AttributeError):
        raise ValueError(f"Could not import {algorithm} from {file_path}")

    stmt = f"{algorithm_func.__name__}({array})"
    times = repeat(
        setup=f"from {module_name} import {algorithm}",
        stmt=stmt,
        repeat=3,
        number=10,
    )
    return min(times), max(times), sum(times) / len(times)
