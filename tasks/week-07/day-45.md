# Day 45: Resolve Dockerfile Issues

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
cat /opt/docker/Dockerfile
    ``
```

**Step 2:** Execute the command to complete this step.

```bash
2. Let's try to Build Image
```

**Step 3:** Execute the command to complete this step.

```bash
> It seems network timeout issue

3. Let's Pull the base image First
```

**Step 4:** Execute the command to complete this step.

```bash
> Image pulled successfully

4. Let's try to build again
```

**Step 5:** Build Docker image from Dockerfile.

```bash
> Now, we are getting certs file path issues. It's because the Dockerfile is trying to copy files from relative paths, but those files need to be in the Docker build context. We need to use the COPY instruction instead of RUN cp with absolute paths.
```

**Step 6:** Execute the command to complete this step.

```bash
5. We fixed Dockerfile, now let's build again
```

**Step 7:** Execute the command to complete this step.

```bash
6. We can verify using this command
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 44](day-44.md) | [Day 46 →](day-46.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
