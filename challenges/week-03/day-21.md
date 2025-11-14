# Challenge 21: Setup Git Repository on Server

## 📊 Metadata
- **Day**: 21
- **Week**: 3
- **Day in Week**: 7/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus development team has provided requirements to the DevOps team for a new application development project, specifically requesting the establishment of a Git repository. Follow the instructions below to create the Git repository on the Storage server in the Stratos DC:

- Utilize yum to install the git package on the Storage Server.
- Create a bare repository named /opt/demo.git (ensure exact name usage).


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
- Day 12: Linux Network Services (recommended)
- Day 14: Linux Process Troubleshooting (recommended)
- Day 18: Configure LAMP Server (LAMP Stack) (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Login to Storage Server and Install git

    ```sh
    sudo yum update -y
    sudo yum install -y git
    ```

2. Create a bare repository

    ```sh
   sudo git init --bare /opt/demo.git
   ```

## Good to Know?

### Git Repository Types

- **Working Repository**: Contains working directory with checked-out files
- **Bare Repository**: Contains only Git data, no working directory
- **Purpose**: Bare repos used for sharing/collaboration (central repositories)
- **Location**: Usually stored on servers for team access

### Bare Repository Benefits

- **No Working Directory**: Prevents conflicts when pushing
- **Central Hub**: Multiple developers can push/pull
- **Server Storage**: Efficient storage on servers
- **Collaboration**: Standard for team development workflows

### Git Installation

- **Package Managers**: `yum`, `apt`, `dnf` for Linux distributions
- **Version Control**: Track changes in source code
- **Distributed**: Every clone is a full repository
- **Branching**: Lightweight branching and merging

### Repository Naming

- **Convention**: Use `.git` suffix for bare repositories
- **Descriptive Names**: Choose meaningful repository names
- **Path Structure**: Organize repos in logical directory structure

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

- **← Previous**: [Day 20 - Configure Nginx + PHP-FPM Using Unix Sock](./day-20.md)
- **Next →**: [Day 22 - Clone Git Repository](../week-04/day-22.md)

### Similar Challenges (Linux)
- [Day 11 - Install and Setup Tomcat Server](../week-02/day-11.md)
- [Day 12 - Linux Network Services](../week-02/day-12.md)
- [Day 14 - Linux Process Troubleshooting](../week-02/day-14.md)

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

