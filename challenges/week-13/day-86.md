# Challenge 86: Ansible Ping Module Usage

## 📊 Metadata
- **Day**: 86
- **Week**: 13
- **Day in Week**: 2/7
- **Category**: Ansible
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team is planning to test several Ansible playbooks on different app servers in Stratos DC. Before that, some pre-requisites must be met. Essentially, the team needs to set up a password-less SSH connection between Ansible controller and Ansible managed nodes. One of the tickets is assigned to you; please complete the task as per details mentioned below:

a. Jump host is our Ansible controller, and we are going to run Ansible playbooks through thor user from jump host.

b. There is an inventory file `/home/thor/ansible/inventory` on jump host. Using that inventory file test Ansible ping from jump host to App Server 3, make sure ping works.


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
- Day 83: Troubleshoot and Create Ansible Playbook (recommended)

**Required Skills:**
- ✅ Write inventory files
- ✅ Create playbooks with proper YAML syntax
- ✅ Use Ansible modules effectively
- ✅ Configure SSH connectivity
- ✅ Handle privilege escalation (become)

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Update the inventory file with specific user:

    ```ini
    stapp01 ansible_host=172.16.238.10 ansible_user=tony ansible_ssh_pass=Ir0nM@n
    stapp02 ansible_host=172.16.238.11 ansible_user=steve ansible_ssh_pass=Am3ric@
    stapp03 ansible_host=172.16.238.12 ansible_user=banner ansible_ssh_pass=BigGr33n

    [all:vars]
    ansible_ssh_common_args='-o StrictHostKeyChecking=no'
    ```

2. Test ping module
    - To ping all servers:

        ```sh
        ansible all -i inventory -m ping
        ```

    - To ping specific server:

        ```sh
        ansible stapp03 -i inventory -m ping
        ```

## Good to Know?

### Ansible Ping Module

- **Purpose**: Test connectivity and authentication
- **Not ICMP**: Uses SSH connection, not network ping
- **Authentication Test**: Verifies SSH credentials work
- **Python Check**: Ensures Python is available on target

### Connection Testing

- **SSH Connectivity**: Verify network connectivity
- **Authentication**: Test username/password or SSH keys
- **Python Availability**: Ensure Python interpreter exists
- **Sudo Access**: Test privilege escalation if needed

### Inventory Variables

- **ansible_host**: Override hostname/IP address
- **ansible_user**: SSH username for connection
- **ansible_ssh_password**: SSH password (use vault)
- **ansible_ssh_common_args**: Additional SSH options

### Troubleshooting Connectivity

- **Network Issues**: Check firewall, routing, DNS
- **SSH Configuration**: Verify SSH service and config
- **Authentication**: Check credentials and SSH keys
- **Python**: Ensure Python is installed on targets

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

- **← Previous**: [Day 85 - Create Files on App Servers using Ansible](./day-85.md)
- **Next →**: [Day 87 - Ansible Install Package](../week-13/day-87.md)

### Similar Challenges (Ansible)
- [Day 83 - Troubleshoot and Create Ansible Playbook](../week-12/day-83.md)
- [Day 87 - Ansible Install Package](../week-13/day-87.md)
- [Day 88 - Ansible Blockinfile Module](../week-13/day-88.md)

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

