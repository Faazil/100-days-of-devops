# Challenge 10: Create Backup Script with SSH

## 📊 Metadata
- **Day**: 10
- **Week**: 2
- **Day in Week**: 3/7
- **Category**: Linux
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 30-40 minutes

---

## 🎯 Challenge Scenario

The production support team of xFusionCorp Industries is working on developing bash scripts to automate different day-to-day tasks. One task is to create a bash script for taking website backups. They have a static website running on App Server 3 in Stratos Datacenter, and they need to create a bash script named `beta_backup.sh` which should accomplish the following tasks. (Remember to place the script under `/scripts` directory on App Server 3).

**Requirements:**
- Create a zip archive named `xfusioncorp_beta.zip` of `/var/www/html/beta` directory
- Save the archive in `/backup/` on App Server 3 (temporary storage)
- Copy the created archive to Nautilus Backup Server in `/backup/` location
- Script must NOT ask for password when copying the archive file
- The respective server user must be able to run it

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ App Server 3 and Backup Server
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `ssh`, `ssh-keygen`, `ssh-copy-id`, `zip`, `scp`
- **Key Concepts**:
  - Bash scripting basics
  - SSH key-based authentication
  - File archiving with zip
  - Secure copy (scp) over SSH
  - Script permissions

**Foundation from Earlier Challenges:**
- Day 4: Script Execute Permissions (recommended)
- Day 7: SSH Automation (strongly recommended - uses SSH keys)

**Required Skills:**
- ✅ Write bash scripts
- ✅ Set up SSH keys for passwordless authentication
- ✅ Create compressed archives
- ✅ Copy files securely between servers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

## 💡 Understanding the Task

**Why Automate Backups?**

Manual backups are:
- Time-consuming
- Error-prone (easy to forget)
- Inconsistent
- Not scalable

Automated backup scripts ensure:
- Regular, consistent backups
- Reduced human error
- Easy integration with cron jobs
- Repeatable, reliable process

**Why Passwordless SSH?**

For automation, scripts need to run without human intervention. SSH keys provide:
- Secure authentication without passwords
- No password storage in scripts (security risk)
- Ability to automate safely
- Better access control

**Backup Strategy:**

This challenge implements a simple backup strategy:
1. **Local backup** - Archive on the source server (`/backup/`)
2. **Remote backup** - Copy to dedicated backup server
3. **Compression** - Zip reduces storage space

---

## 📝 Solution

### Step 1: Connect to App Server 3

SSH into App Server 3 where the website lives:

```bash
ssh <your-username>@<app-server-3>
```

💡 **Example:** `ssh banner@stapp03`

---

### Step 2: Generate SSH Key Pair

Generate an SSH key for passwordless authentication:

```bash
ssh-keygen -t rsa
```

💡 **Example:** `ssh-keygen -t rsa`

**When prompted:**
- **Enter file to save the key**: Press Enter (accept default `~/.ssh/id_rsa`)
- **Enter passphrase**: Press Enter (no passphrase for automation)
- **Enter same passphrase again**: Press Enter

**Expected output:**
```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/banner/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/banner/.ssh/id_rsa.
Your public key has been saved in /home/banner/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:abc123... banner@stapp03
```

**What this does:**
- Creates two files: `id_rsa` (private key) and `id_rsa.pub` (public key)
- Private key stays on App Server 3
- Public key will be copied to Backup Server

---

### Step 3: Copy Public Key to Backup Server

Copy your public key to the backup server to enable passwordless login:

```bash
ssh-copy-id <backup-user>@<backup-server>
```

💡 **Example:** `ssh-copy-id clint@stbkp01`

**You'll be asked for the backup server user's password (one time only):**
```
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s)
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed
clint@stbkp01's password: [enter password]

Number of key(s) added: 1

Now try logging into the machine, with: "ssh 'clint@stbkp01'"
and check to make sure that only the key(s) you wanted were added.
```

---

### Step 4: Test Passwordless SSH

Verify you can SSH without a password:

```bash
ssh <backup-user>@<backup-server>
```

💡 **Example:** `ssh clint@stbkp01`

