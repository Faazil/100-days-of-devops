# Day 32: Git Rebase

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
sudo -i
    cd /usr/src/kodekloudrepos/games
```

**Step 2:** Create or list Git branches.

```sh
git branch
```

**Step 3:** Execute the command to complete this step.

```sh
git rebase master
```

**Step 4:** Push local commits to remote repository.

```sh
git push --force --set-upstream origin feature
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 31](day-31.md) | [Day 33 →](day-33.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
