# Day 36: Run a NGINX Container on Docker

## Task Overview

Build custom Docker images using Dockerfiles to package applications with their dependencies. Images serve as blueprints for creating containers.

**Image Creation:**
- Write Dockerfile with build instructions
- Define base image and dependencies
- Configure application setup
- Build and verify image

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Start a new container from the image.

```sh
sudo docker run -d --name nginx_1 -p 80:80 nginx:alpine
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 35](../week-05/day-35.md) | [Day 37 →](day-37.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
