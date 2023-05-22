CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT,
    PRIMARY KEY(id),
    state_id INT NOT NULL FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
