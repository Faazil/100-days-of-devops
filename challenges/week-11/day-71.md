# Challenge 71: Configure Jenkins Job for Package Installation

## 📊 Metadata
- **Day**: 71
- **Week**: 11
- **Day in Week**: 1/7
- **Category**: Jenkins
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

Some new requirements have come up to install and configure some packages on the Nautilus infrastructure under Stratos Datacenter. The Nautilus DevOps team installed and configured a new Jenkins server so they wanted to create a Jenkins job to automate this task. Find below more details and complete the task accordingly:

1. Access the Jenkins UI by clicking on the Jenkins button in the top bar. Log in using the credentials: username `admin` and password `Adm!n321`.

2. Create a new Jenkins job named `install-packages` and configure it with the following specifications:

    - Add a string parameter named `PACKAGE`.
    - Configure the job to install a package specified in the `$PACKAGE` parameter on the **`storage server`** within the `Stratos Datacenter`.

Note:

1. Ensure to install any required plugins and restart the Jenkins service if necessary. Opt for `Restart Jenkins when installation is complete and no jobs are running` on the plugin installation/update page. Refresh the UI page if needed after restarting the service.

2. Verify that the Jenkins job runs successfully on repeated executions to ensure reliability.

3. Capture screenshots of your configuration for documentation and review purposes. Alternatively, use screen recording software like loom.com for comprehensive documentation and sharing.


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
- Day 69: Install Jenkins Plugins (recommended)

**Required Skills:**
- ✅ Create and configure Jenkins jobs
- ✅ Install and configure plugins
- ✅ Manage credentials securely
- ✅ Configure build parameters
- ✅ Set up build triggers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

0. Update Plugins and Restart

1. Let's install the following plugins

    - SSH
    - SSH Credentials
    - SSH Build Agent

2. Find the Nautilus Storage Server Details from [this page](https://kodekloudhub.github.io/kodekloud-engineer/docs/projects/nautilus#infrastructure-details)

3. Go to Manage Jenkins > Credentials > System > Global credentials and Add credentials
![credential](../screenshots/add-credentials-jenkins.png)

4. Go to Manage Jenkins > System  and Add SSH sites under SSH remote Posts
![ssh-remote-hosts](../screenshots/add-ssh-remote-host.png)

5. Create a freestyle job `install-packages` with following configs

    - Add Parameter "PACKAGE"
    ![parameterized](../screenshots/jenkins-parameterized.png)

    - Build Steps
    Choose `Execute shell script on remote host using ssh`
    ![shell-execute](../screenshots/execute-shell-script.png)

    - Apply and Save

6. To execute: Dashboard > install-packages > Build with Parameters

    ![build-with-parameter](../screenshots/build-with-parameter-jenkins.png)

    - Execute
    ![job execute](../screenshots/jenkins-job-execution.png)

## Good to Know?

### Jenkins Remote Execution

- **SSH Plugin**: Execute commands on remote servers via SSH
- **Credentials Management**: Secure storage of SSH credentials
- **Remote Hosts**: Configure target servers for execution
- **Parameterized Jobs**: Dynamic job configuration with parameters

### SSH Configuration

- **Host Key Verification**: Disable for automation (security consideration)
- **Authentication**: Username/password or SSH key-based
- **Connection Pooling**: Reuse SSH connections for efficiency
- **Timeout Settings**: Configure connection and execution timeouts

### Package Management Automation

- **Remote Installation**: Install packages on multiple servers
- **Idempotent Operations**: Safe to run multiple times
- **Error Handling**: Proper error reporting and handling
- **Logging**: Capture installation logs for troubleshooting

### Best Practices

- **Credential Security**: Use Jenkins credential store
- **Parameter Validation**: Validate user inputs
- **Error Recovery**: Handle network and execution failures
- **Audit Trail**: Log all remote operations

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

- **← Previous**: [Day 70 - Configure Jenkins User Access](./day-70.md)
- **Next →**: [Day 72 - Jenkins Parameterized Builds](../week-11/day-72.md)

### Similar Challenges (Jenkins)
- [Day 69 - Install Jenkins Plugins](../week-10/day-69.md)
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

