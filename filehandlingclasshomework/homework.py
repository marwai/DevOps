# 1. Accept from the user some text. Ensure user enters something else raise an exception.
# After that write that text to a file and then read from this file to  write to another file simultaneously
# 2. Reading an image to  writing to another file simultaneously

import cv2

class User_Input:
    # initialise the class
    def __init__(self):
        pass
    # defining a method to user input
    def user_input(self):
        # user input attribute

        # when the condition runs true, the loop conitnues to run
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
                # confirms_name = input(f"Proceed as {self.name}, Y/N: ") # COMMENT
                # if confirms_name.lower() == "y": # COMMENT
                    print(f"Hello {self.name}")
                    return self.name
                # else: # COMMENT
                #     print("Please try again\n") #COMMENT




    # writes the output of user_input
    def write_user_input(self):
        self.user_input()
        with open("user_name.txt", "w+") as file:  # w+ write and read mode (OVERRIDES value)
            file.write(self.name)  # What is dynamically type, strongly type
            file.seek(0)
            self.new_text = str(file.read())

    # repeats previous method but writes on another file
    def again(self):
        self.write_user_input()
        with open("user_name_two.txt", "w+") as file:
            file.write(self.new_text)




object1 = User_Input()
object1.again()




