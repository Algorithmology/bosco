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