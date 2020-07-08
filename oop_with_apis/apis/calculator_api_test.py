# import unit test module fail-implement-refactor
import unittest

# purposely fail, test correct method and then refactor to clean up the code
from  calculator_api import Functions

class Calc_Test(unittest.TestCase):
    f = Functions()
    def test_sqrt(self):
        self.assertEqual(self.f.find_sqrt(25), 5)
    def test_find_ceil(self):
        self.assertEqual(self.f.find_ceil(10.6), 11)
