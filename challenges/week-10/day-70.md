# Challenge 70: Configure Jenkins User Access

## 📊 Metadata
- **Day**: 70
- **Week**: 10
- **Day in Week**: 7/7
- **Category**: Linux
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus team is integrating Jenkins into their CI/CD pipelines. After setting up a new Jenkins server, they're now configuring user access for the development team, Follow these steps:

1. Click on the Jenkins button on the top bar to access the Jenkins UI. Login with username `admin` and password `Adm!n321`.

2. Create a jenkins user named `mark` with the password `Rc5C9EyvbU`. Their full name should match `Mark`.

3. Utilize the `Project-based Matrix Authorization Strategy` to assign `overall read` permission to the `mark` user.

4. Remove all permissions for `Anonymous` users (if any) ensuring that the `admin` user retains overall `Administer` permissions.

5. For the existing job, grant `mark` user only `read` permissions, disregarding other permissions such as Agent, SCM etc.

Note:

1. You may need to install plugins and restart Jenkins service. After plugins installation, select Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page.

2. After restarting the Jenkins service, wait for the Jenkins login page to reappear before proceeding. Avoid clicking Finish immediately after restarting the service.

3. Capture screenshots of your configuration for review purposes. Consider using screen recording software like loom.com for documentation and sharing.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

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
- Day 68: Set Up Jenkins Server (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Update required plugins and restart jenkins (check [this](./069.md))
2. Manage Jenkins > Users > Create user > set username, full name, password to create user
3. Manage Jenkins > Plugins > Available Plugins > Search Matrix Authorization Strategy > Install it > restart jenkins
4. Manage Jenkins > Security > Authorization > Select Project-based Matrix authorization Strategy > Update permission like below > save and apply

    ![matrix-authorization-strategy](../screenshots/project-based-matrix-authorization-strategy-jenkins.png)

5. Dashboard > HelloWorld > Configuration > Enable Project-based security > add user `mark` > give only read permission > Save and Apply

    ![hello-world-security](../screenshots/project-based-security-jenkins.png)

## Good to Know?

### Jenkins Security Model

- **Authentication**: Verify user identity (who you are)
- **Authorization**: Control user permissions (what you can do)
- **Matrix-based Security**: Fine-grained permission control
- **Project-based Security**: Per-project permission settings

### Authorization Strategies

- **Anyone can do anything**: No security (development only)
- **Legacy mode**: Simple logged-in users have full access
- **Matrix-based**: Global permission matrix
- **Project-based Matrix**: Per-project permission matrix

### Permission Types

- **Overall**: Global Jenkins permissions (Administer, Read)
- **Agent**: Build agent management permissions
- **Job**: Job-specific permissions (Build, Configure, Read)
- **SCM**: Source control management permissions

### Security Best Practices

- **Principle of Least Privilege**: Grant minimum required permissions
- **Remove Anonymous Access**: Disable anonymous user permissions
- **Regular Audits**: Review user permissions regularly
- **Role-based Access**: Group users by roles and responsibilities

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

- **← Previous**: [Day 69 - Install Jenkins Plugins](./day-69.md)
- **Next →**: [Day 71 - Configure Jenkins Job for Package Installation](../week-11/day-71.md)

### Similar Challenges (Linux)
- [Day 68 - Set Up Jenkins Server](../week-10/day-68.md)

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

