# Parent Class
class Function:
    def __init__(self, add, sub, div, mult, remainder):
        # Attributes (variables in a class)
        self.add = add
        self.sub =sub
        self.div = div
        self.mult = mult
        self.remainder = remainder

    def add(num1, num2):
        return num1 + num2

     # calls Main

    # create a Main with two arguments to return a subtraction of 2 values given
    def sub(num1, num2):
        return num1 + num2

     # calls Main

    # Create a Main with two args to return a division of the 2 values given
    def div(num1, num2):
        return num1 / num2

    print(div(8, 4))

    # Create a Main with two args to return a * of the 2 values given
    def mult(num1, num2):
        return num1 * num2


    # Create a Main witha  remainder of the 2 values given
    def remainder(num1, num2):
        return num1 % num2

