# Challenge 68: Set Up Jenkins Server

## 📊 Metadata
- **Day**: 68
- **Week**: 10
- **Day in Week**: 5/7
- **Category**: Linux
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The DevOps team at xFusionCorp Industries is initiating the setup of CI/CD pipelines and has decided to utilize Jenkins as their server. Execute the task according to the provided requirements:

1. Install Jenkins on the jenkins server using the yum utility only, and start its service.
    - If you face a timeout issue while starting the Jenkins service, refer to [this](https://www.jenkins.io/doc/book/system-administration/systemd-services/#starting-services).
2. Jenkin's admin user name should be `theadmin`, password should be `Adm!n321`, full name should be `John` and email should be `john@jenkins.stratos.xfusioncorp.com`.

Note:

1. To access the jenkins server, connect from the jump host using the `root` user with the password `S3curePass`.

2. After Jenkins server installation, click the Jenkins button on the top bar to access the Jenkins UI and follow on-screen instructions to create an admin user.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `ssh`, `sudo`, `useradd`, `cat`, `grep`
- **Key Concepts**:
  - SSH remote access
  - User and group management
  - File permissions and ownership
  - Linux file system hierarchy

**Foundation from Earlier Challenges:**
- Day 56: Deploy Nginx Web Server on Kubernetes Cluster (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Login into jenkins server and find operating system

    ```bash
    ssh root@jenkins
    ```

    ```shell
     cat /etc/os-release 
    NAME="CentOS Stream"
    VERSION="9"
    ID="centos"
    ID_LIKE="rhel fedora"
    VERSION_ID="9"
    PLATFORM_ID="platform:el9"
    PRETTY_NAME="CentOS Stream 9"
    ANSI_COLOR="0;31"
    LOGO="fedora-logo-icon"
    CPE_NAME="cpe:/o:centos:centos:9"
    HOME_URL="https://centos.org/"
    BUG_REPORT_URL="https://issues.redhat.com/"
    REDHAT_SUPPORT_PRODUCT="Red Hat Enterprise Linux 9"
    REDHAT_SUPPORT_PRODUCT_VERSION="CentOS Stream"
    ```

    > We can see its' centos 9 os based server

2. Run the following command to update packages:

    ```sh
    yum update -y
    yum install -y wget
    ```

3. We will install jenkins for fedora with stable version, following this [[Documentation](https://www.jenkins.io/doc/book/installing/linux/#fedora-stable)]

    ```sh
    sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
    sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
    sudo dnf upgrade -y
    # Add required dependencies for the jenkins package
    sudo dnf install fontconfig java-21-openjdk -y
    sudo dnf install jenkins -y
    sudo systemctl daemon-reload
    ```

4. Start Jenkins server

    ```sh
    sudo systemctl enable --now jenkins
    ```

5. Copy the password:

    ```sh
    cat /var/lib/jenkins/secrets/initialAdminPassword
    ```

6. Login into Jenkins UI and Setup Jenkins

    - Paste the initial password
    - Install suggested plugins (it will take some time)
    - Continue (skil retry)
    - set: username, password, confirm password, full name and email
    - Save and Continue > Save and Finish
    - Start Jenkins
    - Done

## Good to Know?

### Jenkins Fundamentals

- **CI/CD**: Continuous Integration and Continuous Deployment
- **Automation**: Automate build, test, and deployment processes
- **Pipeline**: Series of automated steps for software delivery
- **Plugins**: Extend functionality with thousands of plugins

### Jenkins Architecture

- **Master Node**: Coordinates builds and manages configuration
- **Agent Nodes**: Execute build jobs (slaves)
- **Jobs**: Individual tasks or projects
- **Builds**: Execution instances of jobs

### Key Features

- **Pipeline as Code**: Define pipelines in Jenkinsfile
- **Distributed Builds**: Scale across multiple machines
- **Plugin Ecosystem**: Integrate with various tools
- **Web Interface**: User-friendly management console

### Installation Components

- **Java Runtime**: Required for Jenkins execution
- **Web Server**: Built-in Jetty server
- **User Management**: Authentication and authorization
- **Initial Setup**: Security configuration and plugin installation

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
- Practical application of Linux skills
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

- **← Previous**: [Day 67 - Deploy Guest Book App on Kubernetes](./day-67.md)
- **Next →**: [Day 69 - Install Jenkins Plugins](../week-10/day-69.md)

### Similar Challenges (Linux)
- [Day 70 - Configure Jenkins User Access](../week-10/day-70.md)

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

