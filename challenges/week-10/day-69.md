# Challenge 69: Install Jenkins Plugins

## 📊 Metadata
- **Day**: 69
- **Week**: 10
- **Day in Week**: 6/7
- **Category**: Jenkins
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team has recently setup a Jenkins server, which they want to use for some CI/CD jobs. Before that they want to install some plugins which will be used in most of the jobs. Please find below more details about the task

1. Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username `admin` and `Adm!n321` password.

2. Once logged in, install the `Git and GitLab` plugins. Note that you may need to restart Jenkins service to complete the plugins installation, If required, opt to Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre.

Note:

1. After restarting the Jenkins service, wait for the Jenkins login page to reappear before proceeding.

2. For tasks involving web UI changes, capture screenshots to share for review or consider using screen recording software like loom.com for documentation and sharing.


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

**Required Skills:**
- ✅ Create and configure Jenkins jobs
- ✅ Install and configure plugins
- ✅ Manage credentials securely
- ✅ Configure build parameters
- ✅ Set up build triggers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Access Jenkins UI
2. Manage Jenkins
3. Plugins in System Configuration > Update plugins > Select plugins that required to update > restart jenkins
4. Manage Jenkins > Plugins > Available Plugins > Search Git, and GitLab and select them
5. Click on Install (It will start installing plugins)
6. At the end, opt for jenkins restart

## Verify

To verify result, you can check if git and github are installed or not from installed plugins.

## Issues

> It's better to update required plugin before installing new one
> If plugins failed to install, then go to updates section, and select plugins that are require to update
> Once Update completed, install the plugins
> You may get timeout/error, just try again
> You may need to restart jenkins server several times.

## Good to Know?

### Jenkins Plugin Management

- **Plugin Ecosystem**: Thousands of plugins extend Jenkins functionality
- **Update Center**: Central repository for plugin downloads
- **Dependencies**: Plugins may have dependencies on other plugins
- **Restart Required**: Some plugins require Jenkins restart to activate

### Essential Plugins

- **Git**: Source code management integration
- **GitLab**: GitLab repository and CI/CD integration
- **Pipeline**: Define build pipelines as code
- **SSH**: Remote execution and file transfer

### Plugin Installation Process

- **Available Plugins**: Browse and search available plugins
- **Install**: Select plugins and install without restart
- **Update Dependencies**: Update required dependencies first
- **Restart**: Restart Jenkins when installation complete

### Troubleshooting

- **Network Issues**: Check internet connectivity
- **Update First**: Update existing plugins before installing new ones
- **Retry**: Plugin installation may fail, retry if needed
- **Safe Restart**: Restart when no jobs are running

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

- **← Previous**: [Day 68 - Set Up Jenkins Server](./day-68.md)
- **Next →**: [Day 70 - Configure Jenkins User Access](../week-10/day-70.md)

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

