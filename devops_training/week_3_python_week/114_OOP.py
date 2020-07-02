# OOP - 4 pillars of OOP

# inheritance - parent, child classes
# polymorphism -  override parent attributes
# encapsulation -
# abstraction -


class Dog:
    animal_kind = "canine"
    speed = 0
    def __init__(self, name, color):
        self.name = name # methods are objects that belong to a class
        self.color = color

    def bark(self):
        return "woof woof"

    def sleep(self):
        return "sleepy boy"

    def breathe(self):
        return "alive boy"

    def run(self):
        self.__speed = 30

    def eat(self):
        return "eating boy"



fido = Dog("canine", "white") # creating an object of a class


print(fido.color) # printing an attribute of a class

lucy = Dog("lucy", "brown")
print(lucy.color)

# Create a method inside for sleep, breath, run, eat,
class Dog1(Dog):
    def __init__(self, name, color):
        Dog1.__init__(self, name, color)


chowchow = Dog1("chowchow", "brown")
chowchow.printname()


#code
class Animal:
    def __init(self, name, color, mood, hunger, sleepy, species):
        self.name