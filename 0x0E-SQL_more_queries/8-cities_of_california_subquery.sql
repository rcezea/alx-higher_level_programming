-- list all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name FROM cities AS c
WHERE c.state_id = (
    SELECT id FROM states
    WHERE name = 'California'
)
ORDER BY c.id;
