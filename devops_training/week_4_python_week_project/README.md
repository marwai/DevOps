# Overview
- [x] [117 OOP](https://github.com/marwai/oop)   
    - [x] [118 OOP Inheritance](https://github.com/marwai/oop_inheritance)
    - [x] [119 OOP Asbtraction](https://github.com/marwai/oop_abstraction)
    - [x] [120 OOP Polymorphism](https://github.com/marwai/oop_polymorphism)
    - [x] [121 OOP Encapsulation](https://github.com/marwai/DevOps/tree/master/oop_encapsulation)
- [x] Examples: 
    - [x] [122 Student Data Inheritance](https://github.com/marwai/student_data_inheritance)
    - [x] [123 Student Data Encapsulation Example](https://github.com/marwai/DevOps/tree/master/student_data_encapsulation)
    - [x] [124 Studet Data Polymorphism Example](https://github.com/marwai/student_data_polymorphism)
    - [x] [125 Student Data Abstraction Example](https://github.com/marwai/student_data_abstraction)     
- [x] [126 OOP with apis](https://github.com/marwai/oop_with_apis)  
    - [x] [127 json encoding decoding](https://github.com/marwai/oop_with_apis/json_encoding_decoding.py)
    - [x] [128 json parsing](https://github.com/marwai/DevOps/blob/master/oop_with_apis/json_parsing_with_api.py)
    - [x] [129 Exchange rates](https://github.com/marwai/DevOps/blob/master/oop_with_apis/json_exchange_rates.py)
    - [x] [130 exchange rates](https://github.com/marwai/DevOps/blob/master/oop_with_apis/exchange_rates.json) 
    - [x] [131json homework](https://github.com/marwai/DevOps/blob/master/oop_with_apis/json_api_homework.py)
- [x] [132 Test Driven Development (TDD)](https://github.com/marwai/DevOps/tree/master/python_tdd_pytest)
    - [x] [133 Calculator Exercise](https://github.com/marwai/DevOps/blob/master/devops_training/week_4_python_week_project/day_three/in_class_calc.py) , [Part IIlo](https://github.com/marwai/DevOps/blob/master/devops_training/week_4_python_week_project/day_three/in_class_calc_test.py)
- [x] [133 File Handling](https://github.com/marwai/DevOps/tree/master/filehandlingclasses)
- [x] [134 File Handling Homework](https://github.com/marwai/DevOps/tree/master/filehandlingclasshomework) 
- [x] [135 Database Connections](https://github.com/marwai/DevOps/tree/master/database_connections)

## Terminology

**APIs**
- **A**pplication **P**rogramming **I**interface (API)
- Set of tools that takes data and information and makes it universally accessible
- API makes a call to a server or database, executes request and returns response
- Gives programmers access to company's product or set of code that can be injected into your own project without having to build from scratch.
- Lately used to describe a kind of web interface.
- Web API is part of website designed to interact with programs that use specific URLs to request certain information (API call)
- Requested data returned in an easily processed format such as JSON or CSV.
- Built around HTTP protocol (meaning any programming language can be used to access them) e.g. Python, Java, Javascript, etc have at least one HTTP library to make this process easier.

---

**CRUD**
- When building APIs, we want our models to provide four basic types of functionality.
- The model must be able to `CREATE`, `READ`, `UPDATE`, and `DELETE` resources.
- CRUD paradigm common in constructing web applications, because it provides a memorable framework for reminding developers of how to construct full, usable models.

---
**CSV**
- **C**omma-**s**eparated **v**alues file
- Allows data to be saved in a tabular format 

Using pandas library to import CSV file into Python 
```bash
import pandas as pd
```

Using pyodbc to connect Python to SQL server
```bash
import pyodbc
```
---

**HTTP(Hypertext Transfer Protocol)**
- Foundation of WWW, used to load web pages using hypertext links.
- HTTP is an application layer **protocol** designed to transfer information between networked devices and runs on top of other layers of the network protocol stack
- A typical flow over HTTP involves a client machines making a request to a server, which then sends a response message.

---

**JSON(Javascript Object Notation)**
- Based on a subset of JavaScript language, it is a data storage language, similar to XML but adopts a 'dictionary' style syntax
- It is commonly used for transmitting data in web applications (e.g. sending data from server to the client, so it can be displayed on a web)

Example of JSON object
```json
{
  "first_name" : "Marcus",
  "last_name" : "Tse",
  "location" : "Kent",
  "online" : true,
  "no_friends" : 1200
}
```

---
**REST(Representational State Transfer)**
- Architectural style that defines set of **standards** to be used for creating Web services.
- REST-compliant systems or RESTful systems are characterised by how they are stateless and separate the concerns of client and server.
- REST is based on four methods defined by the HTTP protocol: `POST`, `GET`, `PUT`, and `DELETE`. These correspond to the four traditional actions performed on data in a database (CRUD): `CREATE`, `READ`, `UPDATE`, and `DELETE`.
---


`__name__ == __main__:`

---

**Try, Except, Else, Finally**
- Exceptions in python are objects that represent errors.
- Exceptions can be raised in many ways e.g passing invalid arguments to functions ("string" + int) or performing illegal operations (12/0).
- By default, exceptions stop Python programs and print a traceback to the console with information about the exception.

```python
try:
    """
    Code with exception you want to catch. 
    If exception raised (error occurs), control leaves this block and goes to except block
    """
except:
    """
    Executed only if an exception was raised in the try block. Code executed in this block is like normal code. 
    """
else:
    """
    Code executed only if no exceptions were raised in the try block
    """
finally:
    """
    This code ALWAYS executes after the other blocks, even if there was an uncaught exception or a return statement in one of the other blocks.
    """
```