# Day 1: Linux User Setup with Non-interactive Shell

## Task Overview

Create a user with non-interactive shell for your organization on a specific server. This is essential for service accounts and automated processes that don't require interactive login capabilities.

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
ssh <your-username>@<server-name>
```

**Step 2:**
```bash
sudo useradd -m -s /usr/sbin/nologin <username>
```

**Step 3:**
```bash
cat /etc/passwd | grep <username>
```

**Step 4:**
```bash
kareem:x:1003:1004::/home/kareem:/usr/sbin/nologin
```

**Step 5:**
```bash
sudo su - <username>
```

**Step 6:**
```bash
This account is currently not available.
```

**Step 7:**
```bash
# View user ID and groups
id <username>

# List all users with nologin shell
grep nologin /etc/passwd

# View home directory permissions
ls -ld /home/<username>
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[Day 2 →](day-02.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
