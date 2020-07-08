class Text_File_Handling:
    def __init__(self, file_path, text_storage=None):
        self.file_path = file_path  # self.__file_path to make private
        self.text_storage = text_storage  # self.__text_storage

        # variables should be made private so public can access methods but not variables
        # Going to read in two ways and write in two ways

    # Create methods first
    def read_text_file(self):
        # open file
        # read file
        # close file
        # file = open(self.file_path, 'r')
        # self.text_storage = file.read() #read 3 characters
        # # self.text_storage = file.read(3) # It reads
        # file.close()

        try:
            file = open(self.file_path, "r")
        except Exception as e:
                print(e)
        else:
            # self.text_storage = file.read()
            # self.text_storage = file.read(3) # read characters in the text file
            print(file.read(0))  # buffer
            self.text_storage = file.readline()  # reads first line
            self.text_storage = file.readline()  # reads second line, changes pointer when another is added
            print(file.tell())  # the pointer is at the current position
            file.seek(0)  # telling the pointer to go back at that particular position mentioned
            self.text_storage = file.readlines()  # reads rest of the lines from current position
            file.close()
            # file = open(self.file_path, "r")
            # self.text_storage = file.read()
            # for line in file:
            #     print(line)
            #     file.close()

        finally:  # always run irrespective whether an exception is raised or not
            print("Always run")
            return self.text_storage


    def write_text_file(self):
        # open, write, close
        file = open("writer.txt", "w")  # "w" write two arguments - one is the file and other is made
        file.write("My first python created")
        file.close()
        file = open("writer.txt", "a+")  # "a" append, "a+" appends and read, DOES NOT OVERRIDE
        file.write("\n I am overriding the file")  # append mode
        file.seek(0)
        self.text_storage = file.read()  # storing what I read from the file to the instance variable
        file.close()  # gives status of closure
        print(file.name)  # gives you the name of the current file
        print(file.mode)
        return self.text_storage

    def read_text_using_with(self):
        # reduce the overhead of closing files

        # open the file and read it. No overhead of closing
        # Automatically closes the file and also closes it during the times of exception being raised
        # Removes the manual use of close
        with open("order.txt", "r") as file:
            self.text_storage = file.read()
            return self.text_storage

    def write_text_file_using_with(self):
        with open("writer.txt", "w+") as file:  # w+ write and read mode (OVERRIDES value)
            file.write("Using writer with functionality")
            print(file.tell())  # tells you the position of the pointer
            file.seek(0)  # reposition the pointer at the beginning
            self.text_storage = file.read()# What is dynamically type, strongly type
            return self.text_storage# LEARN DYNAMICALLY (PYTHON) AND STATICALLY TYPE

    def playin_with_python_os_module(self):
        import os
        print(os.getcwd())  # current working directory
        # os.remove("writer.txt")
        print(os.listdir())
        # os.rename("order.txt", "modified.txt")
        os.chdir("C:/Users/marcu/PycharmProjects/devops/different")
        print(os.getcwd())  # edit this
        # flags = os.O_RDWR
        # os.open("modified.txt", flags)
        # os.mkdir("Marcus")
        # os.rmdir("Marcu") # remove directory
        os.chdir("C:/Users/marcu/PycharmProjects/devops/filehandlingclasses")
        print(os.getcwd())


    def playing_with_exception(self):
        try:
            file = open(self.file_path, "r")
        except Exception as e:
            print(e)
            print("File is not present")
        else:
            self.text_storage = file.readline()
            self.text_storage = file.reading()
            file.close()
        finally:
            print("Will run for sure!!")
            return self.text_storage