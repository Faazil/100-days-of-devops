# Day 25: Git Branch Merge

## Task Overview

The Nautilus application development team has been working on a project repository /opt/demo.git. This repo is cloned at /usr/src/kodekloudrepos on storage server in Stratos DC. They recently shared the following requirements with DevOps team:

> Create a new branch nautilus in /usr/src/kodekloudrepos/demo repo from master and copy the /tmp/index.html file (present on storage server itself) into the repo. Further, add/commit this file in the new branch and merge back that branch into master branch. Finally, push the changes to the origin for both of the branches.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
ssh user@storage-server
```

**Step 2:**
```bash
sudo su
    cd /usr/src/kodekloudrepos/demo
```

**Step 3:**
```bash
# ensure current branch is master branch
    git branch
    # create a new branch
    git checkout -b nautilus
```

**Step 4:**
```bash
cp /tmp/index.html .
```

**Step 5:**
```bash
git add .
    git commit -m "added tmp file"
```

**Step 6:**
```bash
git switch master
```

**Step 7:**
```bash
git merge nautilus
    git push
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 24](day-24.md) | [Day 26 →](day-26.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