You should connect immediately without a password prompt. Type `exit` to return to App Server 3.

---

### Step 5: Create the Scripts Directory

Create the directory where the script will live:

```bash
sudo mkdir -p /scripts
```

💡 **Example:** `sudo mkdir -p /scripts`

The `-p` flag creates parent directories if needed and doesn't error if it already exists.

---

### Step 6: Create the Backup Script

Create and edit the backup script:

```bash
sudo vi /scripts/beta_backup.sh
```

💡 **Example:** `sudo vi /scripts/beta_backup.sh`

**Write the following script content:**

```bash
#!/bin/bash

# Website Backup Script
# Archives website files and copies to backup server

# Create zip archive of the website directory
zip -r /backup/xfusioncorp_beta.zip /var/www/html/beta

# Copy archive to backup server (passwordless SSH required)
scp /backup/xfusioncorp_beta.zip clint@stbkp01:/backup/
```

**Save and exit:** Press `ESC`, then type `:wq` and press `Enter`

**What this script does:**
- Line 1: `#!/bin/bash` - Shebang tells system to use bash
- Line 5: `zip -r` - Creates recursive zip archive
  - `-r` = recursive (include all files and subdirectories)
  - First path = where to save the zip file
  - Second path = what to back up
- Line 8: `scp` - Secure copy over SSH
  - Copies the archive to the backup server
  - Uses SSH keys (no password prompt)

---

### Step 7: Make Script Executable

Give the script execute permissions:

```bash
sudo chmod +x /scripts/beta_backup.sh
```

💡 **Example:** `sudo chmod +x /scripts/beta_backup.sh`

**Verify permissions:**
```bash
ls -l /scripts/beta_backup.sh
```

**Expected output:**
```
-rwxr-xr-x 1 root root 245 Aug 10 10:30 /scripts/beta_backup.sh
```

The `x` in `-rwxr-xr-x` means it's executable.

---

### Step 8: Test the Backup Script

Run the script to ensure it works:

```bash
sudo /scripts/beta_backup.sh
```

💡 **Example:** `sudo /scripts/beta_backup.sh`

**Expected output:**
```
  adding: var/www/html/beta/ (stored 0%)
  adding: var/www/html/beta/index.html (deflated 45%)
  adding: var/www/html/beta/style.css (deflated 58%)
xfusioncorp_beta.zip                    100%   15KB   1.5MB/s   00:00
```

The script zips the files and copies to the backup server.

---

### Step 9: Verify Backup on App Server

Check that the backup exists locally:

```bash
ls -lh /backup/xfusioncorp_beta.zip
```

💡 **Example:** `ls -lh /backup/xfusioncorp_beta.zip`

**Expected output:**
```
-rw-r--r-- 1 root root 15K Aug 10 10:35 /backup/xfusioncorp_beta.zip
```

---

### Step 10: Verify Backup on Backup Server

Log into the backup server and check the file arrived:

```bash
ssh clint@stbkp01
ls -lh /backup/xfusioncorp_beta.zip
exit
```

💡 **Example:**
```bash
ssh clint@stbkp01
ls -lh /backup/xfusioncorp_beta.zip
```

**Expected output:**
```
-rw-r--r-- 1 clint clint 15K Aug 10 10:35 /backup/xfusioncorp_beta.zip
```

The backup file is now on both servers!

---

## ✅ Verification Checklist

Before marking this challenge complete, verify:

- [ ] SSH key generated on App Server 3 (`ls ~/.ssh/id_rsa`)
- [ ] Public key copied to Backup Server (passwordless SSH works)
- [ ] Script created at `/scripts/beta_backup.sh`
- [ ] Script has execute permissions (`ls -l /scripts/beta_backup.sh` shows `x`)
- [ ] Script runs without errors (`sudo /scripts/beta_backup.sh`)
- [ ] Backup exists on App Server 3 (`ls /backup/xfusioncorp_beta.zip`)
- [ ] Backup copied to Backup Server (`ssh clint@stbkp01 'ls /backup/xfusioncorp_beta.zip'`)
- [ ] No password prompts during script execution
- [ ] KodeKloud validation passes

---

## 🔧 Troubleshooting

