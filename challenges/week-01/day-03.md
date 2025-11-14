# Challenge 3: Secure SSH Root Access

## 📊 Metadata
- **Day**: 3
- **Week**: 1
- **Day in Week**: 3/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Scenario

Disable all app server SSH root access.

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
- **Command Line Tools**: `ssh`, `sudo`, `sed`, `systemctl`
- **Key Concepts**:
  - SSH security configuration
  - Service management
  - Text file editing

**Required Skills:**
- ✅ Edit configuration files
- ✅ Restart system services
- ✅ Verify security settings

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

## 💡 Understanding the Task

**Why Disable Root SSH Login?**

Allowing direct root SSH access is one of the biggest security risks. If attackers gain root credentials, they have complete control over your system.

**Security Benefits:**
- Forces users to log in with personal accounts first
- Creates an audit trail (who did what)
- Enables sudo logging for all admin actions
- Prevents automated brute-force attacks on root account

**Best Practice:** Never allow direct root SSH login. Always require users to connect as themselves, then use `sudo` for admin tasks.

---

## 📝 Solution

### Step 1: Connect to App Server

SSH into each app server that needs to be secured:

```bash
ssh <your-username>@<server-name>
```

💡 **Example:** `ssh tony@stapp01`

**Note:** Repeat this process for all app servers in your environment.

---

### Step 2: Modify SSH Configuration

Update the SSH server configuration to disable root login:

```bash
sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config
```

💡 **Example:** `sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config`

**What this command does:**
- `sudo` - Run with admin privileges
- `sed -i` - Edit the file in-place (directly modify the file)
- `'s/PermitRootLogin yes/PermitRootLogin no/g'` - Find "PermitRootLogin yes" and replace with "PermitRootLogin no"
- `/etc/ssh/sshd_config` - SSH daemon configuration file

**Expected result:** Command completes silently (no output = success).

---

### Step 3: Restart SSH Service

Apply the configuration changes by restarting the SSH daemon:

```bash
sudo systemctl restart sshd
```

💡 **Example:** `sudo systemctl restart sshd`

**Note:** Your current SSH connection will stay active. New connections will use the updated settings.

---

### Step 4: Verify the Change

Confirm that root login is now disabled:

```bash
grep PermitRootLogin /etc/ssh/sshd_config
```

💡 **Example:** `grep PermitRootLogin /etc/ssh/sshd_config`

**Expected output:**
```
PermitRootLogin no
```

The setting should now show "no" instead of "yes".

---

## ✅ Verification Checklist

Before marking this challenge complete:

- [ ] SSH config file shows `PermitRootLogin no`
- [ ] SSH service restarted without errors
- [ ] Configuration persists (check with `grep` command)
- [ ] KodeKloud validation passes

---

## 🔧 Troubleshooting

**SSH service won't restart:**
- Check configuration syntax: `sudo sshd -t`
- Look for error messages in output
- Verify you have correct permissions

**Configuration didn't change:**
- Check file permissions: `ls -l /etc/ssh/sshd_config`
- Ensure you used `sudo` with sed command
- Verify the exact text "PermitRootLogin yes" exists in file

**Lost SSH access:**
- Don't close your current session until verified
- Test from another terminal first
- Make sure you can still login as regular user

**Still can connect as root:**
- Ensure you restarted sshd: `sudo systemctl status sshd`
- Check if there are multiple PermitRootLogin lines in config
- Verify you're testing from a new SSH connection

---

## 💡 Good to Know

**Manual Configuration Method:**
```bash
# Edit file manually if you prefer
sudo vi /etc/ssh/sshd_config

# Find this line:
#PermitRootLogin yes

# Change to:
PermitRootLogin no

# Save and exit, then test config
sudo sshd -t

# If no errors, restart
sudo systemctl restart sshd
```

**Additional SSH Security:**
```bash
# Disable password authentication (use keys only)
PasswordAuthentication no

# Change default SSH port
Port 2222

# Limit users who can SSH
AllowUsers user1 user2

# Enable key-based authentication only
PubkeyAuthentication yes
```

**Why This Matters:**
- Root brute-force attacks are extremely common
- Every server on the internet gets scanned constantly
- Disabling root SSH is security 101
- Required by most compliance standards (PCI-DSS, SOC 2)

---

## 📚 Navigation

- **← Previous**: [Day 2 - Temporary User Setup with Expiry Date](./day-02.md)
- **Next →**: [Day 4 - Script Execute Permissions](./day-04.md)

**🔗 Challenge Source**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

*Security first - protect your root account!*
