# What - we are trying to establish a connection and read data from the database in the python console
# In real time we see the output in the graphical user interface GUI
# pyodbc - just a python library helps you connect to database
# as per the wiki pyodbc is an open source python moudle that
# why - helping us to showcase data in the console which in real time, we would display

# import correct module
# find variables with login detaails (server,databse, username, password)
# connectionstring concatenated the variables
# troubleshoot
# with loop
# try for 5 seconds


# Specifying the ODBC driver, server name, database, etc. directly
import pyodbc

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'


server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print(cnxn)
print(cursor)

try:
    with pyodbc.connect(connection, timeout=5) as connection:
        print("Connection did not time out")
except:
    print("Connection Time out")
else:
    pass

query_result = cursor.execute('SELECT * FROM Products')

# # notes 1
# rows = query_result.fetchone()
# print(type(rows)) # pyodbc.row object
# print(rows[1]) # second column of rows-columns start from 0th index
# # print("Printing result object:", query_result)
# print(rows.ProductName)

# # notes 2
rows = query_result.fetchone()
print(type(rows)) # pyodbc.row object
print(rows[1]) # second column of rows-columns start from 0th index
print(rows.ProductName)

print("Executing fetchmany::", query_result.fetchmany(30))
for row in rows:
    print(row)

print("______FETCHALL-----")
rows = query_result.fetchall() # better way to fetch

for row in rows:
    print("ProductName::"+row.ProductName, "Costs:", row.UnitPrice)


# if you want to get back to the start, you need a new cursor or to run the excute command again
# fetchone row-fetchone(), if fetch many rows that is fetchmany(), if fetch all rows that is fetchall()



# acquire a cursor from a connection-execute the code-through
# the cursor-cursor.fetch-iterate through the results by using the raw objects that are returned by the cursor.fetch
# Cursor is a control structure that allows to control and manage rows of data from a response. In the pyodbc instance
# it is usd to manage our queries directly with the db