**"Permission denied" when creating script:**
- Use `sudo` when creating files in `/scripts/`
- Check directory exists: `ls -ld /scripts`

**SSH still asking for password:**
- Verify key was copied: `ssh clint@stbkp01 'cat ~/.ssh/authorized_keys'`
- Check private key permissions: `ls -l ~/.ssh/id_rsa` (should be 600)
- Fix permissions if needed: `chmod 600 ~/.ssh/id_rsa`

**"zip: command not found":**
- Install zip: `sudo yum install zip -y` (RHEL/CentOS) or `sudo apt install zip -y` (Ubuntu)

**"No such file or directory" for /var/www/html/beta:**
- Verify the directory exists: `ls -la /var/www/html/beta`
- Check the challenge description for the exact path (it may vary)

**SCP fails with "lost connection":**
- Test SSH connection first: `ssh clint@stbkp01`
- Ensure backup directory exists on remote: `ssh clint@stbkp01 'mkdir -p /backup'`
- Check for network/firewall issues

**Script doesn't run:**
- Verify shebang is on first line: `head -1 /scripts/beta_backup.sh`
- Check execute permission: `sudo chmod +x /scripts/beta_backup.sh`
- Run with full path: `sudo /scripts/beta_backup.sh`

---

## 💡 Good to Know

**Enhancing the Backup Script:**

```bash
#!/bin/bash

# Enhanced backup script with error checking and logging

LOG_FILE="/var/log/backup.log"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="/backup/xfusioncorp_beta_${TIMESTAMP}.zip"

# Log function
log() {
    echo "[$(date +%Y-%m-%d\ %H:%M:%S)] $1" | tee -a "$LOG_FILE"
}

log "Starting backup process..."

# Create backup
if zip -r "$BACKUP_FILE" /var/www/html/beta; then
    log "Successfully created archive: $BACKUP_FILE"
else
    log "ERROR: Failed to create archive"
    exit 1
fi

# Copy to backup server
if scp "$BACKUP_FILE" clint@stbkp01:/backup/; then
    log "Successfully copied to backup server"
else
    log "ERROR: Failed to copy to backup server"
    exit 1
fi

log "Backup completed successfully"
```

**Improvements:**
- Timestamped backups (don't overwrite previous ones)
- Error checking (exit if something fails)
- Logging for troubleshooting
- Better visibility into what's happening

**Scheduling with Cron:**

To run this backup daily at 2 AM:

```bash
# Edit crontab
sudo crontab -e

# Add this line:
0 2 * * * /scripts/beta_backup.sh
```

**Alternative Backup Tools:**

```bash
# tar (tape archive) - common on Linux
tar -czf backup.tar.gz /var/www/html/beta

# rsync - efficient, only copies changes
rsync -avz /var/www/html/beta/ clint@stbkp01:/backup/beta/

# duplicity - encrypted backups
duplicity /var/www/html/beta sftp://clint@stbkp01/backup/
```

**SSH Key Security:**

```bash
# Use ed25519 keys (more secure, faster)
ssh-keygen -t ed25519 -C "backup-script@stapp03"

# Or use RSA with longer key
ssh-keygen -t rsa -b 4096

# Restrict what the key can do on backup server
# Add to ~/.ssh/authorized_keys on backup server:
command="/usr/bin/rsync --server",no-port-forwarding,no-X11-forwarding ssh-rsa AAAAB3...
```

**Real-World Backup Strategies:**

Production environments typically use:
- **3-2-1 Rule**: 3 copies, 2 different media types, 1 off-site
- **Versioning**: Keep multiple backup versions
- **Retention policies**: How long to keep backups
- **Testing**: Regularly test restoring from backups
- **Monitoring**: Alert if backups fail
- **Encryption**: Protect sensitive data
- **Automation**: Scheduled, hands-off backups

---

## 📚 Navigation

- **← Previous**: [Day 9 - Troubleshoot and Fix MariaDB Service](./day-09.md)
- **Next →**: [Day 11 - Install and Setup Tomcat Server](./day-11.md)

**🔗 Challenge Source**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

*Automated backups - protecting data the DevOps way!*
