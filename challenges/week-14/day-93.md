# Challenge 93: Using Ansible Conditions

## 📊 Metadata
- **Day**: 93
- **Week**: 14
- **Day in Week**: 2/7
- **Category**: Ansible
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team had a discussion about, how they can train different team members to use Ansible for different automation tasks. There are numerous ways to perform a particular task using Ansible, but we want to utilize each aspect that Ansible offers. The team wants to utilise Ansible's conditionals to perform the following task:

An inventory file is already placed under /home/thor/ansible directory on jump host, with all the Stratos DC app servers included.

Create a playbook /home/thor/ansible/playbook.yml and make sure to use Ansible's when conditionals statements to perform the below given tasks.

1. Copy `blog.txt` file present under `/usr/src/itadmin` directory on jump host to `App Server 1` under `/opt/itadmin` directory. Its user and group owner must be user tony and its permissions must be 0655 .

2. Copy `story.txt` file present under `/usr/src/itadmin` directory on jump host to `App Server 2` under `/opt/itadmin` directory. Its user and group owner must be user steve and its permissions must be 0655 .

3. Copy `media.txt` file present under `/usr/src/itadmin` directory on jump host to `App Server 3` under `/opt/itadmin` directory. Its user and group owner must be user banner and its permissions must be 0655.

> NOTE:

- You can use `ansible_nodename` variable from gathered facts with when condition. Additionally, please make sure you are running the play for all hosts i.e use - hosts: all.

- Validation will try to run the playbook using command ansible-playbook -i inventory playbook.yml, so please make sure the playbook works this way without passing any extra arguments.


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
- Day 90: Managing ACLs Using Ansible (recommended)
- Day 91: Ansible Lineinfile Module (recommended)
- Day 92: Managing Jinja2 Templates Using Ansible (recommended)

**Required Skills:**
- ✅ Write inventory files
- ✅ Create playbooks with proper YAML syntax
- ✅ Use Ansible modules effectively
- ✅ Configure SSH connectivity
- ✅ Handle privilege escalation (become)

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

0. Move into ansible directory and check files

    ```sh
    cd ansible
    ls -la
    cat inventory
    ```

1. Create an empty `playbook.yml` file

    ```sh
    touch playbook.yml
    ```

2. Update `playbook.yml` with the contents from this [YAML file](../files/ansible_playbook_conditions_093.yml)

    - Make sure you have update `src path` and `mode` based on your task description

3. Run the playbook

    ```sh
    ansible-playbook -i inventory playbook.yml
    ```

4. Verify

    - login into each app server and run the command

    ```sh
    ls -la /opt/itadmin
    ```

## Good to Know

- **Ansible Facts**: `ansible_nodename` is an automatically gathered fact that contains the hostname of the target machine
- **When Conditions**: Use `when:` clause to conditionally execute tasks based on facts, variables, or expressions
- **Fact Gathering**: Ansible automatically gathers facts about target hosts unless disabled with `gather_facts: no`
- **Conditional Operators**: Support for `==`, `!=`, `in`, `not in`, `is defined`, `is not defined`
- **Multiple Conditions**: Use `and`, `or` operators to combine multiple conditions
- **File Permissions**: Octal notation (0655) sets read/write for owner, read/execute for group and others

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

- **← Previous**: [Day 92 - Managing Jinja2 Templates Using Ansible](./day-92.md)
- **Next →**: [Day 94 - Create VPC Using Terraform](../week-14/day-94.md)

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

