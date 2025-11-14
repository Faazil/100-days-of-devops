# Day 31: Git Stash

## Task Overview

The Nautilus application development team was working on a git repository `/usr/src/kodekloudrepos/ecommerce` present on Storage server in Stratos DC. One of the developers stashed some in-progress changes in this repository, but now they want to restore some of the stashed changes. Find below more details to accomplish this task:

- Look for the stashed changes under `/usr/src/kodekloudrepos/ecommerce` git repository, and restore the stash with stash@{1} identifier. Further, commit and push your changes to the origin.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo -i
    cd /usr/src/kodekloudrepos/ecommerce
```

**Step 2:**
```bash
git stash list
```

**Step 3:**
```bash
[root@ststor01 ecommerce]# git stash list
    stash@{0}: WIP on master: 7fe985d initial commit
    stash@{1}: WIP on master: 7fe985d initial commit
```

**Step 4:**
```bash
git stash apply stash@{1}
```

**Step 5:**
```bash
git add .
    git commit -m "Restored stash files"
    git push
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 30](day-30.md) | [Day 32 →](day-32.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
