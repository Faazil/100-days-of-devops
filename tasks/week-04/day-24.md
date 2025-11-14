# Day 24: Git Branch Create

## Task Overview

Nautilus developers are actively working on one of the project repositories, `/usr/src/kodekloudrepos/media`. Recently, they decided to implement some new features in the application, and they want to maintain those new changes in a separate branch. Below are the requirements that have been shared with the DevOps team:

- On Storage server in Stratos DC create a new branch `xfusioncorp_media` from master branch in `/usr/src/kodekloudrepos/media` git repo.

- Please do not try to make any changes in the code.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo su
    cd /usr/src/kodekloudrepos/media
```

**Step 2:**
```bash
git branch
```

**Step 3:**
```bash
git switch master
```

**Step 4:**
```bash
git checkout -b xfusioncorp_media
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 23](day-23.md) | [Day 25 →](day-25.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
