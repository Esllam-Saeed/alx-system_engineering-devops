-- script to setup replica user on master sql server

CREATE USER IF NOT EXISTS 'holberton_user'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'holberton_user'@'%';
GRANT SELECT ON *.* TO 'holberton_user'@'%';

-- check that it was configured properly 
SELECT user, Repl_slave_priv FROM mysql.user;
