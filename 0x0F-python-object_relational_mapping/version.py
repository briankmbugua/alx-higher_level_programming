#!/usr/bin/python3
#Import the the MySQLdb module, which is a python interface for MySQL
import MySQLdb
#Import the sys module which provides acces to some variables used or maintained by the interpreter and to functions that interact strongly with the intepretor
import sys

# establish a connection to the MySQL  database using the MySQLdb.connect() function.The function takes four parameters:The host name, user name, password and the database name
try:
    con = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='password',
        db='record_company',
    )
    # create a cusor object to execute queries on the database connection
    cusor = con.cursor()
    # Execute a SELECT statement to retrieve the version number of the MySQL server using the cursor.execute() method.The version number is obtained by calling cursor.fethone() method.
    cusor.execute('SELECT VERSION()')
    result = cusor.fetchone()
    # print the version number using the result obtained from the SELECT statement
    print('MySQL version: {}'.format(result[0]))
    # catch any errors that might occur and print the error message using the except statement
except MySQLdb.Error as e:
    print('Error {}: {}'.format(e.args[0], e.args[1]))
    sys.exit(1)
# finally, close the database connection using the con.close() method
finally:
    if con:
        con.close()

