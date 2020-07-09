# storing data from json
# print(type(json_data))
# for key in json_data:
#     print(key)
#
# print(json_data)

# exercise - fetch data by key value pairs within dictionaries
# Create a function to return the above values (Key:value)
# Create a class and move the code inside the class

import requests
import json
post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
json_data = post_codes_req.json()
    # getattr (getter) retrieves all values
class Fetch_Json_pairs:
    def get_all_values(self, nested_dictionary):
        # for loop iterates through the key:value pairs
        for key, value in nested_dictionary.items(): #  items() method is used to return the list with all dictionary
            # keys with values
            if type(value) is dict:  # if the value of a key is a dictionary, then you have found a nested dictionary
                self.get_all_values(value) # recall this method passing in that dictionary to iterate through it
            else:
                print(key, ":", value) #  iterates through nested dictionaries until a value is given

f = Fetch_Json_pairs() # An instance of the function is created

f.get_all_values(json_data) # All values and nested dictionaries are returned


  (type_json)  # Returns all the values inside a dictionary including any nested dictionaries