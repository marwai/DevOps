"""
fuction, excetpion, while, manners, looping 
"""
import math

def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person required to split the check")
    return math.ceil(total/number_of_people)

#Try this code 
try:
    total_due = float(input("What is the total?  "))
    number_of_people = int(input("How may people? "))
    amount_due = split_check(total_due,number_of_people)

#except if value error occurs 
except ValueError as err:
    print("Oh no! That's not a valid value. Try again...")  
    print("({})".format(err))
# otherwise continue code as usual 
else:
    print("Each person owes £{}".format(amount_due))