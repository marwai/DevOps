# Project 1 
```
phase 1: build a simple calculator class containing add, subtract, multiply, divide.
phase 2: expand by creating:
Divisible by method that returns true or false dependent on the outcome
Work out and return the area of a triangle
inch to cm converter
NOTE -> Must be in class and method format
```
# Project 2 

# Project 3

# Project 4 
Base Scrabble word calculator instructions
```
Given the below scoring create a Scrabble word calculator that will provide the correct scores dependent on the string provided.

Letter Value
A, E, I, O, U, L, N, R, S, T 1
D, G 2
B, C, M, P 3
F, H, V, W, Y 4
K 5
J, X 8
Q, Z 10
```
# 4 Pillars of OOP

### Inheritance
* Inheritance allows us to define a class that inherits all the methods and properties from another class.
* **Parent class** is the class being inherited from, also called base class
* **Child class** is the class that inherits from another class, also called derived class.

Child class is the class that inherits from another class, also called derived class.
``` bash
# super class

class Animal:

    def __init__(self):

        self.alive = True
        self.eyes = True

    def breathe(self):
        return "NOTHING MORE IMPORTANT TO LIVE THAN KEEP BREATHING! "

reptiles = Animal()

# print(reptiles.eyes)
# print(reptiles.breathe())
```

``` bash
from animal import Animal


# inheriting animal class in Reptile class

class Reptile(Animal):
    # creating Reptile class and passing Animal class as an arg

    def __init__(self):
        super().__init__()
        self.venom = True
        self.fly = False

        def _hidden_method(self):
            return " I am hidden"


snake = Reptile()
```


### Abstraction
```bash 
when using methods in our code

def bark(self):
    return "woof"
modelling class 
print(fido.bark())

when you want to hide the complexity so the simplicity on the surface is simple in the child class
```


## Polymorphism
``` bash
When a new object is created, it inherits as well as overrides particular attributes or behaviour without affecting 
the classes 

```
## Encapsulation 
``` bash 
Making variables or methods private to hide various aspects of a class from  a user

def __sleep():
```