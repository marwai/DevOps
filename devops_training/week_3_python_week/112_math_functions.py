# Using builting python library
from random import random
import math

float_num = 24.5 # float

# round the float number
print(math.ceil(float_num))
print(math.floor(float_num))
# print(math.pi) # pi figure

# print(random())
#
# def round():
#     num1, num2 = int(input("What is your first number? \n")), int(input("what is your second number? \n"))
#     return math.ceil(num1), math.ceil(num2)
# round()

# create a method that would take 2 arguments
# def muliply(num1, num2):
#     print("The numbers you want to return are")
#     return math.ceil(num1)

# calculate cm into inches or vice versa
def conversion():
    user = str(input("Do you want to convert to inches or cm?: \n"))
    num1 = int(input("What's the number? \n"))
    if user == "inches":
        conversion = num1/2.54
        return conversion
    elif user == "cm":
        conversion = num1*2.54
        return conversion
    else:
        return "please try again"
print(conversion())
# def add(num1, num2):
#     conversion = num1 + num22
#     print("The answer is \n")
#     return conversion/2.5
#
# def inches_to_cm(num1):
#     conversion = math.ceil(num1*2.54)
#     print("That converts to {} cm",conversion)
#
# def cm_to_inches(cm):
#     print("cm converted into inches is:")
#     return (cm/2.54)
# print(cm_to_inches((10)))
# calculate cm + 2.4 into inches or vice versa

# user input