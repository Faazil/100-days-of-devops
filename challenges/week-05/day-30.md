# Challenge 30: Git Reset Hard

## 📊 Metadata
- **Day**: 30
- **Week**: 5
- **Day in Week**: 2/7
- **Category**: Git
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus application development team was working on a git repository `/usr/src/kodekloudrepos/ecommerce` present on Storage server in Stratos DC. This was just a test repository and one of the developers just pushed a couple of changes for testing, but now they want to clean this repository along with the commit history/work tree, so they want to point back the HEAD and the branch itself to a commit with message `add data.txt file`. Find below more details:

- In `/usr/src/kodekloudrepos/ecommerce` git repository, reset the git commit history so that there are only two commits in the commit history i.e initial commit and add data.txt file.

- Also make sure to push your changes.


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
- Day 27: Git Revert Some Changes (recommended)
- Day 28: Git Cherry Pick (recommended)
- Day 29: Git Pull Request (recommended)

**Required Skills:**
- ✅ Initialize and clone repositories
- ✅ Create commits with meaningful messages
- ✅ Manage branches effectively
- ✅ Push and pull from remotes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Log into storage server and move into repository

    ```sh
    sudo -i
    cd /usr/src/kodekloudrepos/ecommerce
    ```

2. Check commits history

    ```sh
    git log --oneline
    ```

    ```shell
    [root@ststor01 ecommerce]# git log --oneline
    81e08fc (HEAD -> master, origin/master) Test Commit10
    686cb01 Test Commit9
    f0ff119 Test Commit8
    a8404ed Test Commit7
    a9fccf0 Test Commit6
    2554746 Test Commit5
    461c467 Test Commit4
    287d981 Test Commit3
    a63283d Test Commit2
    5479bcb Test Commit1
    90b2925 add data.txt file
    848a423 initial commit
    ```

3. Let's reset the commit history to old one

    ```ssh
    git reset --hard 90b2925
    ```

    ```shell
    root@ststor01 ecommerce]# git status
    On branch master
    Your branch is behind 'origin/master' by 10 commits, and can be fast-forwarded.
    (use "git pull" to update your local branch)

    nothing to commit, working tree clean
    ```

4. Push the changes

    ```sh
    git push --force
    ```

## Good to Know?

### Git Reset Types

- **Soft**: `--soft` - Move HEAD, keep staging and working directory
- **Mixed**: `--mixed` (default) - Move HEAD, reset staging, keep working
- **Hard**: `--hard` - Reset everything to specified commit
- **Keep**: `--keep` - Reset but keep uncommitted changes

### Reset Dangers

- **Data Loss**: Hard reset can permanently lose changes
- **Shared History**: Never reset commits pushed to shared repositories
- **Force Push**: Required after resetting pushed commits
- **Team Impact**: Can break other developers' work

### Safe Alternatives

- **Revert**: Use for shared repositories
- **New Branch**: Create branch before risky operations
- **Backup**: Create backup branch before reset
- **Stash**: Save work-in-progress before reset

### Recovery Options

- **Reflog**: `git reflog` shows recent HEAD movements
- **Recovery**: `git reset --hard HEAD@{n}` to restore
- **Time Limit**: Reflog entries expire after ~90 days
- **Garbage Collection**: `git gc` can remove unreachable commits

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

- **← Previous**: [Day 29 - Git Pull Request](./day-29.md)
- **Next →**: [Day 31 - Git Stash](../week-05/day-31.md)

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

