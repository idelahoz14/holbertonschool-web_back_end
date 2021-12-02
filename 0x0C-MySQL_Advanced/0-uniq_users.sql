-- SQl script that creates a table
-- Table user with id, email and name

DROP TABLE IF EXIST 'users'
CREATE TABLE 'users'(
    'id' INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    'email' VARCHAR(255) UNIQUE,
    'name' VARCHAR(255)
);
