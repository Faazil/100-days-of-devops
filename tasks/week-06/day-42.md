# Day 42: Create Docker Network

## Task Overview

The Nautilus DevOps team needs to set up several docker environments for different applications. One of the team members has been assigned a ticket where he has been asked to create some docker networks to be used later. fulfill this objective based on the following ticket description:

- Create a docker network named as `blog` on App Server 2 in Stratos DC.
- Configure it to use `macvlan` drivers.
- Set it to use subnet `10.10.1.0/24` and iprange `10.10.1.0/24`.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
docker network create blog -d macvlan --ip-range 10.10.1.0/24 --subnet 10.10.1.0/24
```

**Step 2:**
```bash
docker network ls
```

**Step 3:**
```bash
docker network --help
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 41](day-41.md) | [Day 43 →](../week-07/day-43.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
