# Day 24: Git Branch Create

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
    cd /usr/src/kodekloudrepos/media
```

**Step 2:** Create or list Git branches.

```sh
git branch
```

**Step 3:** Execute the command to complete this step.

```sh
git switch master
```

**Step 4:** Switch to the specified branch.

```sh
git checkout -b xfusioncorp_media
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 23](day-23.md) | [Day 25 →](day-25.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
