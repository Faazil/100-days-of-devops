# Day 34: Configure Git Hook

## Task Overview

The Nautilus application development team was working on a git repository /opt/demo.git which is cloned under /usr/src/kodekloudrepos directory present on Storage server in Stratos DC. The team want to setup a hook on this repository, please find below more details:

- Merge the feature branch into the master branch`, but before pushing your changes complete below point.

- Create a post-update hook in this git repository so that whenever any changes are pushed to the master branch, it creates a release tag with name release-2023-06-15, where 2023-06-15 is supposed to be the current date. For example if today is 20th June, 2023 then the release tag must be release-2023-06-20. Ensure you test the hook at least once and create a release tag for today's release.

- Finally remember to push your changes.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo -i
    cd /usr/src/kodekloudrepos/demo
```

**Step 2:**
```bash
git branch
    git switch master
```

**Step 3:**
```bash
git merge feature
```

**Step 4:**
```bash
cp /opt/demo.git/hooks/post-update.sample /opt/demo.git/hooks/post-update
    chmod +x /opt/demo.git/hooks/post-update
```

**Step 5:**
```bash
vi /opt/demo.git/hooks/post-update
```

**Step 6:**
```bash
day=$(date +"%Y-%m-%d")
    TAG="release-$day"

    git tag -a $TAG -m "Released at: $day"
```

**Step 7:**
```bash
git push
```

**Step 8:**
```bash
git fetch --tags
    git tag
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 33](day-33.md) | [Day 35 →](day-35.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
