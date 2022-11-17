import unittest
from .google_sum import google_sum


class TestSum(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(google_sum([1, 2, 3, 9], 8), [])

    def test_negative(self):
        self.assertEqual(google_sum([-1, -2, 3, 9], 8), [(-1, 9)])

    def test_repetetive(self):
        self.assertEqual(google_sum([1, 2, 4, 4], 8), [(4, 4)])

    def test_negetive_sum(self):
        self.assertEqual(google_sum([-4, -4, 1, 2], -8), [(-4, -4)])

    def test_multi_results(self):
        self.assertEqual(google_sum([1, 2, 3, 4, 5, 6], 8), [(2, 6), (3, 5)])


if __name__ == "__main__":
    unittest.main()
