# Day 39: Create a Docker Image From a Container

## Task Overview

One of the Nautilus developer was working to test new changes on a container. He wants to keep a backup of his changes to the container. A new request has been raised for the DevOps team to create a new image from this container. Below are more details about it:

- Create an image `ecommerce:nautilus` on `Application Server 3` from a container `ubuntu_latest` that is running on same server.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
docker commit container-name image-repository:tag
```

**Step 2:**
```bash
docker commit ubuntu_latest ecommerce:nautilus
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 38](day-38.md) | [Day 40 →](day-40.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
