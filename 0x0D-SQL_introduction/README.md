# Learning Objectives
Explain this
# General
- What's a database
- What's a relational database
- What does SQL stand for
- What's MySQL
- How to create a database in MySQL
- What does <span style="color:red">DDL</span> and <span style="color:red">DML</span>  stand for
- How to <span style="color:red">CREATE</sapn> or <span style="color:red">ALTER</span> a table
- How to <span style="color:red">SELECT</span> data from a table
- How to <span style="color:red">INSERT</span>,<span style="color:red">UPDATE</span> or <span style="color:red">DELETE</span> data
- What are <span style="color:red">subqueries</span>
- How to use MySQL functions

# WHATS IS DATA
In simple words data can be facts related to any object inconsideration.
For example your name, age, height, weight, etc
# WHAT IS A DATABASE
A database is a systematic collection of data since the data in databases is organized it makes data management easy
# WHAT IS A DATABASE MANAGEMENT SYSTEM(DBMS)?
is a collection of programs which enables its users to acces database, manipulate data and help in representation of data
# TYPES OF DBMS
- ## Hierarchical
This types of dbms employ the child parent relationship pf storing data
- ## Network dbms
This type supports many to many relationship
- ## Relatioal dbms
This type defines database relationships in form of tables also called relations does not support many to many relationships they usually have defined data types they can use
- ## Oject oriented relation dbms
This type supports storage of new data types the data to be stored is in the form of objects the objects to be stored in the database have attributes e.g gender or age and methods that define what to do with the data e.g postgressSQL


# WHAT IS SQL
Structured query language can be used to insert, search, update and delete database records.
Relational databases like MYSQL, ORACLE, MS SQL SERVER, SYBASE ETC USE SQL! The sql syntax in thes databases is almost similar except the fact that some databases use different syntaxes and even proprietary sql syntaxes

# Basic SQL statements: DDL and DML
SQL statements are divided into two major categories: <span style="color:yellow">data defination language(DDL)</span> and <span style="color:yellow">data manipulation language(DML)</span>

# Data defination language
DDL statements are used to build and modify the structure of your tables and other objects in the database.  
When you execute a DDL statement it takes effect immediately
- The create table statement does excatly that
```sql
CREATE TABLE<table name>(  
    < attribute name 1 > < data type 1 >  
    < attribute name n > < data type n >  
    );
```
The <span style="color:yellow"> data types </span> that you will use most frequently are character strings, which might be called VARCHAR or CHAR for variable or fixed length strings: numeric types such as NUMBER or INTERGER, which will usually specify a precision; and DATE or related types  
### Alter table is also part of the ddl
```sql
ALTER TABLE < table name >
ADD CONSTRAINT < constraint name > PRIMARY KEY (< attribute list >);
```

### Drop table is also part of the ddl
```sql
DROP TABLE < table name >;  
ALTER TABLE < table name >
DROP CONSTRAINT < constraint name>;  
```
All of the information about your objects in your schema is contained, not suprisingly, in a set of tables that is called the <span style="color:yellow">data dictionary</span>

# Data manipulation language
DML statements are used to work with the data in tables.  
When you are connected to most multi-user databases you are in effect working with a private copy of your tables that can't be seen by anyoone else untill you are finished or tell the system that you are finished  
The SELECT statement is considered to be part of DML even though it just retrieves data rather than modifying it.
- The insert statement is used to add new rows to a table
```sql
INSERT INTO < table name >  
VALUES (<value 1>, ... <value n>);
```
The comma-delimited list of values must match the table structure excatly in the number of attributes and the data type of each attribute
Character type values are always in quotes; date values are often(but not always) in the format 'yyy-mm-d'
YOU WILL NEED TO SEPARATE <span style="color:yellow">INSERT</span> statement for every row
- The update statement is used to change values that are already in a table
```sql
UPDATE <table name>
SET <attribute> = <expression>
WHERE <condition>;
```

