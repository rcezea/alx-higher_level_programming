-- list all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name FROM hbtn_0d_usa.cities AS s
WHERE id = (
    SELECT id FROM hbtn_0d_usa.states AS c
    WHERE c.id = s.id
);
