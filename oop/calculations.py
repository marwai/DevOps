class Function:
    def __init__(self, add, sub, div, mult, remainder):
        # Attributes (variables in a class)
        self.add = add
        self.sub =sub
        self.div = div
        self.mult = mult
        self.remainder = remainder

    # Behaviours (methods) are defined in a class
    def add(num1, num2):
        return num1 + num2


    # create a behaviour with two arguments to return a subtraction of 2 values given
    def sub(num1, num2):
        return num1 - num2

     # calls Main

    # Create a Main with two args to return a division of the 2 values given
    def div(num1, num2):
        return num1 / num2



    # Create a Main with two args to return a * of the 2 values given
    def mult(num1, num2):
        return num1 * num2


    # Create a Main witha  remainder of the 2 values given
    def remainder(num1, num2):
        return num1 % num2

    def conversion():
        user = str(input("Do you want to convert to inches or cm?: \n"))
        num1 = int(input("What's the number? \n"))
        if user == "inches":
            conversion = num1 / 2.54
            print(conversion)
        elif user == "cm":
            conversion = num1 * 2.54
            print(conversion)
        else:
            return "please try again"

    def area(num1, num2):
        return 0.5 * num1 * num2


