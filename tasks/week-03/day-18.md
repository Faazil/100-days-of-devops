# Day 18: Configure LAMP Server (LAMP Stack)

## Task Overview

Install and configure web server software for hosting applications. Set up HTTP service with custom port and configuration.

**Web Server Setup:**
- Install web server package
- Configure server settings
- Adjust ports and document root
- Start and enable service

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Install packages using the package manager.

```sh
sudo yum install -y httpd php php-mysqli
```

**Step 2:** Enable service to start automatically on boot.

```sh
sudo cp /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.bak
    sudo sed -i 's/\<80\>/3003/g' /etc/httpd/conf/httpd.conf
    sudo systemctl enable --now httpd
```

**Step 3:** Check the service status to verify it's running.

```sh
sudo yum install -y mariadb-server
    sudo systemctl enable --now mariadb
    sudo systemctl status mariadb | grep "running"
```

**Step 4:** Connect to database server and verify configuration.

```sh
mysql -u root -e "CREATE DATABASE kodekloud_db2;"
    mysql -u root -e "CREATE USER 'kodekloud_cap'@'%' IDENTIFIED BY 'your-pass';"
    mysql -u root -e "GRANT ALL ON kodekloud_db2.* TO 'kodekloud_cap'@'%';"
    mysql -u root -e "FLUSH PRIVILEGES;"
```

**Step 5:** Connect to database server and verify configuration.

```bash
# Current Session
export PATH=${PATH}:/usr/local/mysql/bin
# Permanantly
echo 'export PATH="/usr/local/mysql/bin:$PATH"' >> ~/.bash_profile
```

**Step 6:** Connect to database server and verify configuration.

```bash
mysql -u root -p
```

**Step 7:** Connect to database server and verify configuration.

```sql
SELECT User, Host FROM mysql.user;
```

**Step 8:** Execute the command to complete this step.

```sql
CREATE USER 'someuser'@'localhost' IDENTIFIED BY 'somepassword';
```

**Step 9:** Execute the command to complete this step.

```sql
GRANT ALL PRIVILEGES ON * . * TO 'someuser'@'localhost';
FLUSH PRIVILEGES;
```

**Step 10:** Execute the command to complete this step.

```sql
SHOW GRANTS FOR 'someuser'@'localhost';
```

**Step 11:** Execute the command to complete this step.

```sql
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'someuser'@'localhost';
```

**Step 12:** Execute the command to complete this step.

```sql
DROP USER 'someuser'@'localhost';
```

**Step 13:** Execute the command to complete this step.

```sql
exit;
```

**Step 14:** Execute the command to complete this step.

```sql
SHOW DATABASES
```

**Step 15:** Execute the command to complete this step.

```sql
CREATE DATABASE acme;
```

**Step 16:** Execute the command to complete this step.

```sql
DROP DATABASE acme;
```

**Step 17:** Execute the command to complete this step.

```sql
USE acme;
```

**Step 18:** Execute the command to complete this step.

```sql
CREATE TABLE users(
id INT AUTO_INCREMENT,
   first_name VARCHAR(100),
   last_name VARCHAR(100),
   email VARCHAR(50),
   password VARCHAR(20),
   location VARCHAR(100),
   dept VARCHAR(100),
   is_admin TINYINT(1),
   register_date DATETIME,
   PRIMARY KEY(id)
);
```

**Step 19:** Execute the command to complete this step.

```sql
DROP TABLE tablename;
```

**Step 20:** Execute the command to complete this step.

```sql
SHOW TABLES;
```

**Step 21:** Execute the command to complete this step.

```sql
INSERT INTO users (first_name, last_name, email, password, location, dept, is_admin, register_date) values ('Brad', 'Traversy', 'brad@gmail.com', '123456','Massachusetts', 'development', 1, now());
```

**Step 22:** Execute the command to complete this step.

```sql
INSERT INTO users (first_name, last_name, email, password, location, dept,  is_admin, register_date) values ('Fred', 'Smith', 'fred@gmail.com', '123456', 'New York', 'design', 0, now()), ('Sara', 'Watson', 'sara@gmail.com', '123456', 'New York', 'design', 0, now()),('Will', 'Jackson', 'will@yahoo.com', '123456', 'Rhode Island', 'development', 1, now()),('Paula', 'Johnson', 'paula@yahoo.com', '123456', 'Massachusetts', 'sales', 0, now()),('Tom', 'Spears', 'tom@yahoo.com', '123456', 'Massachusetts', 'sales', 0, now());
```

**Step 23:** Execute the command to complete this step.

```sql
SELECT * FROM users;
SELECT first_name, last_name FROM users;
```

**Step 24:** Execute the command to complete this step.

```sql
SELECT * FROM users WHERE location='Massachusetts';
SELECT * FROM users WHERE location='Massachusetts' AND dept='sales';
SELECT * FROM users WHERE is_admin = 1;
SELECT * FROM users WHERE is_admin > 0;
```

