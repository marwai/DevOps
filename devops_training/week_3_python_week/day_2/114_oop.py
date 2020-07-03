# OOP - 4 pillars of OOP

# inheritance - parent, child classes
# polymorphism -  override parent attributes
# encapsulation - set
# abstraction -

class Animal:
    def __init__(self, name, colour, mood, hunger, sleepy, species):
        self.name = name
        self.colour = colour
        self.mood = mood
        self.hunger = hunger
        self.sleepy = sleepy
        self.species = species

    # this initialises the characteristics of the kingdom
    def feed(self):
        self.hunger = "full" # changes the object to full

    def sleep(self):
        self.sleepy = False
        print("zzzzzz")

    def check_status(self):
        print(f"is {self.name} sleepy?", self.sleepy)
        print(f"How is {self.name}'s hunger levels?", self.hunger)
        print(f"what is {self.name}'s mood?", self.mood)
        print(f"what species is {self.name}?", self.species)
        print(f"What colours is {self.name}?", self.colour, "\n")


class Dog(Animal):
    species = "Canine"

    # class to create a dog
    def bark(self):
        return "woof woof"

    def run(self):
        self.mood = "happy"


class Cat(Animal):
    species = "Feline"

    def meow(self):
        return print("Meow meow")

    def play(self):
        self.mood = "happy"


# class to create a cat

# create a methods inside for sleep, breath, run, eat

# thor was is an object so it is an instance of class
thor = Cat("thor", "white", mood="mad", hunger="starving", sleepy=True, species=Cat.species)
zeus = Dog("zeus", "black", mood="sad", hunger="hungry", sleepy=True, species=Dog.species)

#thor.check_status()
# thor.feed()
# thor.check_status()
# thor.meow()
# zeus.check_status()
# thor.feed()
# zeus.feed()
# zeus.run()
# thor.play()
# thor.check_status()
# zeus.check_status()


# chowchow = Dog1("chowchow", "brown")
# chowchow.printname()


#code
class Animal:
    def __init(self, name, color, mood, hunger, sleepy, species):
        self.name