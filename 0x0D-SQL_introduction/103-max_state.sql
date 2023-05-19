-- a script that displays the max temparature of each state(ordered by state name).
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
