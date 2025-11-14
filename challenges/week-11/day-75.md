# Challenge 75: Jenkins Slave Nodes

## 📊 Metadata
- **Day**: 75
- **Week**: 11
- **Day in Week**: 5/7
- **Category**: Jenkins
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team has installed and configured new Jenkins server in Stratos DC which they will use for CI/CD and for some automation tasks. There is a requirement to add all app servers as slave nodes in Jenkins so that they can perform tasks on these servers using Jenkins. Find below more details and accomplish the task accordingly.

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

1. Add all app servers as SSH build agent/slave nodes in Jenkins. Slave node name for app server 1, app server 2 and app server 3 must be App_server_1, App_server_2, App_server_3 respectively.

2. Add labels as below:
  
   - App_server_1 : stapp01
   - App_server_2 : stapp02
   - App_server_3 : stapp03

3. Remote root directory for
   - App_server_1 must be `/home/tony/jenkins`,
   - App_server_2 must be `/home/steve/jenkins` and
   - App_server_3 must be `/home/banner/jenkins`.

4. Make sure slave nodes are online and working properly.

Note:

1. You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.

2. For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.


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
- Day 72: Jenkins Parameterized Builds (recommended)
- Day 73: Jenkins Scheduled Jobs (recommended)
- Day 74: Jenkins Database Backup Job (recommended)

**Required Skills:**
- ✅ Create and configure Jenkins jobs
- ✅ Install and configure plugins
- ✅ Manage credentials securely
- ✅ Configure build parameters
- ✅ Set up build triggers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

0. Update plugins and restart
1. Install the following plugins
    - SSH Build Agents
2. Add Credentials for three nodes
3. Add all three slave node following this way: `Manage Jenkins > Credentials > System > Global Credentials > Add Credentials`
   - username
   - password
   - ID

4. Login into each App Server and install java

   ```sh
   sudo yum install java-21-openjdk -y
   ```

5. Add Agent Nodes: Manage Jenkins > Nodes > Create an Agent Node:

   - label
   - Remote Directory
   - Launch Method: Launch Agent via SSH
      - Host
      - Credentials

6. Create a freestyle job: `testNode`:

   - Restrict where to run this job
   - select node label
   - Add execute shell as build step
   - paste these sample lines:

   ```sh
   echo "Hello from Agent"
   pwd
   echo $USER
   ```

7. Build job, it should be successfull

## Good to Know?

### Jenkins Distributed Builds

- **Master-Slave Architecture**: Master coordinates, slaves execute
- **Scalability**: Distribute build load across multiple machines
- **Isolation**: Separate build environments
- **Resource Optimization**: Use appropriate hardware for different tasks

### Build Agents (Slaves)

- **SSH Agents**: Connect via SSH protocol
- **JNLP Agents**: Java Web Start agents
- **Docker Agents**: Containerized build environments
- **Cloud Agents**: Dynamic agents in cloud platforms

### Agent Configuration

- **Labels**: Tag agents for specific job requirements
- **Remote Directory**: Workspace location on agent
- **Executors**: Number of concurrent builds per agent
- **Node Properties**: Environment variables and tools

### Benefits

- **Parallel Execution**: Run multiple builds simultaneously
- **Environment Diversity**: Different OS, tools, configurations
- **Load Distribution**: Prevent master overload
- **Fault Tolerance**: Continue builds if some agents fail

## Youtube Video

Watch the video tutorial here: [https://youtu.be/KILDE85z8iw](https://youtu.be/KILDE85z8iw)

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

- **← Previous**: [Day 74 - Jenkins Database Backup Job](./day-74.md)
- **Next →**: [Day 76 - Jenkins Project Security](../week-11/day-76.md)

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
**Difficulty**: ⭐
**Category**: DevOps

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
```

