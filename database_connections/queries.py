from database_OOP import Database_OOP
import panda as pd

# database_OOP parent class
class queries_class:
    # static method in python, static includes the whole method. self is part of the instance,
    # methods are at a class level once static methods assigned
    # no static variables but are class variables, doesn't remember it's state level
    def All_products(self):
        object = Database_OOP()  # object of Database_OOP class
        # cursor runs all queries
        cursor = object.establishing_connection()  # cursor required to run queries in databse
        query_result = "SELECT * FROM products"
        rows = cursor.execute(query_result)
        for row in rows:
            print(row)

    def all_customers(self):
        object = Database_OOP()  # object of Database_OOP class
        # cursor runs all queries
        cursor = object.establishing_connection()  # cursor required to run queries in databse
        query_result = "SELECT * FROM customers"
        rows = cursor.execute(query_result)
        for row in rows:
            print(row)

    def average_product_price(self):
        object = Database_OOP()  # object of Database_OOP class
        # cursor runs all queries
        cursor = object.establishing_connection()  # cursor required to run queries in databse
        query_result = "SELECT AVG(UnitPrice) FROM Products"
        rows = cursor.execute(query_result)
        for row in rows:
            print(row)

    def choice(self):
        user_input = int(input("Please enter the number for the operation you want to execute::"
                               "\n 1. All products \n 2. All customers \n 3. Average unit price \n 4. Fetch Many\n "))
        if user_input == 1:
            self.All_products()
        elif user_input == 2:
            self.all_customers
        elif user_input == 3:
            self.average_product_price()
        elif user_input == 4:
            self.execute_sql()
        else:
            pass

    # def workingWith_fetchmany(self):
    #     object = Database_OOP
    #     cursor = object.establishing_connection()
    #     rows = cursor.fetchmany(30)
    #     for row in rows:
    #         print("Product Name::" + row.ProductName, "Costs::", row.UnitPrice)
    #
    #
    # # need to update this
    # def execute_sql(self):
    #     cursor = self.create_cursor(connection)
    #     query_result = cursor.execute(sql_command)
    #     try:
    #         if user_input == 1:
    #             self.workingWith_fetchone(query_result)
    #         elif user_input == 2:
    #             self.workingWith_fetchmany(query_result)
    #         else:
    #             raise ValueError
    #
    #     except ValueError:
    #         print("This is incorrect user_input")
    #
    # def workingWith_fetchone(self):
    #     pass
    #
    # def workingWith_fetchmany(self, query_result):
    #     rows = query_result.fetchmany(30)
    #     for row in rows:
    #         print("Product Name::" + row.ProductName, "Costs::", row.UnitPrice)
    #
    # def execute_sq1(self, parameter, oop_connection, user_input):
    #     pass
