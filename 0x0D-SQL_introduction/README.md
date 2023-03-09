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
> <span style="color:yellow"> CREATE TABLE </span> < table name > (  
    < attribute name 1 > < data type 1 >  
    < attribute name n > < data type n >  
    );
>
The <span style="color:yellow"> data types </span> that you will use most frequently are character strings, which might be called VARCHAR or CHAR for variable or fixed length strings: numeric types such as NUMBER or INTERGER, which will usually specify a precision; and DATE or related types  
### Alter table is also part of the ddl
> ALTER TABLE < table name >
ADD CONSTRAINT < constraint name > PRIMARY KEY (< attribute list >);
>

### Drop table is also part of the ddl
> DROP TABLE < table name >;  
ALTER TABLE < table name >
DROP CONSTRAINT < constraint name>;  
>
