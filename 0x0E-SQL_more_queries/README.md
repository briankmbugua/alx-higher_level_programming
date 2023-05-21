# 0 My privilages
A script that lists all privilages of MySQL users user_0d_1 and user_0d_2 on your server in localhost

# Root user
a script that creates the MySQL server user user_0d_1, the user should have all privilages on your MySQL server, The password should be set to user_0d_1_pwd, the script should not fail

# Read User
Write a script that creates the database hbtn_0d_2 and the user_0d_2
- user_0d_2 should have only SELECT privilage in the databse hbtn_0d_2
- The user_0d_2 password should be set to user_0d_2_pwd
- the script should not fail if hbtn_0d_2 and user_0d_2 already exists

# Always a name
Wtite a script that creates the table force_name on your MySQL server.
- force_name description
   - id INT
   - name VARCHAR(256) can't be null
- the database name should be passe as an argument of the mysql command
- if the table force_name already exists, your script should not fail

# ID can't be null
Write a script that creates the table id_not_null on your MySQL server.
- id_not_null description
   - id INT with default value 1
   - name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table is_not_null already exists, your script should not fail

# Unique ID
Write a script that creates the table unique_id on your MySQL server
- unique_id description
  - id INT with the default value 1 and must be unique
  - name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- if the table unique_id already exists, your script should not fail

# States table
Write a script that creates the database hbnt_0d_usa and the table states(in the database hbtn_0d_usa) on your MySQL sever
- states description:
   - id INT unique, auto generated, can't be null and is a primary key
   - name VARCHAR(256) can't be null
-If the database hbtn_0d_usa already exists, your script should not fail
- IF the tables states already exists, your script should not fail

# Cities table
creat hbtn_0d_usa ab and the table cities on your MySQL server
- cities
   - id INT, auto generated, can't be null and is a primary key
   - state_id INT, can't be null and must be a FOREIGN KEY that references to id of the states table
   - name VARCHAR(256) can't be null
- If both the table and the database exist your script should not fail
# Cities of california
list all cities of california that can be found in hbtn_0d_usa database
- The states table contains only one record where name = california the id can be different
- sorted in ascending order by cities.id
- don't use JOIN keyword

# Cites by States
list all cities contained in the database hbtn_0d_usa
- Each record should display cities.id - cities.name - states.name
- sort in asceding order by cities.id
- you can only use one SELECT statement
# Genre ID by show
import database dump hbtn_0d_tvshowa
- List all shows contained in hbtn_0d_tvshows that have atleast one genre linked
- Result must be sorted in asceding order by tv_shows.title and tv_show_genres.genre_id
- Only one SELECT statement

# Genre ID for all shows
use database hbtn_0d_tvshows
List all shows
- display tv_shows.title - tv_show_genres.genre_id
- Ascending order by tv_shows.title and tv_shows_genres.genre_id
- If a show has no genre display NULL
- One SELECT statement

# No genre
hbtn_0d_tvshows
List all shows where genre is not linked
- Each  record should display tv_shows.title - tv_shows_genres.genere_id
- Ascending order by tv_shows.title and tv_shows_genres.genere_id
- You can only one SELECT statement

# My genres
List all genres of the show Dexter
- The tv_show contains only one record where title = Dexter but the id can be different
- display tv_genres.name
- Asceding order by the genre name
- One SELECT statement
# 15. Only Comedy
list all comedy shows
- Thw tv_genres table contains only one record where name = Comedy but the id can be different
- Each record should display tv_shows.title
- Ascending order by the shpw title
- One SELECT  statement
# List shows and genres
list all shows and all gemres linked to that show
- if a show dosen't have genre display NULL in the genre column
- display tv_shows.title - tv_generes.name
- Ascending order by the tv show title and genere name
- One SELECT statement


