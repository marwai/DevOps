#   let's create a variable

# print("Hello world ")
#
# x = 9 # type of integer
# y = 9.1 #float
#
# print(x)
# age = 23
# NHS = 12456789
# name = input("Please enter your name")
#
#
# #   salary = 50000
#
# print(name)
# print(age)
# a = x + y
#   Casting an int to string
#   print(str(a) + (name))
# name = "James"
# print(name)
# name = "bond"
# print(name)

#   Exercise
#   Create a variable called first_name, last_name
# first_name = Marcus, last_name = Tse
#   Create a variable called full_name
# full_name = first_name + last_name
# #   create a variable called age
# age = 23
# #   create a variable called address
# addres = "123, 122""
# #   prompt the user get all the information above
#
# ##### ``` Marcus' ``` Trainee Notes
# def details(info):
#     first_name = Marcus
#     last_name = Tse
#     age = 23
#     #   create a variable called address
#     addres = "123, 122""
#     #   prompt the user get all the information above

def information():
    first_name = input("What is your name?")
    last_name = input("What is your last name?")
    age = input("What is your age?")
    address = input("What is your address?")
    full_name = first_name + " " + last_name
    details = full_name + " " + age + " " + address
    print(details)
information()

# def information():
#     first_name = input("What is your name?")
#     if first_name == "Marcus":
#         print(first_name,"Learning python is fun!")
#     elif first_name == Marwai:
#         print("Hey", first_name, "welcome to the league of python!")
#     else:
#         print("You should learn python, {}!".format(first_name))
#     last_name = input("What is your last name?")
#     age = int(input("What is your age?"))
#     if age <= 10:
#         print("wow you are {} already, you should learn python!".format(age))
#     address = input("What is your address?")
#     if  "sunnybank" in address:
#         print("You must be from kent! since you're from {}".format(address))
#     full_name = first_name + " " + last_name
#     details = full_name + ", " + str(age) + " ," + address
#     print(details)
# information()