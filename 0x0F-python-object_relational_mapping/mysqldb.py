#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connect(user='root',passwd='password',database='record_company');
# to perform a query, you first need a cursor, and then you can execute queries on it
c = db.cursor()
c.execute("""SELECT * FROM albums""") # this will return a result set of the MySQL query which will be stored on the cursor object
#The cursor object works as a pointer to the current row in the result set, and you can use cursor methods such as fetchone(), fetchmany() and fetchall() to retrieve the data from the result set one row at a time or in batches.
#The cursor object only stores the result set of the most recent query that was executed.If you execute another query with the same cursor object the previous result set will be discarded and replaced with the new result set.
row = c.fetchone() #fetchone() is one of the methods of the cursor object
while row is not None:
    print(row)
    row = c.fetchone()

# sql = """SET 'release_year = 1986
# WHERE id = 1"""
# c.execute(sql)
# c.commit()
# c.close()