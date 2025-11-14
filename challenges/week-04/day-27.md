# Challenge 27: Git Revert Some Changes

## 📊 Metadata
- **Day**: 27
- **Week**: 4
- **Day in Week**: 6/7
- **Category**: Git
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus application development team was working on a git repository /usr/src/kodekloudrepos/demo present on Storage server in Stratos DC. However, they reported an issue with the recent commits being pushed to this repo. They have asked the DevOps team to revert repo HEAD to last commit. Below are more details about the task:

- In /usr/src/kodekloudrepos/demo git repository, revert the latest commit ( HEAD ) to the previous commit (JFYI the previous commit hash should be with initial commit message ).
- Use revert demo message (please use all small letters for commit message) for the new revert commit.


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
- Day 24: Git Branch Create (recommended)
- Day 25: Git Branch Merge (recommended)
- Day 26: Git Manage Remotes (recommended)

**Required Skills:**
- ✅ Initialize and clone repositories
- ✅ Create commits with meaningful messages
- ✅ Manage branches effectively
- ✅ Push and pull from remotes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Login into storage server
2. Move into repository directory

    ```sh
    sudo su
    cd /usr/src/kodekloudrepos/demo
    ```

3. Check git log to find initial commit

    ```sh
    git log --oneline
    ```

    > if you find initial commit message, then copy commit hash and run the following command

    ```sh
    git revert HEAD -m "revert demo"
    ```

4. Push the changes

    ```sh
    git push
    ```

## Good to Know?

### Git Revert vs Reset

- **Revert**: Creates new commit that undoes changes (safe)
- **Reset**: Moves HEAD pointer, can lose history (destructive)
- **Public History**: Use revert for shared repositories
- **Private History**: Reset acceptable for local changes

### Revert Operations

- **Single Commit**: `git revert commit-hash`
- **HEAD**: `git revert HEAD` - Revert latest commit
- **Range**: `git revert HEAD~3..HEAD` - Revert multiple commits
- **No Commit**: `git revert --no-commit` - Stage changes without committing

### Commit Messages

- **Descriptive**: Explain what is being reverted and why
- **Reference**: Include original commit hash or message
- **Convention**: Follow team's commit message standards
- **Traceability**: Help future developers understand changes

### Safety Considerations

- **Shared Repositories**: Always use revert, never reset
- **Testing**: Test reverted code before pushing
- **Communication**: Inform team about reverted changes
- **Documentation**: Update relevant documentation

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

- **← Previous**: [Day 26 - Git Manage Remotes](./day-26.md)
- **Next →**: [Day 28 - Git Cherry Pick](../week-04/day-28.md)

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

