# 1. Accept from the user some text. Ensure user enters something else raise an exception.
# After that write that text to a file and then read from this file to  write to another file simultaneously
# 2. Reading an image to  writing to another file simultaneously
# 08/07/20
import os
from PIL import Image


class User_Input:
    # initialise the class
    def __init__(self):
        pass
    # defining a method to user input
    def user_input(self):
        # user input attribute

        # when the condition runs true, the loop continues to run
        while True:
            # if the name is more than 0 characters
            try:
                # requires user input
                self.name = input("Enter your name: \n")
                if len(self.name) <= 0:
                    raise Exception
            # catches exception
            except Exception:
                # prints this statement when exception is caught
                print("Empty name is not accepted")
            # if more than 0 characters are entered prints that name out
            else:
                confirms_name = input(f"Proceed as {self.name}, Y/N: ") # COMMENT
                if confirms_name.lower() == "y": # COMMENT
                    print(f"Hello {self.name}")
                    return self.name
                else: # COMMENT
                    print("Please try again\n") #COMMENT

    # method 1 continued COMMENT
    # writes the output of user_input
    def write_user_input(self):
        self.user_input()
        with open("user_name.txt", "w+") as file:  # w+ write and read mode (OVERRIDES value)
            file.write(self.name)  #
            file.seek(0) # sets the position to 0
            self.new_text = str(file.read()) # writes in new file

    # repeats previous method but writes on another file
    def again(self):
        self.write_user_input()
        with open("user_name_two.txt", "w+") as file:
            file.write(self.new_text)

        # method two shorthand
        # while True:
        #     try:
        #         self.name = str(input(("Please enter the text\n")))
        #         # If statement to say if the character length is less than 0
        #         if (len(self.name)) == 0:
        #             raise Exception
        #     except Exception:
        #         print("We do not accept empty texts")
        #     else:
        #         # Opening the homework.txt file just created. using w+ to read and write.
        #         with open("user_name.txt", "w+") as file:
        #             # Writing the user input into the file
        #             file.write(self.name)
        #             self.new_text = str(file.read())  # This stores a new self
        #             print("Thank you for entering your name: ", self.name)
        #             with open("user_name_two.txt", "w+") as file2:
        #                 file2.write(self.name)
        #                 self.new_text = str(file.read())
        #                 return self.name

    def image_writefile(self):
        with open('me.JPG', 'rb') as f, open('global.png', 'wb') as f2:
            f2.write(f.read())
            Image.open('me.JPG').show()


object1 = User_Input()

# Exercise 1
# object1.user_input() # METHOD 1
# object1.again() # METHOD 2

# Exercise 2
object1.image_writefile()



