# Challenge 76: Jenkins Project Security

## 📊 Metadata
- **Day**: 76
- **Week**: 11
- **Day in Week**: 6/7
- **Category**: Jenkins
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The xFusionCorp Industries has recruited some new developers. There are already some existing jobs on Jenkins and two of these new developers need permissions to access those jobs. The development team has already shared those requirements with the DevOps team, so as per details mentioned below grant required permissions to the developers.

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username admin and password Adm!n321.

1. There is an existing Jenkins job named `Packages`, there are also two existing Jenkins users named `sam` with password `sam@pass12345` and `rohan` with password `rohan@pass12345`.

2. Grant permissions to these users to access Packages job as per details mentioned below:

   - Make sure to select `Inherit permissions from parent ACL` under inheritance strategy for granting permissions to these users.

   - Grant mentioned permissions to sam user : `build, configure and read`.

   - Grant mentioned permissions to rohan user : `build, cancel, configure, read, update and tag`.

Note:

- Please do not modify/alter any other existing job configuration.

- You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.

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
- Day 73: Jenkins Scheduled Jobs (recommended)
- Day 74: Jenkins Database Backup Job (recommended)
- Day 75: Jenkins Slave Nodes (recommended)

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
1. Install the plugins:
   - Project based matrix authorization
2. Manage Jenkins > Security > Authorization: Select Project based matrix
   - Add Admin user and permit all changes
   ![project-matrix](../screenshots/jenkins-project-based-matrix-authz.png)

3. Dashboard > Packages Job > Configure > Enable project-based security
   - instance securityL inherit from ACL
   - Add user, rohan, and sam and set required permissions
   ![matrix-security](../screenshots/jenkins-project-based-security-config.png)

## Good to Know?

### Project-Level Security

- **Granular Control**: Per-project permission management
- **Inheritance**: Inherit permissions from parent ACL
- **Override**: Override global permissions for specific projects
- **Team Isolation**: Separate team access to different projects

### Permission Matrix

- **Users and Groups**: Assign permissions to users or groups
- **Permission Types**: Build, Configure, Read, Update, Tag, Cancel
- **Inheritance Strategy**: Control how permissions are inherited
- **Explicit Permissions**: Override inherited permissions

### Security Strategies

- **Role-based Access**: Define roles with specific permissions
- **Least Privilege**: Grant minimum required permissions
- **Regular Reviews**: Audit permissions regularly
- **Documentation**: Document permission rationale

### Common Permissions

- **Read**: View job configuration and build history
- **Build**: Trigger job builds
- **Configure**: Modify job configuration
- **Cancel**: Stop running builds
- **Update**: Modify job settings
- **Tag**: Create build tags

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

- **← Previous**: [Day 75 - Jenkins Slave Nodes](./day-75.md)
- **Next →**: [Day 77 - Jenkins Deploy Pipeline](../week-11/day-77.md)

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

