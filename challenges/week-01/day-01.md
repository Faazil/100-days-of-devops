# Challenge 1: Linux User Setup with Non-interactive Shell

## 📊 Metadata
- **Day**: 1
- **Week**: 1
- **Day in Week**: 1/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

**Difficulty**: 🟢 Beginner | **Time**: 10 minutes | **Category**: Linux Administration

## 🎯 Objective

Create a user with non-interactive shell for your organization on a specific server. This is essential for service accounts and automated processes that don't require interactive login capabilities.

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

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## 🔧 Technologies Used

- Linux user management commands
- SSH access
- System administration

## Steps

1. First, login into the app server using `SSH`:

    ```sh
    ssh user@app-server-ip or ssh user@server-name
    ```

    > It will ask for user password, enter the correct password.

2. After login into server, run the following command to create user with non-interactive shell

    ```sh
    sudo useradd -m -s /usr/sbin/nologin user-name
    ```

    `s`: for shell, here we are giving nologin shell

    `m`: for user home directory, It will create a directory with user-name under /home

3. Verify the result

    ```sh
    cat /etc/passwd
    ```

    It should give you a list of users where you will find your created user. It will look like this:
    `kareem:x:1003:1004::/home/kareem:/usr/sbin/nologin`

    Try to login using:

    ```sh
    sudo su user-name
    ```

    Output: `This account is currently not available.`

## Verification & Troubleshooting

### Common Issues

- **Permission denied**: Ensure you have sudo privileges
- **User already exists**: Check existing users with `cat /etc/passwd | grep username`
- **Shell not found**: Verify `/usr/sbin/nologin` exists on your system

### Additional Commands

```bash
# List all users with nologin shell
grep nologin /etc/passwd

# Check user details
id username

# Remove user if needed
sudo userdel -r username
```

## Related Topics

- [Day 002: Temporary User Setup with Expiry Date](./002.md)
- [Day 003: Secure SSH Root Access](./003.md)
- Linux user management best practices

## Key Takeaways

- Non-interactive shells prevent direct user login
- Service accounts should use `/usr/sbin/nologin` or `/bin/false`
- Always verify user creation with multiple methods
- Understanding user shells is crucial for system security

## Good to Know?

### Linux User Management

- **User Types**: Regular users, system users, service accounts
- **Shell Types**: `/bin/bash` (interactive), `/usr/sbin/nologin` (non-interactive), `/bin/false` (deny access)
- **User Database**: `/etc/passwd` stores user information, `/etc/shadow` stores passwords

### useradd Command Options

- `-m`: Create home directory
- `-s`: Specify shell
- `-d`: Custom home directory path
- `-g`: Primary group
- `-G`: Additional groups
- `-e`: Account expiry date

### Security Best Practices

- Service accounts should use non-interactive shells
- Regular users need interactive shells like `/bin/bash`
- Always verify user creation with multiple commands
- Use principle of least privilege

**Next Challenge**: [Day 002 - Temporary User Setup](./002.md)

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

- **Next →**: [Day 2 - Temporary User Setup with Expiry Date](../week-01/day-02.md)

### Similar Challenges (Linux)
- [Day 2 - Temporary User Setup with Expiry Date](../week-01/day-02.md)
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

