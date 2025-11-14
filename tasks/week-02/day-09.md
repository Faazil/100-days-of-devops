# Day 9: Troubleshoot and Fix MariaDB Service

## Task Overview

A critical problem exists with the Nautilus application in Stratos DC. The production support team discovered that the application cannot connect to the database. After investigating, it was determined that the mariadb service has stopped on the database server.

Your task is to troubleshoot and fix the MariaDB service so the application can reconnect to the database.

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
ssh <your-username>@<database-server>
```

**Step 2:**
```bash
sudo systemctl status mariadb
```

**Step 3:**
```bash
○ mariadb.service - MariaDB 10.5 database server
   Loaded: loaded (/usr/lib/systemd/system/mariadb.service; enabled; preset: disabled)
   Active: inactive (dead) since Sun 2025-08-03 08:54:14 UTC; 5min ago
   ...
   Status: "MariaDB server is down"
```

**Step 4:**
```bash
sudo tail -30 /var/log/mariadb/mariadb.log
```

**Step 5:**
```bash
2025-08-03  8:54:14 0 [Note] InnoDB: Starting shutdown...
2025-08-03  8:54:14 0 [Note] InnoDB: Shutdown completed
2025-08-03  8:54:14 0 [Note] /usr/libexec/mariadbd: Shutdown complete
```

**Step 6:**
```bash
sudo systemctl start mariadb
```

**Step 7:**
```bash
sudo systemctl status mariadb -l
```

**Step 8:**
```bash
sudo cat /etc/my.cnf.d/mariadb-server.cnf
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 8](day-08.md) | [Day 10 →](day-10.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
