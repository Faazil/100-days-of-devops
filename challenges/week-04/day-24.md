# Challenge 24: Git Branch Create

## 📊 Metadata
- **Day**: 24
- **Week**: 4
- **Day in Week**: 3/7
- **Category**: Git
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

Nautilus developers are actively working on one of the project repositories, `/usr/src/kodekloudrepos/media`. Recently, they decided to implement some new features in the application, and they want to maintain those new changes in a separate branch. Below are the requirements that have been shared with the DevOps team:

- On Storage server in Stratos DC create a new branch `xfusioncorp_media` from master branch in `/usr/src/kodekloudrepos/media` git repo.

- Please do not try to make any changes in the code.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

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
- Day 23: Fork a repository (recommended)

**Required Skills:**
- ✅ Initialize and clone repositories
- ✅ Create commits with meaningful messages
- ✅ Manage branches effectively
- ✅ Push and pull from remotes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Login into storage server and run the following commands:

    ```sh
    sudo su
    cd /usr/src/kodekloudrepos/media
    ```

2. Let's check current branch

    ```sh
    git branch
    ```

    if current branch is n't master branch, then switch to master branch:

    ```sh
    git switch master
    ```

3. Create a new branch

    ```sh
    git checkout -b xfusioncorp_media
    ```

## Good to Know?

### Git Branching Fundamentals

- **Purpose**: Parallel development lines for features/fixes
- **Lightweight**: Branches are just pointers to commits
- **Isolation**: Changes in branches don't affect other branches
- **Merging**: Combine changes from different branches

### Branch Operations

- **Create**: `git branch branch-name` (create only)
- **Create + Switch**: `git checkout -b branch-name`
- **Switch**: `git checkout branch-name` or `git switch branch-name`
- **List**: `git branch` (local) or `git branch -a` (all)

### Branching Strategies

- **Feature Branches**: Separate branch for each feature
- **Git Flow**: master, develop, feature, release, hotfix branches
- **GitHub Flow**: Simple master + feature branch workflow
- **Release Branches**: Prepare releases without blocking development

### Best Practices

- **Descriptive Names**: Use clear, meaningful branch names
- **Short-lived**: Keep feature branches small and focused
- **Regular Updates**: Sync with main branch frequently
- **Clean History**: Use meaningful commit messages

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

- **← Previous**: [Day 23 - Fork a repository](./day-23.md)
- **Next →**: [Day 25 - Git Branch Merge](../week-04/day-25.md)

### Similar Challenges (Git)
- [Day 22 - Clone Git Repository](../week-04/day-22.md)
- [Day 23 - Fork a repository](../week-04/day-23.md)
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
**Difficulty**: ⭐
**Category**: DevOps

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
```

