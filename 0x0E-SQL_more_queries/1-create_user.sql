-- create a user on MySQL server and grant them all the privilages of the root user.user_0d_1 password should be set to user_0d_1_pwd
CREATE USER 'user.user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'
GRANT ALL PRIVILAGES ON *.* TO 'user_0d_1'@'localhost';
