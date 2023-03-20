# Object-relational Mapppers(ORMs)
An object relational mapper is a code library that automates the transfer of data stored in relational database tables into objects that are commonly used in application code.

# Why are ORMS useful?
ORMs provide a high-level abstraction upon a relational database that allows a developer to write python code instead of SQL to create, read, update and delete data schemas in their database.

# Downsides of using an ORM?
- Impedance mismatch
- potential for reduced performance
- Shifting complexity from the database into the application code
# TASKS
## 0. Get all states
Write a script that list all states from the database hbtn_0e_0_usa:
- Your script should take 3 arguments: mysql username, mysql password, and databse name
- You must use the module MySQLdb import MySQLdb
- Your script should connect to a MySQL sever
- Results must be stored in asceding order by states.id
- Your code should not be executed when imported

