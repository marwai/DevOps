# Goal
# 1. Reading form and writing to files
# 2. Exception and handling
# 3. CSV
# 4. Assignments

from try_explain.try_textfile import Text_File_Handling

file_path = "../modified.txt"

text_file_object = Text_File_Handling(file_path)

# print(text_file_object.read_text_file())
#
# text_file_object.write_text_file();

# print(text_file_object.write_text_file())

# print(text_file_object.read_text_using_with())

# print(text_file_object.write_text_file_using_with())

# text_file_object.playing_with_python_os_module()

# try-put the code which you will think will raise an exception
# exception - catches the thrown exception
# else - if exception is not thrown, then the program can run the following code
# finally - whether an exception is raised or not, the code in this part will run. Usually used for closing drivers or
# database connections



# text_file_object.write_text_file();
# print(text_file_object.write_text_file())
# print(text_file_object.read_text_using_with())
# print(text_file_object.write_text_file_using_with())
text_file_object.playing_with_exception()

text_file_object.raiseException()