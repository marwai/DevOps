# Sparta Global Training :star:
####    **Man-Wai Tse (```Marcus```)**,
#####   Trainee DevOps Engineer,
#####   [mtse@spartaglobal.com](mailto:mtse@spartaglobal.com)  
  
[![Marcus' github stats](https://github-readme-stats.vercel.app/api?username=marwai)](https://github.com/marwai/github-readme-stats)
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=marwai)](https://github.com/marwai/github-readme-stats)
  
    Hi, welcome to my Github. 
    All my learning material will be documented here. 
    Please see the calendar for indivdiual breakdown of the work
 :notebook_with_decorative_cover:      
 
##### ``` Marcus' ``` Trainee Notes  [Here](https://github.com/marwai/DevOps)
##### ```Marcus' ``` Linkedin [Here](https://www.linkedin.com/in/man-wai-tse-96mt/)
##### ```Marcus' ``` Projects [Here](https://github.com/marwai/projects)
##### ```Marcus' ``` Additional exercises [Here](https://github.com/marwai/additional_exercises) 
___

#### :calendar: Calendar 
- [x] Week 1 - [Business Week](https://github.com/marwai/DevOps/tree/master/devops_training/week_1_business_week)
- [x] Week 2 - [SQL](https://github.com/marwai/DevOps/tree/master/devops_training/week_2_sql_week)
- [x] Week 3 - [Python](https://github.com/marwai/DevOps/tree/master/devops_training/week_3_python_week)
- [x] Week 4 - [Python Week 2](https://github.com/marwai/DevOps/tree/master/devops_training/week_4_python_week)
- [x] Week 5 - [Project Week](https://github.com/marwai/pythonProject)
- [x] Week 6 - [Flask](https://github.com/marwai/mvc_flask)
- [x] Week 7 - [Introduction to DevOps](https://github.com/marwai/DevOps/tree/master/devops_training/week_7)


---

#### Setting up new Repository 
```
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:marwai/help.git
git push -u origin master
```
___
#### Pushing commits

```
git add .
git commit -m "comment"
git push
```
## **Terminology**

**Abstraction**
- Abstraction focuses on hiding the internal implementations of a process or method from the user. In this way, the user knows what he is doing but not how the work is being done. 

---

**Control Flow**
- The order in which the program's code executes
- The control flow of a Python program is regulated by conditional statements, loops, and function calls

```python
# Control Flow Statements with if. Conditionals
required_age = 18
age = int(input("How old are you?"))

if age < 18:
    print("You are too young to watch this movie.\nThe required age to watch this movie is {}".format(str(required_age)))
elif age<18 and age > 15:
    print("You can watch 15 rated films accompanied with an adult")
else:
    print("You can watch U films")
```
---

**Dictionary**
- An unordered collection of data values, used to store data values like a map
- Dictionary holds key:value pair
- Key value is provided in the dictionary to make it more optimised
- We use curly brackets {} to create a dictionary, separated by 'comma'
- Values in a dictionary can be of any data type and can be duplicated, whereas keys cannot be repeated and must be immutable
- Dictionaries are accessed via keys and not via their index position
- Can be nested

```python
student_record = {
    "name": "Marcus",
    "stream": "DevOps",
    "completed_lesson": 5,
    "completed_lesson_names": ["Business ", "SQL", "Python"]
}
```

---

**Collections**
- Containers used to store collections of data, e.g. list, dict, set, tuple
- They have different characteristics based on the declaration and the usage.
- Built-in Python module that implements specialised container datatypes.
- Developed to provide additional data structures to store collections of data. 

---
**Dynamic vs Static**
- Python is dynamically typed meaning variable names (unless `NULL`) is bound only to an object
- Data type determined at run time, not in advance, so no need to specify type of variable.
- This makes python a strongly typed language (type checking happens at run time), python interpreter keeps track of all variables types. 
- In python, it is the program's responsibility to use built-in functions like `isinstance()` or `issubclass` to test variable types.



**Python: strongly typed**
- In python, you cannot perform operations inappropriate to the type of object e.g adding numbers to strings
```python
'x' + 3
>>> # Returns error. Integer MUST be converted to string 
```
---

**Encapsulation**
- Concept of encapsulation is to keep together the implementation (code) and the data it manipulates (variables). 
- In python, we can **restrict** access to methods and variables. This prevents data from being modified (encapsulation).
- In python, we denote private attributes using underscore `_` or dunder (double underscore) `__` as the prefix.

---
**Function**
- A block of organised, reusable code that is used to perform a single, related action
- DRY *Don't* *Repeat* *Yourself*
- You can pass data (parameters), into a function.

```python
def greet(name):
    name = input("What is your name? \n")
    return "Hello, " + name + " Good morning!"
```

---
**List**
- A data structure that is mutable, or changeable.
- Each element or value that is inside of a list is called an item.
- Lists are defined by having values between square brackets []

```python
cities = ["Paris", "Hong Kong", "Buenos Aires", "London,", "Tel Aviv", "Amsterdam"]
print(cities)
```

---
**Inheritance**
- Inheritance is a way of creating a new class for using details of an **existing** class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class(or parent class).

---
**Loops**
- There are two types of loops, for and while 
- For loops can iterate over a sequence of numbers using the 'range' and 'xrange' functions
- While loops repeat as long as a certain boolean condition is met

```python
list_data = [1, 2, 3]

# Using for 
# Prints 1, 2, 3
for n in list_data:
    print(n)

# Using while
# Prints out the numbers 0, 1, 2, 3, 4
for x in range(5):
    print(x)
```

---
**Sets**
- An unordered collection data type that is iterable, mutable and has no duplicate elements
- They are very similar to lists but it has a highly optimised method for checking whether a specific element is contained in the set.
- This is based on a data structure known as a has table

```python
# Normal Set
# Prints b, c, a, d
normal_set = set(["a", "b", "c"])
normal_set.add("d")
print(normal_set)

# Frozen Set
# Prints f, e, g, cannot use 'add' attribute 
frozen_set = frozenset(["e", "f", "g"])
print(frozen_set)
```

---

**Polymorphism**
- Refers to the ability of an object taking many forms. 
- Python being an OOP supports Polymorphism through Method overriding and operator overloading. 
- Polymorphism can be achieved through inheritance - Method overriding
- Method overriding provides ability to change the implementation of a method in a child class which is already defined in one of its super class or parent class. 
- If there is a method in a super class the method having the same name number of arguments in a child class is said to be **overriding** the parent class method. 
- We can use the concept of polymorphism while creating class methods as Python allows different classes to have methods with the same name. 
- We can then later generalise calling these methods by disregarding the object we are working with. 

---
**Tuple**
- They are the same as lists but immutable meaning they cannot be changed
- Tuples use parenthesis ()

```python
dob = ("name", "dob", "passport number")
print(dob)
```
---

[Variable](https://github.com/marwai/DevOps/blob/master/devops_training/week_3_python_week/day_1/101_variable.py)
- Another name for placeholder
- A reserved memory location to store data values 
- Variables can be declared by any name 
```python
this_is_variable = 19
this_is_another_variable = "Hello World"
this_is_also_a_variable = (str(this_is_variable) + this_is_another_variable)
``` 

---
**List** vs **tuple** vs **set** vs **dictionary**

[List](https://github.com/marwai/DevOps/blob/master/devops_training/week_3_python_week/day_1/104%20_lists.py)
- mutable, stores duplicate values, elements accessed using indexes, ordered collection
- Methods = `.append()`, `.remove()`, `.insert()`, `.pop()`
- `.remove()` removes first matching value, `del list_name[index]` removes item at specific index. `.pop()` removes item at specific index and returns it.

[Tuple](https://github.com/marwai/DevOps/blob/master/devops_training/week_3_python_week/day_1/105_tuples.py)
- Like a list but immutable, stores duplicate values, ordered collection, accessed using indexes.
- Methods = `.add()`, `.discard()`, `.count()`, `.del`

[Set](https://github.com/marwai/DevOps/blob/master/devops_training/week_3_python_week/day_1/108_sets.py)
- Unordered, not indexed, does not store duplicate entries
- Methods = `.add()`, `.clear()`, `.update()`, `.remove()`

[Dictionary](dictionaries.py) {key:value}
- Key value pairs, mutable, unordered
- Methods = `.items()`, `.keys()`, `.values()`
- More useful than lists when mapping unique keys to values
- Dict elements accessed via keys NOT position of items so slicing cannot happen.
- `.pop("key")` method to remove entry in dictionary or `del`




