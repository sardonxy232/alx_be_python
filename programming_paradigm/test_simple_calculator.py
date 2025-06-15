import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Addition Tests
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_addition_mixed_sign(self):
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_addition_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    # Subtraction Tests
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtraction_mixed_sign(self):
        self.assertEqual(self.calc.subtract(5, -2), 7)

    def test_subtraction_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # Multiplication Tests
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiplication_mixed_sign(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_multiplication_by_zero(self):
        self.assertEqual(self.calc.multiply(0, 1000), 0)

    # Division Tests
    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_mixed_sign(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
