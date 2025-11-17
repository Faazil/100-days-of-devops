# Day 43: Docker Ports Mapping

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

**Step 1:** Download the Docker image from registry.

```sh
docker pull nginx:stable
```

**Step 2:** Start a new container from the image.

```sh
docker run -d --name cluster -p 5002:80 nginx:stable
```

**Step 3:** List running containers to verify deployment.

```sh
docker ps
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 42](../week-06/day-42.md) | [Day 44 →](day-44.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
