# Challenge 80: Jenkins Chained Builds

## 📊 Metadata
- **Day**: 80
- **Week**: 12
- **Day in Week**: 3/7
- **Category**: Jenkins
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The DevOps team was looking for a solution where they want to restart Apache service on all app servers if the deployment goes fine on these servers in Stratos Datacenter. After having a discussion, they came up with a solution to use Jenkins chained builds so that they can use a downstream job for services which should only be triggered by the deployment job. So as per the requirements mentioned below configure the required Jenkins jobs.

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and Adm!n321 password.

Similarly you can access Gitea UI on port 8090 and username and password for Git is sarah and Sarah_pass123 respectively. Under user sarah you will find a repository named web.

Apache is already installed and configured on all app server so no changes are needed there. The doc root /var/www/html on all these app servers is shared among the Storage server under /var/www/html directory.

1. Create a Jenkins job named `nautilus-app-deployment` and configure it to pull change from the master branch of web repository on `Storage server` under `/var/www/html` directory, which is already a local git repository tracking the origin web repository. Since /var/www/html on Storage server is a shared volume so changes should auto reflect on all apps.

2. Create another Jenkins job named `manage-services` and make it a downstream job for `nautilus-app-deployment` job. Things to take care about this job are:

    - This job should restart `httpd` service on all app servers.

    - Trigger this job only if the upstream job i.e `nautilus-app-deployment` is stable.

LB server is already configured. Click on the App button on the top bar to access the app. You should be able to see the latest changes you made. Please make sure the required content is loading on the main URL `https://<LBR-URL>` i.e there should not be a sub-directory like `https://<LBR-URL>/web` etc.

Note:

1. You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also some times Jenkins UI gets stuck when Jenkins service restarts in the back end so in such case please make sure to refresh the UI page.

2. Make sure Jenkins job passes even on repetitive runs as validation may try to build the job multiple times.

3. Deployment related tasks should be done by sudo user on the destination server to avoid any permission issues so make sure to configure your Jenkins job accordingly.

4. For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

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
- Day 76: Jenkins Project Security (recommended)
- Day 77: Jenkins Deploy Pipeline (recommended)
- Day 78: Jenkins Conditional Pipeline (recommended)

**Required Skills:**
- ✅ Create and configure Jenkins jobs
- ✅ Install and configure plugins
- ✅ Manage credentials securely
- ✅ Configure build parameters
- ✅ Set up build triggers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Update plugins and restart jenkins
2. Install following plugins
    - Git
    - Publish Over SSH
3. Add SSH Server, Goto Manage Jenkins > System > SSH Servers > Add Servers:
    Add all 3 app servers with name, hostname, username and password

4. Create primary deployment JOb:
    - Job Name: `nautilus-app-deployment`
    - Type: Freestyle Project
    - SCM: GIT
        - Add Repository URL
    - Build Steps:
        - Shell Execute, and add this line:

        ```sh
        sshpass -p "Bl@kW" scp -r -o StrictHostKeyChecking=no ./* natasha@ststor01:/var/www/html
        ```

5. Create Another Job: manage-services
    - job name: `manage-services`
    - Build Steps: create 3 build steps of `Send or Execute shell over the SSH`
        - For each build step, select each app servers and execution command:

        ```sh
        echo 'app-server-password' | sudo -S systemctl restart httpd
        ```

6. Goto `nautilus-app-deployment` job and add post build action:
    ![post-action](../screenshots/jenkins-post-build-action.png)

7. Now build `nautilus-app-deployment` job, once it build successfully manage-services will start building automatically.

8. Reload app link

## Good to Know?

### Chained Builds

- **Upstream/Downstream**: Jobs trigger other jobs
- **Build Pipeline**: Sequence of related jobs
- **Conditional Triggers**: Trigger based on upstream success
- **Parallel Execution**: Run multiple downstream jobs

### Build Dependencies

- **Sequential Execution**: Jobs run in specific order
- **Dependency Management**: Handle job dependencies
- **Failure Handling**: Stop pipeline on upstream failure
- **Status Propagation**: Pass build status downstream

### Post-Build Actions

- **Trigger Builds**: Start downstream jobs
- **Archive Artifacts**: Save build outputs
- **Send Notifications**: Email, Slack notifications
- **Publish Results**: Test results, coverage reports

### Pipeline Benefits

- **Separation of Concerns**: Each job has specific purpose
- **Reusability**: Downstream jobs can be reused
- **Parallel Processing**: Independent tasks run in parallel
- **Failure Isolation**: Isolate failures to specific stages

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

- **← Previous**: [Day 79 - Jenkins Deployment Job](./day-79.md)
- **Next →**: [Day 81 - Jenkins Multistage Pipeline](../week-12/day-81.md)

### Similar Challenges (Jenkins)
- [Day 71 - Configure Jenkins Job for Package Installation](../week-11/day-71.md)
- [Day 72 - Jenkins Parameterized Builds](../week-11/day-72.md)
- [Day 73 - Jenkins Scheduled Jobs](../week-11/day-73.md)

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

