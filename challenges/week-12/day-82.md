# Challenge 82: Create Ansible Inventory for App Server Testing

## 📊 Metadata
- **Day**: 82
- **Week**: 12
- **Day in Week**: 5/7
- **Category**: Linux
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team is testing Ansible playbooks on various servers within their stack. They've placed some playbooks under /home/thor/playbook/ directory on the jump host and now intend to test them on app server 1 in Stratos DC. However, an inventory file needs creation for Ansible to connect to the respective app. Here are the requirements:

a. Create an ini type Ansible inventory file `/home/thor/playbook/inventory` on jump host.

b. Include App Server 1 in this inventory along with necessary variables for proper functionality.

c. Ensure the inventory hostname corresponds to the server name as per the wiki, for example stapp01 for app server 1 in Stratos DC.

Note: Validation will execute the playbook using the command ansible-playbook -i inventory playbook.yml. Ensure the playbook functions properly without any extra arguments.


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
- Day 68: Set Up Jenkins Server (recommended)
- Day 70: Configure Jenkins User Access (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Create an inventory file:
    - Move into directory and create the file

    ```sh
    cd playbook
    vi inventory
    ```

    - copy-paste contents into inventory file

    ```ini
    [app]
    stapp01

    [app:vars]
    ansible_user=tony
    ansible_ssh_pass=Ir0nM@n
    ansible_ssh_common_args='-o StrictHostKeyChecking=no'
    ```

2. Run the ansible playbook command:

    ```sh
    ansible-playbook -i inventory playbook.yml
    ```

## Good to Know?

### Ansible Inventory

- **Purpose**: Define managed nodes and their properties
- **Formats**: INI, YAML, JSON formats supported
- **Groups**: Organize hosts into logical groups
- **Variables**: Define host and group variables

### Inventory Structure

- **Hosts**: Individual server definitions
- **Groups**: Collections of related hosts
- **Group Variables**: Variables applied to all group members
- **Host Variables**: Variables specific to individual hosts

### Connection Variables

- **ansible_user**: SSH username for connection
- **ansible_ssh_password**: SSH password (use vault for security)
- **ansible_host**: Target hostname or IP address
- **ansible_port**: SSH port (default 22)
- **ansible_ssh_common_args**: Additional SSH arguments

### Best Practices

- **Group Organization**: Group hosts by function, environment
- **Variable Hierarchy**: Use group_vars and host_vars directories
- **Security**: Use Ansible Vault for sensitive data
- **Documentation**: Comment inventory files for clarity

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

- **← Previous**: [Day 81 - Jenkins Multistage Pipeline](./day-81.md)
- **Next →**: [Day 83 - Troubleshoot and Create Ansible Playbook](../week-12/day-83.md)

### Similar Challenges (Linux)
- [Day 84 - Copy Data to App Servers using Ansible](../week-12/day-84.md)
- [Day 85 - Create Files on App Servers using Ansible](../week-13/day-85.md)
- [Day 89 - Ansible Manage Services](../week-13/day-89.md)

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

