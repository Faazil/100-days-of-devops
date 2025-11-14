# Challenge 23: Fork a repository

## 📊 Metadata
- **Day**: 23
- **Week**: 4
- **Day in Week**: 2/7
- **Category**: Git
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

There is a Git server utilized by the Nautilus project teams. Recently, a new developer named Jon joined the team and needs to begin working on a project. To begin, he must fork an existing Git repository. Follow the steps below:

- Click on the Gitea UI button located on the top bar to access the Gitea page.

- Login to Gitea server using username jon and password Jon_pass123.

- Once logged in, locate the Git repository named sarah/story-blog and fork it under the jon user.


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

**Foundation from Earlier Challenges:**
- Day 22: Clone Git Repository (recommended)

**Required Skills:**
- ✅ Initialize and clone repositories
- ✅ Create commits with meaningful messages
- ✅ Manage branches effectively
- ✅ Push and pull from remotes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

Pretty simple and straight forward.

1. Login into UI with given user password
2. CLick on the repository (at right sidebar)
3. Click on the fork option (top right)

## Good to Know?

### Git Forking Concepts

- **Purpose**: Create personal copy of someone else's repository
- **Independence**: Fork is separate from original repository
- **Contribution**: Common workflow for open source contributions
- **Ownership**: You own and control your fork

### Fork vs Clone

- **Fork**: Server-side copy (GitHub, GitLab, Gitea)
- **Clone**: Local copy on your machine
- **Relationship**: Fork maintains connection to original
- **Workflow**: Fork → Clone → Modify → Pull Request

### Collaboration Workflow

1. **Fork**: Create your copy of the repository
2. **Clone**: Download fork to local machine
3. **Branch**: Create feature branch for changes
4. **Commit**: Make and commit your changes
5. **Push**: Upload changes to your fork
6. **Pull Request**: Propose changes to original repository

### Gitea Features

- **Self-hosted**: Git service similar to GitHub
- **Lightweight**: Minimal resource requirements
- **Web Interface**: User-friendly repository management
- **Collaboration**: Issues, pull requests, wikis

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

- **← Previous**: [Day 22 - Clone Git Repository](./day-22.md)
- **Next →**: [Day 24 - Git Branch Create](../week-04/day-24.md)

### Similar Challenges (Git)
- [Day 22 - Clone Git Repository](../week-04/day-22.md)
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

