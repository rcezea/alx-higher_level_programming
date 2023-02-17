-- create database hbtn_0d_usa with table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY
    state_id INT NOT NULL FOREIGN KEY,
    name VARCHAR(256) NOT NULL
);
