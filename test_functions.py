from unittest import TestCase
from functions import divide, multiply


class unit_testing(TestCase):
    def test_result(self):
        result = 5.08
        return self.assertAlmostEqual(divide(15, 3), result, delta=1.08)

    def test_result_zero(self):
        result = 0
        return self.assertEqual(divide(0, 5), result)

    def test_result_error(self):
        with self.assertRaises(ValueError):
            divide(25, 0)

    def test_multiply_error(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_one(self):
        result = 5
        return self.assertEqual(multiply(5), result)

    def test_multiply_normal(self):
        values = (3, 6, 5)
        result = 90
        return self.assertEqual(multiply(*values), result)

    def test_multiply_value_zero(self):
        values = (3, 0, 5)
        result = 0
        return self.assertEqual(multiply(*values), result)

    def test_multiply_negative(self):
        values = (3, -5)
        result = -15
        return self.assertEqual(multiply(*values), result)

    def test_multiply_float(self):
        values = (3.5, 2.5)
        result = 8.75
        return self.assertEqual(multiply(*values), result)
