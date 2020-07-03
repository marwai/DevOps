import function
class python_calculator:
    def __init__(self, add, sub, div, mult, remainder, num1,num2, user_input):
        super().__init__(add, sub, div, mult, remainder)
        self.num1 = int(num1)
        self.num2 = int(num2)
        self.user_input = str(user_input)

    num1 = int(input("Please input your first number "))
    # input the second number
    num2 = int(input("Please input your second number "))
    # input the operator
    user_input = input("Please input what you want to do: + - * / %")
    # if operator is +
    if user_input == "+":
        print(str(num1) + " Plus " + str(num2) + " equals: ",  function.add(num1, num2))
    # if operator is -
    elif user_input == "-":
        print(str(num1) + " Minus " + str(num2) + " equals: ", function.sub(num1, num2))
    # if operator is *
    elif user_input == "*":
        print(str(num1) + " Times " + str(num2) + " equals: ", function.multi(num1, num2))
    # if operator is /
    elif user_input == "/":
        print(str(num1) + " Divide " + str(num2) + " equals: ", function.div(num1, num2))
    # if operator is %
    elif user_input == "%":
        print(str(num1) + " Mod " + str(num2) + " equals: ", function.remainder(num1, num2))
    # if operator is unknown
    else:
        print("You have entered an unknown value")
# print out the result of the above code
print(Python_Calculator)
