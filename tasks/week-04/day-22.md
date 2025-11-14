# Day 22: Clone Git Repository

## Task Overview

The DevOps team established a new Git repository last week, which remains unused at present. However, the Nautilus application development team now requires a copy of this repository on the Storage Server in the Stratos DC. Follow the provided details to clone the repository

- The repository to be cloned is located at `/opt/games.git`
- Clone this Git repository to the `/usr/src/kodekloudrepos` directory. Ensure no modifications are made to the repository during the cloning process.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
cd /usr/src/kodekloudrepos
    git clone /opt/games.git
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 21](../week-03/day-21.md) | [Day 23 →](day-23.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
