USE Northwind
DROP DATABASE Marcus_Tse_db;
CREATE DATABASE Marcus_Tse_db;
USE Marcus_Tse_db;

-- Create Statements
DROP TABLE film_table;
/* CREATING A DATABASE*/
--Identity(1,1)--->1, 1+1=2,3,4

CREATE TABLE film_table
(
    film_name VARCHAR(11),
    film_type VARCHAR(10),
    Date_of_release DATE,
    Director VARCHAR(20),
    Writer VARCHAR(10),
    STAR INT,
    Film_language CHAR(10),
    Official_Website VARCHAR(20),
    Plot_Summary VARCHAR(2000),
)
;

--film_id INT IDENTITY(1,1) PRIMARY KEY,
ALTER TABLE film_table
ADD film_id INT IDENTITY(1,5) PRIMARY KEY;


INSERT INTO film_table
    (film_name, film_type, Date_of_release, Director, Writer, STAR, Film_language, Official_Website, Plot_Summary)
VALUES
    ('Inception', 'Sci-fi', '2017-11-05', 'Christopher Nolan', 'Marcus Tse', 5, 'English', 'IMDB', 'Good film')
;

INSERT INTO film_table
    (film_name, film_type)
VALUES
    ('Star Wars', 'Sci-fi'),
    ('Star Trek', 'Sci-fi');

/*
CREATE TABLE film_table(
    film_id INT IDENTITY(1,1) PRIMARY KEY,
    film_name VARCHAR(50) NOT NULL,
    film_type VARCHAR(50)
)
*/

DROP TABLE director
CREATE TABLE director
(
    director_id INT IDENTITY(1,1),
    director_name VARCHAR(50),
    city VARCHAR(20) DEFAULT 'LONDON',
    film_id INT,
    PRIMARY KEY(director_id),
    FOREIGN KEY(film_id) REFERENCES film_table(film_id)
)
;

INSERT INTO director
    (director_name, film_id)
VALUES
    ('Steve', 1),
    ('Tom', 6);

INSERT INTO director
    (director_name, film_id)
VALUES
    ('Bob', 11);

SELECT * FROM director;
SELECT * FROM film_table;


UPDATE director SET director_name='Jamie' WHERE film_id=1
*/
--foreign key is a primary key as a reference
/*old code
ALTER TABLE director
ALTER film_id INT 
FOREIGN KEY 
REFERENCES film_table (film_id) ON DELETE CASCADE;
*/

-- constraint key = foreign

ALTER TABLE director
DROP CONSTRAINT film_id

-- One to many relationship one film_id and many film_id in director
ALTER TABLE director
ADD CONSTRAINT foreign_key_onFilmId FOREIGN KEY (film_id) 
REFERENCES film_table (film_id) ON DELETE CASCADE;

--Drop cascade
DELETE FROM film_table WHERE film_id=6;


-- Wednesday 24th June 2020 
/*
CHARINDEX('a','text) to search for a string e.g. find 'a' ina  colum called text

SUBSTRING (expression,start,length)
SUBSTRING(name,1,1) for the initial

LEFT or RIGHT - Left(name,5) for the first (or last) 5 characters 

LTRIM or RTRIM - Used to remove spaces at the beginning or end of a String 

REPLACE - Replaces (name, ' ', '_') to replace spaces with underscores 

LEN - finds length including spaces



*/
SELECT film_name, CHARINDEX('s', film_name)