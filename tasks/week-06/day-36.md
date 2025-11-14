# Day 36: Run a NGINX Container on Docker

## Task Overview

The Nautilus DevOps team is conducting application deployment tests on selected application servers. They require a nginx container deployment on Application Server 1. Complete the task with the following instructions:

On Application Server 1 create a container named nginx_1 using the nginx image with the alpine tag. Ensure container is in a running state.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo docker run -d --name nginx_1 -p 80:80 nginx:alpine
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 35](../week-05/day-35.md) | [Day 37 →](day-37.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
