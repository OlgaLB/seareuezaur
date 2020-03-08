DROP DATABASE IF EXISTS airports_db;
CREATE DATABASE airports_db CHARACTER SET utf8 COLLATE utf8_general_ci;
DROP USER IF EXISTS 'airports_db_user'@'%';
CREATE USER 'airports_db_user'@'%' IDENTIFIED BY '12345678';
GRANT ALL PRIVILEGES ON airports_db.* TO 'airports_db_user'@'%';
USE airports_db;

CREATE TABLE `airports` (
  `name` varchar(128),
  `iata` varchar(32),
  `icao` varchar(32),
  `city` varchar(64),
  `country` varchar(64),
  `latitude` float,
  `longitude` float
);
