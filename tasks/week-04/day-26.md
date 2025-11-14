# Day 26: Git Manage Remotes

## Task Overview

The xFusionCorp development team added updates to the project that is maintained under /opt/beta.git repo and cloned under /usr/src/kodekloudrepos/beta. Recently some changes were made on Git server that is hosted on Storage server in Stratos DC. The DevOps team added some new Git remotes, so we need to update remote on /usr/src/kodekloudrepos/beta repository as per details mentioned below:

- In `/usr/src/kodekloudrepos/beta` repo add a new remote `dev_beta` and point it to `/opt/xfusioncorp_beta.git` repository.
- There is a file `/tmp/index.html` on same server; copy this file to the repo and `add/commit` to `master branch`.
- Finally `push master branch` to this new `remote origin`.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo su
    cd /usr/src/kodekloudrepos/beta
```

**Step 2:**
```bash
git remote -v
    git branch
```

**Step 3:**
```bash
git remote add dev_beta /opt/xfusioncorp_beta.git
    git remote -v
```

**Step 4:**
```bash
cp /tmp/index.html .
    git add .
    git commit -m "added tmp file"
```

**Step 5:**
```bash
git push dev_beta master
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 25](day-25.md) | [Day 27 →](day-27.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
