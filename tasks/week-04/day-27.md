# Day 27: Git Revert Some Changes

## Task Overview

The Nautilus application development team was working on a git repository /usr/src/kodekloudrepos/demo present on Storage server in Stratos DC. However, they reported an issue with the recent commits being pushed to this repo. They have asked the DevOps team to revert repo HEAD to last commit. Below are more details about the task:

- In /usr/src/kodekloudrepos/demo git repository, revert the latest commit ( HEAD ) to the previous commit (JFYI the previous commit hash should be with initial commit message ).
- Use revert demo message (please use all small letters for commit message) for the new revert commit.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo su
    cd /usr/src/kodekloudrepos/demo
```

**Step 2:**
```bash
git log --oneline
```

**Step 3:**
```bash
git revert HEAD -m "revert demo"
```

**Step 4:**
```bash
git push
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 26](day-26.md) | [Day 28 →](day-28.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
