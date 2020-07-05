"""
WHILE LOOP 


"""

import sys

MASTER_PASSWORD = 'opensesame'

password = input("please enter the super secret password: ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again: ")
    attempt_count += 1
print("welcome to secret town")