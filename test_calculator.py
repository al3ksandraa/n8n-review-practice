import unittest

from calculator import divide


class DivideTests(unittest.TestCase):
    def test_divides_numbers(self):
        self.assertEqual(divide(3, 2), 1.5)

    def test_rejects_numeric_zero_divisor(self):
        with self.assertRaisesRegex(ValueError, '^Division by zero$'):
            divide(6, 0)

    def test_divides_numeric_strings(self):
        self.assertEqual(divide(' 7.5 ', '2.5'), 3.0)

    def test_accepts_numeric_string_as_dividend(self):
        self.assertEqual(divide('3', 2), 1.5)

    def test_accepts_numeric_string_as_divisor(self):
        self.assertEqual(divide(3, '2'), 1.5)

    def test_rejects_string_zero_divisor(self):
        with self.assertRaisesRegex(ValueError, '^Division by zero$'):
            divide(6, '0')
