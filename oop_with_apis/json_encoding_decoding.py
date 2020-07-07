import json

car_data = {"name": "tesla", "engine": "electric"} # Dictionary

print(car_data) #Printing the dictionary
print(type(car_data))

#Checking the type of dictionary
car_data_json_string = json.dumps(car_data)

#json.dumps changes python dict to json str

print(type(car_data_json_string)) #json format is changed the type to a string

#Creating a jsonfile
with open("new_json_file.json", "w") as jsonfile: #enter the name of the file, permission type - write "w"
    json.dump(car_data, jsonfile) #json.dump take 2 arguments
    # first one - the dictionary created with the name car_data
    # second - file_type jsonfile on this occasion
    # Encoding and writing into json_file

with open("new_json_file.json") as jsonfile: # decoding
    #reading from the file we just created
    car = json.load(jsonfile)
    print(type(car))
    print(car['name']) # to get the value stored in key called name
    print(car['engine']) # to get the value of second key value pair
# we have decoded our file new_json.json that we created earlier
# we have used dumps(), dump() and load() methods