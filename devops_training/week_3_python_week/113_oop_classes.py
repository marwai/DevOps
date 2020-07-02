# class python_calculator:
#
#     def add_values(self, num1 ,num2)
#     pass

# create a basic calculator
# methods to +,-,/,%

import 111_functions


class python_calculator:
    def add(self,num1, num2):
        return num1 + num2

    def minus(self,num1, num2):
        return num1 - num2

    def multiply(self,num1, num2):
        return num1 * num2

    def divide(self,num1, num2):
        return num1/ num2

    def remainder(num1, num2):
        return num1%num2

    print("select operation")
    print("1: add")
    print("2: minus")
    print("3: multiply")
    print("4: divide")

    num1 = int(input("select your first number "))
    num2 = int(input("select your second number "))
    option = int(input("select your option(1/2/3/4) "))

    if option == 1:
        print(num1, "+", num2, "=", 111_functions.add(num1, num2))

    if option == 2:
        print(num1, "-", num2, "=", minus(num1, num2))

    if option == 3:
        print(num1, "X", num2, "=", multiply(num1, num2))

    if option == 4:
        print(num1, "/", num2, "=", divide(num1, num2))

# Another Method
# create classmethod

# imports the function class
import functions

class Python_Calculator:
    # def calculate(self):
    # input the first number
    number_1 = int(input("Please input your first number"))
    # input the second number
    number_2 = int(input("Please input your first number"))
    # input the operator
    user_input = input("Please input what you want to do: + - * / %")

    # if operator is +
    if user_input == "+":
        print(str(number_1) + " Plus " + str(number_2) + " equals: ",  functions.add_values(number_1, number_2))
    # if operator is -
    elif user_input == "-":
        print(str(number_1) + " Minus " + str(number_2) + " equals: ", functions.sub_values(number_1, number_2))
    # if operator is *
    elif user_input == "*":
        print(str(number_1) + " Times " + str(number_2) + " equals: ", functions.multi_values(number_1, number_2))
    # if operator is /
    elif user_input == "/":
        print(str(number_1) + " Divide " + str(number_2) + " equals: ", functions.divide_values(number_1, number_2))
    # if operator is %
    elif user_input == "%":
        print(str(number_1) + " Mod " + str(number_2) + " equals: ", functions.modo_values(number_1, number_2))
    # if operator is unknown
    else:
        print("You have entered an unknown value")
# print out the result of the above code
print(Python_Calculator)


