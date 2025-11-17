# Day 46: Deploy an App on Docker Containers

## Task Overview

Create a Docker Compose configuration file to orchestrate multi-container applications. Docker Compose defines services, networks, and volumes in a single YAML file.

**Compose Configuration:**
- Define services and their configurations
- Specify container images and build contexts
- Configure ports, volumes, and networks
- Enable multi-container application deployment

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Start multi-container application using Docker Compose.

```sh
sudo touch /opt/itadmin/docker-compose.yml
```

**Step 2:** Connect to database server and verify configuration.

```yaml
services:
        web:
            image: php:apache
            container_name: php_web
            ports:
                - 6400:80
            volumes:
                - /var/www/html:/var/www/html
        
        db:
            image: mariadb:latest
            container_name: mysql_web
            ports:
                - 3306:3306
            volumes:
                - /var/lib/mysql:/var/lib/mysql
            environment:
                - MARIADB_DATABASE=database_web
                - MARIADB_USER=kkloud
                - MARIADB_PASSWORD=your-user-password
                - MARIADB_ROOT_PASSWORD=your-root-password
```

**Step 3:** Start multi-container application using Docker Compose.

```sh
docker compose -f /opt/itadmin/docker-compose.yml
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 45](day-45.md) | [Day 47 →](day-47.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
