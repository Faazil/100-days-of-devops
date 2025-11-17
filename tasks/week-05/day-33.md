# Day 33: Git Merge Conflict Resolve

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

**Step 1:** Perform the initial setup or connection.

```sh
git fetch origin
```

**Step 2:** Stage files for commit.

```sh
git rebase origin/main

    git add .

    git rebase --continue
```

**Step 3:** Push local commits to remote repository.

```sh
git push
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 32](day-32.md) | [Day 34 →](day-34.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
