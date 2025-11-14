# Challenge 2: Temporary User Setup with Expiry Date

## 📊 Metadata
- **Day**: 2
- **Week**: 1
- **Day in Week**: 2/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Scenario

As part of the temporary assignment to the Nautilus project, a developer named yousuf requires access for a limited duration. To ensure smooth access management, a temporary user account with an expiry date is needed.

> Create a user named `yousuf` on `App Server 1` in Stratos Datacenter. Set the expiry date to `2024-01-28`, ensuring the user is created in lowercase as per standard protocol.

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
- **Command Line Tools**: `ssh`, `sudo`, `useradd`, `chage`
- **Key Concepts**:
  - User account management
  - Account expiration dates
  - Date formats (YYYY-MM-DD)

**Required Skills:**
- ✅ Create users with specific attributes
- ✅ Set account expiry dates
- ✅ Verify account properties

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

---

## 💡 Understanding the Task

**What's a Temporary User Account?**

This is an account that automatically becomes unusable after a specified date. The user can log in and work normally until the expiry date, after which the system blocks their access.

**Common Use Cases:**
- Contractors with fixed-term contracts
- Temporary project team members
- Intern or trainee accounts
- Time-limited testing accounts

**Why It Matters:** Automatic expiration means you don't have to remember to manually disable accounts. It's a security best practice that reduces the risk of forgotten temporary access.

---

## 📝 Solution

### Step 1: Connect to Your Server

Access the target app server:

```bash
ssh <your-username>@<server-name>
```

💡 **Example:** `ssh tony@stapp01`

---

### Step 2: Create User with Expiry Date

Create the user with an automatic expiration date:

```bash
sudo useradd -m -e 2024-01-28 yousuf
```

💡 **Example:** `sudo useradd -m -e 2024-01-28 yousuf`

**What each part does:**
- `sudo` - Run with administrator privileges
- `useradd` - Create new user
- `-m` - Create home directory
- `-e 2024-01-28` - Set expiry date (YYYY-MM-DD format)
- `yousuf` - Username to create

**Expected result:** Command completes silently. After 2024-01-28, this account will be disabled automatically.

---

### Step 3: Verify User Was Created

Check that the user exists:

```bash
cat /etc/passwd | grep yousuf
```

💡 **Example:** `cat /etc/passwd | grep yousuf`

**Expected output:**
```
yousuf:x:1002:1002::/home/yousuf:/bin/bash
```

---

### Step 4: Confirm Expiry Date

Verify the expiration date was set correctly:

```bash
sudo chage -l yousuf
```

💡 **Example:** `sudo chage -l yousuf`

**Expected output:**
```
...
Account expires: Jan 28, 2024
...
```

The `chage -l` command shows all account aging information, including the expiry date.

---

## ✅ Verification Checklist

Before marking this challenge complete:

- [ ] User appears in `/etc/passwd`
- [ ] `chage -l` shows correct expiry date (2024-01-28)
- [ ] Can switch to user: `sudo su - yousuf` (works before expiry)
- [ ] KodeKloud validation passes

---

## 🔧 Troubleshooting

**"Invalid date format" error:**
- Date must be in YYYY-MM-DD format
- Example: `2024-01-28` not `01/28/2024`

**"User already exists" error:**
- Check: `id yousuf`
- Delete if needed: `sudo userdel -r yousuf`
- Then recreate with correct expiry date

**Can't see expiry date:**
- Use `sudo chage -l yousuf` (requires sudo)
- Check Account expires line in output

**Permission denied:**
- Make sure you're using `sudo` before `useradd`

---

## 💡 Good to Know

**Managing Account Expiry:**
```bash
# View account expiry details
sudo chage -l <username>

# Change expiry date for existing user
sudo usermod -e 2024-12-31 <username>

# Remove expiry (set to never expire)
sudo usermod -e "" <username>
```

**Date Format:**
- Always use: YYYY-MM-DD
- Example: 2024-12-31
- This is ISO 8601 standard format

**What Happens After Expiry:**
- User cannot log in
- Account still exists in system
- Files and home directory remain
- Can be reactivated by changing expiry date

**Real-World Usage:**
Organizations use this for:
- 30-day contractor access
- 90-day trial periods
- Seasonal worker accounts
- Automatic compliance with termination dates

---

## 📚 Navigation

- **← Previous**: [Day 1 - Linux User Setup with Non-interactive Shell](./day-01.md)
- **Next →**: [Day 3 - Secure SSH Root Access](./day-03.md)

**🔗 Challenge Source**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

---

*Automated access management - set it and forget it!*
