# print("Hello world ")

# commit naming convention

# x = 9 #   Type of integer
# y = 9.1 # Type of float
# name = #  'Marcus' Type of String

# print(x)
# age = 23
# NHS = 12456789
# name = input("Please enter your name")
# salary = 50000

# print(name)
# print(age)
# a = x + y
# name = "James"
# print(name)
# name = "bond"
# print(str(a) + (name))
# print(name)

# print(type(name)) # Returns the type of data in this case it is a string

# print( x + name ) # You cannot add together data types of string and int

# print(str(x) + name) # You must convert the INT into a string using the str() function. This is known as casting.

# A Python variable is a reserved memory location to store values.
# In other words, a variable in a python program gives data to the computer for processing

# Exercise
# Create a variable called first_name, last_name
# Create a variable called full_name
# full_name = first_name + last_name
# create a variable called age
# create a variable called address
# prompt the user get all the information above

# def details(info):
#     first_name = Marcus
#     last_name = Tse
#     age = 23
#     create a variable called address
#     addres = "123, 122""
#     prompt the user get all the information above

def information():
    first_name = input("What is your name?")
    last_name = input("What is your last name?")
    age = input("What is your age?")
    address = input("What is your address?")
    full_name = (first_name + " " + last_name)
    details = (full_name + " " + age + " " + address)
    print(details)
information()

# Additional Work
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