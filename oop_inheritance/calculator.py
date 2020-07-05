from calculations import Function
from area import Area
class python_calculator(Function):
    def __init__(self, add, sub, div, mult, remainder, num1,num2, user_input, base, height,area,*nums):
        super().__init__(add, sub, div, mult, remainder, height, base)
        self.num1 = int(num1)
        self.num2 = int(num2)
        self.user_input = str(user_input)
        self.area_arithmetic = area_arithmetic
        self.nums = nums
    area_arithmetic = input("Calculate Area or use Arithmetic functions: A or AR ")
    if area_arithmetic == "AR":
        num1 = int(input("Please input your first number "))
        # input the second number
        num2 = int(input("Please input your second number "))
        # input the operator
        user_input = input("Please input what you want to do: + - * / %")
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

        elif user_input == "%":
            if (Function.remainder(num1,num2)) == 0:
                print(True)
            else:
                print(False)
    elif area_arithmetic == "A":
        num1 = int(input("What is the height? "))
        # input the second number
        num2 = int(input("What is the base? "))
        print(str("0.5 * base * height =",Area.area(num1,num2,int(nums))))
    else:
        pass
        #
        # # if operator is unknown
        # else:
        #     print("You have entered an unknown value")
    # print out the result of the above code
    # print(Python_Calculator())
