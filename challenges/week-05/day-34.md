# Challenge 34: Configure Git Hook

## 📊 Metadata
- **Day**: 34
- **Week**: 5
- **Day in Week**: 6/7
- **Category**: Git
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus application development team was working on a git repository /opt/demo.git which is cloned under /usr/src/kodekloudrepos directory present on Storage server in Stratos DC. The team want to setup a hook on this repository, please find below more details:

- Merge the feature branch into the master branch`, but before pushing your changes complete below point.

- Create a post-update hook in this git repository so that whenever any changes are pushed to the master branch, it creates a release tag with name release-2023-06-15, where 2023-06-15 is supposed to be the current date. For example if today is 20th June, 2023 then the release tag must be release-2023-06-20. Make sure you test the hook at least once and create a release tag for today's release.

- Finally remember to push your changes.


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
- Day 31: Git Stash (recommended)
- Day 32: Git Rebase (recommended)
- Day 33: Git Merge Conflict Resolve (recommended)

**Required Skills:**
- ✅ Initialize and clone repositories
- ✅ Create commits with meaningful messages
- ✅ Manage branches effectively
- ✅ Push and pull from remotes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Login into storage server and move into directory

    ```sh
    sudo -i
    cd /usr/src/kodekloudrepos/demo
    ```

2. Find the current branch and switch into master branch

    ```sh
    git branch
    git switch master
    ```

3. Merge the feature branch

    ```sh
    git merge feature
    ```

4. Add the script in hooks

    ```sh
    cp /opt/demo.git/hooks/post-update.sample /opt/demo.git/hooks/post-update
    chmod +x /opt/demo.git/hooks/post-update
    ```

5. Update script to push tags

    ```sh
    vi /opt/demo.git/hooks/post-update
    ```

    > Add these lines

    ```shell
    day=$(date +"%Y-%m-%d")
    TAG="release-$day"

    git tag -a $TAG -m "Released at: $day"
    ```

6. Finally, push the changes

    ```sh
    git push
    ```

    > It will add a new tags and push it

    We can verify using these commands:

    ```sh
    git fetch --tags
    git tag
    ```

## Good to Know?

### Git Hooks

- **Purpose**: Scripts that run automatically on Git events
- **Automation**: Enforce policies, run tests, deploy code
- **Client-side**: Run on local operations (commit, merge)
- **Server-side**: Run on remote operations (push, receive)

### Hook Types

- **pre-commit**: Run before commit is created
- **post-commit**: Run after commit is created
- **pre-push**: Run before push to remote
- **post-update**: Run after remote repository is updated

### Hook Implementation

- **Location**: `.git/hooks/` directory
- **Executable**: Must have execute permissions
- **Language**: Any scripting language (bash, Python, etc.)
- **Exit Codes**: Non-zero exit prevents operation (pre-hooks)

### Common Use Cases

- **Code Quality**: Run linters, formatters
- **Testing**: Execute test suites before commits
- **Deployment**: Automatic deployment on push
- **Notifications**: Send alerts on repository changes
- **Tagging**: Automatic version tagging

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

- **← Previous**: [Day 33 - Git Merge Conflict Resolve](./day-33.md)
- **Next →**: [Day 35 - Setup Docker Installation](../week-05/day-35.md)

### Similar Challenges (Git)
- [Day 24 - Git Branch Create](../week-04/day-24.md)
- [Day 25 - Git Branch Merge](../week-04/day-25.md)
- [Day 26 - Git Manage Remotes](../week-04/day-26.md)

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

