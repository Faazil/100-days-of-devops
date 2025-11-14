# Challenge 81: Jenkins Multistage Pipeline

## 📊 Metadata
- **Day**: 81
- **Week**: 12
- **Day in Week**: 4/7
- **Category**: Jenkins
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The development team of xFusionCorp Industries is working on to develop a new static website and they are planning to deploy the same on Nautilus App Servers using Jenkins pipeline. They have shared their requirements with the DevOps team and accordingly we need to create a Jenkins pipeline job. Please find below more details about the task:

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

Similarly, click on the Gitea button on the top bar to access the Gitea UI. Login using username sarah and password Sarah_pass123.

There is a repository named sarah/web in Gitea that is already cloned on Storage server under `/var/www/html` directory.

 1. Update the content of the file index.html under the same repository to **`Welcome to xFusionCorp Industries`** and push the changes to the origin into the master branch.

 2. Apache is already installed on all app Servers its running on port 8080.

 3. Create a Jenkins pipeline job named `deploy-job` (it must not be a Multibranch pipeline job) and pipeline should have two stages Deploy and Test ( names are case sensitive ). Configure these stages as per details mentioned below.

    a. The Deploy stage should deploy the code from web repository under `/var/www/html` on the Storage Server, as this location is already mounted to the document root `/var/www/html` of all app servers.

    b. The Test stage should just test if the app is working fine and website is accessible. Its up to you how you design this stage to test it out, you can simply add a curl command as well to run a curl against the LBR URL (`http://stlb01:8091`) to see if the website is working or not. Make sure this stage fails in case the website/app is not working or if the Deploy stage fails.

Click on the App button on the top bar to see the latest changes you deployed. Please make sure the required content is loading on the main URL `http://stlb01:8091` i.e there should not be a sub-directory like `http://stlb01:8091/web` etc.

Note:

- You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.

- For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.


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
- Day 77: Jenkins Deploy Pipeline (recommended)
- Day 78: Jenkins Conditional Pipeline (recommended)
- Day 80: Jenkins Chained Builds (recommended)

**Required Skills:**
- ✅ Create and configure Jenkins jobs
- ✅ Install and configure plugins
- ✅ Manage credentials securely
- ✅ Configure build parameters
- ✅ Set up build triggers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

0. Update plugins and restart jenkins
1. Install the following plugins
    - Pipeline
2. Add Storage Server credential:
    - Goto Manage Jenkins > Credentials > System > Global:
    - Add Credential > add username, password, and ID
3. Create the pipeline job:
    - job name: `deploy-job`
    - type: Pipeline
    - Jenkins Script: copy-paste contents from [this jenkins file](../files/jenkins-multistage-pipeline.jenkinsfile)

4. Login into gitea with sarah credential and update `index.html`

5. Build the job

## Good to Know?

### Multistage Pipelines

- **Stage Organization**: Logical grouping of related tasks
- **Sequential Execution**: Stages run in defined order
- **Failure Handling**: Pipeline stops on stage failure
- **Visual Representation**: Clear pipeline visualization

### Common Pipeline Stages

- **Checkout**: Retrieve source code
- **Build**: Compile and package application
- **Test**: Run automated tests
- **Deploy**: Deploy to target environment
- **Verify**: Post-deployment validation

### Stage Design Principles

- **Single Responsibility**: Each stage has one purpose
- **Fast Feedback**: Fail fast on errors
- **Idempotent**: Safe to run multiple times
- **Atomic**: Complete success or complete failure

### Testing Strategies

- **Unit Tests**: Test individual components
- **Integration Tests**: Test component interactions
- **Smoke Tests**: Basic functionality verification
- **Health Checks**: Verify application is running

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

- **← Previous**: [Day 80 - Jenkins Chained Builds](./day-80.md)
- **Next →**: [Day 82 - Create Ansible Inventory for App Server Testing](../week-12/day-82.md)

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

