import unittest
import pytest
from in_class_calc import arithmetic


class in_class_calc_test(unittest.TestCase):
    # creating class object
    calc = arithmetic()

    # creating test method for addition
    def test_addition(self):
        # assertEqual function equates arg one and two, returns True and passes test, or False and fails.
        self.assertEqual(self.calc.addition(5,5), 10)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10,6), 4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(50,10),500)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10,2),5)

# Test
calc = arithmetic
print(calc.addition(5,5),10)
print(calc.subtract(10,6),4)
print(calc.multiply(50,10),500)
print(calc.divide(10,2),5)