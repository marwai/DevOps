# Same idea, different behaviour
# Imports everything (*) from student_data
from student_data import *

# The subclass devops has student as its base class
class Devops(Student): # The class inherits all the characteristics from student_data
    def __init__(self, name, age, course, skills):
        super().__init__(name, age, course)
        self.skills = skills # unique to devops only

    # defines methods in child class which are define in the parent class
    def new_skill(self): # method is unique to Person
        self.details()
        print("You have learned " + self.skills, "at Sparta global\n")
    def intro(self):
        print(self.name, "is a spartan learning" ,self.skills)

# bob has become a spartan with additional skills
a =  Devops("bob", "25", "Computer Science", "SQL, Python and AWS\n")
# introduction of bob before joining sparta
b = Student("bob", "25", "Computer Science\n")

# intro() has two different functions
b.intro() # acquires method from Student class
a.intro() # Acquires characteristics from Devops Class