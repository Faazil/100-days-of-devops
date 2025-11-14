# Day 32: Git Rebase

## Task Overview

The Nautilus application development team has been working on a project repository /opt/games.git. This repo is cloned at /usr/src/kodekloudrepos on storage server in Stratos DC. They recently shared the following requirements with DevOps team:

> One of the developers is working on feature branch and their work is still in progress, however there are some changes which have been pushed into the master branch, the developer now wants to rebase the feature branch with the master branch without loosing any data from the feature branch, also they don't want to add any merge commit by simply merging the master branch into the feature branch. Accomplish this task as per requirements mentioned.

- Also remember to push your changes once done.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo -i
    cd /usr/src/kodekloudrepos/games
```

**Step 2:**
```bash
git branch
```

**Step 3:**
```bash
git rebase master
```

**Step 4:**
```bash
git push --force --set-upstream origin feature
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 31](day-31.md) | [Day 33 →](day-33.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
