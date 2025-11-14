# Challenge 79: Jenkins Deployment Job

## 📊 Metadata
- **Day**: 79
- **Week**: 12
- **Day in Week**: 2/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus development team had a meeting with the DevOps team where they discussed automating the deployment of one of their apps using Jenkins (the one in Stratos Datacenter). They want to auto deploy the new changes in case any developer pushes to the repository. As per the requirements mentioned below configure the required Jenkins job.

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and Adm!n321 password.

Similarly, you can access the Gitea UI using Gitea button, username and password for Git is `sarah` and `Sarah_pass123` respectively. Under user sarah you will find a repository named web that is already cloned on the Storage server under sarah's home. sarah is a developer who is working on this repository.

1. Install `httpd` (whatever version is available in the yum repo by default) and configure it to serve on port `8080` on All app servers. You can make it part of your Jenkins job or you can do this step manually on all app servers.

2. Create a Jenkins job named `nautilus-app-deployment` and configure it in a way so that if anyone pushes any new change to the origin repository in master branch, the job should auto build and deploy the latest code on the `Storage server` under `/var/www/html` directory. Since `/var/www/html` on Storage server is shared among all apps. Before deployment, ensure that the ownership of the `/var/www/html` directory is set to user `sarah`, so that Jenkins can successfully deploy files to that directory.

3. SSH into Storage Server using sarah user credentials mentioned above. Under sarah user's home you will find a cloned Git repository named web. Under this repository there is an index.html file, update its content to `Welcome to the xFusionCorp Industries`, then push the changes to the origin into master branch. This push must trigger your Jenkins job and the latest changes must be deployed on the servers, also make sure it deploys the entire repository content not only index.html file.

Click on the App button on the top bar to access the app, you should be able to see the latest changes you deployed. Please make sure the required content is loading on the main URL `https://<LBR-URL>` i.e there should not be any sub-directory like `https://<LBR-URL>/web` etc.

Note:

1. You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also some times Jenkins UI gets stuck when Jenkins service restarts in the back end so in such case please make sure to refresh the UI page.

2. Make sure Jenkins job passes even on repetitive runs as validation may try to build the job multiple times.

3. Deployment related tasks should be done by sudo user on the destination server to avoid any permission issues so make sure to configure your Jenkins job accordingly.

4. For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Kubernetes cluster with kubectl configured
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `kubectl`, `kubectl apply`, `kubectl get`, `kubectl describe`, `kubectl logs`
- **Key Concepts**:
  - Kubernetes resources (Pods, Deployments, Services)
  - YAML manifest structure
  - Resource requests and limits
  - Labels and selectors
- **File Formats**: YAML syntax and structure
- **Environment**: kubectl configured to access Kubernetes cluster

**Foundation from Earlier Challenges:**
- Day 65: Deploy Redis Deployment on Kubernetes (recommended)
- Day 66: Deploy MySQL on Kubernetes (recommended)
- Day 67: Deploy Guest Book App on Kubernetes (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

0. Upgrade Jenkins plugins and Restart Jenkins
1. Install Required Plugin
    - SSH Pipeline Steps
    - Gitea
    - Pipeline

    > restart and try again if it fails to install

2. Add storage server credentials
3. Create a pipeline job to install package:
    - Add parameters: HOSTNAME, USER, PASSWORD, PACKAGE
    - Pipeline script: copy-paste this [jenkins File](../files/jenkins_httpd_installation_job.jenkinsfile)
    - Run for each app server

    > It will install httpd package on each server and replace port 80 to 8080.You may need to repalce port here.

    ![httpd](../screenshots/jenkins_httpd_installation_job.png)

4. Go to Manage Jenkins > System > Gitea Servers:
    - Add Gitea server
    - name: gitea, url: gitea
5. Create api token:
    - Manage Jenkins > Users > Admin > Security
    - Generate API Token
    - Copy token

6. Create a freestyle job for deployment:
    - name: `nautilus-app-deployment`
    - Trigger: Build trigger remotely:
        - BUILD TOKEN: `kodekloud`, anything you like
    - Build Steps:

        ```sh
        rm -rf web
        git clone repo-url 
        cd web
        sshpass -p "storage-server-pass" scp -r -o StrictHostKeyChecking=no ./* natasha@ststor01:/var/www/html
        ```

7. Login into gitea

    - Repo > Settings > webhooks:
    - Target URL: `https://admin:api-token@jenkins-url/job/nautilus-app-deployment/build?token=kodekloud`
    - Example: `https://admin:11a3bafd516952ecf4b9103a02348f653c@8080-port-3c6aqh4fy2nkx3vf.labs.kodekloud.com/job/nautilus-app-deployment/build?token=kodekloud`
    - Save and Test Delivery
    ![gitea](../screenshots/jenkins-gitea-webhook.png)
8. Login into storage server:
    - Give permission to natasha:

    ```sh
    sudo chown -R natasha:natasha /var/www/html
    ```

    - Switch user sarah

    ```sh
    sudo su sarah
    cd /home/sarah/web
    ```

    - Modify index.html and push

## Good to Know?

### Webhook-Triggered Deployments

- **Automatic Triggers**: Deploy on code changes
- **Git Hooks**: Repository events trigger builds
- **Continuous Deployment**: Automated deployment pipeline
- **Event-driven**: React to repository events

### Webhook Configuration

- **Payload URL**: Jenkins endpoint for webhook
- **Authentication**: Secure webhook with tokens
- **Event Types**: Push, pull request, tag events
- **Filtering**: Trigger only on specific branches

### CI/CD Pipeline

- **Source Control**: Monitor repository for changes
- **Build**: Compile and test application
- **Deploy**: Deploy to target environment
- **Notify**: Send deployment notifications

### Security Considerations

- **API Tokens**: Secure Jenkins API access
- **Network Security**: Restrict webhook sources
- **Credential Management**: Secure storage of secrets
- **Audit Logging**: Track deployment activities

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
- Practical application of Kubernetes skills
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

- **← Previous**: [Day 78 - Jenkins Conditional Pipeline](./day-78.md)
- **Next →**: [Day 80 - Jenkins Chained Builds](../week-12/day-80.md)

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

