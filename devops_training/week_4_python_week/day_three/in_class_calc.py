
class arithmetic:
    #static methods are used to create utility functions
    @staticmethod
    # pre-built method to calculate square root
    def addition(num1,num2):
        return num1 + num2
    # A static method is also a method which is bound to the class and not the object of the class.
    # A static method can’t access or modify class state.

    # method rounds up
    @staticmethod
    def subtract(num1,num2):
        return num1 - num2

    @staticmethod
    def multiply(num1,num2):
        return num1 * num2

    @staticmethod
    def divide(num1,num2):
        return num1/num2