The update expression can a constant, any computed value, or even the result of a SELECT statement that returns a single row and a single column.  
If the WHERE clause is omitted, then the specified attribute is set to the same value in every row of the table
You can also set multiple attributes values at the same time with a comma-delimited list of attribute=expression pairs
- The <span style="color:yellow">DELETE</span> does just that for rows in a table
```sql
DELETE FROM <table name>
  WHERE <condtion>;
```
If the WHERE clause is omitted then every row of the table is deleted
- if you are using a multi-user system, you may need to make your DML changes visible to the rest of the users of the database.When you log out just type:
```sql
COMMIT;
```
- If you've messed up your changes in this type of system, and want to restore your private copy of the database to the way it was before you started(this works if you haven't already typed COMMIT), just type:
```sql
ROLLBACK
```

# Basic queries: SQL and RA
In SQL, to retrieve data stored in our tables, we use the SELECT statement.The result of this statement is always in form of a table that we can view with our database client software or use with programming languages to build dynamic web pages or desktop applications.  
While the result may look like a table, it is not stored in the database like the named tables are.  
The result of a SELECT statement can also be used a part of another statement.
# Basic syntax of SELECT statement
SELECT Statement Consists of four clauses
```sql
SELECT {attribute}+
  FROM {table}+
  [ WHERE {boolean predicate to pick rows} ]
  [ ORDER BY {attribute}+ ]
```
Of the four clauses, only the first two are required.The two shown in square brackets are optional.
It is helpful to follow a specific step-by-step sequence.
- The SELECT clause allows us to specify a comma-separated list of attribute names corresponding to the columns that are to be retrieved.You can use the * asterisk character, to retrieve all the columns
- The FROM clause is where we specify the name of the table from which to retrieve rows
- The WHERE clause is used to constrain which rows to retrieve.By specifying a boolean predicate that compares the values of table columns to literal values or to other columns
- The OEDER BY clause gives us a way to order the display of the rows in the result statement

# Retrival with relational algebra
SQL is a declarative language As such, SQL is used to declare what is to be retrieved from the database.
In an imperative language, we do specifiy the steps to take to solve a problem, such as how to retrieve data from a database.Thus, it is the responsibility of the database system to determine how to retrieve what is declared in SQL.  
In relational database systems this is done by translating SQL into <span style="color:blue">Relational Algebra</span>

# SQL technique: functions
Sometime the information we need is not actually in the database, but has to be computed in some way.
There are many functions in the implementation of SQL.

# Computed columns
We can compute values from information that is in a table simply by showing the computation in the SELECT clause.Each computation creates a new column in the output table, just as if it were a named table
Example from orderlines table which has a unitSaleprice column
```sql
SELECT unitSalePrice * quantity
FROM orderlines;
```
Computations are not just limited to column names;they also include constants e.g
```sql
SELECT unitSalePrice * 1.06
FROM orderlines;
```
We can create our own column heading or alias using the AS keyword.
```sql
SELECT unitSalePrice * quantity AS subtotal
FROM orderlines;
```
# Aggregate functions
SQL <span style="color:yellow">aggregate functions</span> let us compute values based on multiple rows.They are used as part of the SELECT clause, and also create new columns in the output.  
***Example*** Let's just find the total amount of all our sales from the orderline table
```sql
SELECT SUM(unitSalePrice * quantity) AS totalsales
FROM orderlines;
``` 
### GROUP BY clause
```sql
SELECT custID, orderDate, SUM(unitSalePrice * quantity)
FROM orderlines
GROUP BY custID, orderDate;
```
The SELECT clause and the GROUP BY clause contain excatly the same list of attributes, except for the calculation.In most cases there will be an error message if you forget to do this.
Other frequently-used functions that work the same way as SUM include MIN(minimum value of those in the grouping), MAX(max value of those in the grouping), and AVG(avarage of those in the grouping)

The COUNT function is slightly different, since it returns the number of rows in a grouping.To count all rows we can use the asterisk * 
```sql
SELECT COUNT(*)
FROM orders;
```
# Other functions
Refer to documentation to use different functions from database management systems
- Functions for rounding, truncating, converting, and formatting numeric data types.
- Functions for concatenating, altering case, and manipulating data types.
- Functions for formatting dates and times, or retrieving the date and time from the OS
- Functions for converting data types such as dates or numeric to character string, and vice-versa
- Functions for supplying visible values to null attributes, allowing conditional output and other miscellaneous tasks.

