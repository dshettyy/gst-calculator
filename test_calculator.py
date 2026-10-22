
import unittest
from calculator import calculate_total


class TestCalculateTotal(unittest.TestCase):

    def test_without_discount(self):
        self.assertEqual(calculate_total(200), 210.00)

    def test_with_discount(self):
        self.assertEqual(calculate_total(400), 378.00)

    def test_exactly_300_no_discount(self):
        self.assertEqual(calculate_total(300), 315.00)

    def test_just_above_300(self):
        self.assertEqual(calculate_total(301), 284.45)

    def test_zero_subtotal(self):
        self.assertEqual(calculate_total(0), 0.00)

    def test_negative_subtotal(self):
        with self.assertRaises(ValueError):
            calculate_total(-100)


if __name__ == "__main__":
    unittest.main()
