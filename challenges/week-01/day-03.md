# Challenge 3: Secure SSH Root Access

## 📊 Metadata
- **Day**: 3
- **Week**: 1
- **Day in Week**: 3/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

Disable all app server SSH root access.


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
- Day 2: Temporary User Setup with Expiry Date (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Login into each app server ([this way](./001.md))
2. Modify `sshd_config` and restart sshd `service`

    ```sh
    sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config
    sudo systemctl restart sshd
    ```

## Good to Know?

### SSH Security Best Practices

- **Root Access**: Disable direct root login for security
- **Alternative**: Use sudo for administrative tasks
- **Key-based Auth**: Prefer SSH keys over passwords
- **Port Changes**: Consider changing default SSH port (22)

### SSH Configuration Options

- `PermitRootLogin no`: Disable root login
- `PasswordAuthentication no`: Disable password auth
- `PubkeyAuthentication yes`: Enable key-based auth
- `Port 2222`: Change default port

### Security Benefits

- **Audit Trail**: sudo logs all administrative actions
- **Principle of Least Privilege**: Users get minimal required access
- **Attack Surface**: Reduces brute force attack targets
- **Accountability**: Individual user accountability vs shared root

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

- **← Previous**: [Day 2 - Temporary User Setup with Expiry Date](./day-02.md)
- **Next →**: [Day 4 - Script Execute Permissions](../week-01/day-04.md)

### Similar Challenges (Linux)
- [Day 1 - Linux User Setup with Non-interactive Shell](../week-01/day-01.md)
- [Day 2 - Temporary User Setup with Expiry Date](../week-01/day-02.md)
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

