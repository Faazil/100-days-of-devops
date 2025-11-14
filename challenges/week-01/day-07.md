# Challenge 7: Linux SSH Automation

## 📊 Metadata
- **Day**: 7
- **Week**: 1
- **Day in Week**: 7/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Scenario

The system admins team of xFusionCorp Industries has set up some scripts on jump host that run on regular intervals and perform operations on all app servers in Stratos Datacenter. To make these scripts work properly we need to make sure the thor user on jump host has password-less SSH access to all app servers through their respective sudo users (i.e tony for app server 1).

Set up a password-less authentication from user thor on jump host to all app servers through their respective sudo users.

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
- **Command Line Tools**: `ssh-keygen`, `ssh-copy-id`, `ssh`
- **Key Concepts**:
  - SSH key-based authentication
  - Public/private key pairs
  - Authorized keys

**Required Skills:**
- ✅ Generate SSH keys
- ✅ Copy keys to remote servers
- ✅ Test password-less authentication

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

## 💡 Understanding the Task

**What is Password-less SSH?**

Instead of typing a password every time you SSH to a server, you use cryptographic keys. The server recognizes your key and lets you in automatically.

**How It Works:**
1. Generate a key pair (public + private)
2. Copy public key to remote server
3. Server recognizes your private key
4. Auto-login without password

**Why It Matters:**
- Essential for automation (scripts can't type passwords)
- More secure than passwords (no brute-force attacks)
- Required for CI/CD pipelines
- Standard practice in DevOps

---

## 📝 Solution

### Step 1: Generate SSH Key Pair

On the jump host, generate an SSH key:

```bash
ssh-keygen -t rsa -b 2048
```

💡 **Example:** `ssh-keygen -t rsa -b 2048`

**What this does:**
- `-t rsa` - Use RSA algorithm
- `-b 2048` - 2048-bit key (good security)

**During generation:**
- Press ENTER to accept default location (`~/.ssh/id_rsa`)
- Press ENTER for no passphrase (required for automation)
- Press ENTER again to confirm

**Expected result:**
```
Your identification has been saved in /home/thor/.ssh/id_rsa
Your public key has been saved in /home/thor/.ssh/id_rsa.pub
```

---

### Step 2: Copy Public Key to App Servers

Use `ssh-copy-id` to copy your public key to each app server:

```bash
ssh-copy-id <username>@<server-name>
```

💡 **Examples:**
```bash
ssh-copy-id tony@stapp01
ssh-copy-id steve@stapp02
ssh-copy-id banner@stapp03
```

**What this does:**
- Automatically copies your public key
- Adds it to `~/.ssh/authorized_keys` on the remote server
- Sets correct permissions

**During copy:**
- Type "yes" to accept server fingerprint
- Enter the user's password when prompted

**Expected result:**
```
Number of key(s) added: 1
```

**Repeat for all app servers** in your environment.

---

### Step 3: Test Password-less Login

Verify you can now SSH without a password:

```bash
ssh <username>@<server-name>
```

💡 **Example:** `ssh tony@stapp01`

**Expected result:** You should connect immediately without being asked for a password!

Test all servers to confirm password-less access works.

---

## ✅ Verification Checklist

Before marking this challenge complete:

- [ ] SSH key pair generated on jump host
- [ ] Public key exists at `~/.ssh/id_rsa.pub`
- [ ] Key copied to all app servers
- [ ] Can SSH to all servers without password
- [ ] KodeKloud validation passes

---

## 🔧 Troubleshooting

**ssh-keygen fails:**
- Check if `.ssh` directory exists: `ls -la ~/.ssh`
- Create if needed: `mkdir -p ~/.ssh`
- Verify permissions: `chmod 700 ~/.ssh`

**ssh-copy-id command not found:**
- Use manual method (see "Good to Know" section)
- Or install: `sudo yum install openssh-clients`

**Still asking for password:**
- Verify key was copied: `ssh <user>@<server> "cat ~/.ssh/authorized_keys"`
- Check file permissions on remote: `~/.ssh` should be `700`, `authorized_keys` should be `600`
- Ensure using correct username for each server

**Permission denied (publickey):**
- Key might not be copied correctly
- Check remote server SSH config allows key authentication
- Verify private key exists locally: `ls -l ~/.ssh/id_rsa`

---

## 💡 Good to Know

**Manual Key Copy Method:**
If `ssh-copy-id` isn't available:

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

**Key Types:**
```bash
# RSA (traditional, widely supported)
ssh-keygen -t rsa -b 4096

# Ed25519 (modern, faster, smaller)
ssh-keygen -t ed25519

# ECDSA (another option)
ssh-keygen -t ecdsa -b 521
```

**Security Best Practices:**
- Use passphrase for keys (except automation)
- Use 4096-bit RSA for higher security
- Regularly rotate SSH keys
- Never share private keys
- Use separate keys for different purposes

**Automation Use Cases:**
- CI/CD pipeline deployments
- Automated backups across servers
- Configuration management (Ansible)
- Monitoring and health checks
- Log collection scripts

---

## 📚 Navigation

- **← Previous**: [Day 6 - Setup a Cron Job](./day-06.md)
- **Next →**: [Week 2 - Day 8](../week-02/day-08.md)

**🔗 Challenge Source**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

*Password-less SSH - automation's best friend!*
