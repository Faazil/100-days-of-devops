# Day 2: Temporary User Setup with Expiry Date

## Task Overview

Establish a time-limited user account with automatic expiration. This approach supports temporary project assignments by ensuring accounts become inactive after a specified date without manual intervention.

**Account Requirements:**
- Username: specific user (as per task)
- Expiration date: set to future date (YYYY-MM-DD format)
- Home directory: standard creation
- Automatic deactivation: triggered on expiry date

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Create user account with expiration date set.

```sh
sudo useradd -m -e 2024-01-28 yousuf
```

**Step 2:** Verify the user was created and check its configuration.

```sh
cat /etc/passwd
    sudo su yousuf
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 1](day-01.md) | [Day 3 →](day-03.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
