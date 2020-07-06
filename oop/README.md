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
```
The Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a 
string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is 
"ATGCTTCAGAAAGGTCTTACG."
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and
 'T' occur in s.
Sample Dataset:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
```
# Project 3
```
The Problem

"Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number 
and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."

```
# Project 4 
Base Scrabble word calculator instructions
```
Given the below scoring create a Scrabble word calculator that will provide the correct scores dependent on the string
 provided.

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
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)
```
In the code above, there are the the parent (base) class ```Rectangle```
and the child class ```Square```

The child classes behaviour is similiar to rectangle, however it only inherits length 
because it is the only attribute required

``` super``` is inside ```__init__()``` to create methods of a parent class

___

## Polymorphism

#### Class Polymorphism
* *Polymorphism** uses methods from another class to perform different tasks
* Polymorphism performs a single action in different ways. It is evident in data overriding in: **operators** , 
**methods** and **classes**
* Polymorphism means* "many forms"

```
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
```
In the code above, ```cat``` and ```dog``` have the same method names ```info ``` and   ```make sound``` with different 
outputs 
due to polymorphism 

#### Method Overriding - Inheritance and Polymorpism 
``` bash
from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
```
```str``` has been overriden in the child classes, and were used from the parent class

The ```fact()``` method for ```a(Square)``` is overridden. Whereas object ```b``` isn't overriden, it used the Parent 
```shape``` class
___

### Abstraction
* Process of hiding the real implementation of an application from the user and emphasising only the usage of it. For example, 
consider a electronic gadget with instruction of the application. The user guide has instructions on how to use the gadget 
but but no information regarding the internal working of the gadget
* A programmer can hide all the irrelevant data/processes of an application to reduce complexity and increase efficiency
* An abstract class cannot be instantiated, i.e.,objects cannot be created for the abstract class.


___

## Encapsulation 
* **Encapsulation** involves wrapping data and methods to restrict directly accessing them, preventing the accidental modifcaiton of data
* To make a variable private in Python it involes using **double underscore** ```__``` 

```bash 
class Car:
    def __init__(self, speed, color):
        # __speed and __color has been to set to private to prevent accidentally changing the variable 
        self.__speed = speed
        self.__color = color

    # set attribute (set attr) has to be called to change the speed
    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed


    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color

ford = Car(200, 'red')
honda = Car(250, 'blue')
audi = Car(300, 'black')

ford.set_speed(300)
# ford.__speed = 400 # uncommenting this will produce an error because speed has been set to a private variable
print(ford.get_speed())
# ford.__color # will also produce an error 
print(ford.get_color())
```