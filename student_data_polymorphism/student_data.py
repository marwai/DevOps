# The super class, Student is the class that other classes inherits from
class Student:
    # method (behaviour) initialises the variables
    def __init__(self, name, age, course): # (name, age, course attributes are defined)
        self.name = name
        self.age = age
        self.course = course

    # Details of the student
    def details(self):
        # basic print functions
        print("Name: " + self.name)
        print("Age: " + self.age)
        print("University course: " + self.course)

    def age(self):
        print(self.name, "is {} years old".format(self.age))

    def intro(self):
        print(self.name ,"is a student")