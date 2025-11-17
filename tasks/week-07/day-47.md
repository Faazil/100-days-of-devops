# Day 47: Docker Python App

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

**Step 1:** Perform the initial setup or connection.

```sh
sudo -i
    cd /pythona_app
```

**Step 2:** Execute the command to complete this step.

```sh
sudo vi Dockerfile
```

**Step 3:** Execute the command to complete this step.

```Dockerfile
FROM python:3.9.23-slim

    WORKDIR /app

    COPY ./src/* /app/

    RUN pip install -r requirements.txt

    EXPOSE 6300

    CMD ["python", "server.py"]
```

**Step 4:** Build Docker image from Dockerfile.

```sh
docker build -t nautilus/python-app .
```

**Step 5:** Start a new container from the image.

```sh
docker run -d --name pythonapp_nautilus -p 8096:6300 nautilus/python-app
```

**Step 6:** List running containers to verify deployment.

```sh
docker ps
    curl http://localhost:8096
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 46](day-46.md) | [Day 48 →](day-48.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
