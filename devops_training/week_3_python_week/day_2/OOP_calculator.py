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
