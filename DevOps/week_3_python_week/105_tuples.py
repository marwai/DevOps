# Tuples

# Similiar to lists but are IMMUTABLE
# WHY Tuples - Store the data that remain constant i.e Date of birth, passport number etc.
# Syntax of Tuples: we use() to create a Tuple

date_of_birth = ("Name", "dob", "passport number")


#Exercise

# convert the tuple into string uses list() function
date_of_birth_list = list(date_of_birth)
print(date_of_birth_list)

# add your name into the string at 0
date_of_birth_list.insert(0,"marcus")
print(date_of_birth_list)

# tuple()
date_of_birth_tuple = tuple(date_of_birth_list)
print(date_of_birth_tuple)