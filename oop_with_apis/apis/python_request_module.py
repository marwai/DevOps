# Application Programme Interface
# WHat is it?
# Why Use is
# in python we have a module called request to interact with web-oop_with_apis
# To install: pip install requests

# import requests
from status_codes import *
#check HTTP/HTTPS 200 success - 400 - 404 page no found
#
# print(response_bbc.status_code)
# print(response_bbc)
# print(response_bbc.headers)
# print(response_bbc.content)
#
# # 1st iteration
# receive a response and check if 200 - print success
# elif code 400 - page not found
# else 404 OOPs - sorry something went wrong
# response_fb = requests.get("https://www.facebook.com/")
# if response_fb.status_code == 200:
#      print("The page has been loaded successfully")
# elif response_fb.status_code == 400:
#      print("Code 400 - page not found")
# else:
#      print("Error 404 - Oops something went wrong")
#
# # 2nd iteration
# create a functinon called check_response_code() including all the above
# returns the message with status code
# def check_response_code():
def check_response():
    response_fb = requests.get("https://www.facebook.com/")
    if response_fb.status_code == 200:
        print("The page has been loaded successfully")

    elif response_fb.status_code == 400:
        print("Something has gone wrong, please try again later")

    else:
        print("Error 404 - Oops something went wrong")
check_response()

# 3rd iteration
class Response:
    status()
    pass

Response()
# hi