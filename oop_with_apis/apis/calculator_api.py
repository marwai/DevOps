#import the math module to use mathematical functions in python
import math


class Functions:
    #static methods are used to create utility functions
    @staticmethod
    # pre-built method to calculate square root
    def find_sqrt(num):
        return math.sqrt(num)
    # A static method is also a method which is bound to the class and not the object of the class.
    # A static method can’t access or modify class state.

    # method rounds up
    @staticmethod
    def find_ceil(num):
        return math.ceil(num)


