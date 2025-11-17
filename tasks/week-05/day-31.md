# Day 31: Git Stash

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
    cd /usr/src/kodekloudrepos/ecommerce
```

**Step 2:** Execute the command to complete this step.

```sh
git stash list
```

**Step 3:** Execute the command to complete this step.

```shell
[root@ststor01 ecommerce]# git stash list
    stash@{0}: WIP on master: 7fe985d initial commit
    stash@{1}: WIP on master: 7fe985d initial commit
```

**Step 4:** Execute the command to complete this step.

```sh
git stash apply stash@{1}
```

**Step 5:** Stage files for commit.

```sh
git add .
    git commit -m "Restored stash files"
    git push
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 30](day-30.md) | [Day 32 →](day-32.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
