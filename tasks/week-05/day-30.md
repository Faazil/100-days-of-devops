# Day 30: Git Reset Hard

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
git log --oneline
```

**Step 3:** Execute the command to complete this step.

```shell
[root@ststor01 ecommerce]# git log --oneline
    81e08fc (HEAD -> master, origin/master) Test Commit10
    686cb01 Test Commit9
    f0ff119 Test Commit8
    a8404ed Test Commit7
    a9fccf0 Test Commit6
    2554746 Test Commit5
    461c467 Test Commit4
    287d981 Test Commit3
    a63283d Test Commit2
    5479bcb Test Commit1
    90b2925 add data.txt file
    848a423 initial commit
```

**Step 4:** Execute the command to complete this step.

```ssh
git reset --hard 90b2925
```

**Step 5:** Fetch and merge changes from remote repository.

```shell
root@ststor01 ecommerce]# git status
    On branch master
    Your branch is behind 'origin/master' by 10 commits, and can be fast-forwarded.
    (use "git pull" to update your local branch)

    nothing to commit, working tree clean
```

**Step 6:** Push local commits to remote repository.

```sh
git push --force
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 29](day-29.md) | [Day 31 →](day-31.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
