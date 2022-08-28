import unittest
from .seperator import seperator


class TestSeperator(unittest.TestCase):
    def test_one_digit_left(self):
        self.assertEqual(seperator("1234567890"), "1,234,567,890")

    def test_two_digit_left(self):
        self.assertEqual(seperator("12234567890"), "12,234,567,890")

    def test_three_digit_left(self):
        self.assertEqual(seperator("122234567890"), "122,234,567,890")

    def test_long_number(self):
        self.assertEqual(
            seperator("1222234567654565456545674567890"),
            "1,222,234,567,654,565,456,545,674,567,890",
        )


if __name__ == "__main__":
    unittest.main()
