# Challenge 72: Jenkins Parameterized Builds

## 📊 Metadata
- **Day**: 72
- **Week**: 11
- **Day in Week**: 2/7
- **Category**: Jenkins
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

A new DevOps Engineer has joined the team and he will be assigned some Jenkins related tasks. Before that, the team wanted to test a simple parameterized job to understand basic functionality of parameterized builds. He is given a simple parameterized job to build in Jenkins. Please find more details below:

Click on the Jenkins button on the top bar to access the Jenkins UI. Login using username `admin` and password `Adm!n321`.

1. Create a parameterized job which should be named as `parameterized-job`

2. Add a string parameter named `Stage`; its default value should be `Build`.

3. Add a choice parameter named `env`; its choices should be `Development`, `Staging` and `Production`.

4. Configure job to execute a shell command, which should echo both parameter values (you are passing in the job).

5. Build the Jenkins job at least once with choice parameter value Production to make sure it passes.

Note:

1. You might need to install some plugins and restart Jenkins service. So, we recommend clicking on Restart Jenkins when installation is complete and no jobs are running on plugin installation/update page i.e update centre. Also, Jenkins UI sometimes gets stuck when Jenkins service restarts in the back end. In this case, please make sure to refresh the UI page.

2. For these kind of scenarios requiring changes to be done in a web UI, please take screenshots so that you can share it with us for review in case your task is marked incomplete. You may also consider using a screen recording software such as loom.com to record and share your work.


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
- Day 69: Install Jenkins Plugins (recommended)
- Day 71: Configure Jenkins Job for Package Installation (recommended)

**Required Skills:**
- ✅ Create and configure Jenkins jobs
- ✅ Install and configure plugins
- ✅ Manage credentials securely
- ✅ Configure build parameters
- ✅ Set up build triggers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

0. Update plugins and restart jenkins

1. Create a job named: `parameterized-job`

2. Select `This project is parameterised` > Add Parameters:

    - String Parameter:
      - Name: `Stage`
      - Default Value: Build
    - Choice Parameter:
      - Name: `env`
      - Choices:
        - Development
        - Staging
        - Production

3. Add Build Steps > Execute Shell

    ```sh
    echo $Stage
    echo $env
    ```

4. Execute the job with Production env

## Good to Know?

### Parameterized Builds

- **Purpose**: Make jobs flexible and reusable
- **Runtime Configuration**: Pass values at build time
- **Dynamic Behavior**: Change job behavior based on parameters
- **User Input**: Collect input from users before build

### Parameter Types

- **String**: Text input with optional default value
- **Choice**: Dropdown list with predefined options
- **Boolean**: Checkbox for true/false values
- **File**: Upload file as parameter
- **Password**: Secure text input (masked in logs)

### Parameter Usage

- **Environment Variables**: Parameters become env vars in build
- **Shell Scripts**: Access via `$PARAMETER_NAME`
- **Pipeline**: Use `params.PARAMETER_NAME`
- **Build Triggers**: Pass parameters to downstream jobs

### Best Practices

- **Default Values**: Provide sensible defaults
- **Validation**: Validate parameter values in build script
- **Documentation**: Describe parameter purpose and format
- **Security**: Use password parameters for sensitive data

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

- **← Previous**: [Day 71 - Configure Jenkins Job for Package Installation](./day-71.md)
- **Next →**: [Day 73 - Jenkins Scheduled Jobs](../week-11/day-73.md)

### Similar Challenges (Jenkins)
- [Day 69 - Install Jenkins Plugins](../week-10/day-69.md)
- [Day 71 - Configure Jenkins Job for Package Installation](../week-11/day-71.md)
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
**Difficulty**: {get_difficulty_emoji(day)}
**Category**: {task_info['category']}

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
python3 ../../tools/progress.py --complete {day}
```

