# Day 25: Git Branch Merge

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

**Step 1:** Connect to the target server using SSH.

```sh
ssh user@storage-server
```

**Step 2:** Attempt to switch to the user and verify login is blocked.

```sh
sudo su
    cd /usr/src/kodekloudrepos/demo
```

**Step 3:** Switch to the specified branch.

```sh
# ensure current branch is master branch
    git branch
    # create a new branch
    git checkout -b nautilus
```

**Step 4:** Execute the command to complete this step.

```sh
cp /tmp/index.html .
```

**Step 5:** Stage files for commit.

```sh
git add .
    git commit -m "added tmp file"
```

**Step 6:** Execute the command to complete this step.

```sh
git switch master
```

**Step 7:** Merge changes from one branch into another.

```sh
git merge nautilus
    git push
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 24](day-24.md) | [Day 26 →](day-26.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
