# Challenge 22: Clone Git Repository

## 📊 Metadata
- **Day**: 22
- **Week**: 4
- **Day in Week**: 1/7
- **Category**: Git
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The DevOps team established a new Git repository last week, which remains unused at present. However, the Nautilus application development team now requires a copy of this repository on the Storage Server in the Stratos DC. Follow the provided details to clone the repository

- The repository to be cloned is located at `/opt/games.git`
- Clone this Git repository to the `/usr/src/kodekloudrepos` directory. Ensure no modifications are made to the repository during the cloning process.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `git`, `git init`, `git add`, `git commit`, `git push`
- **Key Concepts**:
  - Version control fundamentals
  - Branching and merging strategies
  - Remote repositories
  - Commit history management

**Required Skills:**
- ✅ Initialize and clone repositories
- ✅ Create commits with meaningful messages
- ✅ Manage branches effectively
- ✅ Push and pull from remotes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Login into Storage server and run the following commands

    ```sh
    cd /usr/src/kodekloudrepos
    git clone /opt/games.git
    ```

## Good to Know?

### Git Clone Operations

- **Purpose**: Create local copy of remote repository
- **Full History**: Downloads complete project history
- **Remote Tracking**: Automatically sets up origin remote
- **Working Directory**: Creates working files from latest commit

### Clone Sources

- **Local Path**: Clone from local filesystem path
- **HTTP/HTTPS**: `git clone https://github.com/user/repo.git`
- **SSH**: `git clone git@github.com:user/repo.git`
- **Git Protocol**: `git clone git://server/repo.git`

### Clone Options

- **Shallow Clone**: `--depth 1` (only latest commit)
- **Specific Branch**: `--branch branch-name`
- **Bare Clone**: `--bare` (no working directory)
- **Mirror Clone**: `--mirror` (exact copy including refs)

### Post-Clone Setup

- **Remote Origin**: Automatically configured
- **Default Branch**: Checked out automatically
- **Tracking Branches**: Set up for push/pull operations
- **Configuration**: Inherits repository settings

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
- Practical application of Git skills
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

- **← Previous**: [Day 21 - Setup Git Repository on Server](./day-21.md)
- **Next →**: [Day 23 - Fork a repository](../week-04/day-23.md)

### Similar Challenges (Git)
- [Day 23 - Fork a repository](../week-04/day-23.md)
- [Day 24 - Git Branch Create](../week-04/day-24.md)
- [Day 25 - Git Branch Merge](../week-04/day-25.md)

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

