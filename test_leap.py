import unittest

from leap import is_leap, main


class IsLeapTest(unittest.TestCase):
    def test_divisible_by_four(self):
        self.assertTrue(is_leap(2024))
        self.assertTrue(is_leap(1996))

    def test_not_divisible_by_four(self):
        self.assertFalse(is_leap(2023))
        self.assertFalse(is_leap(2025))

    def test_century_not_leap(self):
        self.assertFalse(is_leap(1900))
        self.assertFalse(is_leap(2100))

    def test_four_hundred_is_leap(self):
        self.assertTrue(is_leap(2000))
        self.assertTrue(is_leap(2400))


class CommandLineTest(unittest.TestCase):
    def test_leap_year_exit_code_zero(self):
        self.assertEqual(main(["2024"]), 0)

    def test_common_year_exit_code_one(self):
        self.assertEqual(main(["2023"]), 1)

    def test_mixed_years_exit_code_one(self):
        self.assertEqual(main(["2024", "2023"]), 1)


if __name__ == "__main__":
    unittest.main()