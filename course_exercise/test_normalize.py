import unittest
from .normalize import normalize


class TestNormalize(unittest.TestCase):
    def test_all_english(self):
        self.assertEqual(normalize("1234567890"), "1234567890")

    def test_all_persian(self):
        self.assertEqual(normalize("۱۲۳۴۵۶۷۸۹۰"), "1234567890")

    def test_mix_english_persian(self):
        self.assertEqual(normalize("۰67۴"), "0674")

    def test_all_numbers_english_persian(self):
        self.assertEqual(normalize("1234567890۱۲۳۴۵۶۷۸۹۰"), "12345678901234567890")


if __name__ == "__main__":
    unittest.main()
