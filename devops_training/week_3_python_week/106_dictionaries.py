# Dictionary
# More than dynamic than tuples and lists
# Useful tool within coding
# Uses concept of Key:value pairs

# syntax - Curly brackets {} are used to create a dictionary

# Example
student_record = {"Name" : "Marcus",
                  "Stream":"DevOps",
                  "completed_lesson": 5,
                  "completed_lessons_name": ["strings","tuples","variables"]
}
# sorted() sorts a list alphabetically
# print(sorted(student_record))
# print(type(student_record))

# .values() recalls values
# print(student_record.values())

#recalls keys()
# print(student_record.keys())

# print(student_record["completed_lesson"])
# student_record["completed_lesson"] = 5 # assigns new value to the key in key:value
# new_list = student_record["completed_lessons_name"]


# add 2 topics that we have covered
# display the answer
# student_record["completed_lessons_name"].append("Lists") # adds new values
# student_record["completed_lessons_name"].append("slice") # adds new values
# print(student_record)

# fetch the values of stream
# print(student_record["Stream"])

# fetches specific index data
# print(student_record["completed_lessons_name"][1]) # fetches second value within "completed lessons name"

# fetches specific index data
# print(student_record["completed_lessons_name"][2])

#Exercise - fetch the specific index data of
# print(student_record.get("Name"))
# print(student_record["Name"])


