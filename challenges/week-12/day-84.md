# Challenge 84: Copy Data to App Servers using Ansible

## 📊 Metadata
- **Day**: 84
- **Week**: 12
- **Day in Week**: 7/7
- **Category**: Linux
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team needs to copy data from the jump host to all application servers in Stratos DC using Ansible. Execute the task with the following details:

a. Create an inventory file `/home/thor/ansible/inventory` on jump_host and add all application servers as managed nodes.

b. Create a playbook `/home/thor/ansible/playbook.yml` on the jump host to copy the `/usr/src/sysops/index.html` file to all application servers, placing it at `/opt/sysops`.

Note: Validation will run the playbook using the command `ansible-playbook -i inventory playbook.yml`. Ensure the playbook functions properly without any extra arguments.


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
- Day 68: Set Up Jenkins Server (recommended)
- Day 70: Configure Jenkins User Access (recommended)
- Day 82: Create Ansible Inventory for App Server Testing (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Move into ansible directory

    ```sh
    cd ansible
    ```

2. Create an `inventory` file and copy-paste the contents:

    ```ini
    [app]
    stapp01 ansible_user=tony ansible_ssh_password=Ir0nM@n
    stapp02 ansible_user=steve ansible_ssh_password=Am3ric@
    stapp03 ansible_user=banner ansible_ssh_password=BigGr33n

    [all:vars]
    ansible_ssh_common_args='-o StrictHostKeyChecking=no'
    ```

3. Create an `playbook.yml` file and copy-paste the contents from [this playbook file](../files/ansible_playbook_mulit-servers-84.yaml)

4. Run the playbook command:

    ```sh
    ansible-playbook -i inventory playbook.yml
    ```

## Good to Know?

### Ansible File Management

- **copy Module**: Transfer files from control node to managed nodes
- **fetch Module**: Retrieve files from managed nodes
- **synchronize Module**: Efficient file synchronization (rsync)
- **template Module**: Process and deploy template files

### File Copy Operations

- **Source Path**: File location on control node
- **Destination Path**: Target location on managed nodes
- **Permissions**: Set file ownership and permissions
- **Backup**: Create backup of existing files

### Multi-Server Management

- **Inventory Groups**: Target multiple servers simultaneously
- **Parallel Execution**: Ansible runs tasks in parallel
- **Error Handling**: Continue on some failures, stop on critical errors
- **Idempotency**: Safe to run multiple times

### Best Practices

- **File Validation**: Verify file integrity after copy
- **Atomic Operations**: Use atomic moves for critical files
- **Backup Strategy**: Always backup before modifying
- **Permission Management**: Set appropriate file permissions

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

- **← Previous**: [Day 83 - Troubleshoot and Create Ansible Playbook](./day-83.md)
- **Next →**: [Day 85 - Create Files on App Servers using Ansible](../week-13/day-85.md)

### Similar Challenges (Linux)
- [Day 82 - Create Ansible Inventory for App Server Testing](../week-12/day-82.md)
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
**Difficulty**: ⭐
**Category**: DevOps

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
```

