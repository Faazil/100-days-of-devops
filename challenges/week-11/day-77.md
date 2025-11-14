# Challenge 77: Jenkins Deploy Pipeline

## 📊 Metadata
- **Day**: 77
- **Week**: 11
- **Day in Week**: 7/7
- **Category**: Jenkins
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The development team of xFusionCorp Industries is working on to develop a new static website and they are planning to deploy the same on Nautilus App Servers using Jenkins pipeline. They have shared their requirements with the DevOps team and accordingly we need to create a Jenkins pipeline job. Please find below more details about the task:

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username `admin` and password `Adm!n321`.

Similarly, click on the Gitea button on the top bar to access the Gitea UI. Login using username `sarah` and password `Sarah_pass123`. There under user sarah you will find a repository named `web_app` that is already cloned on `Storage server` under `/var/www/html`. sarah is a developer who is working on this repository.

1. Add a slave node named `Storage Server`. It should be labeled as `ststor01` and its remote root directory should be `/var/www/html`.

2. We have already cloned repository on Storage Server under `/var/www/html`.

3. `Apache` is already installed on all app Servers its running on port `8080`.

4. Create a Jenkins pipeline job named `datacenter-webapp-job` (it must not be a Multibranch pipeline) and configure it to:

    - Deploy the code from web_app repository under /var/www/html on Storage Server, as this location is already mounted to the document root /var/www/html of app servers. The pipeline should have a single stage named Deploy ( which is case sensitive ) to accomplish the deployment.

LB server is already configured. You should be able to see the latest changes you made by clicking on the App button. Please make sure the required content is loading on the main URL `https://<LBR-URL>` i.e there should not be a sub-directory like `https://<LBR-URL>/web_app` etc.

Note:

- You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.

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
- Day 74: Jenkins Database Backup Job (recommended)
- Day 75: Jenkins Slave Nodes (recommended)
- Day 76: Jenkins Project Security (recommended)

**Required Skills:**
- ✅ Create and configure Jenkins jobs
- ✅ Install and configure plugins
- ✅ Manage credentials securely
- ✅ Configure build parameters
- ✅ Set up build triggers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

0. Login into Storage server and install java

    ```sh
    sudo yum install java-21-openjdk -y
    ```

    > Add the permission of `/var/www/html` directory:  # "Perform this step before creating  "Storage server" Agent, as it prevents the error: 'This agent is offline because Jenkins failed to launch the agent process on it.'

    ```sh
    sudo chown -R natasha:natasha /var/www/html
    ```

1. Update plugins and restart jenkins
2. Install following plugins:
    - SSH Build Agent
    - Pipeline
3. Add storage server credential; Manage Jenkins > Credentials > System > Global > Add credentials:
    - username: `natasha`
    - Password: `Bl@kW`
    - ID: `ststor01`
4. Add agent:
    - name: `Storage Server`
    - remote dir: `/var/www/html`
    - label: `ststor01`
    - Launch Method: `SSH`
        - host: ststor01
        - credential: `natasha/pass`
        - host key: no verification
    - Save

5. Create a jenkins pipeline job:
    - name: `datacenter-webapp-job`
    - type: pipeline
    - Build steps: pipeline script
    - Add this pipeline script: [jenkins-pipeline-deploy.jenkinsfile](../files/jenkins-pipeline-deploy-077.jenkinsfile)

6. Build

## Good to Know?

### Jenkins Pipelines

- **Pipeline as Code**: Define build process in code
- **Version Control**: Store pipeline definitions in SCM
- **Declarative**: Structured, easy-to-read syntax
- **Scripted**: Flexible, Groovy-based syntax

### Pipeline Components

- **Stages**: Logical groupings of steps
- **Steps**: Individual actions (shell, git, etc.)
- **Agents**: Where pipeline executes
- **Post Actions**: Cleanup and notifications

### Deployment Pipelines

- **Source Control**: Pull code from repository
- **Build**: Compile and package application
- **Test**: Run automated tests
- **Deploy**: Deploy to target environment

### Best Practices

- **Modular Stages**: Break pipeline into logical stages
- **Error Handling**: Proper error handling and notifications
- **Parallel Execution**: Run independent tasks in parallel
- **Shared Libraries**: Reuse common pipeline code

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

- **← Previous**: [Day 76 - Jenkins Project Security](./day-76.md)
- **Next →**: [Day 78 - Jenkins Conditional Pipeline](../week-12/day-78.md)

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

