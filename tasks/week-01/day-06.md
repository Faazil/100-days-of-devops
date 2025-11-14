# Day 6: Setup a Cron Job

## Task Overview

The Nautilus system admins team has prepared scripts to automate several day-to-day tasks. They want them to be deployed on all app servers in Stratos DC on a set schedule. Before that they need to test similar functionality with a sample cron job. Therefore, perform the steps below:

- Install `cronie` package on all Nautilus app servers and start `crond` service
- Add a cron `*/5 * * * * echo hello > /tmp/cron_text` for `root` user

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
*/5  *  *  *  *  command
 |   |  |  |  |
 |   |  |  |  └─ Day of week (0-7, Sun=0 or 7)
 |   |  |  └──── Month (1-12)
 |   |  └─────── Day of month (1-31)
 |   └────────── Hour (0-23)
 └────────────── Minute (0-59)
```

**Step 2:**
```bash
ssh <your-username>@<server-name>
```

**Step 3:**
```bash
sudo yum install cronie -y
```

**Step 4:**
```bash
sudo systemctl enable crond
sudo systemctl start crond
```

**Step 5:**
```bash
sudo systemctl enable crond
sudo systemctl start crond
```

**Step 6:**
```bash
sudo systemctl status crond
```

**Step 7:**
```bash
● crond.service - Command Scheduler
   Loaded: loaded...
   Active: active (running)...
```

**Step 8:**
```bash
sudo crontab -e
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 5](day-05.md) | [Day 7 →](day-07.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
