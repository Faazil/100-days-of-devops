# Challenge 31: Git Stash

## 📊 Metadata
- **Day**: 31
- **Week**: 5
- **Day in Week**: 3/7
- **Category**: Git
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus application development team was working on a git repository `/usr/src/kodekloudrepos/ecommerce` present on Storage server in Stratos DC. One of the developers stashed some in-progress changes in this repository, but now they want to restore some of the stashed changes. Find below more details to accomplish this task:

- Look for the stashed changes under `/usr/src/kodekloudrepos/ecommerce` git repository, and restore the stash with stash@{1} identifier. Further, commit and push your changes to the origin.


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
- Day 28: Git Cherry Pick (recommended)
- Day 29: Git Pull Request (recommended)
- Day 30: Git Reset Hard (recommended)

**Required Skills:**
- ✅ Initialize and clone repositories
- ✅ Create commits with meaningful messages
- ✅ Manage branches effectively
- ✅ Push and pull from remotes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Access storage server and move into repository

    ```sh
    sudo -i
    cd /usr/src/kodekloudrepos/ecommerce
    ```

2. Review the stash list:

    ```sh
    git stash list
    ```

    ```shell
    [root@ststor01 ecommerce]# git stash list
    stash@{0}: WIP on master: 7fe985d initial commit
    stash@{1}: WIP on master: 7fe985d initial commit
    ```

3. Restart stash files

    ```sh
    git stash apply stash@{1}
    ```

4. Push changes

    ```sh
    git add .
    git commit -m "Restored stash files"
    git push
    ```

## Good to Know?

### Git Stash Purpose

- **Temporary Storage**: Save work-in-progress without committing
- **Branch Switching**: Clean working directory for branch changes
- **Emergency Fixes**: Quickly switch to fix urgent issues
- **Experiment**: Try different approaches without losing work

### Stash Operations

- **Save**: `git stash` or `git stash push -m "message"`
- **List**: `git stash list` - Show all stashes
- **Apply**: `git stash apply stash@{n}` - Restore without removing
- **Pop**: `git stash pop` - Apply and remove latest stash

### Stash Management

- **Multiple Stashes**: Stack of saved changes
- **Naming**: Use descriptive messages for identification
- **Selective**: `git stash push -p` for partial stashing
- **Cleanup**: `git stash drop stash@{n}` to remove stash

### Advanced Stashing

- **Include Untracked**: `git stash -u` includes new files
- **Include Ignored**: `git stash -a` includes ignored files
- **Branch from Stash**: `git stash branch name` creates branch
- **Show Changes**: `git stash show -p stash@{n}` displays diff

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

- **← Previous**: [Day 30 - Git Reset Hard](./day-30.md)
- **Next →**: [Day 32 - Git Rebase](../week-05/day-32.md)

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

