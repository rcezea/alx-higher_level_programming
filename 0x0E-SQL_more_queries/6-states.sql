-- create database hbtn_0d_usa with table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE AUTO NOT NULL PRIMARY KEY,
    name VARCHAR(256)
);
