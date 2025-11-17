# Day 42: Create Docker Network

## Task Overview

Establish Docker networks to enable communication between containers. Networks provide isolation and connectivity for containerized services.

**Network Configuration:**
- Create custom Docker network
- Define network driver type
- Connect containers to network
- Verify network connectivity

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Create a custom Docker network for container communication.

```sh
docker network create blog -d macvlan --ip-range 10.10.1.0/24 --subnet 10.10.1.0/24
```

**Step 2:** Execute the command to complete this step.

```sh
docker network ls
```

**Step 3:** Execute the command to complete this step.

```sh
docker network --help
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 41](day-41.md) | [Day 43 →](../week-07/day-43.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