**Step 25:** Execute the command to complete this step.

```sql
DELETE FROM users WHERE id = 6;
```

**Step 26:** Execute the command to complete this step.

```sql
UPDATE users SET email = 'freddy@gmail.com' WHERE id = 2;
```

**Step 27:** Execute the command to complete this step.

```sql
ALTER TABLE users ADD age VARCHAR(3);
```

**Step 28:** Execute the command to complete this step.

```sql
ALTER TABLE users MODIFY COLUMN age INT(3);
```

**Step 29:** Execute the command to complete this step.

```sql
SELECT * FROM users ORDER BY last_name ASC;
SELECT * FROM users ORDER BY last_name DESC;
```

**Step 30:** Execute the command to complete this step.

```sql
SELECT CONCAT(first_name, ' ', last_name) AS 'Name', dept FROM users;
```

**Step 31:** Execute the command to complete this step.

```sql
SELECT DISTINCT location FROM users;
```

**Step 32:** Execute the command to complete this step.

```sql
SELECT * FROM users WHERE age BETWEEN 20 AND 25;
```

**Step 33:** Execute the command to complete this step.

```sql
SELECT * FROM users WHERE dept LIKE 'd%';
SELECT * FROM users WHERE dept LIKE 'dev%';
SELECT * FROM users WHERE dept LIKE '%t';
SELECT * FROM users WHERE dept LIKE '%e%';
```

**Step 34:** Execute the command to complete this step.

```sql
SELECT * FROM users WHERE dept NOT LIKE 'd%';
```

**Step 35:** Execute the command to complete this step.

```sql
SELECT * FROM users WHERE dept IN ('design', 'sales');
```

**Step 36:** Execute the command to complete this step.

```sql
CREATE INDEX LIndex On users(location);
DROP INDEX LIndex ON users;
```

**Step 37:** Execute the command to complete this step.

```sql
CREATE TABLE posts(
id INT AUTO_INCREMENT,
   user_id INT,
   title VARCHAR(100),
   body TEXT,
   publish_date DATETIME DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY(id),
   FOREIGN KEY (user_id) REFERENCES users(id)
);
```

**Step 38:** Execute the command to complete this step.

```sql
INSERT INTO posts(user_id, title, body) VALUES (1, 'Post One', 'This is post one'),(3, 'Post Two', 'This is post two'),(1, 'Post Three', 'This is post three'),(2, 'Post Four', 'This is post four'),(5, 'Post Five', 'This is post five'),(4, 'Post Six', 'This is post six'),(2, 'Post Seven', 'This is post seven'),(1, 'Post Eight', 'This is post eight'),(3, 'Post Nine', 'This is post none'),(4, 'Post Ten', 'This is post ten');
```

**Step 39:** Execute the command to complete this step.

```sql
SELECT
  users.first_name,
  users.last_name,
  posts.title,
  posts.publish_date
FROM users
INNER JOIN posts
ON users.id = posts.user_id
ORDER BY posts.title;
```

**Step 40:** Execute the command to complete this step.

```sql
CREATE TABLE comments(
    id INT AUTO_INCREMENT,
    post_id INT,
    user_id INT,
    body TEXT,
    publish_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) references users(id),
    FOREIGN KEY(post_id) references posts(id)
);
```

**Step 41:** Execute the command to complete this step.

```sql
INSERT INTO comments(post_id, user_id, body) VALUES (1, 3, 'This is comment one'),(2, 1, 'This is comment two'),(5, 3, 'This is comment three'),(2, 4, 'This is comment four'),(1, 2, 'This is comment five'),(3, 1, 'This is comment six'),(3, 2, 'This is comment six'),(5, 4, 'This is comment seven'),(2, 3, 'This is comment seven');
```

**Step 42:** Execute the command to complete this step.

```sql
SELECT
comments.body,
posts.title
FROM comments
LEFT JOIN posts ON posts.id = comments.post_id
ORDER BY posts.title;
```

**Step 43:** Execute the command to complete this step.

```sql
SELECT
comments.body,
posts.title,
users.first_name,
users.last_name
FROM comments
INNER JOIN posts on posts.id = comments.post_id
INNER JOIN users on users.id = comments.user_id
ORDER BY posts.title;
```

**Step 44:** Execute the command to complete this step.

```sql
SELECT COUNT(id) FROM users;
SELECT MAX(age) FROM users;
SELECT MIN(age) FROM users;
SELECT SUM(age) FROM users;
SELECT UCASE(first_name), LCASE(last_name) FROM users;
```

**Step 45:** Execute the command to complete this step.

```sql
SELECT age, COUNT(age) FROM users GROUP BY age;
SELECT age, COUNT(age) FROM users WHERE age > 20 GROUP BY age;
SELECT age, COUNT(age) FROM users GROUP BY age HAVING count(age) >=2;
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 17](day-17.md) | [Day 19 →](day-19.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
