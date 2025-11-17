# Day 27: Git Revert Some Changes

## Task Overview

Execute Git version control operations for source code management. Track changes, collaborate, and maintain project history.

**Git Operations:**
- Configure Git settings
- Perform repository operations
- Manage commits and history
- Collaborate with remotes

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Attempt to switch to the user and verify login is blocked.

```sh
sudo su
    cd /usr/src/kodekloudrepos/demo
```

**Step 2:** Execute the command to complete this step.

```sh
git log --oneline
```

**Step 3:** Execute the command to complete this step.

```sh
git revert HEAD -m "revert demo"
```

**Step 4:** Push local commits to remote repository.

```sh
git push
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 26](day-26.md) | [Day 28 →](day-28.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
