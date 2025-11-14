# Day 7: Linux SSH Automation

## Task Overview

The system admins team of xFusionCorp Industries has set up some scripts on jump host that run on regular intervals and perform operations on all app servers in Stratos Datacenter. To make these scripts work properly we need to make sure the thor user on jump host has password-less SSH access to all app servers through their respective sudo users (i.e tony for app server 1).

Set up a password-less authentication from user thor on jump host to all app servers through their respective sudo users.

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
ssh-keygen -t rsa -b 2048
```

**Step 2:**
```bash
Your identification has been saved in /home/thor/.ssh/id_rsa
Your public key has been saved in /home/thor/.ssh/id_rsa.pub
```

**Step 3:**
```bash
ssh-copy-id <username>@<server-name>
```

**Step 4:**
```bash
ssh-copy-id tony@stapp01
ssh-copy-id steve@stapp02
ssh-copy-id banner@stapp03
```

**Step 5:**
```bash
Number of key(s) added: 1
```

**Step 6:**
```bash
ssh <username>@<server-name>
```

**Step 7:**
```bash
# 1. View your public key
cat ~/.ssh/id_rsa.pub

# 2. SSH to remote server (with password)
ssh user@server

# 3. Create .ssh directory if needed
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# 4. Add public key to authorized_keys
nano ~/.ssh/authorized_keys
# Paste your public key
chmod 600 ~/.ssh/authorized_keys

# 5. Exit and test
exit
ssh user@server  # Should work without password
```

**Step 8:**
```bash
# RSA (traditional, widely supported)
ssh-keygen -t rsa -b 4096

# Ed25519 (modern, faster, smaller)
ssh-keygen -t ed25519

# ECDSA (another option)
ssh-keygen -t ecdsa -b 521
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 6](day-06.md) | [Day 8 →](../week-02/day-08.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
