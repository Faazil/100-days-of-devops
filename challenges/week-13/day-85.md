# Challenge 85: Create Files on App Servers using Ansible

## 📊 Metadata
- **Day**: 85
- **Week**: 13
- **Day in Week**: 1/7
- **Category**: Linux
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team is testing various Ansible modules on servers in Stratos DC. They're currently focusing on file creation on remote hosts using Ansible. Here are the details:

a. Create an inventory file `~/playbook/inventory` on jump host and include all `app servers`.

b. Create a playbook `~/playbook/playbook.yml` to create a blank file `/tmp/nfsshare.txt` on all app servers.

c. Set the permissions of the `/tmp/nfsshare.txt` file to 0644.

d. Ensure the user/group owner of the `/tmp/nfsshare.txt` file is `tony` on app server 1, `steve` on app server 2 and `banner` on app server 3.

Note: Validation will execute the playbook using the command a`nsible-playbook -i inventory playbook.yml`, so ensure the playbook functions correctly without any additional arguments.


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
- Day 70: Configure Jenkins User Access (recommended)
- Day 82: Create Ansible Inventory for App Server Testing (recommended)
- Day 84: Copy Data to App Servers using Ansible (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

0. Move into playbook directory

    ```sh
    cd playbook
    ```

1. Create an inventory file with these contents:

    ```ini
        [app]
    stapp01 ansible_user=tony ansible_ssh_password=Ir0nM@n
    stapp02 ansible_user=steve ansible_ssh_password=Am3ric@
    stapp03 ansible_user=banner ansible_ssh_password=BigGr33n

    [all:vars]
    ansible_ssh_common_args='-o StrictHostKeyChecking=no'
    ```

2. Create the `playbook.yml` and copy-paste the contents from this [Playbook YAML file](../files/ansible-playbook_copy_with_ownership.yml)

3. Run the ansible command:

    ```sh
    ansible-playbook -i inventory playbook.yml
    ```

4. Verify Results:
    To verify the results we can login into each app server and check tmp directory.

    ```sh
    ls -la /tmp
    ```

## Good to Know?

### File Creation with Ansible

- **file Module**: Create files, directories, symlinks
- **State Parameter**: `touch` creates empty files
- **Ownership**: Set user and group ownership
- **Permissions**: Set file mode (octal notation)

### File Attributes

- **Owner**: User who owns the file
- **Group**: Group that owns the file
- **Mode**: File permissions (read, write, execute)
- **State**: File type (file, directory, link, absent)

### Permission Management

- **Octal Notation**: 0644 = rw-r--r--
- **Symbolic Notation**: u=rw,g=r,o=r
- **Special Permissions**: Sticky bit, setuid, setgid
- **Default Permissions**: umask affects default permissions

### Cross-Platform Considerations

- **User Mapping**: Different users on different systems
- **Group Mapping**: Group names may vary
- **Permission Models**: Windows vs Unix permissions
- **Path Separators**: Forward vs backward slashes

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

- **← Previous**: [Day 84 - Copy Data to App Servers using Ansible](./day-84.md)
- **Next →**: [Day 86 - Ansible Ping Module Usage](../week-13/day-86.md)

### Similar Challenges (Linux)
- [Day 82 - Create Ansible Inventory for App Server Testing](../week-12/day-82.md)
- [Day 84 - Copy Data to App Servers using Ansible](../week-12/day-84.md)
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

