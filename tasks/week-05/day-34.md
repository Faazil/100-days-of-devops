# Day 34: Configure Git Hook

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

**Step 1:** Perform the initial setup or connection.

```sh
sudo -i
    cd /usr/src/kodekloudrepos/demo
```

**Step 2:** Create or list Git branches.

```sh
git branch
    git switch master
```

**Step 3:** Merge changes from one branch into another.

```sh
git merge feature
```

**Step 4:** Make the script executable for all users.

```sh
cp /opt/demo.git/hooks/post-update.sample /opt/demo.git/hooks/post-update
    chmod +x /opt/demo.git/hooks/post-update
```

**Step 5:** Execute the command to complete this step.

```sh
vi /opt/demo.git/hooks/post-update
```

**Step 6:** Execute the command to complete this step.

```shell
day=$(date +"%Y-%m-%d")
    TAG="release-$day"

    git tag -a $TAG -m "Released at: $day"
```

**Step 7:** Push local commits to remote repository.

```sh
git push
```

**Step 8:** Execute the command to complete this step.

```sh
git fetch --tags
    git tag
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 33](day-33.md) | [Day 35 →](day-35.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
