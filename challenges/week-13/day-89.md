# Challenge 89: Ansible Manage Services

## 📊 Metadata
- **Day**: 89
- **Week**: 13
- **Day in Week**: 5/7
- **Category**: Linux
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

Developers are looking for dependencies to be installed and run on Nautilus app servers in Stratos DC. They have shared some requirements with the DevOps team. Because we are now managing packages installation and services management using Ansible, some playbooks need to be created and tested. As per details mentioned below please complete the task:

a. On jump host create an Ansible playbook `/home/thor/ansible/playbook.yml` and configure it to install `httpd` on all app servers.

b. After installation make sure to `start` and `enable` `httpd` service on all app servers.

c. The inventory `/home/thor/ansible/inventory` is already there on jump host.

d. Make sure user `thor` should be able to run the playbook on jump host.

Note: Validation will try to run playbook using command `ansible-playbook -i inventory playbook.yml` so please make sure playbook works this way, without passing any extra arguments.


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
- Day 82: Create Ansible Inventory for App Server Testing (recommended)
- Day 84: Copy Data to App Servers using Ansible (recommended)
- Day 85: Create Files on App Servers using Ansible (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

0. Move into ansible directory:

    ```sh
    cd ansible
    ls
    ```

1. Create empty playbook.yml file:

    ```sh
    touch playbook.yml
    ```

2. Update `playbook.yml` with the contents from this [YAML file](../files/ansible_playbook_httpd_install.yml)

3. Run the playbook command:

    ```sh
    ansible-playbook -i inventory playbook.yml
    ```

## Good to Know?

### Ansible Service Management

- **service Module**: Manage system services (start, stop, restart)
- **systemd Module**: Specific to systemd-based systems
- **State Management**: Control service running state
- **Boot Configuration**: Enable/disable services at boot

### Service States

- **started**: Ensure service is running
- **stopped**: Ensure service is not running
- **restarted**: Restart service (stop then start)
- **reloaded**: Reload service configuration

### Service Configuration

- **enabled**: Start service at boot time
- **disabled**: Don't start service at boot
- **masked**: Prevent service from being started
- **daemon_reload**: Reload systemd configuration

### Web Server Management

- **Installation**: Install web server package
- **Configuration**: Configure server settings
- **Service Control**: Start and enable service
- **Content Deployment**: Deploy web content
- **Monitoring**: Ensure service remains running

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

- **← Previous**: [Day 88 - Ansible Blockinfile Module](./day-88.md)
- **Next →**: [Day 90 - Managing ACLs Using Ansible](../week-13/day-90.md)

### Similar Challenges (Linux)
- [Day 82 - Create Ansible Inventory for App Server Testing](../week-12/day-82.md)
- [Day 84 - Copy Data to App Servers using Ansible](../week-12/day-84.md)
- [Day 85 - Create Files on App Servers using Ansible](../week-13/day-85.md)

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

