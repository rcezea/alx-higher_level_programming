-- create a table called unique_id
CREATE TABLE IF NOT EXISTS unique_id(
    id INTEGER UNIQUE NOT NULL,
    name VARCHAR(256)
);