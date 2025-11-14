# Challenge 83: Troubleshoot and Create Ansible Playbook

## 📊 Metadata
- **Day**: 83
- **Week**: 12
- **Day in Week**: 6/7
- **Category**: Ansible
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

An Ansible playbook needs completion on the jump host, where a team member left off. Below are the details:

- The inventory file `/home/thor/ansible/inventory` requires adjustments. The playbook must run on App Server 2 in Stratos DC. Update the inventory accordingly.

- Create a playbook `/home/thor/ansible/playbook.yml`. Include a task to create an empty file `/tmp/file.txt` on App Server 2.

> Note: Validation will run the playbook using the command ansible-playbook -i inventory playbook.yml. Ensure the playbook works without any additional arguments.


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

**Required Skills:**
- ✅ Write inventory files
- ✅ Create playbooks with proper YAML syntax
- ✅ Use Ansible modules effectively
- ✅ Configure SSH connectivity
- ✅ Handle privilege escalation (become)

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

0. Move into ansible directory:

    ```sh
    cd ansible
    ls
    ```

1. Fix the inventory file:

    ```ini
    stapp02 ansible_host=172.238.16.204 ansible_user=steve ansible_ssh_common_args='-o StrictHostKeyChecking=no'
    ```

    > The host is not the correct one for app server 2. replace host ip with hostname of app server 2: `stapp02` and add `ansible_ssh_password`

    ```ini
    stapp02 ansible_host=stapp02 ansible_user=steve ansible_ssh_password=Am3ric@ ansible_ssh_common_args='-o StrictHostKeyChecking=no'
    ```

2. Create a playbook.yml file and copy-paste contents from [this playbook file](../files/ansible-simple-playbook-83.yaml)

3. Run the playbook command:

    ```sh
    ansible-playbook -i inventory playbook.yml
    ```

## Good to Know?

### Ansible Troubleshooting

- **Connection Issues**: Verify SSH connectivity and credentials
- **Inventory Problems**: Check host definitions and variables
- **Module Errors**: Validate module syntax and parameters
- **Permission Issues**: Ensure proper sudo/root access

### Common Issues

- **Host Unreachable**: Network connectivity problems
- **Authentication Failed**: Wrong credentials or SSH keys
- **Module Not Found**: Missing Ansible modules
- **Syntax Errors**: YAML formatting issues

### Debugging Techniques

- **Verbose Mode**: Use `-v`, `-vv`, `-vvv` for detailed output
- **Check Mode**: Use `--check` for dry-run execution
- **Limit Hosts**: Use `--limit` to target specific hosts
- **Step Mode**: Use `--step` for interactive execution

### File Operations

- **file Module**: Create, modify, delete files and directories
- **copy Module**: Copy files from control node to managed nodes
- **template Module**: Process Jinja2 templates
- **lineinfile Module**: Modify specific lines in files

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

- **← Previous**: [Day 82 - Create Ansible Inventory for App Server Testing](./day-82.md)
- **Next →**: [Day 84 - Copy Data to App Servers using Ansible](../week-12/day-84.md)

### Similar Challenges (Ansible)
- [Day 86 - Ansible Ping Module Usage](../week-13/day-86.md)
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
**Difficulty**: {get_difficulty_emoji(day)}
**Category**: {task_info['category']}

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
python3 ../../tools/progress.py --complete {day}
```

