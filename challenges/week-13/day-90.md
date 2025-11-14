# Challenge 90: Managing ACLs Using Ansible

## 📊 Metadata
- **Day**: 90
- **Week**: 13
- **Day in Week**: 6/7
- **Category**: Ansible
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

There are some files that need to be created on all app servers in Stratos DC. The Nautilus DevOps team want these files to be owned by user root only however, they also want that the app specific user to have a set of permissions on these files. All tasks must be done using Ansible only, so they need to create a playbook. Below you can find more information about the task.

Create a playbook named `playbook.yml` under `/home/thor/ansible` directory on jump host, an inventory file is already present under `/home/thor/ansible directory` on Jump Server itself.

1. Create an empty file `blog.txt` under `/opt/devops/` directory on app server 1. Set some acl properties for this file. Using acl provide `read '(r)' permissions to group tony` (i.e entity is tony and etype is group).

2. Create an empty file `story.txt` under `/opt/devops/` directory on app server 2. Set some acl properties for this file. Using acl provide `read + write '(rw)'` permissions to `user` `steve` (i.e entity is steve and etype is user).

3. Create an empty file `media.txt` under `/opt/devops/` on app server 3. Set some acl properties for this file. Using acl provide read + write '(rw)' `permissions to group banner` (i.e entity is banner and etype is group).

> Note: Validation will try to run the playbook using command ansible-playbook -i inventory playbook.yml so please make sure the playbook works this way, without passing any extra arguments.


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
- Day 86: Ansible Ping Module Usage (recommended)
- Day 87: Ansible Install Package (recommended)
- Day 88: Ansible Blockinfile Module (recommended)

**Required Skills:**
- ✅ Write inventory files
- ✅ Create playbooks with proper YAML syntax
- ✅ Use Ansible modules effectively
- ✅ Configure SSH connectivity
- ✅ Handle privilege escalation (become)

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

0. Move into Ansible directory

    ```sh
    cd ansible
    ls
    ```

1. Check inventory file:

    ```sh
    cat inventory
    ```

2. Create an empty playbook.yml file

    ```sh
    touch playbook.yml
    ```

3. Update `playbook.yml` file with copy-paste contents from this [YAML file](../files/ansible_playbook_acl_users_090.yml)

4. Run the playbook command:

    ```sh
    ansible-playbook -i inventory playbook.yml
    ```

## Good to Know?

### Access Control Lists (ACLs)

- **ACLs** extend traditional Unix permissions beyond owner/group/other
- Allow fine-grained permissions for specific users and groups
- **Entity Types**: `user`, `group`, `mask`, `other`
- **Permissions**: `r` (read), `w` (write), `x` (execute)

### Ansible ACL Module

- **Module**: `ansible.posix.acl` - manages file/directory ACLs
- **Key Parameters**:
  - `path`: Target file/directory path
  - `entity`: User/group name for ACL entry
  - `etype`: Entity type (`user`, `group`, `mask`, `other`)
  - `permissions`: Permission string (`r`, `w`, `x`, `rw`, `rwx`)
  - `state`: `present` (default) or `absent`

### ACL Commands

- **View ACLs**: `getfacl filename`
- **Set ACLs**: `setfacl -m u:user:rw filename`
- **Remove ACLs**: `setfacl -x u:user filename`

### Best Practices

- Always specify `etype` and `entity` for clarity
- Use minimal permissions required
- Test ACL changes before production deployment
- Document ACL requirements in playbook comments

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

- **← Previous**: [Day 89 - Ansible Manage Services](./day-89.md)
- **Next →**: [Day 91 - Ansible Lineinfile Module](../week-13/day-91.md)

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

