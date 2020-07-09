

# self to say it's working in this file
# simple calculator is the attribute

import pytest
import unittest
from calc import *

#ran four tests of TDD by testing, failing
class Calc_Test(unittest.TestCase):
    simple_calc = Calc()
    # to pytest
    def test_add(self):
        self.assertEqual(self.simple_calc.add(2, 2), 4)
    def test_subtract(self):
        self.assertEqual(self.simple_calc.subtract(3, 1), 2)
    def test_mulitply(self):
        self.assertEqual(self.simple_calc.multiply(2, 2),4 )
    def test_divide(self):
        self.assertEqual(self.simple_calc.divide(9,3),3)
    def test_modulo(self):
        self.assertTrue(self.simple_calc.modulo(3,3),0)
    def test_cm_to_inch(self):
        self.assertEqual(self.simple_calc.cm_to_inch(10),3.94)
