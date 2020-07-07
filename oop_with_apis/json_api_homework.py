# storing data from json
# print(type(json_data))
# for key in json_data:
#     print(key)
#
# print(json_data)

# exercise - fetch data by key value pairs within dictionaries
# Create a function to return the above values (Key:value)
# Create a class and move the code inside the class


# class Fetch_Json:
#     json_data= post_codes_req.json()
#     # getattr (getter) retrieves all values
#     def get_all_values(self, nested_dictionary):
#         # for lopo iterates through the key:value pairs
#         for key, value in nested_dictionary.items():
#             if type(value) is dict:
#                 self.get_all_values(value)
#             else:
#                 print(key, ":", value)
#
# json_reader = Fetch_Json()
# json_reader.get_all_values(json_data)

import requests
import json
post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
json_data = post_codes_req.json()

class JSONReader:
    def get_all_values(self, nested_dictionary):
        for key, value in nested_dictionary.items():
            if type(value) is dict:
                self.get_all_values(value)
            else:
                print(key, ":", value)


json_reader = JSONReader()
json_reader.get_all_values(json_data)