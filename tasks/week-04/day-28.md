# Day 28: Git Cherry Pick

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

**Step 1:** Attempt to switch to the user and verify login is blocked.

```sh
sudo su
    cd /usr/src/kodekloudrepos/official
```

**Step 2:** Create or list Git branches.

```sh
git branch
```

**Step 3:** Execute the command to complete this step.

```sh
git log
```

**Step 4:** Push local commits to remote repository.

```sh
git switch master
    git cherry-pick commit-hash
    git push
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 27](day-27.md) | [Day 29 →](../week-05/day-29.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
