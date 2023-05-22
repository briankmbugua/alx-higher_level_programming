-- script that lists all the cities of california that can be found in the database hbtn_0d_usa
SELECT cities FROM states
WHERE name = california
SORT BY cities.id
