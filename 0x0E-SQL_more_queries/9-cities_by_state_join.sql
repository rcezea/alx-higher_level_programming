--list all  cities
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN  states
ON states.id = cities.state_id;
