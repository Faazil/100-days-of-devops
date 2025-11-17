# Day 10: Create a BASH Script

## Task Overview

Develop automation scripts for system administration tasks. Create bash scripts to streamline repetitive operations.

**Script Development:**
- Write bash script
- Implement required logic
- Set executable permissions
- Test script functionality

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Copy file to remote server using secure copy.

```sh
#!/bin/sh

    zip -r /backup/xfusioncorp_beta.zip /var/www/html/beta
    scp /backup/xfusioncorp_beta.zip clint@stbkp01:/backup/
```

**Step 2:** Make the script executable for all users.

```sh
chmod +x /scripts/beta_backup.sh
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 9](day-09.md) | [Day 11 →](day-11.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
