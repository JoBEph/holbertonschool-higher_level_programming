-- 2-create_read_user.sql
-- Create user 'user_0d_2'@'localhost' identified by 'user_0d_2_pwd';
-- add read privileges to user_0d_2
--
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;