# Challenge 91: Ansible Lineinfile Module

## 📊 Metadata
- **Day**: 91
- **Week**: 13
- **Day in Week**: 7/7
- **Category**: Ansible
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team want to install and set up a simple httpd web server on all app servers in Stratos DC. They also want to deploy a sample web page using Ansible. Therefore, write the required playbook to complete this task as per details mentioned below.

We already have an inventory file under `/home/thor/ansible directory` on jump host. Write a playbook `playbook.yml` under `/home/thor/ansible` directory on jump host itself. Using the playbook perform below given tasks:

1. Install `httpd` web server on all app servers, and make sure its service is up and running.
2. Create a file `/var/www/html/index.html` with content:

    ```html
    <p> This is a Nautilus sample file, created using Ansible! <p>
    ```

3. Using lineinfile Ansible module add some more content in `/var/www/html/index.html` file. Below is the content:

    ```html
    <h1> Welcome to xFusionCorp Industries!</h1>
    ```

    Also make sure this new line is added at the top of the file.

4. The `/var/www/html/index.html` file's `user` and `group` owner should be `apache` on all app servers.

5. The /var/www/html/index.html file's permissions should be 0755 on all app servers.

> Note: Validation will try to run the playbook using command `ansible-playbook -i inventory playbook.yml` so please make sure the playbook works this way without passing any extra arguments.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Ansible installed with target servers configured
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `ansible`, `ansible-playbook`
- **Key Concepts**:
  - Inventory file structure (INI/YAML)
  - Playbook anatomy (plays, tasks, modules)
  - Ansible modules (yum, apt, copy, file, etc.)
  - Variables and facts
- **File Formats**: YAML, INI syntax and structure
- **Environment**: Ansible installed

**Foundation from Earlier Challenges:**
- Day 87: Ansible Install Package (recommended)
- Day 88: Ansible Blockinfile Module (recommended)
- Day 90: Managing ACLs Using Ansible (recommended)

**Required Skills:**
- ✅ Write inventory files
- ✅ Create playbooks with proper YAML syntax
- ✅ Use Ansible modules effectively
- ✅ Configure SSH connectivity
- ✅ Handle privilege escalation (become)

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

0. Move into ansible directory and look at the inventory file

    ```sh
    cd ansible
    cat inventory
    ```

1. Create an empty `playbook.yml` file:

    ```sh
    touch playbook.yml
    ```

2. Update `playbook.yml` with the contents from this [YAML file](../files/ansible_playbook_lineinfile_module_091.yml)

3. Run the playbook command:

    ```sh
    ansible-playbook -i inventory playbook.yml
    ```

4. Verify with curl

    ```sh
    curl http://stapp01
    curl http://stapp02
    curl http://stapp03
    ```

## Good to Know

- **lineinfile module**: Manages lines in text files - can add, modify, or remove specific lines
- **insertbefore: BOF**: Inserts content at the Beginning of File (top of the file)
- **state: present**: Ensures the line exists in the file (default behavior)
- **File permissions 0755**: Owner has read/write/execute, group and others have read/execute
- **Apache user/group**: Default web server user for file ownership and security
- **Idempotency**: Running the playbook multiple times produces the same result
- **Module order**: Tasks execute sequentially - create file first, then modify with lineinfile

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
- Practical application of Ansible skills
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

- **← Previous**: [Day 90 - Managing ACLs Using Ansible](./day-90.md)
- **Next →**: [Day 92 - Managing Jinja2 Templates Using Ansible](../week-14/day-92.md)

### Similar Challenges (Ansible)
- [Day 83 - Troubleshoot and Create Ansible Playbook](../week-12/day-83.md)
- [Day 86 - Ansible Ping Module Usage](../week-13/day-86.md)
- [Day 87 - Ansible Install Package](../week-13/day-87.md)

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

