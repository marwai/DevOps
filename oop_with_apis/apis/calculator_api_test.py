# import unit test module fail-implement-refactor
import unittest
import pytest
# purposely fail, test correct method and then refactor to clean up the code
# from  calculator_api import Functions

class Calc_Test(unittest.TestCase):

    # f refers to Functions class in the parent class calculator_api. Aliasing used to shorten the class name
    # f = Functions()


    def test_sqrt(self):
        # assertEqual function equates arg one and two, returns True and passes test, or False and fails.
        self.assertEqual(self.f.find_sqrt(25), 5)
    def test_find_ceil(self):
        self.assertEqual(self.f.find_ceil(10.6), 11)
