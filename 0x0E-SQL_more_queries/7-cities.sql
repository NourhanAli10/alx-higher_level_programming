-- script that creates the database hbtn_0d_usa and the table cities 
-- (in the database hbtn_0d_usa) on your MySQL server.
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities` (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
    state_id INT NOT NULL
    FOREGIN KEY (state_id) REFERENCES states(id)
)
