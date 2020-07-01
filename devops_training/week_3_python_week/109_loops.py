# Loops

# For Loops are used to iterate through lists, strings Dictionaries and Tuples
# While loops runs if True

# Syntax: For loop
# iterate through a whole list in ms
list_data = [1, 2, 3, 4, 5, 6]
# print(list_data[0])
# print(list_data[1])
# print(list_data[2])

for data in list_data:
    if data > 5:
        break
    print(data)
