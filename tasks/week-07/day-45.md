# Day 45: Resolve Dockerfile Issues

## Task Overview

The Nautilus DevOps team is working to create new images per requirements shared by the development team. One of the team members is working to create a Dockerfile on App Server 1 in Stratos DC. While working on it she ran into issues in which the docker build is failing and displaying errors. Look into the issue and fix it to build an image as per details mentioned below:

- The Dockerfile is placed on App Server 1 under /opt/docker directory.

- Fix the issues with this file and make sure it is able to build the image.

- Do not change base image, any other valid configuration within Dockerfile, or any of the data been used — for example, index.html.

Note: Please note that once you click on FINISH button all existing images, the containers will be destroyed and new image will be built from your Dockerfile.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
cat /opt/docker/Dockerfile
    ``
```

**Step 2:**
```bash
2. Let's try to Build Image
```

**Step 4:**
```bash
> It seems network timeout issue

3. Let's Pull the base image First
```

**Step 6:**
```bash
> Image pulled successfully

4. Let's try to build again
```

**Step 8:**
```bash
> Now, we are getting certs file path issues. It's because the Dockerfile is trying to copy files from relative paths, but those files need to be in the Docker build context. Next, use the COPY instruction instead of RUN cp with absolute paths.
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 44](day-44.md) | [Day 46 →](day-46.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
