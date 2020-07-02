# Loops

# For Loops are used to iterate through lists, strings Dictionaries and Tuples
# While loops runs if True

# Syntax: For loop
# iterate through a whole list in ms
list_data = [1, 2, 3, 4, 5, 6]
print(list_data[0])
print(list_data[1])
print(list_data[2])

list_data = [1, 2, 3, 4, 5, 6]
for data in list_data:
# if condition will come inside For loop

    if data > 5:

        # break condition will come inside if block
        break
    print(data)

list_data = [1, 2, 3, 4, 5, 6]
list_data = input("What is your list data 1-6? ")
for data in list_data:
    if data > "5":
       print("The data is correct")
    elif data < "0":
        print("Please enter number above 0")
    print(data)

# Create a string and loop through the string
city = "London"
for letter in city:
    print(letter)

# print the string in one line
name = "Marcus Tse"
for index in name:
    letters += " " + index
    if name[-1] == index:
        print(letters)

# For loop in dictionaries
student_record = {"Name" : "Marcus",
                  "Stream":"DevOps",
                  "completed_lesson": 5,
                  "completed_lessons_name": ["strings","tuples","variables"]
                  }
for record in student_record.values():
    print(record)

# Exercise
# Dictionary with employee records with minimum 5 key:value pairs
# Using loop iterate through the dictionary
# Display the values and keys of the dictionary

employee_records = {"Name" : "Marcus",
                    "Role":"DevOps",
                    "Spartan_ID": 12342,
                    "Skills": ["SQL", "Python", "GitHub"],
                    "comments": "Enjoys longboarding"
                  }
for key,value in employee_records.items():
    print(key,":",value)

