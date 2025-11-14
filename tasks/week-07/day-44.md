# Day 44: Creating a Docker Compose File

## Task Overview

Nautilus dev team members shared static website content that needs to be hosted on the httpd web server using a containerised platform. The team has shared details with the DevOps team, and we need to set up an environment according to those guidelines. Below are the details:

- On App Server 3 in Stratos DC create a container named `httpd` using a docker compose file `/opt/docker/docker-compose.yml` (please use the exact name for file).

- Use `httpd` (preferably latest tag) image for container and make sure container is named as `httpd`; you can use any name for `service`.

- Map `80` number port of container with port `3003` of docker host.

- Map container's `/usr/local/apache2/htdocs` volume with `/opt/itadmin` volume of docker host which is already there. (please do not modify any data within these locations).

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
docker ps
```

**Step 2:**
```bash
sudo touch /opt/docker/docker-compose.yml
```

**Step 3:**
```bash
docker compose -f /opt/docker/docker-compose.yml up -d
```

**Step 4:**
```bash
docker ps
```

**Step 5:**
```bash
banner@stapp03 ~]$ docker ps
    CONTAINER ID   IMAGE          COMMAND              CREATED          STATUS          PORTS                  NAMES
    31c6d90cafa8   httpd:latest   "httpd-foreground"   37 seconds ago   Up 35 seconds   0.0.0.0:3003->80/tcp   httpd
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 43](day-43.md) | [Day 45 →](day-45.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
