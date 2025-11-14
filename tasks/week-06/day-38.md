# Day 38: Docker Pull Images

## Task Overview

Nautilus project developers are planning to start testing on a new project. As per their meeting with the DevOps team, they want to test containerized environment application features. As per details shared with DevOps team, we need to accomplish the following task:

a. Pull busybox:musl image on App Server 3 in Stratos DC and re-tag (create new tag) this image as busybox:blog.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
docker pull busybox:musl
```

**Step 2:**
```bash
docker tag busybox:musl busybox:blog
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 37](day-37.md) | [Day 39 →](day-39.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
