# Day 74: Jenkins Database Backup Job

## Task Overview

Install and configure Jenkins plugins to extend functionality. Plugins add capabilities for build tools, version control, and deployment targets.

**Plugin Management:**
- Access Jenkins plugin manager
- Search and select required plugins
- Install plugins
- Restart Jenkins if needed

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Connect to the target server using SSH.

```sh
mkdir -p /tmp/db-backup
    mysqldump -u kodekloud_roy -p'asdfgdsd' kodekloud_db01 > /tmp/db-backup/db_$(date +%F).sql

    ls -la
    sudo apt install sshpass -y

    sshpass -p 'H@wk3y3' scp -o StrictHostKeyChecking=no /tmp/db-backup/*.sql clint@stbkp01:/home/clint/db_backups

    rm -rf /tmp/db-backup
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 73](day-73.md) | [Day 75 →](day-75.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
