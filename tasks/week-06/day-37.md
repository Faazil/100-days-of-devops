# Day 37: Copy File to Docker Container

## Task Overview

The Nautilus DevOps team is conducting application deployment tests on selected application servers. They require completing a task on app server 1.

On Application Server 1 a container named ubuntu_latest is running, you have to copy the encrypted file `/tmp/nautilus.tx.gpg` from docker hosts to container folder `/usr/src`.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
docker cp /tmp/nautilus.txt.gpg ubuntu_latest:/usr/src/
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 36](day-36.md) | [Day 38 →](day-38.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
