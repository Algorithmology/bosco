import os
import sys
from unittest.mock import Mock, patch

import pytest

from bosco.benchmark import run_sorting_algorithm


@pytest.fixture
def setup():
    array = [5, 2, 8, 12, 1, 6]
    file_path = "bosco/sorting.py"
    algorithm = "bubble_sort"
    return array, file_path, algorithm


def test_run_sorting_algorithm_success(setup):
    array, file_path, algorithm = setup
    with patch(
        "builtins.__import__", return_value=Mock(bubble_sort=lambda x: x)
    ):
        min_time, max_time, avg_time = run_sorting_algorithm(
            file_path, algorithm, array
        )
        assert isinstance(min_time, float)
        assert isinstance(max_time, float)
        assert isinstance(avg_time, float)
        assert max_time >= min_time


def test_run_sorting_algorithm_import_error(setup):
    array, file_path, algorithm = setup
    with patch("builtins.__import__", side_effect=ImportError):
        with pytest.raises(ValueError) as exc_info:
            run_sorting_algorithm(file_path, algorithm, array)
        assert (
            str(exc_info.value)
            == f"Could not import {algorithm} from {file_path}"
        )


def test_run_sorting_algorithm_attribute_error(setup):
    array, file_path, algorithm = setup
    with patch("builtins.__import__", return_value=Mock(spec=[])):
        with pytest.raises(ValueError) as exc_info:
            run_sorting_algorithm(file_path, algorithm, array)
        assert (
            str(exc_info.value)
            == f"Could not import {algorithm} from {file_path}"
        )


def test_run_sorting_algorithm_directory_in_path(setup):
    array, _, algorithm = setup
    file_path = "algorithms/sorting_algorithms.py"
    with patch(
        "builtins.__import__", return_value=Mock(bubble_sort=lambda x: x)
    ):
        with patch.object(sys, "path", []):
            run_sorting_algorithm(file_path, algorithm, array)
            assert "algorithms" in sys.path
