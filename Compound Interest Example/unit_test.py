import unittest
from compound_interest import compound_interest


class CompoundInterestTesting(unittest.TestCase):
    def test_happy(self):
        """
        happy path: user enter values we expect
        """
        self.assertEqual(
            5384.45, compound_interest(savings=5000, interest=2.5, years=3)
        )

    def test_edge(self):
        """
        edge case: boundary of user input
        """
        self.assertEqual(
            5020.03, compound_interest(savings=5000, interest=0.1, years=4)
        )

    def test_sad(self):
        """
        sad case: user enters values and there should be errors raised
        """
        with self.assertRaises(TypeError):
            # user enters a year that isnt whole
            compound_interest(savings=5000, interest=2.5, years=3.6)
        with self.assertRaises(ValueError):
            # user enters savings thats negative
            compound_interest(savings=-1000, interest=5, years=4)


if __name__ == "__main__":
    unittest.main()
