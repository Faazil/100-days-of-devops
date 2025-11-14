# Challenge 5: Install and Configuration Selinux

## 📊 Metadata
- **Day**: 5
- **Week**: 1
- **Day in Week**: 5/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

Following a security audit, the xFusionCorp Industries security team has opted to enhance application and server security with SELinux. To initiate testing, the following requirements have been established for App server 2 in the Stratos Datacenter:

- Install the required SELinux packages.
- Permanently disable SELinux for the time being; it will be re-enabled after necessary configuration changes.
- No need to reboot the server, as a scheduled maintenance reboot is already planned for tonight.
- Disregard the current status of SELinux via the command line; the final status after the reboot should be disabled.


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
- Day 3: Secure SSH Root Access (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Install selinux packages:

    ```sh
    sudo dnf install selinux-policy selinux-policy-targeted policycoreutils policycoreutils-python-utils
    ```

2. Modify file in `/etc/selinux/config:

    ```sh
    vi /etc/selinux/config
    ```

    add this line:

    ```nano
    SELINUX=disabled
    ```

## Good to Know?

### SELinux (Security-Enhanced Linux)

- **Purpose**: Mandatory Access Control (MAC) security framework
- **Modes**: Enforcing, Permissive, Disabled
- **Policies**: Targeted (default), Strict, MLS (Multi-Level Security)
- **Context**: Every file/process has security context (user:role:type:level)

### SELinux States

- **Enforcing**: Policies actively enforced, violations blocked
- **Permissive**: Policies logged but not enforced (audit mode)
- **Disabled**: SELinux completely turned off

### Key Commands

- `getenforce`: Check current SELinux mode
- `setenforce 0/1`: Temporarily set permissive/enforcing
- `sestatus`: Detailed SELinux status
- `sealert`: Analyze SELinux denials

### Configuration Files

- `/etc/selinux/config`: Main configuration
- `/var/log/audit/audit.log`: SELinux violations
- `/etc/selinux/targeted/`: Policy files

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

- **← Previous**: [Day 4 - Script Execute Permissions](./day-04.md)
- **Next →**: [Day 6 - Setup a Cron Job](../week-01/day-06.md)

### Similar Challenges (Linux)
- [Day 1 - Linux User Setup with Non-interactive Shell](../week-01/day-01.md)
- [Day 2 - Temporary User Setup with Expiry Date](../week-01/day-02.md)
- [Day 3 - Secure SSH Root Access](../week-01/day-03.md)

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

