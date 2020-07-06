# phase 1: build a simple calculator class containing add, subtract, multiply, divide.
# phase 2: expand by creating:
# Divisible by method that returns true or false dependent on the outcome
# Work out and return the area of a triangle
# inch to cm converter
# NOTE -> Must be in class and method format


from calculations import Function
class python_calculator(Function):
    # def __init__ defines all the varibles used in current class that will it initialised
    def __init__(self, add, sub, div, mult, remainder, num1,num2, user_input,area):
        # super() defines all the attributes that were defines in parent class
        super().__init__(add, sub, div, mult, remainder,area)
        self.num1 = int(num1)
        self.num2 = int(num2)
        self.user_input = str(user_input)
        self.area_arithmetic = area_arithmetic

    area_arithmetic = input("Calculate Area, Arithmetic functions or converting measures: A, AR, Convert: ")
    # Phase 1
    if area_arithmetic == "AR":
        num1 = int(input("Please input your first number "))
        # input the second number
        num2 = int(input("Please input your second number "))
        # input the operator
        user_input = input("Please input what you want to do: + - * / % convert")
        # if operator is +
        if user_input == "+":
            print(Function.add(num1, num2))
        # if operator is -
        elif user_input == "-":
            print(str(num1) + " Minus " + str(num2) + " equals: ", Function.sub(num1, num2))
        # if operator is *
        elif user_input == "*":
            print(str(num1) + " Times " + str(num2) + " equals: ", Function.multi(num1, num2))
        # if operator is /
        elif user_input == "/":
            print(str(num1) + " Divide " + str(num2) + " equals: ", Function.div(num1, num2))

        # phase 2 returning true of false
        # if operator is %
        elif user_input == "%":
            if (Function.remainder(num1,num2)) == 0:
                print(True)
            else:
                print(False)

    # phase 2: returning rea
    elif area_arithmetic == "A":
        num1 = int(input("What is the height? "))
        # input the second number
        num2 = int(input("What is the base? "))
        print(str("0.5 * base * height ="), Function.area(num1,num2), str("cm\u00b2"))

        # converting cm to inches or vice versa
    elif area_arithmetic == "Convert":
        Function.conversion()
    else:
        pass
        #
        # # if operator is unknown
        # else:
        #     print("You have entered an unknown value")
    # print out the result of the above code
    # print(Python_Calculator())
