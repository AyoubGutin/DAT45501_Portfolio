# -- Imports --
import unittest
from src.algorithms.sorting.bubble_sort import bubble_sort_func
from src.algorithms.sorting.selection_sort import selection_sort_func
from src.algorithms.sorting.insertion_sort import insertion_sort_func

from typing import List


# -- Test Suite # 1 --
class testBubbleSort(unittest.TestCase):
    """
    Test whether the bubble sort is accurate
    """

    def test_happy_path(self):
        """
        Test the sort with a typical, positive integer based list
        """
        # Set up the data
        arr = [10, 5, 1, 20, 4]
        expected_arr = [1, 4, 5, 10, 20]

        sorted_arr = bubble_sort_func(arr)

        # Test types
        self.assertIsInstance(sorted_arr, List)

        # Test expected vs actual values
        self.assertEqual(sorted_arr, expected_arr)

    def test_edge_case(self):
        """
        Test the sort with a list with negative values
        """
        # Set up the data
        arr = [-1, 5, -10, 3]
        expected_arr = [-10, -1, 3, 5]

        sorted_arr = bubble_sort_func(arr)

        # Test types
        self.assertIsInstance(sorted_arr, List)

        # Test expected vs actual values
        self.assertEqual(sorted_arr, expected_arr)

    def test_sad_path(self):
        """
        Test the sort with a non-array, which should raise an error
        """
        arr = 2

        with self.assertRaises(TypeError):
            bubble_sort_func(arr)


# -- Test Suite # 2 --
class testSelectionSort(unittest.TestCase):
    """
    Test whether the bubble sort is accurate
    """

    def test_happy_path(self):
        """
        Test the sort with a typical, positive integer based list
        """
        # Set up the data
        arr = [10, 5, 1, 20, 4]
        expected_arr = [1, 4, 5, 10, 20]

        sorted_arr = selection_sort_func(arr)

        # Test types
        self.assertIsInstance(sorted_arr, List)

        # Test expected vs actual values
        self.assertEqual(sorted_arr, expected_arr)

    def test_edge_case(self):
        """
        Test the sort with a list with negative values
        """
        # Set up the data
        arr = [-1, 5, -10, 3]
        expected_arr = [-10, -1, 3, 5]

        sorted_arr = selection_sort_func(arr)

        # Test types
        self.assertIsInstance(sorted_arr, List)

        # Test expected vs actual values
        self.assertEqual(sorted_arr, expected_arr)

    def test_sad_path(self):
        """
        Test the sort with a non-array, which should raise an error
        """
        arr = 2

        with self.assertRaises(TypeError):
            selection_sort_func(arr)


# -- Test Suite # 3 --
class testInsertionSort(unittest.TestCase):
    """
    Test whether the bubble sort is accurate
    """

    def test_happy_path(self):
        """
        Test the sort with a typical, positive integer based list
        """
        # Set up the data
        arr = [10, 5, 1, 20, 4]
        expected_arr = [1, 4, 5, 10, 20]

        sorted_arr = insertion_sort_func(arr)

        # Test types
        self.assertIsInstance(sorted_arr, List)

        # Test expected vs actual values
        self.assertEqual(sorted_arr, expected_arr)

    def test_edge_case(self):
        """
        Test the sort with a list with negative values
        """
        # Set up the data
        arr = [-1, 5, -10, 3]
        expected_arr = [-10, -1, 3, 5]

        sorted_arr = insertion_sort_func(arr)

        # Test types
        self.assertIsInstance(sorted_arr, List)

        # Test expected vs actual values
        self.assertEqual(sorted_arr, expected_arr)

    def test_sad_path(self):
        """
        Test the sort with a non-array, which should raise an error
        """
        arr = 2

        with self.assertRaises(TypeError):
            insertion_sort_func(arr)
