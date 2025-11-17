# Day 21: Setup Git Repository on Server

## Task Overview

Manage Git branches for parallel development workflows. Branches enable isolated feature development and experimentation.

**Branch Operations:**
- Create new branches
- Switch between branches
- Merge or rebase branches
- Manage branch lifecycle

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Install packages using the package manager.

```sh
sudo yum update -y
    sudo yum install -y git
```

**Step 2:** Execute the command to complete this step.

```sh
sudo git init --bare /opt/demo.git
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 20](day-20.md) | [Day 22 →](../week-04/day-22.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
