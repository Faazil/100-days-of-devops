# Day 87: Ansible Install Package

## Task Overview

Nautilus dev team members wanted to test some applications on app servers within the Stratos DC. They shared some pre-requisites with the DevOps team, and packages need to be installed on app servers. Since we are already using Ansible for automating such tasks, please perform this task using Ansible as per details mentioned below:

- Create an inventory file `/home/thor/playbook/inventory` on jump host and add all app servers in it.

- Create an Ansible playbook `/home/thor/playbook/playbook.yml` to install `samba package` on all  app servers using `Ansible yum module`.

- Ensure user `thor` should be able to run the playbook on jump host.

> Note: Validation will try to run playbook using command `ansible-playbook -i inventory playbook.yml` so please make sure playbook works this way, without passing any extra arguments.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
cd playbook
```

**Step 2:**
```bash
touch inventory playbook.yml
```

**Step 3:**
```bash
[app]
    stapp01 ansible_user=tony ansible_ssh_password=Ir0nM@n
    stapp02 ansible_user=steve ansible_ssh_password=Am3ric@
    stapp03 ansible_user=banner ansible_ssh_password=BigGr33n

    [all:vars]
    ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

**Step 4:**
```bash
ansible-playbook -i inventory playbook.yml
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 86](day-86.md) | [Day 88 →](day-88.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
