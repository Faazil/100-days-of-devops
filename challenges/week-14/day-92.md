# Challenge 92: Managing Jinja2 Templates Using Ansible

## 📊 Metadata
- **Day**: 92
- **Week**: 14
- **Day in Week**: 1/7
- **Category**: Ansible
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

One of the Nautilus DevOps team members is working on to develop a role for httpd installation and configuration. Work is almost completed, however there is a requirement to add a jinja2 template for index.html file. Additionally, the relevant task needs to be added inside the role. The inventory file ~/ansible/inventory is already present on jump host that can be used. Complete the task as per details mentioned below:

- Update ~/ansible/playbook.yml playbook to run the `httpd` role on App Server 2.

- Create a jinja2 template `index.html.j2` under `/home/thor/ansible/role/httpd/templates/` directory and add a line `This file was created using Ansible on <respective server>` (for example This file was created using Ansible on stapp01 in case of App Server 1). Also please make sure not to hard code the server name inside the template. Instead, use `inventory_hostname` variable to fetch the correct value.

- Add a task inside `/home/thor/ansible/role/httpd/tasks/main.yml` to copy this template on App Server 2 under `/var/www/html/index.html`. Also make sure that `/var/www/html/index.html` file's permissions are `0777`.

- The user/group owner of `/var/www/html/index.html` file must be respective sudo user of the server (for example tony in case of stapp01).

> Note: Validation will try to run the playbook using command ansible-playbook -i inventory playbook.yml so please make sure the playbook works this way without passing any extra arguments.


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
- Day 88: Ansible Blockinfile Module (recommended)
- Day 90: Managing ACLs Using Ansible (recommended)
- Day 91: Ansible Lineinfile Module (recommended)

**Required Skills:**
- ✅ Write inventory files
- ✅ Create playbooks with proper YAML syntax
- ✅ Use Ansible modules effectively
- ✅ Configure SSH connectivity
- ✅ Handle privilege escalation (become)

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

0. Move into ansible directory and check each files

    ```sh
    cd ansible
    ls
    cat inventory
    cat playbook.yml
    ls role
    ```

1. Create index.html.j2 file

    ```sh
    vi role/httpd/templates/index.html.j2
    ```

    > copy paste the following line:

    ```j2
    <p> This file was created using Ansible on {{ inventory_hostname }} </p>
    ```

2. Update `main.yml` of httpd role

    ```sh
    vi role/httpd/tasks/main.yml
    ```

    > add these lines at the below:

    ```yaml
    - name: Copy index.html template
      ansible.builtin.template:
        src: index.html.j2
        dest: /var/www/html/index.html
        mode: '0777'
        owner: "{{ ansible_user }}"
        group: "{{ ansible_user }}"
    ```

    > Or you can replace all contents with this [YAML file](../files/ansible_playbook_jinja2_template_092.yml)

3. Add target hosts in `playbook.yml`

    ```yaml
    hosts: all
    ```

    > `playbook.yml` file should be look like this:

    ```yaml
    ---
    - hosts: all 
      become: yes
      become_user: root
      roles:
        - role/httpd
    ```

4. Run the playbook command:

    ```sh
    ansible-playbook -i inventory playbook.yml
    ```

5. verify with curl

    ```sh
    curl http://stapp01
    curl http://stapp02
    curl http://stapp03
    ```

    ![ansible curl result](../screenshots/ansible_curl_output_092.png)

6. Further check?

    > login into each app server and run this command

    ```sh
    ls -la /var/www/html
    ```

    ```sh
    [tony@stapp01 ~]$ ls -la /var/www/html
    total 12
    drwxr-xr-x 2 root root 4096 Oct 25 02:47 .
    drwxr-xr-x 4 root root 4096 Oct 25 02:46 ..
    -rwxrwxrwx 1 tony tony   57 Oct 25 02:47 index.html
    [tony@stapp01 ~]$ 
    ```

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

- **← Previous**: [Day 91 - Ansible Lineinfile Module](./day-91.md)
- **Next →**: [Day 93 - Using Ansible Conditions](../week-14/day-93.md)

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

