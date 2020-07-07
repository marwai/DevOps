# dumps() python dictinaries to json string - use type() to confirm
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

#Iteration 1
# print(post_codes_req.status_code)
#
# class Check_Status_code:
#     def check_status_code(self):
#         if post_codes_req.status_code:
#             return (" success ")
#         elif post_codes_req.status_code: # library
#             return (" Sorry page not available ")
#
# status = Check_Status_code() # creating a class object/instantiating
# print(status.check_status_code()) # Calling the method of check_status_code within the class
# # Iteration 2

# notes
# print(post_codes_req.json())

json_data= post_codes_req.json()
# storing data from json
print(type(json_data))
for key in json_data:
    print(key)

print(json_data)

# exercise - fetch data by key value pairs within dictionaries
# create a function

def fetch_data():
    import requests
    # Iteration 2, doing same output with oop
    class Status_code:
        # Getting user input of url
        def __init__(self, url):
            self.url = url

        def check_status_code(self):
            # Getting status of website, using requests function
            self.post_codes_req = requests.get(self.url)
            print(self.post_codes_req.status_code)

    class Live_web_status(Status_code):
        # Inheriting url attribute from Status_code class
        def __init__(self, url):
            super().__init__(url)

        def live_web_status(self):
            # Calling function from parent class to get status code of the website
            self.check_status_code()
            # Dont need to manually declare == 200, built in packages do it already
            if self.post_codes_req.status_code == 200:
                print("It worked!")
            elif self.post_codes_req.status_code:
                print("Page not available")

    obj1 = Live_web_status("https://api.postcodes.io/postcodes/se120nb")
    obj1.live_web_status()









