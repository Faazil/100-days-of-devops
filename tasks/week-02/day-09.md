# Day 9: Debugging MariaDB Issues

## Task Overview

Install and configure MySQL/MariaDB database server. Set up relational database for application data storage.

**Database Setup:**
- Install database server
- Configure service settings
- Secure installation
- Create databases and users

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Connect to the target server using SSH.

```sh
ssh peter@stdb01
```

**Step 2:** Check log files to identify the issue.

```sh
tail -f /var/log/mariadb.log
```

**Step 3:** Check log files to identify the issue.

```bash
[root@stdb01 mariadb]# tail -f mariadb.log 
    2025-08-03  8:54:14 0 [Note] /usr/libexec/mariadbd (initiated by: unknown): Normal shutdown
    2025-08-03  8:54:14 0 [Note] Event Scheduler: Purging the queue. 0 events
    2025-08-03  8:54:14 0 [Note] InnoDB: FTS optimize thread exiting.
    2025-08-03  8:54:14 0 [Note] InnoDB: Starting shutdown...
    2025-08-03  8:54:14 0 [Note] InnoDB: Dumping buffer pool(s) to /var/lib/mysql/ib_buffer_pool
    2025-08-03  8:54:14 0 [Note] InnoDB: Buffer pool(s) dump completed at 250803  8:54:14
    2025-08-03  8:54:14 0 [Note] InnoDB: Removed temporary tablespace data file: "ibtmp1"
    2025-08-03  8:54:14 0 [Note] InnoDB: Shutdown completed; log sequence number 45091; transaction id 21
    2025-08-03  8:54:14 0 [Note] /usr/libexec/mariadbd: Shutdown complete
```

**Step 4:** Check the service status to verify it's running.

```sh
sudo systemctl status mariadb
```

**Step 5:** Check the service status to verify it's running.

```bash
[peter@stdb01 ~]$ systemctl status mariadb
    ○ mariadb.service - MariaDB 10.5 database server
    Loaded: loaded (/usr/lib/systemd/system/mariadb.service; enabled; preset: disabled)
    Active: inactive (dead) since Sun 2025-08-03 08:54:14 UTC; 5min ago
    Duration: 5.819s
    Docs: man:mariadbd(8)
    https://mariadb.com/kb/en/library/systemd/
    ...
    ...
    Status: "MariaDB server is down"
```

**Step 6:** Enable service to start automatically on boot.

```sh
sudo systemctl enable mariadb
    sudo systemctl start mariadb
```

**Step 7:** Connect to database server and verify configuration.

```sh
cat /etc/my.cnf.d/mariadb.service
```

**Step 8:** Restart the service to apply changes.

```sh
systemctl restart mariadb
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 8](day-08.md) | [Day 10 →](day-10.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
