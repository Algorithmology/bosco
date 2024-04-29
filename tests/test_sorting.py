import pytest

from bosco import sorting

class TestBubbleSort:

    # The function sorts a list of integers in ascending order.
    def test_sort_ascending_order(self):
        # Arrange
        input_list = [4, 2, 1, 3]
        expected_output = [1, 2, 3, 4]

        # Act
        result = sorting.bubble_sort(input_list)

        # Assert
        assert result == expected_output

    # The function sorts an empty list and returns an empty list.
    def test_sort_empty_list(self):
        # Arrange
        input_list = []
        expected_output = []

        # Act
        result = sorting.bubble_sort(input_list)

        # Assert
        assert result == expected_output

class TestInsertionSort:

    # The function sorts a list of integers in ascending order.
    def test_sorts_list_in_ascending_order(self):
        # Arrange
        input_list = [4, 2, 1, 3]
        expected_output = [1, 2, 3, 4]

        # Act
        result = sorting.insertion_sort(input_list)

        # Assert
        assert result == expected_output

    # The function works correctly with an empty list.
    def test_works_correctly_with_empty_list(self):
        # Arrange
        input_list = []
        expected_output = []

        # Act
        result = sorting.insertion_sort(input_list)

        # Assert
        assert result == expected_output

class TestMerge:

    # Merging two non-empty arrays of equal length
    def test_merge_equal_length(self):
        # Arrange
        left = [1, 3, 5]
        right = [2, 4, 6]
        expected_result = [1, 2, 3, 4, 5, 6]

        # Act
        result = sorting.merge(left, right)

        # Assert
        assert result == expected_result

    # Merging an empty array with a non-empty array
    def test_merge_empty_array(self):
        # Arrange
        left = []
        right = [1, 2, 3]
        expected_result = [1, 2, 3]

        # Act
        result = sorting.merge(left, right)

        # Assert
        assert result == expected_result

class TestMergeSort:

    # The function correctly sorts a list of integers in ascending order.
    def test_sort_list_of_integers(self):
        # Arrange
        array = [5, 2, 8, 1, 9, 3]
        expected_result = [1, 2, 3, 5, 8, 9]

        # Act
        result = sorting.merge_sort(array)

        # Assert
        assert result == expected_result

    # The function correctly sorts an empty list.
    def test_sort_empty_list(self):
        # Arrange
        array = []
        expected_result = []

        # Act
        result = sorting.merge_sort(array)

        # Assert
        assert result == expected_result

class TestSelectionSort:

    # The function sorts a list of integers in ascending order.
    def test_sort_ascending_order(self):
        # Arrange
        array = [4, 2, 1, 3]
        expected_result = [1, 2, 3, 4]

        # Act
        sorting.selection_sort(array)

        # Assert
        assert array == expected_result

    # The function sorts an empty list.
    def test_sort_empty_list(self):
        # Arrange
        array = []
        expected_result = []

        # Act
        sorting.selection_sort(array)

        # Assert
        assert array == expected_result