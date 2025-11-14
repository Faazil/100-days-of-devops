# Challenge 87: Ansible Install Package

## 📊 Metadata
- **Day**: 87
- **Week**: 13
- **Day in Week**: 3/7
- **Category**: Ansible
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus Application development team wanted to test some applications on app servers in Stratos Datacenter. They shared some pre-requisites with the DevOps team, and packages need to be installed on app servers. Since we are already using Ansible for automating such tasks, please perform this task using Ansible as per details mentioned below:

- Create an inventory file `/home/thor/playbook/inventory` on jump host and add all app servers in it.

- Create an Ansible playbook `/home/thor/playbook/playbook.yml` to install `samba package` on all  app servers using `Ansible yum module`.

- Ensure user `thor` should be able to run the playbook on jump host.

> Note: Validation will try to run playbook using command `ansible-playbook -i inventory playbook.yml` so please make sure playbook works this way, without passing any extra arguments.


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
- Day 86: Ansible Ping Module Usage (recommended)

**Required Skills:**
- ✅ Write inventory files
- ✅ Create playbooks with proper YAML syntax
- ✅ Use Ansible modules effectively
- ✅ Configure SSH connectivity
- ✅ Handle privilege escalation (become)

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Move into playbook directory

    ```sh
    cd playbook
    ```

2. Create two files `inventory` and `playbook.yml`:

    ```sh
    touch inventory playbook.yml
    ```

3. Update inventory file with these contents:

    ```ini
    [app]
    stapp01 ansible_user=tony ansible_ssh_password=Ir0nM@n
    stapp02 ansible_user=steve ansible_ssh_password=Am3ric@
    stapp03 ansible_user=banner ansible_ssh_password=BigGr33n

    [all:vars]
    ansible_ssh_common_args='-o StrictHostKeyChecking=no'
    ```

4. Update the `playbook.yml` with the contents from this [playbook YAML file](../files/ansible_playbook_samba_package_install_87.yml)

5. Run the ansible playbook command:

    ```sh
    ansible-playbook -i inventory playbook.yml
    ```

## Good to Know?

### Ansible Package Management

- **yum Module**: Red Hat/CentOS package management
- **apt Module**: Debian/Ubuntu package management
- **package Module**: Generic package manager (auto-detects)
- **dnf Module**: Modern Red Hat package manager

### Package Operations

- **Install**: `state: present` or `state: installed`
- **Remove**: `state: absent` or `state: removed`
- **Update**: `state: latest` updates to newest version
- **Hold**: Prevent package updates

### Package Management Best Practices

- **Idempotency**: Safe to run multiple times
- **Version Pinning**: Specify exact versions for stability
- **Repository Management**: Ensure proper repositories configured
- **Dependency Handling**: Package managers handle dependencies

### Cross-Platform Considerations

- **Package Names**: May differ between distributions
- **Package Managers**: Different tools (yum, apt, dnf, zypper)
- **Repository Configuration**: Different repo formats
- **Service Names**: Services may have different names

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

- **← Previous**: [Day 86 - Ansible Ping Module Usage](./day-86.md)
- **Next →**: [Day 88 - Ansible Blockinfile Module](../week-13/day-88.md)

### Similar Challenges (Ansible)
- [Day 83 - Troubleshoot and Create Ansible Playbook](../week-12/day-83.md)
- [Day 86 - Ansible Ping Module Usage](../week-13/day-86.md)
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

