# Challenge 8: Install Ansible with pip3

## 📊 Metadata
- **Day**: 8
- **Week**: 2
- **Day in Week**: 1/7
- **Category**: Ansible
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Scenario

During the weekly meeting, the Nautilus DevOps team discussed automation and configuration management solutions. After considering several options, the team decided to go with Ansible due to its simple setup and minimal prerequisites. They want to start testing using Ansible, with the jump host as an Ansible controller to test different tasks on the other servers.

Install ansible version 4.8.0 on Jump host using pip3 only. Ensure Ansible binary is available globally on this system, so all users can run Ansible commands.

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Jump host with Python3 installed
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `pip3`, `ansible`, `which`
- **Key Concepts**:
  - Python package management with pip3
  - Global vs user-level installations
  - PATH environment variable
  - Sudo privileges for system-wide installations

**Required Skills:**
- ✅ Install Python packages with pip3
- ✅ Use sudo for system-wide installations
- ✅ Verify installed software versions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

## 💡 Understanding the Task

**What is Ansible?**

Ansible is an automation tool that lets you configure servers, deploy applications, and orchestrate complex workflows without needing to install agents on target machines. It's like having a remote control for your entire infrastructure.

**Why Use pip3 for Installation?**

Installing Ansible via pip3 (Python's package manager) gives you:
- **Precise version control** - Install exactly version 4.8.0 as required
- **Latest features** - Often newer than OS package repositories
- **Cross-platform consistency** - Works the same way on any Linux distribution
- **Easy upgrades** - Simple to switch between versions

**Global vs User Installation:**

- **Global (with sudo)**: Available to all users, installed system-wide
- **User-level (without sudo)**: Only available to the installing user

This challenge requires a global installation so any user on the jump host can use Ansible.

---

## 📝 Solution

### Step 1: Connect to Jump Host

Access the jump host where Ansible will be installed:

```bash
ssh <your-username>@<jump-host>
```

💡 **Example:** `ssh thor@jump_host`

---

### Step 2: Install Ansible with pip3

Install the specific Ansible version globally using pip3:

```bash
sudo pip3 install ansible==4.8.0
```

💡 **Example:** `sudo pip3 install ansible==4.8.0`

**What this command does:**
- `sudo` - Run with administrator privileges (for global installation)
- `pip3` - Python 3 package installer
- `install` - Install a package
- `ansible==4.8.0` - Specific package and version (== means exact version)

**Expected output:**
```
Collecting ansible==4.8.0
  Downloading ansible-4.8.0.tar.gz (35.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.6/35.6 MB 50.0 MB/s eta 0:00:00
Collecting ansible-core~=2.11.6
  Downloading ansible-core-2.11.12.tar.gz (7.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 80.0 MB/s eta 0:00:00
...
Successfully installed ansible-4.8.0 ansible-core-2.11.12
```

The installation may take a few minutes as it downloads and installs all dependencies.

---

### Step 3: Verify Ansible Installation

Check that Ansible was installed correctly and is accessible globally:

```bash
ansible --version
```

💡 **Example:** `ansible --version`

**Expected output:**
```
ansible [core 2.11.12]
  config file = None
  configured module search path = ['/home/thor/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.9/site-packages/ansible
  ansible collection location = /home/thor/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/local/bin/ansible
  python version = 3.9.18 (main, Jan 24 2024, 00:00:00) [GCC 11.4.1 20230605 (Red Hat 11.4.1-2)]
  jinja version = 3.1.3
  libyaml = True
```

The version line should show Ansible version 4.8.0 or ansible-core 2.11.x (which is part of Ansible 4.8.0).

---

### Step 4: Verify Global Availability

Confirm Ansible is installed globally and available to all users:

```bash
which ansible
```

💡 **Example:** `which ansible`

**Expected output:**
```
/usr/local/bin/ansible
```

If the path shows `/usr/local/bin/ansible`, it's installed globally. If it shows a path in your home directory like `~/.local/bin/ansible`, the installation was user-level only (which would be incorrect for this challenge).

---

## ✅ Verification Checklist

Before marking this challenge complete, verify:

- [ ] Ansible version 4.8.0 is installed (`ansible --version`)
- [ ] Ansible is available globally (`which ansible` shows `/usr/local/bin/ansible`)
- [ ] Installation used pip3 (not yum, apt, or other package managers)
- [ ] All users can run Ansible commands (test by switching users if possible)
- [ ] KodeKloud validation passes

---

## 🔧 Troubleshooting

**"Permission denied" error:**
- Ensure you're using `sudo` before the pip3 command
- Check that you have sudo privileges: `sudo -v`

**"pip3: command not found":**
- Install pip3 first: `sudo yum install python3-pip` (RHEL/CentOS) or `sudo apt install python3-pip` (Ubuntu)
- Verify Python3 is installed: `python3 --version`

**Wrong version installed:**
- Remove the wrong version: `sudo pip3 uninstall ansible`
- Reinstall with the exact version: `sudo pip3 install ansible==4.8.0`
- Don't forget the `==` for exact version matching

**Ansible installed but not found:**
- Check your PATH: `echo $PATH`
- The `/usr/local/bin` directory should be in your PATH
- Try the full path: `/usr/local/bin/ansible --version`

**Ansible only available to one user:**
- You installed without `sudo` - do a user-level uninstall: `pip3 uninstall ansible`
- Reinstall with sudo: `sudo pip3 install ansible==4.8.0`

---

## 💡 Good to Know

**Ansible Version Numbers:**

Ansible uses two version schemes:
- **Ansible Package**: Version 4.8.0 (the full package with collections)
- **Ansible Core**: Version 2.11.x (the core engine)

When you install `ansible==4.8.0`, you're getting both. The `--version` output shows the core version, which is correct.

**Why This Specific Version?**

Different Ansible versions support different features:
- Ansible 4.x includes many community collections by default
- Version 4.8.0 is stable and well-tested for production use
- Newer versions (5.x, 6.x) have breaking changes

**Alternative Installation Methods:**

```bash
# OS package manager (may not have exact version)
sudo yum install ansible           # RHEL/CentOS
sudo apt install ansible           # Ubuntu/Debian

# Python virtual environment (isolated installation)
python3 -m venv ansible-env
source ansible-env/bin/activate
pip install ansible==4.8.0

# From source (for development)
git clone https://github.com/ansible/ansible.git
cd ansible
pip install -e .
```

**Checking What pip3 Installed:**

```bash
# List all Ansible-related packages
pip3 list | grep ansible

# Show detailed package information
pip3 show ansible

# See where files were installed
pip3 show -f ansible
```

**Real-World Usage:**

In production environments, you typically:
- Install Ansible on a dedicated control node (jump host)
- Use a specific version for consistency across your team
- Document the version in your infrastructure-as-code repository
- Test playbooks before upgrading Ansible versions

---

## 📚 Navigation

- **← Previous**: [Day 7 - SSH Automation](../week-01/day-07.md)
- **Next →**: [Day 9 - Debugging MariaDB Issues](./day-09.md)

**🔗 Challenge Source**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

*Ansible installed - ready to automate your infrastructure!*
