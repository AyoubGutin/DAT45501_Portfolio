import unittest
from calculations import calculate_rectangle_area


class TestRectangleCalculations(unittest.TestCase):
    def test_happy(self):
        """
        Test the happy paths, what a user is expected to enter
        """
        self.assertEqual(calculate_rectangle_area(5, 2), 10)
        self.assertEqual(calculate_rectangle_area(5.5, 2.5), 13.75)
        self.assertNotEqual(calculate_rectangle_area(10, 8), 70)

    def test_edge(self):
        """
        Test the edge cases, such as close to 0 decimals
        """
        self.assertEqual(calculate_rectangle_area(0.1, 0.1), 0.01)

    def test_sad(self):
        """
        Test the sad paths, where the function is expected to raise errors.
        """
        with self.assertRaises(TypeError):
            calculate_rectangle_area("test", 3)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-1, 3)


if __name__ == "__main__":
    unittest.main()
