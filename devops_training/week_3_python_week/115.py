class Dog:
    animal_kind = "canine" # class variable

    def bark(self):
        self.animal_kind  # method variable inside the class
        return "woof woof"
    def eat(self):
        self.eat = eat
        return "nom nom nom ..."

fido = Dog() # creating an object of a class/ instantiating our class

print(fido.animal_kind)
print(fido.bark())

fido.animal_kind = "fish"
print(fido.animal_kind)

