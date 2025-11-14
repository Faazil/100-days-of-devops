# Challenge 5: Install and Configuration Selinux

## 📊 Metadata
- **Day**: 5
- **Week**: 1
- **Day in Week**: 5/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Scenario

Following a security audit, the xFusionCorp Industries security team has opted to enhance application and server security with SELinux. To initiate testing, the following requirements have been established for App server 2 in the Stratos Datacenter:

- Install the required SELinux packages
- Permanently disable SELinux for the time being (it will be re-enabled after necessary configuration changes)
- No need to reboot the server (a scheduled maintenance reboot is planned for tonight)
- Disregard the current status via command line; the final status after reboot should be disabled

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
- **Command Line Tools**: `ssh`, `sudo`, `dnf/yum`, `vi/nano`
- **Key Concepts**:
  - SELinux security framework
  - Package management
  - Configuration file editing

**Required Skills:**
- ✅ Install packages using dnf/yum
- ✅ Edit system configuration files
- ✅ Understand SELinux modes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

---

## 💡 Understanding the Task

**What is SELinux?**

SELinux (Security-Enhanced Linux) is a security framework that provides mandatory access control. It adds an extra layer of security beyond traditional Linux permissions.

**SELinux Modes:**
- **Enforcing** - Policies are active, violations are blocked
- **Permissive** - Policies logged but not enforced (audit mode)
- **Disabled** - SELinux is completely off

**Why Disable (Temporarily)?**
Sometimes applications don't work well with SELinux until properly configured. It's common to disable it initially, configure your apps, then create proper SELinux policies and re-enable.

---

## 📝 Solution

### Step 1: Connect to App Server

SSH to App Server 2:

```bash
ssh <your-username>@<server-name>
```

💡 **Example:** `ssh steve@stapp02`

---

### Step 2: Install SELinux Packages

Install all required SELinux packages:

```bash
sudo dnf install selinux-policy selinux-policy-targeted policycoreutils policycoreutils-python-utils -y
```

💡 **Example:** `sudo dnf install selinux-policy selinux-policy-targeted policycoreutils policycoreutils-python-utils -y`

**What this installs:**
- `selinux-policy` - Base SELinux policy
- `selinux-policy-targeted` - Targeted policy (most common)
- `policycoreutils` - SELinux management tools
- `policycoreutils-python-utils` - Python utilities for SELinux

**Expected result:** Packages install successfully. You'll see download progress and "Complete!" message.

---

### Step 3: Edit SELinux Configuration

Open the SELinux config file:

```bash
sudo vi /etc/selinux/config
```

💡 **Example:** `sudo vi /etc/selinux/config`

**Find the line:**
```
SELINUX=enforcing
```

**Change it to:**
```
SELINUX=disabled
```

**Save and exit:**
- Press `i` for insert mode
- Make the change
- Press `ESC`
- Type `:wq` and press ENTER

---

### Step 4: Verify Configuration

Check that the configuration was saved correctly:

```bash
cat /etc/selinux/config | grep SELINUX=
```

💡 **Example:** `cat /etc/selinux/config | grep SELINUX=`

**Expected output:**
```
SELINUX=disabled
```

**Note:** The change takes effect after the next reboot (scheduled for tonight).

---

## ✅ Verification Checklist

Before marking this challenge complete:

- [ ] SELinux packages installed successfully
- [ ] Configuration file shows `SELINUX=disabled`
- [ ] File saved properly (can view with `cat`)
- [ ] KodeKloud validation passes

---

## 🔧 Troubleshooting

**Package installation fails:**
- Check internet connectivity
- Try `sudo yum install` if `dnf` not available
- Verify repository configuration

**Can't edit config file:**
- Make sure you're using `sudo`
- Try `nano` if not comfortable with `vi`
- Check file permissions: `ls -l /etc/selinux/config`

**Configuration not saving:**
- Make sure you saved the file (`:wq` in vi)
- Verify with: `cat /etc/selinux/config`
- Check disk space: `df -h`

**SELinux still showing as enforcing:**
- Configuration only applies after reboot
- Current status doesn't matter for this task
- Check file content, not current status

---

## 💡 Good to Know

**Alternative Editors:**
```bash
# Using nano (easier for beginners)
sudo nano /etc/selinux/config

# Using sed (one-liner)
sudo sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
```

**Checking SELinux Status:**
```bash
# Check current SELinux mode
getenforce

# Detailed SELinux status
sestatus

# Temporarily set mode (until reboot)
sudo setenforce 0  # Permissive
sudo setenforce 1  # Enforcing
```

**SELinux Modes Explained:**
- **Disabled**: SELinux is off (requires reboot to change)
- **Permissive**: Logs violations but allows them (testing mode)
- **Enforcing**: Actively blocks policy violations (production mode)

**Why This Matters:**
- SELinux can prevent applications from running
- Common in RHEL/CentOS environments
- Understanding modes helps troubleshooting
- Proper SELinux configuration is production best practice

---

## 📚 Navigation

- **← Previous**: [Day 4 - Script Execute Permissions](./day-04.md)
- **Next →**: [Day 6 - Setup a Cron Job](./day-06.md)

**🔗 Challenge Source**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

---

*SELinux - powerful security when configured correctly!*
