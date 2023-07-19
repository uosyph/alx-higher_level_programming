-- Creates Database if it doesn't already exist, and grants privileges to a certain user.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2 @localhost IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
