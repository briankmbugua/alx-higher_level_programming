-- script that lists all the cities of california that can be found in the database hbtn_0d_usa
SELECT cities FROM states
WHERE name = California
ORDER BY cities.id ASC;
