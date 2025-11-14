# Challenge 9: Debugging MariaDB Issues

## 📊 Metadata
- **Day**: 9
- **Week**: 2
- **Day in Week**: 2/7
- **Category**: Database
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

There is a critical issue going on with the Nautilus application in Stratos DC. The production support team identified that the application is unable to connect to the database. After digging into the issue, the team found that mariadb service is down on the database server.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `mysql`, `mariadb`, `psql`
- **Key Concepts**:
  - Database server installation
  - User and privilege management
  - Database creation and schema
  - SQL query fundamentals

**Required Skills:**
- ✅ Install database servers
- ✅ Create databases and users
- ✅ Grant and manage privileges
- ✅ Execute SQL commands

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

We have to consider few things:

- files permission
- socket file
- data directory
- config issue

1. Login into Database Server:

    ```sh
    ssh peter@stdb01
    ```

2. look at the mariadb logs:

    ```sh
    tail -f /var/log/mariadb.log
    ```

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

3. lets see the mariadb service status

    ```sh
    sudo systemctl status mariadb
    ```

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

4. Lets up the mariadb service:

    ```sh
    sudo systemctl enable mariadb
    sudo systemctl start mariadb
    ```

5. Still failed to run, lets looking into config:

    ```sh
    cat /etc/my.cnf.d/mariadb.service
    ```

    datadir: `/var/lib/mysql/`

    actual location: `/var/lib/mysqld`

    so update config and `ib_buffer_pool`

6. Restart

    ```sh
    systemctl restart mariadb
    ```

## Good to Know?

### MariaDB Troubleshooting

- **Log Files**: `/var/log/mariadb/mariadb.log`, `/var/log/mysqld.log`
- **Configuration**: `/etc/my.cnf`, `/etc/my.cnf.d/`
- **Data Directory**: Usually `/var/lib/mysql/`
- **Socket File**: `/var/lib/mysql/mysql.sock`

### Common Issues

- **Permission Problems**: Check ownership of data directory
- **Configuration Errors**: Validate syntax in config files
- **Disk Space**: Ensure adequate space for data and logs
- **Port Conflicts**: Default port 3306 might be in use

### Diagnostic Commands

- `systemctl status mariadb`: Service status
- `journalctl -u mariadb`: Systemd logs
- `mysqladmin ping`: Test connectivity
- `mysql -u root -p`: Connect to database

### File Permissions

- **Data Directory**: `mysql:mysql` ownership, `755` permissions
- **Config Files**: `root:root` ownership, `644` permissions
- **Socket File**: `mysql:mysql` ownership
- **Log Files**: `mysql:mysql` ownership, writable

---

## ✅ Verification

After completing the challenge, verify your solution by:

1. **Testing the implementation**
   - Run all commands from the solution
   - Check for any error messages

2. **Validating the results**
   - Ensure all requirements are met
   - Test edge cases if applicable

3. **Clean up (if needed)**
   - Remove temporary files
   - Reset any test configurations

---

## 📚 Learning Notes

### Key Concepts

This challenge covers the following concepts:
- Practical application of Database skills
- Real-world DevOps scenarios
- Best practices for production environments

### Common Pitfalls

- ⚠️ **Permissions**: Ensure you have the necessary permissions to execute commands
- ⚠️ **Syntax**: Double-check command syntax and flags
- ⚠️ **Environment**: Verify you're working in the correct environment/server

### Best Practices

- ✅ Always verify changes before marking as complete
- ✅ Test your solution in a safe environment first
- ✅ Document any deviations from the standard approach
- ✅ Keep security in mind for all configurations

---

## 🔗 Related Challenges

- **← Previous**: [Day 8 - Setup Ansible](./day-08.md)
- **Next →**: [Day 10 - Create a BASH Script](../week-02/day-10.md)

### Similar Challenges (Database)
- [Day 17 - Install and Configure PostgreSQL](../week-03/day-17.md)

---

## 📖 Additional Resources

- [KodeKloud Official Documentation](https://kodekloud.com)
- [Official Technology Documentation](#)
- [Community Discussions](#)

---

## 🎓 Knowledge Check

After completing this challenge, you should be able to:
- [ ] Understand the problem statement clearly
- [ ] Implement the solution independently
- [ ] Verify the solution works correctly
- [ ] Explain the concepts to others
- [ ] Apply these skills to similar problems

---

**Challenge Source**: KodeKloud 100 Days of DevOps
**Difficulty**: {get_difficulty_emoji(day)}
**Category**: {task_info['category']}

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
python3 ../../tools/progress.py --complete {day}
```

