# sets

# Syntax: use {} brackets
# Sets are similiar to Lists

#Example
car_parts = {"wheels", "windows", "doors"}
print(car_parts)

# What can we go with sets
# Add an item to the set

# .add item
car_parts.add("seats") # seats added  list
print(car_parts)

# .discard to delete item
car_parts.discard("windows")
print(car_parts)

# Syntax - () store them in a variable
counting = frozenset([1,2,3,4])
print(counting)
print(type(counting))

