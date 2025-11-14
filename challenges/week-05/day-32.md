# Challenge 32: Git Rebase

## 📊 Metadata
- **Day**: 32
- **Week**: 5
- **Day in Week**: 4/7
- **Category**: Git
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus application development team has been working on a project repository /opt/games.git. This repo is cloned at /usr/src/kodekloudrepos on storage server in Stratos DC. They recently shared the following requirements with DevOps team:

> One of the developers is working on feature branch and their work is still in progress, however there are some changes which have been pushed into the master branch, the developer now wants to rebase the feature branch with the master branch without loosing any data from the feature branch, also they don't want to add any merge commit by simply merging the master branch into the feature branch. Accomplish this task as per requirements mentioned.

- Also remember to push your changes once done.


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
- Day 29: Git Pull Request (recommended)
- Day 30: Git Reset Hard (recommended)
- Day 31: Git Stash (recommended)

**Required Skills:**
- ✅ Initialize and clone repositories
- ✅ Create commits with meaningful messages
- ✅ Manage branches effectively
- ✅ Push and pull from remotes

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Login into storage server and move into repository

    ```sh
    sudo -i
    cd /usr/src/kodekloudrepos/games
    ```

2. Be confirmed that we are in `feature` branch

    ```sh
    git branch
    ```

3. Rebase master branch

    ```sh
    git rebase master
    ```

4. Push feature branch

    ```sh
    git push --force --set-upstream origin feature
    ```

## Good to Know?

### Rebase vs Merge

- **Rebase**: Replays commits on top of target branch (linear history)
- **Merge**: Combines branches with merge commit (preserves context)
- **History**: Rebase creates cleaner, linear history
- **Traceability**: Merge preserves original branch structure

### Rebase Benefits

- **Clean History**: Linear commit sequence
- **No Merge Commits**: Avoids cluttered merge commits
- **Easier Bisect**: Simpler to find bugs with git bisect
- **Professional**: Cleaner project history

### Rebase Risks

- **Shared Branches**: Never rebase published commits
- **Force Push**: Required after rebasing pushed commits
- **Conflicts**: May need to resolve conflicts multiple times
- **Lost Context**: Loses information about when branches diverged

### Interactive Rebase

- **Edit History**: `git rebase -i HEAD~n`
- **Squash**: Combine multiple commits
- **Reword**: Change commit messages
- **Reorder**: Change commit sequence
- **Drop**: Remove commits entirely

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

- **← Previous**: [Day 31 - Git Stash](./day-31.md)
- **Next →**: [Day 33 - Git Merge Conflict Resolve](../week-05/day-33.md)

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

