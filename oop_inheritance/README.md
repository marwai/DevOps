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



