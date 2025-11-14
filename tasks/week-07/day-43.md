# Day 43: Docker Ports Mapping

## Task Overview

The Nautilus DevOps team is planning to host an application on a nginx-based container. There are number of tickets already been created for similar tasks. One of the tickets has been assigned to set up a nginx container on Application Server 2 within the Stratos DC. Please perform the task as per details mentioned below:

- Pull `nginx:stable` docker image on Application Server 2.

- Create a container named `cluster` using the image you pulled.

- Map host port `5002` to container port `80`. Please keep the container in running state.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
docker pull nginx:stable
```

**Step 2:**
```bash
docker run -d --name cluster -p 5002:80 nginx:stable
```

**Step 3:**
```bash
docker ps
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 42](../week-06/day-42.md) | [Day 44 →](day-44.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
