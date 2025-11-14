# Challenge 74: Jenkins Database Backup Job

## 📊 Metadata
- **Day**: 74
- **Week**: 11
- **Day in Week**: 4/7
- **Category**: Jenkins
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

There is a requirement to create a Jenkins job to automate the database backup. Below you can find more details to accomplish this task:

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

1. Create a Jenkins job named `database-backup`.

2. Configure it to take a database dump of the `kodekloud_db01` database present on the `Database server` in `Stratos Datacenter`, the database user is `kodekloud_roy` and password is `asdfgdsd`.

3. The dump should be named in `db_$(date +%F).sql` format, where date `+%F` is the current date.

4. Copy the `db_$(date +%F).sql` dump to the Backup Server under location `/home/clint/db_backups`.

5. Further, schedule this job to run periodically at `*/10 * * * *`(please use this exact schedule format).

Note:

- You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case please make sure to refresh the UI page.

- Please make sure to define you cron expression like this `*/10 * * * *` (this is just an example to run job every 10 minutes).

- For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Jenkins server with admin access
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Key Concepts**:
  - Jenkins UI navigation
  - Job configuration (Freestyle, Pipeline)
  - Plugin installation and management
  - Build triggers and scheduling
- **Environment**: Access to Jenkins server
- **Access**: Jenkins admin credentials

**Foundation from Earlier Challenges:**
- Day 71: Configure Jenkins Job for Package Installation (recommended)
- Day 72: Jenkins Parameterized Builds (recommended)
- Day 73: Jenkins Scheduled Jobs (recommended)

**Required Skills:**
- ✅ Create and configure Jenkins jobs
- ✅ Install and configure plugins
- ✅ Manage credentials securely
- ✅ Configure build parameters
- ✅ Set up build triggers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

0. Update plugins and restart jenkins
1. Install the following plugin
    - SSH Credential
    - Publish Over SSH
2. Go to Manage Jenkins > System > Add SSH servers > Apply:

    ![ssh-servers](../screenshots/jenkins-add-ssh-servers.png)

3. Create a freestyle job named: `database-backup`:

    - Check build periodically and add this cron job: `*/10 * * * *`
    - Add build step > Send files or execute commands over ssh > add this lines in execute command:

    ```sh
    mkdir -p /tmp/db-backup
    mysqldump -u kodekloud_roy -p'asdfgdsd' kodekloud_db01 > /tmp/db-backup/db_$(date +%F).sql

    ls -la
    sudo apt install sshpass -y

    sshpass -p 'H@wk3y3' scp -o StrictHostKeyChecking=no /tmp/db-backup/*.sql clint@stbkp01:/home/clint/db_backups

    rm -rf /tmp/db-backup
    ```

    > It will create dump, transfer to backup and remove the backup from db server

4. Build job

## Good to Know?

### Database Backup Automation

- **Regular Backups**: Scheduled database dumps for data protection
- **Disaster Recovery**: Quick recovery from data loss
- **Point-in-time Recovery**: Restore to specific time
- **Compliance**: Meet data retention requirements

### MySQL Backup Tools

- **mysqldump**: Logical backup tool (SQL statements)
- **mysqlpump**: Parallel backup utility
- **Percona XtraBackup**: Physical backup tool
- **Binary Logs**: Point-in-time recovery capability

### Backup Best Practices

- **Consistent Naming**: Use timestamps in backup filenames
- **Remote Storage**: Store backups on separate servers
- **Compression**: Reduce backup file size
- **Encryption**: Encrypt sensitive database backups
- **Testing**: Regularly test backup restoration

### Jenkins Backup Jobs

- **Scheduled Execution**: Automated backup scheduling
- **Error Handling**: Notification on backup failures
- **Retention Policy**: Automatic cleanup of old backups
- **Monitoring**: Track backup success and file sizes

## Youtube Video

Watch the video tutorial: [https://youtu.be/KDHXdmdH0nM](https://youtu.be/KDHXdmdH0nM)

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
- Practical application of Jenkins skills
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

- **← Previous**: [Day 73 - Jenkins Scheduled Jobs](./day-73.md)
- **Next →**: [Day 75 - Jenkins Slave Nodes](../week-11/day-75.md)

### Similar Challenges (Jenkins)
- [Day 69 - Install Jenkins Plugins](../week-10/day-69.md)
- [Day 71 - Configure Jenkins Job for Package Installation](../week-11/day-71.md)
- [Day 72 - Jenkins Parameterized Builds](../week-11/day-72.md)

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

