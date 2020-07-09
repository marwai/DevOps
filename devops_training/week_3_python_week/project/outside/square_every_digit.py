# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    word = list(str(num))  # turns input into list of strings
    n = list(map(int, word))  # turns list of strings into list of integers
    empty = []  # empty list
    for i in n:  # iterate through the empty list
        empty.append(i ** 2)  # squares itself add and adds this value into the list
    empty2 = ""  # empty string
    for i in empty:  # iterates through list AGAIN1
        empty2 += str(i)  # taking the empty2 string into one big string as a total
    return int(empty2)  # returns asnwer as integer and voila

