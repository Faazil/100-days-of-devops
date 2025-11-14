# Challenge 9: Troubleshoot and Fix MariaDB Service

## 📊 Metadata
- **Day**: 9
- **Week**: 2
- **Day in Week**: 2/7
- **Category**: Database
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 30-40 minutes

---

## 🎯 Challenge Scenario

There is a critical issue with the Nautilus application in Stratos DC. The production support team identified that the application cannot connect to the database. After investigating, the team found that the mariadb service is down on the database server.

Your task is to troubleshoot and fix the MariaDB service so the application can reconnect to the database.

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Database server with MariaDB installed
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `systemctl`, `tail`, `grep`, `cat`
- **Key Concepts**:
  - Systemd service management
  - Log file analysis
  - MariaDB configuration files
  - Linux file permissions
  - Debugging methodology

**Required Skills:**
- ✅ Analyze service logs
- ✅ Identify configuration issues
- ✅ Restart system services
- ✅ Verify service status

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

## 💡 Understanding the Task

**Why Do Database Services Fail?**

Database services can fail for many reasons:
- **Configuration errors** - Wrong paths, typos in config files
- **Permission issues** - Database can't read/write files
- **Disk space** - No room for data or logs
- **Port conflicts** - Another service using the database port
- **Corrupt data files** - Data directory issues

**The Debugging Process:**

Good troubleshooting follows a pattern:
1. **Check service status** - Is it running or stopped?
2. **Read the logs** - What error messages appear?
3. **Examine configuration** - Are settings correct?
4. **Fix the problem** - Address the root cause
5. **Verify the fix** - Ensure service starts successfully

This is the same process professionals use in production environments.

---

## 📝 Solution

### Step 1: Connect to Database Server

SSH into the database server:

```bash
ssh <your-username>@<database-server>
```

💡 **Example:** `ssh peter@stdb01`

---

### Step 2: Check Service Status

First, let's see if MariaDB is running:

```bash
sudo systemctl status mariadb
```

💡 **Example:** `sudo systemctl status mariadb`

**Expected output (service is down):**
```
○ mariadb.service - MariaDB 10.5 database server
   Loaded: loaded (/usr/lib/systemd/system/mariadb.service; enabled; preset: disabled)
   Active: inactive (dead) since Sun 2025-08-03 08:54:14 UTC; 5min ago
   ...
   Status: "MariaDB server is down"
```

The key line is `Active: inactive (dead)` - the service is stopped.

---

### Step 3: Examine the Logs

Check the MariaDB error log to find out WHY it stopped:

```bash
sudo tail -30 /var/log/mariadb/mariadb.log
```

💡 **Example:** `sudo tail -30 /var/log/mariadb/mariadb.log`

**What to look for in logs:**
- Error messages (lines with "ERROR" or "FATAL")
- Permission denied messages
- "Can't find file" or "File not found" errors
- Any mention of configuration issues

**Common log output:**
```
2025-08-03  8:54:14 0 [Note] InnoDB: Starting shutdown...
2025-08-03  8:54:14 0 [Note] InnoDB: Shutdown completed
2025-08-03  8:54:14 0 [Note] /usr/libexec/mariadbd: Shutdown complete
```

---

### Step 4: Try to Start the Service

Attempt to start MariaDB and see what happens:

```bash
sudo systemctl start mariadb
```

💡 **Example:** `sudo systemctl start mariadb`

If it fails, check the status again:

```bash
sudo systemctl status mariadb -l
```

The `-l` flag shows full error messages without truncation.

---

### Step 5: Check the Configuration

Examine the MariaDB configuration file:

```bash
sudo cat /etc/my.cnf.d/mariadb-server.cnf
```

💡 **Example:** `sudo cat /etc/my.cnf.d/mariadb-server.cnf`

**Look for these key settings:**
```
[mysqld]
datadir=/var/lib/mysql/     # Where database files are stored
socket=/var/lib/mysql/mysql.sock
...
```

**Common problem:** The `datadir` in the config doesn't match the actual location of database files.

---

### Step 6: Find the Actual Data Directory

Check where the MariaDB data files actually are:

```bash
sudo ls -la /var/lib/ | grep mysql
```

💡 **Example:** `sudo ls -la /var/lib/ | grep mysql`

**Possible output:**
```
drwxr-xr-x.  6 mysql mysql  4096 Aug  3 08:54 mysql
drwxr-xr-x.  6 mysql mysql  4096 Aug  3 08:54 mysqld
```

If you see `mysqld` but your config says `mysql`, that's the problem!

---

### Step 7: Fix the Configuration

Update the config file to point to the correct directory.

**Option A: Using sed (quick fix):**

```bash
sudo sed -i 's|datadir=/var/lib/mysql|datadir=/var/lib/mysqld|g' /etc/my.cnf.d/mariadb-server.cnf
```

💡 **Example:** `sudo sed -i 's|datadir=/var/lib/mysql|datadir=/var/lib/mysqld|g' /etc/my.cnf.d/mariadb-server.cnf`

**What this does:**
- `sed -i` - Edit file in-place
- `s|old|new|g` - Substitute old path with new path
- Uses `|` as delimiter (cleaner for paths with `/`)

**Option B: Manual editing:**

