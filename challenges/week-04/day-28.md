# Challenge 28: Git Cherry Pick

## 📊 Metadata
- **Day**: 28
- **Week**: 4
- **Day in Week**: 7/7
- **Category**: Git
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus application development team has been working on a project repository /opt/official.git. This repo is cloned at /usr/src/kodekloudrepos on storage server in Stratos DC. They recently shared the following requirements with the DevOps team:

> There are two branches in this repository, master and feature. One of the developers is working on the feature branch and their work is still in progress, however they want to merge one of the commits from the feature branch to the master branch, the message for the commit that needs to be merged into master is Update info.txt. Accomplish this task for them, also remember to push your changes eventually.


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
- Day 25: Git Branch Merge (recommended)
- Day 26: Git Manage Remotes (recommended)
- Day 27: Git Revert Some Changes (recommended)

**Required Skills:**
- ✅ Initialize and clone repositories
- ✅ Create commits with meaningful messages
- ✅ Manage branches effectively
- ✅ Push and pull from remotes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Access Storage Server

2. Move into cloned repository

    ```sh
    sudo su
    cd /usr/src/kodekloudrepos/official
    ```

3. Check Git branches

    ```sh
    git branch
    ```

4. If you are already in feature branch?

    ```sh
    git log
    ```

    > take note of hash for specific commit we are going to merge into master branch

5. Switch to master branch to pick commit and push

    ```sh
    git switch master
    git cherry-pick commit-hash
    git push
    ```

## Good to Know?

### Cherry-Pick Fundamentals

- **Purpose**: Apply specific commits from one branch to another
- **Selective**: Choose individual commits, not entire branches
- **New Commit**: Creates new commit with same changes
- **Preserve Author**: Maintains original author information

### Cherry-Pick Use Cases

- **Bug Fixes**: Apply hotfixes to multiple branches
- **Feature Backporting**: Bring features to older versions
- **Selective Merging**: Include specific changes without full merge
- **Release Management**: Pick commits for release branches

### Cherry-Pick Options

- **Single Commit**: `git cherry-pick commit-hash`
- **Multiple Commits**: `git cherry-pick hash1 hash2`
- **Range**: `git cherry-pick start-hash..end-hash`
- **No Commit**: `git cherry-pick --no-commit` - Stage without committing

### Conflict Resolution

- **Automatic**: Git applies changes if no conflicts
- **Manual**: Resolve conflicts like in merge operations
- **Continue**: `git cherry-pick --continue` after resolving
- **Abort**: `git cherry-pick --abort` to cancel operation

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

- **← Previous**: [Day 27 - Git Revert Some Changes](./day-27.md)
- **Next →**: [Day 29 - Git Pull Request](../week-05/day-29.md)

### Similar Challenges (Git)
- [Day 22 - Clone Git Repository](../week-04/day-22.md)
- [Day 23 - Fork a repository](../week-04/day-23.md)
- [Day 24 - Git Branch Create](../week-04/day-24.md)

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

