# Challenge 7: Linux SSH Automation

## 📊 Metadata
- **Day**: 7
- **Week**: 1
- **Day in Week**: 7/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The system admins team of xFusionCorp Industries has set up some scripts on jump host that run on regular intervals and perform operations on all app servers in Stratos Datacenter. To make these scripts work properly we need to make sure the thor user on jump host has password-less SSH access to all app servers through their respective sudo users (i.e tony for app server 1). Based on the requirements, perform the following:

Set up a password-less authentication from user thor on jump host to all app servers through their respective sudo users.


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
- Day 3: Secure SSH Root Access (recommended)
- Day 5: Install and Configuration Selinux (recommended)
- Day 6: Setup a Cron Job (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. On jump server, run the following command:

    ```sh
    ssh-keygen -t rsa -b 2048
    ```

    It will generate an ssh pub key and private key. We are going to share the pub key to all the app server for respective users.

2. Login into each app server and run the following command:

    ```sh
    mkdir -p .ssh
    vi .ssh/authorized_keys
    ```

    copy id_rsa.pub key from jump host inside /home/thor/.ssh/ and paste it there

## Optimized Automated Solution

```sh
#!/bin/sh

ssh-copy-id user@host
```

It will create .ssh directory for each app server if doesn't exist then copy paste host key to `authorized_keys` file.

## Good to Know?

### SSH Key Authentication

- **Key Types**: RSA (2048+ bits), Ed25519 (modern, faster), ECDSA
- **Components**: Private key (keep secret), Public key (share freely)
- **Location**: `~/.ssh/id_rsa` (private), `~/.ssh/id_rsa.pub` (public)
- **Security**: Much stronger than password authentication

### SSH Key Management

- **Generation**: `ssh-keygen -t rsa -b 4096` (strong RSA key)
- **Copy**: `ssh-copy-id user@host` (automated deployment)
- **Manual**: Copy public key to `~/.ssh/authorized_keys`
- **Permissions**: `700` for `.ssh/`, `600` for private keys, `644` for public keys

### Automation Benefits

- **Password-less**: No interactive password prompts
- **Scripting**: Enables automated deployments and backups
- **Security**: Eliminates password brute force attacks
- **Audit**: Key-based access is more traceable

### Best Practices

- **Passphrase**: Protect private keys with passphrases
- **Agent**: Use `ssh-agent` for passphrase caching
- **Rotation**: Regularly rotate SSH keys
- **Monitoring**: Track key usage and access patterns

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

- **← Previous**: [Day 6 - Setup a Cron Job](./day-06.md)
- **Next →**: [Day 8 - Setup Ansible](../week-02/day-08.md)

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

