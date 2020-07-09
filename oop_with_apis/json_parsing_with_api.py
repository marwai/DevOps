# 3rd iteration create same functionality with OOP - class and a
# create a method called check_status_code():
# create a class live_web_status_code:
# out put should be the same as we achieved without OOP.

# Never commnet
import requests
import json
#Never comment
post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")


# print(post_codes_req.status_code)
# print(post_codes_req.status_code)
# print(post_codes_req.content)
# print(type(post_codes_req.content))
# print(post_codes_req.headers)
# print(post_codes_req)

# Iteration 1
if post_code_req.status_code == 200:
    print("success")
elif post_codes_req.status_code ==404:
    print(" sorry page unavailable")

# Iteration 2
print(post_codes_req.status_code)

class Check_Status_code:
    def check_status_code(self):
        if post_codes_req.status_code:
            return (" success ")
        elif post_codes_req.status_code: # library
            return (" Sorry page not available ")

status = Check_Status_code() # creating a class object/instantiating
print(status.check_status_code()) # Calling the method of check_status_code within the class
# Iteration 3
class Check_Status:
    def check_status_code():
        if post_code_req.status_code:
            print("succes")
        elif post_code_req.status_code == 400:
            print("sorry page unavaiable")


check1 = Check_Status
check1.check_status_code()

# notes
json_data= post_codes_req.json()
# storing data from json
print(type(json_data))
for key in json_data:
    print(key)

print(json_data)

# exercise - fetch data by key value pairs within dictionaries
# Create a function to return the above values (Key:value)
# Create a class and move the code inside the class






