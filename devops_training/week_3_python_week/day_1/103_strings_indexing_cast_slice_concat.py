# strings - casting - slicing  - concatenation

# Concatenation
greeting_welcome = "Hello World"
welcome_user = input("Please enter your name? ")
print("Dear " + welcome_user + " welcome on board") #Concatenation
print(greeting_welcome)
# HELLO WORLD
# 012345678910
print(len(greeting_welcome))
print("Hi {}, welcome to Python".format(welcome_user))

# indexing
# String slicing
hi = "Hello world"
print(len(hi)) # prints length of string
print(hi[0]) # print h because it starts on 0
print(hi[-1]) 0 # prints d
#
print(hi[0:6]) # print hello
print(hi[6:11]) # print world
print(hi[1:3])

# Slicing
remove_white_space = "Remove the space at the end of a string        "
print(len(remove_white_space)
print(len(remove_white_space.strip()))
print(len(remove_white_space))

# .count() counts the substring within the string
use_text = "here's SOME text with lot's of text"
print(use_text.count("text"))
# .lower() lowers the caps within the string
print(use_text.lower())

# .upper() makes the first letters uppercase in each word
print(use_text.upper())

# .title makes everything UPPERCASE
print(use_text.title())

# Capitalize first letter of the sentence
print(use_text.capitalize()) # Used to interact with User a lot

# replacing text in the string
print(use_text.replace("with", ","))

# .startwith prints answer in boolean
print(use_text.startswith("hi"))



