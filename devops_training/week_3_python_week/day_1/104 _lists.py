# Data collection
# Java array in Python Lists are same as arrays
# both serve the same purpose of sotring data
# Lists - manage data - access data in order - it gives us the option to
# add and remove data etc.

# Syntax of list: [list] square brackest, (tuple) round brackets,
# {dictionary - key:value} curly brackets
# Dictionary returns values and key:value pairs
# Tuples are immutable
# List are mutable

# Let's create a list of cities

cities = ["Morrow Wind", "Runeterra","Tokyo", "Paris", "Hong Kong"]
# display(print(cities)) #  list the cities
print(type(cities))
cities[4] = "Bangkok" # this will replace city index 3
# print(cities)

# .append() adds a varibale to the end of list ie. adds the city at the end of string
# cities.append("iceland")

# .remove() removes an entry from the list
# cities.remove("Paris")
# print(cities)

# .pop() removes last entry in the list
# cities.pop()
# print(cities)

# .insert() - index must be define
cities.insert(3,"Madrid")
print(cities)

# mix_type_string = [1,2,3,]
# string_list = ["one","two","three"]
# print(string_list + mix_type_string)
