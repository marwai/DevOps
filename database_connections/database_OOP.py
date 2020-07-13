import pyodbc
# Creating a class with singular method
class Database_OOP:
    # method connects to db
    server = 'databases2.spartaglobal.academy'  #
    database = 'Northwind'
    username = 'SA'
    password = 'Passw0rd2018'

    # when this method, cursor is returned
    def establishing_connection(self):
        connections = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password
        #
        try:
            with pyodbc.connect(connections, timeout=5) as connection:
                print("Connection did not time out")
        except:
            print("Connection Time out")
        else:
            cursor = connection.cursor() # variable set to cursor
            return cursor # return the value of allocated position of the cursor


    # 3
    # def create_cursor(self, connection):
    #     return connection.cursor()

    #4 execute sql commands
#     def execute_sql(self, sql_command, connection, user_input):
#         cursor = self.create_cursor(connection)
#         query_result = cursor.execute(sql_command)
#         try:
#             if user_input ==1:
#                 self.workingWith_fetchone(query_result)
#             elif user_input ==2:
#                 self.workingWith_fetchmany(query_result)
#             else:
#                 raise ValueError
#
#         except ValueError:
#             print("This is incorrect user_input")
#
#     def workingWith_fetchone(self):
#         pass
#
#     def workingWith_fetchmany(self, query_result):
#         rows = query_result.fetchmany(30)
#         for row in rows:
#             print("Product Name::"+row.ProductName, "Costs::", row.UnitPrice)
#
#     def execute_sq1(self, parameter, oop_connection, user_input):
#         pass
#
# # db = database_OOP()
# # db.execute_sql()