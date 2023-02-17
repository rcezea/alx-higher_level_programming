-- create a table called unique_id
CREATE TABLE IF NOT EXISTS unique_id(
    id INTEGER NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
);