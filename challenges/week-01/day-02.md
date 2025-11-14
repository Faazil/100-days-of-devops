# Challenge 2: Temporary User Setup with Expiry Date

## 📊 Metadata
- **Day**: 2
- **Week**: 1
- **Day in Week**: 2/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

As part of the temporary assignment to the Nautilus project, a developer named yousuf requires access for a limited duration. To ensure smooth access management, a temporary user account with an expiry date is needed. Here's what you need to do:

> Create a user named `yousuf` on `App Server 1` in Stratos Datacenter. Set the expiry date to `2024-01-28`, ensuring the user is created in lowercase as per standard protocol.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

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

**Foundation from Earlier Challenges:**
- Day 1: Linux User Setup with Non-interactive Shell (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Follow the [Day 01](./001.md) to connect server and run the following command:

    ```sh
    sudo useradd -m -e 2024-01-28 yousuf
    ```

2. Verify

    ```sh
    cat /etc/passwd
    sudo su yousuf
    ```

## Good to Know?

### User Account Expiry

- **Purpose**: Automatically disable accounts after specified date
- **Format**: YYYY-MM-DD (ISO 8601 standard)
- **Check Expiry**: `chage -l username` shows account aging info
- **Extend Expiry**: `sudo chage -E 2024-12-31 username`

### Temporary Account Management

- **Best Practice**: Always set expiry for temporary accounts
- **Monitoring**: Use `chage -l` to track account status
- **Cleanup**: Expired accounts remain but cannot login
- **Removal**: Use `userdel -r username` to completely remove

### Related Commands

- `chage`: Modify user password expiry information
- `usermod -e`: Modify existing user's expiry date
- `passwd -S`: Check password status

---

## ✅ Verification

After completing the challenge, verify your solution by:

1. **Testing the implementation**
   - Run all commands from the solution
   - Check for any error messages

2. **Validating the results**
   - Ensure all requirements are met
   - Test edge cases if applicable

3. **Clean up (if needed)**
   - Remove temporary files
   - Reset any test configurations

---

## 📚 Learning Notes

### Key Concepts

This challenge covers the following concepts:
- Practical application of Linux skills
- Real-world DevOps scenarios
- Best practices for production environments

### Common Pitfalls

- ⚠️ **Permissions**: Ensure you have the necessary permissions to execute commands
- ⚠️ **Syntax**: Double-check command syntax and flags
- ⚠️ **Environment**: Verify you're working in the correct environment/server

### Best Practices

- ✅ Always verify changes before marking as complete
- ✅ Test your solution in a safe environment first
- ✅ Document any deviations from the standard approach
- ✅ Keep security in mind for all configurations

---

## 🔗 Related Challenges

- **← Previous**: [Day 1 - Linux User Setup with Non-interactive Shell](./day-01.md)
- **Next →**: [Day 3 - Secure SSH Root Access](../week-01/day-03.md)

### Similar Challenges (Linux)
- [Day 1 - Linux User Setup with Non-interactive Shell](../week-01/day-01.md)
- [Day 3 - Secure SSH Root Access](../week-01/day-03.md)
- [Day 5 - Install and Configuration Selinux](../week-01/day-05.md)

---

## 📖 Additional Resources

- [KodeKloud Official Documentation](https://kodekloud.com)
- [Official Technology Documentation](#)
- [Community Discussions](#)

---

## 🎓 Knowledge Check

After completing this challenge, you should be able to:
- [ ] Understand the problem statement clearly
- [ ] Implement the solution independently
- [ ] Verify the solution works correctly
- [ ] Explain the concepts to others
- [ ] Apply these skills to similar problems

---

**Challenge Source**: KodeKloud 100 Days of DevOps
**Difficulty**: {get_difficulty_emoji(day)}
**Category**: {task_info['category']}

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
python3 ../../tools/progress.py --complete {day}
```

