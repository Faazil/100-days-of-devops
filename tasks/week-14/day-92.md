# Day 92: Managing Jinja2 Templates Using Ansible

## Task Overview

One of the Nautilus DevOps team members is working on to develop a role for httpd installation and configuration. Work is almost completed, however there is a requirement to add a jinja2 template for index.html file. Additionally, the relevant task needs to be added inside the role. The inventory file ~/ansible/inventory is already present on jump host that can be used. Complete the task as per details mentioned below:

- Update ~/ansible/playbook.yml playbook to run the `httpd` role on App Server 2.

- Create a jinja2 template `index.html.j2` under `/home/thor/ansible/role/httpd/templates/` directory and add a line `This file was created using Ansible on <respective server>` (for example This file was created using Ansible on stapp01 in case of App Server 1). Also please make sure not to hard code the server name inside the template. Instead, use `inventory_hostname` variable to fetch the correct value.

- Add a task inside `/home/thor/ansible/role/httpd/tasks/main.yml` to copy this template on App Server 2 under `/var/www/html/index.html`. Also make sure that `/var/www/html/index.html` file's permissions are `0777`.

- The user/group owner of `/var/www/html/index.html` file must be respective sudo user of the server (for example tony in case of stapp01).

> Note: Validation will try to run the playbook using command ansible-playbook -i inventory playbook.yml so please make sure the playbook works this way without passing any extra arguments.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
cd ansible
    ls
    cat inventory
    cat playbook.yml
    ls role
```

**Step 2:**
```bash
vi role/httpd/templates/index.html.j2
```

**Step 3:**
```bash
2. Update `main.yml` of httpd role
```

**Step 4:**
```bash
> add these lines at the below:
```

**Step 5:**
```bash
> Or you can replace all contents with this [YAML file](../files/ansible_playbook_jinja2_template_092.yml)

3. Add target hosts in `playbook.yml`
```

**Step 6:**
```bash
> `playbook.yml` file should be look like this:
```

**Step 7:**
```bash
4. Run the playbook command:
```

**Step 8:**
```bash
5. verify with curl
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 91](../week-13/day-91.md) | [Day 93 →](day-93.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
