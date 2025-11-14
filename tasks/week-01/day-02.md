# Day 2: Temporary User Setup with Expiry Date

## Task Overview

As part of the temporary assignment to the Nautilus project, a developer named yousuf requires access for a limited duration. To ensure smooth access management, a temporary user account with an expiry date is needed.

> Create a user named `yousuf` on `App Server 1` in Stratos Datacenter. Set the expiry date to `2024-01-28`, ensuring the user is created in lowercase as per standard protocol.

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
sudo useradd -m -e 2024-01-28 yousuf
```

**Step 3:**
```bash
cat /etc/passwd | grep yousuf
```

**Step 4:**
```bash
yousuf:x:1002:1002::/home/yousuf:/bin/bash
```

**Step 5:**
```bash
sudo chage -l yousuf
```

**Step 6:**
```bash
...
Account expires: Jan 28, 2024
...
```

**Step 7:**
```bash
# View account expiry details
sudo chage -l <username>

# Change expiry date for existing user
sudo usermod -e 2024-12-31 <username>

# Remove expiry (set to never expire)
sudo usermod -e "" <username>
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 1](day-01.md) | [Day 3 →](day-03.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