# SQL techniques: subqueries
Sometimes you don't have enough information available when you desing a query to determine which rows you want.In this case you will have to find the required information with a <span style="color:yellow">subquery</span>
Example: Find the name of customers who live in the same zip code area as Wayne Dick
```sql
SELECT cFirstName, cLastName
FROM customers
WHERE cZipCode = ???
```
- We don't know what zip code to put in the WHERE cluase
- We can find the right zipcode by(since we arleady have Wayne Dick)
```sql
SELECT cZipCode
FROM Customers
WHERE cFirstName = 'Wayne' AND cLastName = 'Dick';
```
Now with the above query we have the zipcode, This query returns a single column and a single row.We can use the result as the condition value for cZipCode in the original query.  
In effect, the output of the second query becomes the input to the first one
- Syntactically, all we have to do is to enclose the subquery in parentheses, in the same place where
```sql
SELECT cFirstName, cLastName
FROM customers
WHERE cZipCode = (SELECT cZipCode
FROM Customers
WHERE cFirstName = 'Wayne' AND cLastName = 'Dick';)
```

A subquery that returns only one column and one row can be used any time we need a single value

# TASKS
- ## 0.list databases
Write a script that lists all databases of your MySQL server.  
### discussion
The most common way to get a list of the MySQL databases is by using the mysql client to connect to the MySQL server and run SHOW DATABASES command.
```bash
$ mysql -u user -p
mysql> SHOW SCHEMAS/DATABASES;
```
The command will print a list of all the databases for which the user has some kind of a privilage granted to.  
You can also use SHOW SCHEMAS; The output will be the same as SHOW DATABASES command
- ## 1.Create a database
The script should not fail if the database already exists.
Don't use SELECT or SHOW statements
### discussion
```bash
mysql> CREATE DATABASE menagerie;
```
Under unix database names are case-sensitive,This is also true for table names.Creating a database does not select it for use.You must do that explicitly.
```bash
mysql> USE menagerie
Database changed
```
You can select the database on the command line when you invoke mysql
```bash
$>mysql -h host -u user -p menagerie
Enter password: ******
```
- ## 2. Delete a database
A script that deletes the database hbtn_0c_0 in your MySQL server.The script should not fail if the database does not exist.
### discussion
The DROP DATABASE statement is used to drop an existing SQL database.
```sql
DROP DATABASE databasename;
```
- ## 3. List tables
List all tables in a MySQL database
### discussion
SHOW TABLES;
- ## 4. First table
Write a script that creates a table called first_table in the current database in your MySQL server
### discussion
Use CREATE TABLE
- ## 5 full table description without using DESCRIBE OR EXPLAIN statements
The script 'SHOW CREATE TABLE first_table' this is a MySQL command that retrieves the complete CREATE TABLE statement used to create the 'first_table' in the specified database.it does not modify the table or its contents; rather it provides you with the original SQL statement used to crate the table
## List all in table
Script that lists all rows of the table first_table

## First add 
insert a new row in a table
### discussion
Use the INSERT INTO SQL statement

## Count 89
A script that displays the number of records with a certain column value

## Full creation 
Create a table in MySQL and add multiple rows and also insert data
### discussion
use CREATE TABLE SQL statement and INSER INTO.

## List by best
select all scores and name of a table with scores and name columns and several other columns and order by the scores highest score at the top

## Select the best
A Script that lists all records with a condition
### discussion
USE SQL WHERE clause

## cheating is bad
Write a script that updates a score
### discussion
Use the UPDATE statement in combination with the WHERE clause to tartget the specific person to update the score for.

## Score too low
Write a script that removes all records with a score<=5
### discussion
Use the delete statement in combination with where clause

## Average
score avarge of all records
### discussion
use AVG clause after selecting all score records also include AS clause

## Number by score
list number of records with the same score

### discussion
Use COUNT and ORDER BY clauses

## Say my name
script that lists all records of second_table
don't list those without a name value and in DESC order
### discussion
To check those without name use IS NOT NULL

## Go to UTF8
converts a database to UTF8(utf8mb4, collate utf8mb4_unicode_ci)

##  Temperatures #0
import in hbtn_0c_ database this table dump temperaturs.sql and write a script that displays the avarage temperature by city ordered by temperature
### discussion
to import use this command mysql -u root -p hbtn_0c_0 < temperatures.sql or import using the MySQL workbench.

## Temperatures #1
a script that displays the top 3 of cities temparature during July and August ordered by temperature(descending)

