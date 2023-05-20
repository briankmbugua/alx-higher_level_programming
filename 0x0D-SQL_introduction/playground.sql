SELECT * FROM first_table;

ALTER TABLE first_table
ADD column_name datatype

INSERT INTO first_table (id, name)
VALUES (89, 'Best School')


SELECT id FROM first_table
WHERE id = 89;

SELECT COUNT(id) FROM first_table
WHERE id = 89;

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
)
INSERT INTO second_table(id, name, score)
VALUES (1, 'john', 10)

SELECT score, name FROM second_table ORDER BY score;

SELECT * FROM second_table WHERE score >= 10;

UPDATE second_table
SET score = 10
WHRER name = 'Bob' 

SELECT AVG(score) FROM second_table;

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;

SELECT score, name FROM second_table ORDER BY score DESC WHERE name IS NOT NULL ORDER BY score DESC;

CREATE TABLE hbtn_0c_0.first_table AS SELECT * FROM hbtn_0e_0_usa.first_table;


mysql -u root -p hbtn_0c_0 < /home/letbmk/Downloads/temparatures.sql;

SELECT AVG(value), city FROM temperatures GROUP BY city ORDER BY AVG(value) DESC;

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP by CITY ORDER BY avg_temp DESC;