```bash
sudo vi /etc/my.cnf.d/mariadb-server.cnf
```

Find the line with `datadir` and change it:
```
# Before:
datadir=/var/lib/mysql/

# After:
datadir=/var/lib/mysqld/
```

---

### Step 8: Fix Socket File Reference

If there's a socket file issue, check for the file:

```bash
sudo ls -la /var/lib/mysqld/mysql.sock
```

The socket file might need to be referenced correctly in the config, or it will be created when the service starts successfully.

---

### Step 9: Enable and Start the Service

Now enable MariaDB to start on boot and start it:

```bash
sudo systemctl enable mariadb
sudo systemctl start mariadb
```

💡 **Example:** `sudo systemctl enable mariadb && sudo systemctl start mariadb`

**Expected output:**
```
Created symlink /etc/systemd/system/multi-user.target.wants/mariadb.service → /usr/lib/systemd/system/mariadb.service.
```

---

### Step 10: Verify the Service is Running

Check that MariaDB is now running properly:

```bash
sudo systemctl status mariadb
```

💡 **Example:** `sudo systemctl status mariadb`

**Expected output (success):**
```
● mariadb.service - MariaDB 10.5 database server
   Loaded: loaded (/usr/lib/systemd/system/mariadb.service; enabled; preset: disabled)
   Active: active (running) since Sun 2025-08-03 09:15:22 UTC; 5s ago
   ...
   Main PID: 1234 (mariadbd)
   Status: "Taking your SQL requests now..."
```

The key line is `Active: active (running)` - success!

---

## ✅ Verification Checklist

Before marking this challenge complete, verify:

- [ ] MariaDB service is running (`systemctl status mariadb` shows "active (running)")
- [ ] Service is enabled to start on boot (`systemctl is-enabled mariadb` shows "enabled")
- [ ] No error messages in logs (`sudo tail -20 /var/log/mariadb/mariadb.log`)
- [ ] Can connect to database (`sudo mysql -e "SELECT 1;"`)
- [ ] KodeKloud validation passes

---

## 🔧 Troubleshooting

**Service still won't start:**
- Read the full log file: `sudo less /var/log/mariadb/mariadb.log`
- Check journalctl: `sudo journalctl -u mariadb -n 50`
- Look for "Permission denied" errors indicating file ownership issues

**Permission errors:**
- Ensure data directory is owned by mysql: `sudo ls -ld /var/lib/mysqld`
- Should show: `drwxr-xr-x. mysql mysql`
- If not, fix ownership: `sudo chown -R mysql:mysql /var/lib/mysqld`

**Socket file not found:**
- Check socket path in config: `grep socket /etc/my.cnf.d/mariadb-server.cnf`
- Socket is created when service starts (it's OK if it doesn't exist before starting)
- Ensure the directory for socket exists and is writable by mysql user

**"Can't connect to local MySQL server":**
- Service might be starting but not fully ready
- Wait 10 seconds and try again: `sleep 10 && sudo systemctl status mariadb`
- Check if firewall is blocking: `sudo systemctl status firewalld`

**Disk space issues:**
- Check available space: `df -h /var/lib/mysqld`
- Database needs space to operate
- If full, you'll need to free up space before starting

---

## 💡 Good to Know

**MariaDB Configuration Files:**

MariaDB reads configuration from multiple locations in this order:
1. `/etc/my.cnf` - Main system-wide config
2. `/etc/my.cnf.d/*.cnf` - Additional config files
3. `~/.my.cnf` - User-specific config (if exists)

Settings in later files override earlier ones.

**Important MariaDB Directories:**

```bash
# Data directory (where databases are stored)
/var/lib/mysql/   # or /var/lib/mysqld/ (depends on setup)

# Log files
/var/log/mariadb/mariadb.log   # Error log
/var/lib/mysql/*.log            # Additional logs

# Configuration
/etc/my.cnf.d/                  # Config files
/etc/my.cnf                     # Main config

# Socket file (for local connections)
/var/lib/mysql/mysql.sock
/var/run/mysqld/mysqld.sock    # Alternative location
```

**Checking Database Connectivity:**

```bash
# Test as root user
sudo mysql -e "SELECT VERSION();"

# Test with password
mysql -u username -p -e "SHOW DATABASES;"

# Test socket connection
mysql -u root -S /var/lib/mysql/mysql.sock

# Check process is running
ps aux | grep mariadb
```

**Reading Logs Effectively:**

```bash
# Last 50 lines
sudo tail -50 /var/log/mariadb/mariadb.log

# Follow log in real-time
sudo tail -f /var/log/mariadb/mariadb.log

# Search for errors
sudo grep -i error /var/log/mariadb/mariadb.log

# View with systemd journal
sudo journalctl -u mariadb --no-pager
```

**Real-World Application:**

Database troubleshooting is a critical skill. In production:
- Always check logs first before making changes
- Document what you find and what you change
- Test database connectivity after fixes
- Monitor database performance after resolving issues
- Set up alerts to catch database failures early

---

## 📚 Navigation

- **← Previous**: [Day 8 - Install Ansible with pip3](./day-08.md)
- **Next →**: [Day 10 - Create Backup Script](./day-10.md)

**🔗 Challenge Source**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

*Database debugging - a critical production skill!*
