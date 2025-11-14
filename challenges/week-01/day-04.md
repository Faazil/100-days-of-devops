# Challenge 4: Script Execute Permissions

## 📊 Metadata
- **Day**: 4
- **Week**: 1
- **Day in Week**: 4/7
- **Category**: DevOps
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Scenario

In a bid to automate backup processes, the xFusionCorp Industries sysadmin team has developed a new bash script named `xfusioncorp.sh`. While the script has been distributed to all necessary servers, it lacks executable permissions on App Server 1 within the Stratos Datacenter.

Your task is to grant executable permissions to the `/tmp/xfusioncorp.sh` script on App Server 1. Additionally, ensure that all users have the capability to execute it.

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer) platform with pre-configured lab infrastructure.

---

## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `ssh`, `chmod`, `ls`
- **Key Concepts**:
  - Linux file permissions
  - Permission modes (read, write, execute)
  - Octal permission notation

**Required Skills:**
- ✅ Understand Linux permission system
- ✅ Modify file permissions
- ✅ Verify permission changes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

---

## 💡 Understanding the Task

**What Are Execute Permissions?**

In Linux, files need execute permission to run as programs or scripts. Without it, even a perfectly written script won't run.

**Permission Types:**
- **Read (r)** - Can view file contents
- **Write (w)** - Can modify file
- **Execute (x)** - Can run file as program

**Who Gets Permissions:**
- **User (owner)** - The file's owner
- **Group** - Users in the file's group
- **Others** - Everyone else

**Why It Matters:** Scripts are just text files until you add execute permission. This is a fundamental Linux security feature.

---

## 📝 Solution

### Step 1: Connect to App Server

SSH to App Server 1:

```bash
ssh <your-username>@<server-name>
```

💡 **Example:** `ssh tony@stapp01`

---

### Step 2: Check Current Permissions

View the script's current permissions:

```bash
ls -la /tmp/xfusioncorp.sh
```

💡 **Example:** `ls -la /tmp/xfusioncorp.sh`

**Expected output:**
```
---------- 1 root root 40 Nov 14 10:30 /tmp/xfusioncorp.sh
```

Notice the `----------` means no permissions at all!

---

### Step 3: Add Execute Permissions

Grant execute permission to everyone:

```bash
chmod 755 /tmp/xfusioncorp.sh
```

💡 **Example:** `chmod 755 /tmp/xfusioncorp.sh`

**What this means:**
- `7` (owner) = read (4) + write (2) + execute (1) = full access
- `5` (group) = read (4) + execute (1) = read and run
- `5` (others) = read (4) + execute (1) = read and run

**Expected result:** Command completes silently.

---

### Step 4: Verify Permissions Changed

Confirm the permissions were updated:

```bash
ls -la /tmp/xfusioncorp.sh
```

💡 **Example:** `ls -la /tmp/xfusioncorp.sh`

**Expected output:**
```
-rwxr-xr-x 1 root root 40 Nov 14 10:30 /tmp/xfusioncorp.sh
```

The `rwxr-xr-x` confirms execute permissions for all users!

---

## ✅ Verification Checklist

Before marking this challenge complete:

- [ ] File shows `-rwxr-xr-x` permissions
- [ ] All three groups (owner, group, others) can execute
- [ ] Script can be run: `/tmp/xfusioncorp.sh`
- [ ] KodeKloud validation passes

---

## 🔧 Troubleshooting

**Permission denied when running chmod:**
- Use `sudo chmod 755 /tmp/xfusioncorp.sh` if file is owned by root
- Check your user permissions

**Permissions didn't change:**
- Verify correct file path `/tmp/xfusioncorp.sh`
- Check if file exists: `ls /tmp/xfusioncorp.sh`

**Still can't execute script:**
- Make sure script has proper shebang line (`#!/bin/bash`)
- Check script syntax errors

**Wrong permissions showing:**
- Verify you used `755` not `555` or other values
- Re-run chmod command

---

## 💡 Good to Know

**Permission Number System:**
```
Owner  Group  Others
 7      5      5
rwx    r-x    r-x

Numbers mean:
4 = read (r)
2 = write (w)
1 = execute (x)

Add them up:
7 = 4+2+1 = rwx (all permissions)
5 = 4+1 = r-x (read + execute)
6 = 4+2 = rw- (read + write)
```

**Common Permission Patterns:**
```bash
chmod 755 script.sh   # Standard executable
chmod 644 file.txt    # Standard file (no execute)
chmod 600 secret.txt  # Private file (owner only)
chmod 777 file.sh     # Full access (dangerous!)
```

**Alternative Method (Symbolic):**
```bash
# Add execute for everyone
chmod +x /tmp/xfusioncorp.sh

# Add execute for owner only
chmod u+x /tmp/xfusioncorp.sh

# Remove execute from others
chmod o-x /tmp/xfusioncorp.sh
```

---

## 📚 Navigation

- **← Previous**: [Day 3 - Secure SSH Root Access](./day-03.md)
- **Next →**: [Day 5 - Install and Configuration Selinux](./day-05.md)

**🔗 Challenge Source**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

---

*Understanding permissions - the foundation of Linux security!*
