# Challenge 26: Git Manage Remotes

## 📊 Metadata
- **Day**: 26
- **Week**: 4
- **Day in Week**: 5/7
- **Category**: Git
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The xFusionCorp development team added updates to the project that is maintained under /opt/beta.git repo and cloned under /usr/src/kodekloudrepos/beta. Recently some changes were made on Git server that is hosted on Storage server in Stratos DC. The DevOps team added some new Git remotes, so we need to update remote on /usr/src/kodekloudrepos/beta repository as per details mentioned below:

- In `/usr/src/kodekloudrepos/beta` repo add a new remote `dev_beta` and point it to `/opt/xfusioncorp_beta.git` repository.
- There is a file `/tmp/index.html` on same server; copy this file to the repo and `add/commit` to `master branch`.
- Finally `push master branch` to this new `remote origin`.


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
- Day 23: Fork a repository (recommended)
- Day 24: Git Branch Create (recommended)
- Day 25: Git Branch Merge (recommended)

**Required Skills:**
- ✅ Initialize and clone repositories
- ✅ Create commits with meaningful messages
- ✅ Manage branches effectively
- ✅ Push and pull from remotes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Login into storage server
2. move into repo directory

    ```sh
    sudo su
    cd /usr/src/kodekloudrepos/beta
    ```

3. Check current remote and branch:

    ```sh
    git remote -v
    git branch
    ```

4. Add new remote and check if it's added or not

    ```sh
    git remote add dev_beta /opt/xfusioncorp_beta.git
    git remote -v
    ```

5. Copy file and commit changes

    ```sh
    cp /tmp/index.html .
    git add .
    git commit -m "added tmp file"
    ```

6. Finallt, Push the changes to dev_beta remote

    ```sh
    git push dev_beta master
    ```

## Good to Know?

### Git Remotes

- **Purpose**: References to remote repositories for collaboration
- **Origin**: Default remote name when cloning
- **Multiple Remotes**: Can have multiple remotes (upstream, fork, etc.)
- **URL Types**: HTTPS, SSH, local file paths

### Remote Operations

- **Add**: `git remote add name url` - Add new remote
- **List**: `git remote -v` - Show all remotes with URLs
- **Remove**: `git remote remove name` - Delete remote
- **Rename**: `git remote rename old new` - Change remote name

### Push to Specific Remote

- **Syntax**: `git push remote-name branch-name`
- **Set Upstream**: `git push -u remote branch` - Set tracking
- **Force Push**: `git push --force` - Overwrite remote history
- **All Branches**: `git push --all` - Push all branches

### Best Practices

- **Descriptive Names**: Use meaningful remote names
- **Multiple Remotes**: Separate remotes for different purposes
- **Upstream Tracking**: Set upstream for easy push/pull
- **Access Control**: Use appropriate authentication methods

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

- **← Previous**: [Day 25 - Git Branch Merge](./day-25.md)
- **Next →**: [Day 27 - Git Revert Some Changes](../week-04/day-27.md)

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
**Difficulty**: {get_difficulty_emoji(day)}
**Category**: {task_info['category']}

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
python3 ../../tools/progress.py --complete {day}
```

