#!/usr/bin/python3
import MySQLdb as mdb

# Establish a connection to the MySQL database
con = mdb.connect('localhost', 'root', 'password', 'record_company')

# Use a 'with' block to ensure that the connection is closed automatically
# when the block is exited (even if there's an exception)
with con:
    
    # Create a cursor object to execute SQL statements
    cur = con.cursor()

    # Drop the 'Writers' table if it exists
    cur.execute("DROP TABLE IF EXISTS Writers")

    # Create a new 'Writers' table with columns 'Id' (auto-incremented integer) and 'Name' (string)
    cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")

    # Insert some records into the 'Writers' table
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
con.close()