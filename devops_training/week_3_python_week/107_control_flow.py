# Control Flow

# Conditional statements and loops
# if, elif, else, for loop, while loop

# weather = input("What's the weather like today? ")
# if weather == "sunny" or "rainy": # both conditions must be True
#     print("let's go to the beach")
# else:
#     print("Lets play games indoors")
age = 18
if age >= 18:
    print("Please proceed to the check out")
else:
    print("Sorry you are not eligible to watch this movie")

# Exercise
# if 21 go to las vegas
# if age <= 17 can't watch 18 rated movie
# if age 15 or less can't watch any movies above the age of 15
# if age 12 or less can't watch any movies above the age of 12
# if PG
# if U
age = input("What is your age? ")
if  age >= "21":
    print("Wow you're {} you can go to Las Vegas".format(age))
elif age >= "18":
    print("{} year olds can watch all films".format(age))
elif age <= "15":
    print("{} years olds can watch films rated 15 and below".format(age))

elif age < "12":
    print("{} year olds can watch films rated with 12A with an adult and any films below unaccompanied".format(age))
else:
    print("{} year olds can watch U films".format(age))