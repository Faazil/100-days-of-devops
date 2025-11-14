# Challenge 25: Git Branch Merge

## 📊 Metadata
- **Day**: 25
- **Week**: 4
- **Day in Week**: 4/7
- **Category**: Git
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus application development team has been working on a project repository /opt/demo.git. This repo is cloned at /usr/src/kodekloudrepos on storage server in Stratos DC. They recently shared the following requirements with DevOps team:

> Create a new branch nautilus in /usr/src/kodekloudrepos/demo repo from master and copy the /tmp/index.html file (present on storage server itself) into the repo. Further, add/commit this file in the new branch and merge back that branch into master branch. Finally, push the changes to the origin for both of the branches.


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
- Day 23: Fork a repository (recommended)
- Day 24: Git Branch Create (recommended)

**Required Skills:**
- ✅ Initialize and clone repositories
- ✅ Create commits with meaningful messages
- ✅ Manage branches effectively
- ✅ Push and pull from remotes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1, Login into Storage server

    ```sh
    ssh user@storage-server
    ```

2. Move into repository:

    ```sh
    sudo su
    cd /usr/src/kodekloudrepos/demo
    ```

3. Create a new branch

    ```sh
    # ensure current branch is master branch
    git branch
    # create a new branch
    git checkout -b nautilus
    ```
4. Copy files

    ```sh
    cp /tmp/index.html .
    ```
5. Commit changes

    ```sh
    git add .
    git commit -m "added tmp file"
    ```

6. Switch to master branch

    ```sh
    git switch master
    ```
7. Finally Merge `nautilus` branch and push chnages

    ```sh
    git merge nautilus
    git push
    ```

## Good to Know?

### Git Merge Types

- **Fast-forward**: Linear history, no merge commit
- **Three-way Merge**: Creates merge commit with two parents
- **Squash Merge**: Combines all commits into single commit
- **Rebase**: Replays commits on top of target branch

### Merge Workflow

1. **Switch to Target**: Checkout branch to merge into
2. **Merge Source**: `git merge source-branch`
3. **Resolve Conflicts**: Fix any merge conflicts
4. **Commit**: Complete merge with commit
5. **Push**: Upload changes to remote repository

### Conflict Resolution

- **Automatic**: Git merges non-conflicting changes
- **Manual**: Developer resolves conflicting changes
- **Merge Tools**: Use `git mergetool` for visual resolution
- **Markers**: `<<<<<<<`, `=======`, `>>>>>>>` show conflicts

### Best Practices

- **Clean Branches**: Ensure branches are up-to-date
- **Test Before Merge**: Verify changes work correctly
- **Meaningful Messages**: Write descriptive merge commit messages
- **Delete Merged Branches**: Clean up after successful merge

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

- **← Previous**: [Day 24 - Git Branch Create](./day-24.md)
- **Next →**: [Day 26 - Git Manage Remotes](../week-04/day-26.md)

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

