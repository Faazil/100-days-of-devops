# Day 10: Create Backup Script with SSH

## Task Overview

The operations team at xFusionCorp Industries is creating shell scripts for automating different day-to-day tasks. One task is to create a bash script to perform website backups. A static site is hosted on App Server 3 within the Stratos DC, requiring development of a bash script named `beta_backup.sh` that must complete these requirements. (Remember to place the script under `/scripts` directory on App Server 3).

**Requirements:**
- Create a zip archive named `xfusioncorp_beta.zip` of `/var/www/html/beta` directory
- Save the archive in `/backup/` on App Server 3 (temporary storage)
- Copy the created archive to Nautilus Backup Server in `/backup/` location
- Script must NOT ask for password when copying the archive file
- The respective server user must be able to run it

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
ssh <your-username>@<app-server-3>
```

**Step 2:**
```bash
ssh-keygen -t rsa
```

**Step 3:**
```bash
Generating public/private rsa key pair.
Enter file in which to save the key (/home/banner/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/banner/.ssh/id_rsa.
Your public key has been saved in /home/banner/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:abc123... banner@stapp03
```

**Step 4:**
```bash
ssh-copy-id <backup-user>@<backup-server>
```

**Step 5:**
```bash
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s)
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed
clint@stbkp01's password: [enter password]

Number of key(s) added: 1

Now try logging into the machine, with: "ssh 'clint@stbkp01'"
and check to make sure that only the key(s) you wanted were added.
```

**Step 6:**
```bash
ssh <backup-user>@<backup-server>
```

**Step 7:**
```bash
sudo mkdir -p /scripts
```

**Step 8:**
```bash
sudo vi /scripts/beta_backup.sh
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 9](day-09.md) | [Day 11 →](day-11.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
