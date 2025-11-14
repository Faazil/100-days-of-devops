# Day 21: Setup Git Repository on Server

## Task Overview

The Nautilus development team has provided requirements to the DevOps team for a new application development project, specifically requesting the establishment of a Git repository. Follow the instructions below to create the Git repository on the Storage server in the Stratos DC:

- Utilize yum to install the git package on the Storage Server.
- Create a bare repository named /opt/demo.git (ensure exact name usage).

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo yum update -y
    sudo yum install -y git
```

**Step 2:**
```bash
sudo git init --bare /opt/demo.git
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 20](day-20.md) | [Day 22 →](../week-04/day-22.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
