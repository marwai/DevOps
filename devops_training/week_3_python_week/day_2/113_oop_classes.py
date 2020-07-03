# class python_calculator:
# create a basic calculator
# methods to +,-,/,%

# class python_calculator:
#     def add(self,num1, num2):
#         return num1 + num2
#
#     def minus(self,num1, num2):
#         return num1 - num2
#
#     def multiply(self,num1, num2):
#         return num1 * num2
#
#     def divide(self,num1, num2):
#         return num1/ num2
#
#     def remainder(num1, num2):
#         return num1%num2
#
#     print("select operation")
#     print("1: add")
#     print("2: minus")
#     print("3: multiply")
#     print("4: divide")
#
#     num1 = int(input("select your first number "))
#     num2 = int(input("select your second number "))
#     option = int(input("select your option(1/2/3/4) "))
#
#     if option == 1:
#         print(num1, "+", num2, "=", add(num1, num2))
#
#     if option == 2:
#         print(num1, "-", num2, "=", minus(num1, num2))
#
#     if option == 3:
#         print(num1, "X", num2, "=", multiply(num1, num2))
#
#     if option == 4:
#         print(num1, "/", num2, "=", divide(num1, num2))

# Another Method
# imports the function class
# from (file) import(objects/functions)

from functions import *


class python_calculator:
    # def calculate(self):
    # input the first number
    num1 = int(input("Please input your first number"))
    # input the second number
    num2 = int(input("Please input your first number"))
    # input the operator
    user_input = input("Please input what you want to do: + - * / %")

    # if operator is +
    if user_input == "+":
        print(str(num1) + " Plus " + str(num2) + " equals: ",  functions.add(num1, num2))
    # if operator is -
    elif user_input == "-":
        print(str(num1) + " Minus " + str(num2) + " equals: ", functions.sub(num1, num2))
    # if operator is *
    elif user_input == "*":
        print(str(num1) + " Times " + str(num2) + " equals: ", functions.multi(num1, num2))
    # if operator is /
    elif user_input == "/":
        print(str(num1) + " Divide " + str(num2) + " equals: ", functions.div(num1, num2))
    # if operator is %
    elif user_input == "%":
        print(str(num1) + " Mod " + str(num2) + " equals: ", functions.remainder(num1, num2))
    # if operator is unknown
    else:
        print("You have entered an unknown value")
# print out the result of the above code
print(Python_Calculator)


