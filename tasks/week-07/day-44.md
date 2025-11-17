# Day 44: Creating a Docker Compose File

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

**Step 1:** List running containers to verify deployment.

```sh
docker ps
```

**Step 2:** Start multi-container application using Docker Compose.

```sh
sudo touch /opt/docker/docker-compose.yml
```

**Step 3:** Start multi-container application using Docker Compose.

```sh
docker compose -f /opt/docker/docker-compose.yml up -d
```

**Step 4:** List running containers to verify deployment.

```sh
docker ps
```

**Step 5:** List running containers to verify deployment.

```shell
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
