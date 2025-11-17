# Day 17: Install and Configure PostgreSQL

## Task Overview

Deploy PostgreSQL database server for application data management. Configure advanced open-source relational database system.

**PostgreSQL Setup:**
- Install PostgreSQL
- Configure authentication
- Create databases
- Set up user access

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Connect to the target server using SSH.

```sh
ssh user@db_host
```

**Step 2:** Connect to PostgreSQL database.

```sh
sudo -i -u postgres
    psql -c "CREATE DATABASE kodekloud_db6;"
    psql -c "CREATE ROLE kodekloud_aim LOGIN PASSWORD 'your-password';"
    psql -c "GRANT ALL PRIVILEGES ON DATABASE kodekloud_db6 TO kodekloud_aim;"
    psql -c "ALTER DATABASE kodekloud_db6 OWNER TO kodekloud_aim;"
```

**Step 3:** Connect to PostgreSQL database.

```sh
sudo psql -U postgres
```

**Step 4:** Execute the command to complete this step.

```SQL
CREATE DATABASE kodekloud_db6;
    CREATE ROLE kodekloud_aim LOGIN PASSWORD 'your-password';
    GRANT ALL PRIVILEGES ON DATABASE kodekloud_db6 TO kodekloud_aim;
    ALTER DATABASE kodekloud_db6 OWNER TO kodekloud_aim;
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 16](day-16.md) | [Day 18 →](day-18.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
