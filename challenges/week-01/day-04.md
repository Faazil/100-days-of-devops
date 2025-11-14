# Challenge 4: Script Execute Permissions

## 📊 Metadata
- **Day**: 4
- **Week**: 1
- **Day in Week**: 4/7
- **Category**: DevOps
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

In a bid to automate backup processes, the `xFusionCorp Industries` sysadmin team has developed a new bash script named `xfusioncorp.sh`. While the script has been distributed to all necessary servers, it lacks executable permissions on `App Server 1` within the Stratos Datacenter.

Your task is to grant executable permissions to the `/tmp/xfusioncorp.sh` script on `App Server 1`. Additionally, ensure that all users have the capability to execute it.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Key Concepts**:
  - DevOps workflow and principles
  - CI/CD pipeline concepts
  - Automation strategies
  - Infrastructure management

**Required Skills:**
- ✅ Understand DevOps methodologies
- ✅ Integrate multiple tools
- ✅ Implement automation workflows

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Connect to App server 1
2. Check the current file permission status:

    ```sh
    ls -la /tmp
    ```

    ```txt
    4 ---------- 1 root root   40 Jul 30 02:21 xfusioncorp.sh
    ```

3. Run the following command to update permissions:

    ```sh
    chmod 755 /tmp/xfusioncorp.sh
    ```

4. Verify the results:

    ```sh
    ls -la /tmp
    ```

    ```txt
    4 -rwxr-xr-x 1 root root   40 Jul 30 02:21 xfusioncorp.sh
    ```

## Understanding `chmod` in Linux

The `chmod` command in Linux is used to change the permissions (mode) of a file or directory. File permissions determine who can read, write, or execute a file.

### File Permission Basics

Each file in Linux has three types of permissions:

- Read (r) – Permission to read the file (4)
- Write (w) – Permission to modify the file (2)
- Execute (x) – Permission to run the file as a program (1)

Permissions are set for three categories of users:

- User (u) – The owner of the file (usually the one who created it)
- Group (g) – Users who belong to the same group as the file
- Others (o) – All other users on the system

Each of these categories can have its own combination of r, w, and x.

Two Ways to Use chmod

1. Symbolic Mode
    Use letters to set permissions:

    ```sh
    chmod u=rwx,g=rx,o=r test.sh
    ```

    This sets:

    - User (u): read, write, execute
    - Group (g): read, execute
    - Others (o): read only

    You can also use +, -, or =:

    - `+` adds permission
    - `-` removes permission
    - `=` sets exact permission

    Example:

    ```sh
    chmod g+w test.sh     # Add write permission for group
    chmod o-r test.sh     # Remove read permission for others
    ```

2. Numeric (Octal) Mode
    Each permission is represented by a binary digit:
    - r = 4
    - w = 2
    - x = 1

    You sum them up per category and write a 3-digit number:

    ```sh
    chmod 754 test.sh
    ```

    Breakdown:

    - 7 (User): 4+2+1 = rwx
    - 5 (Group): 4+0+1 = r-x
    - 4 (Others): 4+0+0 = r--

### Summary Table

| Role | Symbol | Permissions | Value |
|---|---|---|---|
|User|u|rwx|7|
|Group|g|r-x|5|
|Others|o|r--|4|

This system gives you fine-grained control over who can access your files and how they can interact with them.

## Good to Know?

### File Permission Fundamentals

- **Security Model**: Unix permissions protect system resources
- **Three Levels**: User (owner), Group, Others
- **Three Types**: Read (4), Write (2), Execute (1)
- **Octal System**: Base-8 numbering for permission representation

### Common Permission Patterns

- **755**: Standard executable (rwxr-xr-x)
- **644**: Standard file (rw-r--r--)
- **600**: Private file (rw-------)
- **777**: Full access (dangerous - avoid)

### Security Considerations

- **Principle of Least Privilege**: Grant minimum required permissions
- **Execute Bit**: Required for scripts and directories
- **Directory Permissions**: Execute needed to access directory contents
- **Sticky Bit**: Special permission for shared directories (/tmp)

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
- Practical application of DevOps skills
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

- **← Previous**: [Day 3 - Secure SSH Root Access](./day-03.md)
- **Next →**: [Day 5 - Install and Configuration Selinux](../week-01/day-05.md)

### Similar Challenges (DevOps)
- [Day 10 - Create a BASH Script](../week-02/day-10.md)
- [Day 13 - IPtables Installation And Configuration](../week-02/day-13.md)

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

