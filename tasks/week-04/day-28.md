# Day 28: Git Cherry Pick

## Task Overview

The Nautilus application development team has been working on a project repository /opt/official.git. This repo is cloned at /usr/src/kodekloudrepos on storage server in Stratos DC. They recently shared the following requirements with the DevOps team:

> There are two branches in this repository, master and feature. One of the developers is working on the feature branch and their work is still in progress, however they want to merge one of the commits from the feature branch to the master branch, the message for the commit that needs to be merged into master is Update info.txt. Accomplish this task for them, also remember to push your changes eventually.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo su
    cd /usr/src/kodekloudrepos/official
```

**Step 2:**
```bash
git branch
```

**Step 3:**
```bash
git log
```

**Step 4:**
```bash
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
