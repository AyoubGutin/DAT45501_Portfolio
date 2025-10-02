# -- Imports --
import unittest
import numpy as np
from best_fit_line import fit_line


# -- Test Suite #1 --
class TestFitLine(unittest.TestCase):
    """
    Test whether our line of best fit is accurate by comparing it against expected values
    """

    def test_happy_path(self):
        """
        Test line of best fit with linear data, which is the expected user inputs
        """

        # Sample Linear Data
        months = np.array([1, 2, 3, 4])
        sales = np.array([100, 120, 140, 160])

        # Formulae for slope and intercepts
        slope_expected = (sales[1] - sales[0]) / (months[1] - months[0])
        intercept_expected = sales[0] - (slope_expected * months[0])

        # Get the slope, intercept, and line of best fit from our function
        slope, intercept, y_pred = fit_line(months, sales)

        # Test types
        self.assertIsInstance(slope, float)
        self.assertIsInstance(intercept, float)
        self.assertIsInstance(y_pred, np.ndarray)

        # Test expected vs actual values
        self.assertAlmostEqual(slope, slope_expected, places=5)
        self.assertAlmostEqual(intercept, intercept_expected, places=5)
        self.assertTrue(np.allclose(y_pred, sales))

    def test_edge_case(self):
        """
        Test the boundaries of what the function can handle

        Testing: Two points only and a negative slope
        """

        # Sample Edge Case Data
        months = np.array([1, 2])
        sales = np.array([10, 5])

        # Formulae for slope and intercepts
        slope_expected = (sales[1] - sales[0]) / (months[1] - months[0])
        intercept_expected = sales[0] - (slope_expected * months[0])

        # Get the slope, intercept, and line of best fit from our function
        slope, intercept, y_pred = fit_line(months, sales)

        # Test types
        self.assertIsInstance(slope, float)
        self.assertIsInstance(intercept, float)
        self.assertIsInstance(y_pred, np.ndarray)

        # Test expected vs actual values
        self.assertAlmostEqual(slope, slope_expected, places=5)
        self.assertAlmostEqual(intercept, intercept_expected, places=5)
        self.assertTrue(np.allclose(y_pred, sales))

    def test_sad_path(self):
        """
        Testing empty array inputs which should give an error
        """
        months = np.array([])
        sales = np.array([])

        with self.assertRaises(TypeError):
            slope, intercept, y_pred = fit_line(months, sales)
