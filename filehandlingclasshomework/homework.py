# 1. Accept from the user some text. Ensure user enters something else raise an exception.
# After that write that text to a file and then read from this file to  write to another file simultaneously
# 2. Reading an image to  writing to another file simultaneously

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
        # while True:
        #     # if the name is more than 0 characters
        #     try:
        #         # requires user input
        #         self.name = input("Enter your name: \n")
        #         if len(self.name) <= 0:
        #             raise Exception
        #     # catches exception
        #     except Exception:
        #         # prints this statement when exception is caught
        #         print("Empty name is not accepted")
        #     # if more than 0 characters are entered prints that name out
        #     else:
        #         confirms_name = input(f"Proceed as {self.name}, Y/N: ") # COMMENT
        #         if confirms_name.lower() == "y": # COMMENT
        #             print(f"Hello {self.name}")
        #             return self.name
        #         else: # COMMENT
        #             print("Please try again\n") #COMMENT
        # method two shorthand
        while True:
            try:
                stored_user = str(input(("Please enter the text\n")))
                # If statement to say if the character length is less than 0
                if (len(stored_user)) == 0:
                    raise Exception
            except Exception:
                print("We do not accept empty texts")
            else:
                # Opening the homework.txt file just created. using w+ to read and write.
                with open("user_name.txt", "w+") as file:
                    # Writing the user input into the file
                    file.write(stored_user)
                    self.new_text = str(file.read())  # This stores a new self
                    print("Thank you for entering your name: ", stored_user)
                    with open("user_name_two.txt", "w+") as file2:
                        file2.write(stored_user)
                        self.new_text = str(file.read())
                        return self.user_name



    # writes the output of user_input
    # def write_user_input(self):
    #     self.user_input()
    #     with open("user_name.txt", "w+") as file:  # w+ write and read mode (OVERRIDES value)
    #         file.write(self.name)  # What is dynamically type, strongly type
    #         file.seek(0)
    #         self.new_text = str(file.read())
    #
    # # repeats previous method but writes on another file
    # def again(self):
    #     self.write_user_input()
    #     with open("user_name_two.txt", "w+") as file:
    #         file.write(self.new_text)
    #
    # def read_image(self):
    #     with open('tree.JPG', 'r') as i, open('tree.JPG', 'w+') as ii:
    #         ii.write(i.read())
    #         Image.open('tree.JPG').show()


object1 = User_Input()
# object1.again()
object1.again()




