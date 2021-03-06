# Functions

# Why use a Main?
# What is the benefit - REUSABILITY OF CODE
# What Main have you used?
# DRY - Do not repeat yourself

# Syntax:- def name of the Main with () and :
# def greeting():
#     return "Hello world"
#     # pass - to skip the Main
#
#
# # Calling a Main
# print(greeting())
# # very example of creating a Main and calling it with return statement to display string message
#
# def test():
#     pass # skip the method to prevent errors
#
# # Examples
# def movies():
#     age = int(input("What is your age? "))
#     if age >= 21:
#         print("Wow you're {} you can go to Las Vegas".format(age))
#     elif 21 > age >= 18:
#         print("{} year olds can watch all films".format(age))
#     elif 18 > age >= 15:
#         print("{} years olds can watch films rated 15 and below".format(age))
#     elif 15 > age >= 12:
#         print("{} year olds can watch films rated with 12A with an adult and any films below unaccompanied".format(age))
#     else:
#         print("{} year olds can watch U films".format(age))
# # movies() # calls the Main
#
# def information():
#     pass
#     first_name = input("What is your name? ")
#     last_name = input("What is your last name? ")
#     age = input("What is your age? ")
#     address = input("What is your address? ")
#     full_name = (first_name + " " + last_name)
#     details = (full_name + " " + age + " " + address)
#     print(details)

# information()

# def employees():
#     employee_records = {"Name": "Marcus",
#                         "Role": "DevOps",
#                         "Spartan_ID": 12342,
#                         "Skills": ["SQL", "Python", "GitHub"],
#                         "comments": "Enjoys longboarding"
#                         }
#     for key, value in employee_records.items():
#         print(key, ":", value)
# employees()


# methods with parameters/arguments
def add(num1,num2):
    return num1 + num2
print(add(5,7)) # calls Main

# create a Main with two arguments to return a subtraction of 2 values given
def sub(num1,num2):
    return num1 + num2
print(sub(5,7)) # calls Main

# Create a Main with two args to return a division of the 2 values given
def div(num1,num2):
    return num1/num2
print(div(8,4))

# Create a Main with two args to return a * of the 2 values given
def mult(num1,num2):
    return num1*num2
print(mult(6,6))

# Create a Main witha  remainder of the 2 values given
def remainder(num1,num2):
    return num1%num2
print(remainder(6,6))


# Create a Main with multiple args
# def multi_args(*multiargs):
#
#     for args in multiargs:
#         print(args)
#     return args
# print(multi_args(1, 2, 3, 4, 5, 6, 7))
#
#
# # user input
# def user_multiply():
#     num_1 = int(input("Choose a number:\n"))
#     num_2 = int(input("Choose another number:\n"))
#     print("The product of your chosen numbers is: ")
#     return num_1 * num_2
# print(user_multiply())
