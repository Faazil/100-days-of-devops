# Challenge 10: Create a BASH Script

## 📊 Metadata
- **Day**: 10
- **Week**: 2
- **Day in Week**: 3/7
- **Category**: DevOps
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The production support team of `xFusionCorp Industries` is working on developing some bash scripts to automate different day to day tasks. One is to create a bash script for taking websites backup. They have a static website running on `App Server 3` in Stratos Datacenter, and they need to create a bash script named `beta_backup.sh` which should accomplish the following tasks. (Also remember to place the script under `/scripts` directory on `App Server 3`).

- Create a zip archive named `xfusioncorp_beta.zip` of `/var/www/html/beta` directory.
- Save the archive in `/backup/` on `App Server 3`. This is a temporary storage, as backups from this location will be clean on weekly basis. Therefore, we also need to save this backup archive on Nautilus Backup Server.
- Copy the created archive to Nautilus Backup Server server in `/backup/` location.
- Please make sure script won't ask for **password** while copying the archive file. Additionally, the respective server user (for example, tony in case of App Server 1) must be able to run it.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Key Concepts**:
  - DevOps workflow and principles
  - CI/CD pipeline concepts
  - Automation strategies
  - Infrastructure management

**Foundation from Earlier Challenges:**
- Day 4: Script Execute Permissions (recommended)

**Required Skills:**
- ✅ Understand DevOps methodologies
- ✅ Integrate multiple tools
- ✅ Implement automation workflows

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Login into app server 3 and generate ssh-key:
2. Copy ssh-pub key to backup server. Follow [day 07](./007.md) to complete these two steps
3. Write the following script in `/scripts/beta_backup.sh`:

    ```sh
    #!/bin/sh

    zip -r /backup/xfusioncorp_beta.zip /var/www/html/beta
    scp /backup/xfusioncorp_beta.zip clint@stbkp01:/backup/
    ```

4. Give the execute permission:

    ```sh
    chmod +x /scripts/beta_backup.sh
    ```

## Good to Know?

### Bash Scripting Best Practices

- **Shebang**: Always start with `#!/bin/bash` or `#!/bin/sh`
- **Error Handling**: Use `set -e` to exit on errors
- **Variables**: Quote variables: `"$variable"` to prevent word splitting
- **Functions**: Break complex logic into reusable functions

### Backup Strategies

- **Full Backup**: Complete copy of all data
- **Incremental**: Only changed files since last backup
- **Differential**: Changed files since last full backup
- **Compression**: Use zip, tar.gz to save space

### Archive Commands

- **zip**: `zip -r archive.zip directory/` (cross-platform)
- **tar**: `tar -czf archive.tar.gz directory/` (Unix standard)
- **Exclusions**: Skip temporary files and logs
- **Verification**: Test archives before relying on them

### Remote Copy Methods

- **scp**: Secure copy over SSH
- **rsync**: Efficient synchronization tool
- **sftp**: Interactive file transfer
- **Authentication**: Use SSH keys for automation

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
- Practical application of DevOps skills
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

- **← Previous**: [Day 9 - Debugging MariaDB Issues](./day-09.md)
- **Next →**: [Day 11 - Install and Setup Tomcat Server](../week-02/day-11.md)

### Similar Challenges (DevOps)
- [Day 4 - Script Execute Permissions](../week-01/day-04.md)
- [Day 13 - IPtables Installation And Configuration](../week-02/day-13.md)
- [Day 19 - Install and Configure Web Application](../week-03/day-19.md)

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

