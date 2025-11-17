# Day 26: Git Manage Remotes

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
    cd /usr/src/kodekloudrepos/beta
```

**Step 2:** Create or list Git branches.

```sh
git remote -v
    git branch
```

**Step 3:** Execute the command to complete this step.

```sh
git remote add dev_beta /opt/xfusioncorp_beta.git
    git remote -v
```

**Step 4:** Stage files for commit.

```sh
cp /tmp/index.html .
    git add .
    git commit -m "added tmp file"
```

**Step 5:** Push local commits to remote repository.

```sh
git push dev_beta master
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 25](day-25.md) | [Day 27 →](day-27.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
