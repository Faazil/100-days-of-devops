# Challenge 1: Linux User Setup with Non-interactive Shell

## 📊 Metadata
- **Day**: 1
- **Week**: 1
- **Day in Week**: 1/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Scenario

Create a user with non-interactive shell for your organization on a specific server. This is essential for service accounts and automated processes that don't require interactive login capabilities.

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
- **Command Line Tools**: `ssh`, `sudo`, `useradd`, `cat`, `grep`
- **Key Concepts**:
  - SSH remote access
  - User and group management
  - File permissions and ownership
  - Linux file system hierarchy

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

## 💡 Understanding the Task

**What's a Non-Interactive Shell?**

Think of it as a "service account" - the user exists in the system but cannot log in directly. This is perfect for applications and services that need a user account but shouldn't allow human login.

**Common Use Cases:**
- Web server users (nginx, apache)
- Database service accounts (mysql, postgres)
- Application runtime users
- CI/CD automation accounts

**Why It Matters:** Security best practice - if a service gets compromised, attackers can't use it to log into your server.

---

## 📝 Solution

### Step 1: Connect to Your Server

Access the target server using SSH:

```bash
ssh <your-username>@<server-name>
```

💡 **Example:** `ssh tony@stapp01`

Enter your password when prompted. You should see your server's command prompt after successful login.

---

### Step 2: Create the Non-Interactive User

Execute this command to create a user that cannot log in interactively:

```bash
sudo useradd -m -s /usr/sbin/nologin <username>
```

💡 **Example:** `sudo useradd -m -s /usr/sbin/nologin kareem`

**What each part does:**
- `sudo` - Run with administrator privileges
- `useradd` - Command to create new user
- `-m` - Create a home directory for the user
- `-s /usr/sbin/nologin` - Set shell to nologin (prevents interactive login)
- `<username>` - The name of the user to create

**Expected result:** Command completes silently (no output = success in Linux!)

---

### Step 3: Verify the User Was Created

Check that the user exists and has the correct shell:

```bash
cat /etc/passwd | grep <username>
```

💡 **Example:** `cat /etc/passwd | grep kareem`

**Expected output:**
```
kareem:x:1003:1004::/home/kareem:/usr/sbin/nologin
```

The important part is at the end: `/usr/sbin/nologin` - this confirms the non-interactive shell.

---

### Step 4: Test the Non-Interactive Shell

Try to switch to the new user to verify they cannot log in:

```bash
sudo su - <username>
```

💡 **Example:** `sudo su - kareem`

**Expected output:**
```
This account is currently not available.
```

✅ **Perfect!** This message confirms the non-interactive shell is working as intended.

---

## ✅ Verification Checklist

Before marking this challenge complete, verify:

- [ ] User appears in `/etc/passwd` with `/usr/sbin/nologin` shell
- [ ] Attempting to switch to the user shows "account not available" message
- [ ] Home directory was created (`ls -la /home/<username>`)
- [ ] KodeKloud validation passes

---

## 🔧 Troubleshooting

**"Permission denied" error:**
- Make sure you're using `sudo` before the `useradd` command

**"User already exists" error:**
- Check if user exists: `id <username>`
- Either use a different username or delete the existing user: `sudo userdel -r <username>`

**Shell path not found:**
- Try `/bin/false` instead of `/usr/sbin/nologin`
- Verify the path exists: `ls -la /usr/sbin/nologin`

**No home directory created:**
- Make sure you included the `-m` flag in the useradd command

---

## 💡 Good to Know

**Alternative Non-Interactive Shells:**
- `/usr/sbin/nologin` - Modern standard (shows a polite message)
- `/bin/false` - Older approach (just returns false)
- `/sbin/nologin` - Alternative path on some systems

**Checking User Details:**
```bash
# View user ID and groups
id <username>

# List all users with nologin shell
grep nologin /etc/passwd

# View home directory permissions
ls -ld /home/<username>
```

**Real-World Usage:**
When you install services like Nginx or PostgreSQL, they typically create users with non-interactive shells automatically. This is the same principle you're practicing here.

---

## 📚 Navigation

- **Next →**: [Day 2 - Temporary User Setup with Expiry Date](./day-02.md)

**🔗 Challenge Source**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

*Simple, secure user management - the foundation of Linux system administration!*
