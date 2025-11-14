# Challenge 88: Ansible Blockinfile Module

## 📊 Metadata
- **Day**: 88
- **Week**: 13
- **Day in Week**: 4/7
- **Category**: Ansible
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team wants to install and set up a simple httpd web server on all app servers in Stratos DC. Additionally, they want to deploy a sample web page for now using Ansible only. Therefore, write the required playbook to complete this task. Find more details about the task below.

We already have an inventory file under `/home/thor/ansible` directory on jump host. Create a `playbook.yml` under `/home/thor/ansibl`e directory on jump host itself.

- Using the playbook, install `httpd` web server on all app servers. Additionally, make sure its service should up and running.

- Using blockinfile Ansible module add some content in `/var/www/html/index.html` file. Below is the content:

    ```html
    Welcome to XfusionCorp!

    This is  Nautilus sample file, created using Ansible!

    Please do not modify this file manually!
    ```

- The `/var/www/html/index.html` file's user and group owner should be apache on all app servers.

- The `/var/www/html/index.html` file's permissions should be `0644` on all app servers.

Note:

i. Validation will try to run the playbook using command `ansible-playbook -i inventory playbook.yml` so please make sure the playbook works this way without passing any extra arguments.

ii. Do not use any custom or empty marker for blockinfile module.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

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
- Day 83: Troubleshoot and Create Ansible Playbook (recommended)
- Day 86: Ansible Ping Module Usage (recommended)
- Day 87: Ansible Install Package (recommended)

**Required Skills:**
- ✅ Write inventory files
- ✅ Create playbooks with proper YAML syntax
- ✅ Use Ansible modules effectively
- ✅ Configure SSH connectivity
- ✅ Handle privilege escalation (become)

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

0. Move into ansible directory

    ```sh
    cd ansible
    ```

1. Create an empty `playbook.yml` file:

    ```sh
    touch playbook.yml
    ```

2. Add contents to `playbook.yml` from this [YAML file](../files/ansible_playbook_blockinfile_module_88.yml)

    ```sh
    vi playbook.yml
    ```

    > copy-paste contents

3. Run the playbook command:

    ```sh
    ansible-playbook -i inventory playbook.yml
    ```

## Good to Know?

### Ansible blockinfile Module

- **Purpose**: Insert/update/remove blocks of text in files
- **Markers**: Identify block boundaries in target file
- **Idempotent**: Safe to run multiple times
- **Block Management**: Add, modify, or remove text blocks

### Block Markers

- **Default Markers**: `# BEGIN ANSIBLE MANAGED BLOCK` and `# END ANSIBLE MANAGED BLOCK`
- **Custom Markers**: Define custom marker text
- **Marker Format**: Markers help identify managed content
- **Preservation**: Content outside markers is preserved

### Web Server Configuration

- **Document Root**: `/var/www/html` is standard Apache location
- **Index Files**: `index.html` is default page
- **File Ownership**: `apache` user owns web content
- **Permissions**: `0644` allows read access for web server

### File Management Modules

- **blockinfile**: Manage blocks of text
- **lineinfile**: Manage single lines
- **replace**: Replace text patterns
- **template**: Process Jinja2 templates

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

- **← Previous**: [Day 87 - Ansible Install Package](./day-87.md)
- **Next →**: [Day 89 - Ansible Manage Services](../week-13/day-89.md)

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
**Difficulty**: {get_difficulty_emoji(day)}
**Category**: {task_info['category']}

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
python3 ../../tools/progress.py --complete {day}
```

