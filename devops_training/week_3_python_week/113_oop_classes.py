# class python_calculator:
#
#     def add_values(self, num1 ,num2)
#     pass

# create a basic calculator
# methods to +,-,/,%

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
        print(num1, "+", num2, "=", add(num1, num2))

    if option == 2:
        print(num1, "-", num2, "=", minus(num1, num2))

    if option == 3:
        print(num1, "X", num2, "=", multiply(num1, num2))

    if option == 4:
        print(num1, "/", num2, "=", divide(num1, num2))




