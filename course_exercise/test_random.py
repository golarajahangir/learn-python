# test ro che joori test konam?
# ta koja test neveshtan kafie
# bishtar dar morede test yad begiram
# testhayi ke baghiye nevehtan ro bebinam
# level up sham to codewars
# videohamo bebinam
# ketab bekhonam


import unittest
from .random_exercise import rand


class TestRandom(unittest.TestCase):
    def test_less_than_million(self):
        self.assertLessEqual(rand(), 1000000)

    def test_greater_than_1(self):
        self.assertGreaterEqual(rand(), 1)

    def test_unique_in_last_10_results(self):
        result = []
        for num in range(0, 10):
            result.append(rand())

        for item in result:
            result.pop(item)
            if result.index(item):
                self.assertFalse(result.index(item))


if __name__ == "__main__":
    for i in range(1, 100):
        unittest.main()
