import pyodbc

class database_OOP:
    # 1 pass in connection parameters
    def __init__(self,server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    # 2 establishing the connection
    def establishing_connection(self):
        connections = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password

        try:
            with pyodbc.connect(connections, timeout=5) as connection:
                print("Connection did not time out")
        except:
            print("Connection Time out")
        else:
            return connection

    #3
    def create_cursor(self, connection):
        return connection.cursor()

    #4 execute sql commands
    def execute_sql(self, sql_command, connection, user_input):
        cursor = self.create_cursor(connection)
        query_result = cursor.execute(sql_command)
        try:
            if user_input ==1:
                self.workingWith_fetchone(query_result)
            elif user_input ==2:
                self.workingWith_fetchmany(query_result)
            else:
                raise ValueError

        except ValueError:
            print("This is incorrect user_input")

    def workingWith_fetchone(self):
        pass

    def workingWith_fetchmany(self, query_result):
        rows = query_result.fetchmany(30)
        for row in rows:
            print("Product Name::"+row.ProductName, "Costs::", row.UnitPrice)