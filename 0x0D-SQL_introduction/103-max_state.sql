-- a script that displays the max temparature of each state(ordered by state name).
SELECT state, max(value) as maximum_temp
FROM temperatures
GROUP BY state
ORDER BY state;
