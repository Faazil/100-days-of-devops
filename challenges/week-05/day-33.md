# Challenge 33: Git Merge Conflict Resolve

## 📊 Metadata
- **Day**: 33
- **Week**: 5
- **Day in Week**: 5/7
- **Category**: Git
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

Sarah and Max were working on writting some stories which they have pushed to the repository. Max has recently added some new changes and is trying to push them to the repository but he is facing some issues. Below you can find more details:

- SSH into storage server using user max and password Max_pass123. Under /home/max you will find the story-blog repository. Try to push the changes to the origin repo and fix the issues. The story-index.txt must have titles for all 4 stories. Additionally, there is a typo in The Lion and the Mooose line where Mooose should be Mouse.

- Click on the Gitea UI button on the top bar. You should be able to access the Gitea page. You may login to Gitea server from UI using username sarah and password Sarah_pass123 or username max and password Max_pass123.

*Note: For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.*


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
- Day 30: Git Reset Hard (recommended)
- Day 31: Git Stash (recommended)
- Day 32: Git Rebase (recommended)

**Required Skills:**
- ✅ Initialize and clone repositories
- ✅ Create commits with meaningful messages
- ✅ Manage branches effectively
- ✅ Push and pull from remotes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Access storage server
2. Update the remote changes

    ```sh
    git fetch origin
    ```

3. Rebase

    ```sh
    git rebase origin/main

    git add .

    git rebase --continue
    ```

4. Push

    ```sh
    git push
    ```

## Good to Know?

### Merge Conflicts

- **Cause**: Same lines modified in different branches
- **Detection**: Git cannot automatically resolve differences
- **Manual Resolution**: Developer must choose which changes to keep
- **Common Scenarios**: Concurrent edits, file renames, deletions

### Conflict Markers

- **HEAD Section**: `<<<<<<< HEAD` - Current branch changes
- **Separator**: `=======` - Divides conflicting sections
- **Incoming**: `>>>>>>> branch-name` - Changes from other branch
- **Resolution**: Remove markers and choose desired content

### Resolution Process

1. **Identify Conflicts**: Git marks conflicted files
2. **Edit Files**: Manually resolve conflicts
3. **Stage Changes**: `git add` resolved files
4. **Continue**: `git rebase --continue` or commit merge
5. **Test**: Verify resolution works correctly

### Prevention Strategies

- **Frequent Pulls**: Stay updated with remote changes
- **Small Commits**: Reduce conflict probability
- **Communication**: Coordinate with team on file changes
- **Feature Branches**: Isolate work to minimize conflicts

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

- **← Previous**: [Day 32 - Git Rebase](./day-32.md)
- **Next →**: [Day 34 - Configure Git Hook](../week-05/day-34.md)

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
**Difficulty**: ⭐
**Category**: DevOps

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
```

