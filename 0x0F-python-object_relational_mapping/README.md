# Object-relational Mapppers(ORMs)
An object relational mapper is a code library that automates the transfer of data stored in relational database tables into objects that are commonly used in application code.

# Why are ORMS useful?
ORMs provide a high-level abstraction upon a relational database that allows a developer to write python code instead of SQL to create, read, update and delete data schemas in their database.

# Downsides of using an ORM?
- Impedance mismatch
- potential for reduced performance
- Shifting complexity from the database into the application code

# transactions
a transaction is a logical unit of work that consists of one or more operations.These operations are typically database statements such as insert, update or delete which modify the database stored in the database

# cursors
A cursor is a database object that allows you to retrieve and manipulate data row by row.When you execute a query that returns multiple rows of data, the cursor allows you to move through those rows one at a time, and perform operations on each row as you go.
Cursor is like a pointer to a particular row of data within a result set.As you move the cursor, you can read the data in the current row, udate it, delete it, or insert new rows.
# stored procedures
This are precompiled and stored programs or routines that are desinged to execute a specific task or a set of tasks within a database system.They are written in specific programming language such as SQL.
# MySQLdb
MySQLdb is a thin Python wrapper around _mysql which makes it compatible with the pyhton DB API.In reality, a fair amount of the code which implements the API is in _mysql for the sake of efficiency
# Functions and attributes
Only a few top-level functions and attributes are defined within MySQLdb
## connect(parameters...)
Constructor for creating a connection to the database.Returns a connection Object.Note that some parameters must be specified as keyword arguments.The important parameters are
- ### host
name of the host to connect to.Default:use the local host via a UNIX socket where applicable
- ### user
user to authenticate as.Default:current effective user.
- ### password
password to authenticate with.Default:no password
- ### database
database to use.Default:no default database
- ### port
TCP port of MySQL server.Default:standard port(3306)

# Connection Objects
Connection object are returned by the connect() function.
## commit()
if the database and tables support transactions, this commits the current transaction;otherwise this method successfully does nothing
## rollback()
if the database and tables supports transaction, this rolls back(cancels) the current transaction;otherwise a NotSupportedError is raised.
## cursor([cursorclass])
MySQL does not support cursors:however they are easily emulated.You can supply an alternative cursor class as an optional parameter.If this is not present it defaults to the value given when creating the connection object.

# Cursor Objects
## callproc(procname, args)
Calls stored procedure procname with the sequence of arguments in args.Returns the original arguments
## close()
Closes the cursor.Further operations raise <span style="color:red">ProgrammingError</span>
## info()
Returns some information about the last query
## setinputsizes() and setoutputsizes()
Does nothing, successfully
## nextset()
Advances the cursor to the next result set, discarding the remaining rows in the current result set.If there are no additional result sets, it returns None;otherwise it retuns a true value.
# TASKS
## 0. Get all states
Write a script that list all states from the database hbtn_0e_0_usa:
- Your script should take 3 arguments: mysql username, mysql password, and databse name
- You must use the module MySQLdb import MySQLdb
- Your script should connect to a MySQL sever
- Results must be stored in asceding order by states.id
- Your code should not be executed when imported

