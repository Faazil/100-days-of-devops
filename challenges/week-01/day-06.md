# Challenge 6: Setup a Cron Job

## 📊 Metadata
- **Day**: 6
- **Week**: 1
- **Day in Week**: 6/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Scenario

The Nautilus system admins team has prepared scripts to automate several day-to-day tasks. They want them to be deployed on all app servers in Stratos DC on a set schedule. Before that they need to test similar functionality with a sample cron job. Therefore, perform the steps below:

- Install `cronie` package on all Nautilus app servers and start `crond` service
- Add a cron `*/5 * * * * echo hello > /tmp/cron_text` for `root` user

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `ssh`, `sudo`, `yum`, `systemctl`, `crontab`
- **Key Concepts**:
  - Cron scheduling syntax
  - Service management
  - Automated task scheduling

**Required Skills:**
- ✅ Install packages
- ✅ Manage system services
- ✅ Configure cron jobs
- ✅ Understand cron syntax

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

## 💡 Understanding the Task

**What is Cron?**

Cron is Linux's task scheduler. It runs commands automatically at specified times - perfect for backups, cleanups, monitoring, and other repetitive tasks.

**Cron Schedule Format:**
```
*/5  *  *  *  *  command
 |   |  |  |  |
 |   |  |  |  └─ Day of week (0-7, Sun=0 or 7)
 |   |  |  └──── Month (1-12)
 |   |  └─────── Day of month (1-31)
 |   └────────── Hour (0-23)
 └────────────── Minute (0-59)
```

**Why It Matters:** Automation is at the heart of DevOps. Cron is one of the oldest and most reliable automation tools in Linux.

---

## 📝 Solution

### Step 1: Connect to App Servers

SSH to each app server (repeat for all servers):

```bash
ssh <your-username>@<server-name>
```

💡 **Example:** `ssh tony@stapp01`

---

### Step 2: Install Cronie Package

Install the cron daemon package:

```bash
sudo yum install cronie -y
```

💡 **Example:** `sudo yum install cronie -y`

**What this does:**
- Installs the cron daemon and utilities
- `-y` automatically answers "yes" to prompts

**Expected result:** "Complete!" message after installation.

---

### Step 3: Start and Enable Crond Service

Start the cron service and enable it to start on boot:

```bash
sudo systemctl enable crond
sudo systemctl start crond
```

💡 **Example:** 
```bash
sudo systemctl enable crond
sudo systemctl start crond
```

**What each command does:**
- `enable` - Service starts automatically on boot
- `start` - Start the service now

**Expected result:** Commands complete silently or show "Created symlink..." message.

---

### Step 4: Verify Service is Running

Confirm crond is active:

```bash
sudo systemctl status crond
```

💡 **Example:** `sudo systemctl status crond`

**Expected output:**
```
● crond.service - Command Scheduler
   Loaded: loaded...
   Active: active (running)...
```

Look for "active (running)" in green.

---

### Step 5: Add Cron Job for Root

Edit root's crontab:

```bash
sudo crontab -e
```

💡 **Example:** `sudo crontab -e`

**Add this line:**
```
*/5 * * * * echo hello > /tmp/cron_text
```

**What this means:**
- `*/5` - Every 5 minutes
- `* * * *` - Every hour, day, month, day of week
- `echo hello > /tmp/cron_text` - Write "hello" to file

**Save and exit:**
- Press `i` for insert mode
- Paste or type the cron line
- Press `ESC`
- Type `:wq` and ENTER

---

### Step 6: Verify Cron Job Added

List root's cron jobs:

```bash
sudo crontab -l
```

💡 **Example:** `sudo crontab -l`

**Expected output:**
```
*/5 * * * * echo hello > /tmp/cron_text
```

---

### Step 7: Test the Cron Job

Wait 5 minutes, then check if the file was created:

```bash
cat /tmp/cron_text
```

💡 **Example:** `cat /tmp/cron_text`

**Expected output:**
```
hello
```

---

## ✅ Verification Checklist

Before marking this challenge complete:

- [ ] Cronie package installed on all app servers
- [ ] Crond service running (`systemctl status crond`)
- [ ] Cron job appears in `sudo crontab -l`
- [ ] File `/tmp/cron_text` exists with "hello" after 5 minutes
- [ ] KodeKloud validation passes

---

## 🔧 Troubleshooting

**Package not found:**
- Try `dnf` instead of `yum`
- Check internet connectivity
- Verify repo configuration

**Service won't start:**
- Check logs: `sudo journalctl -u crond`
- Verify installation: `rpm -q cronie`
- Try `sudo systemctl restart crond`

**Cron job not running:**
- Check cron syntax is correct
- Verify crond service is running
- Check system logs: `sudo tail -f /var/log/cron`
- Ensure you used `sudo crontab -e` (for root's crontab)

**File not created:**
- Wait full 5 minutes after adding cron
- Check file permissions on /tmp
- Verify cron job with: `sudo crontab -l`

---

## 💡 Good to Know

**Cron Syntax Examples:**
```bash
# Every minute
* * * * * command

# Every hour
0 * * * * command

# Every day at 2:30 AM
30 2 * * * command

# Every Monday at 9 AM
0 9 * * 1 command

# First day of every month
0 0 1 * * command
```

**Useful Cron Commands:**
```bash
# Edit user's crontab
crontab -e

# List user's cron jobs
crontab -l

# Edit root's crontab
sudo crontab -e

# Remove all cron jobs
crontab -r

# View cron logs
sudo tail -f /var/log/cron
```

**Common Use Cases:**
- Automated backups (daily at 2 AM)
- Log rotation (weekly)
- System health checks (every 5 minutes)
- Database cleanups (monthly)
- Report generation (daily)

---

## 📚 Navigation

- **← Previous**: [Day 5 - Install and Configuration Selinux](./day-05.md)
- **Next →**: [Day 7 - Linux SSH Automation](./day-07.md)

**🔗 Challenge Source**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

*Automate everything - let cron do the work!*
