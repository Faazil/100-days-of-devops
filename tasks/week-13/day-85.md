# Day 85: Create Files on App Servers using Ansible

## Task Overview

The Nautilus DevOps team is testing various Ansible modules on servers in Stratos DC. They're currently focusing on file creation on remote hosts using Ansible. Here are the details:

a. Create an inventory file `~/playbook/inventory` on jump host and include all `app servers`.

b. Create a playbook `~/playbook/playbook.yml` to create a blank file `/tmp/nfsshare.txt` on all app servers.

c. Set the permissions of the `/tmp/nfsshare.txt` file to 0644.

d. Ensure the user/group owner of the `/tmp/nfsshare.txt` file is `tony` on app server 1, `steve` on app server 2 and `banner` on app server 3.

Note: Validation will execute the playbook using the command a`nsible-playbook -i inventory playbook.yml`, so ensure the playbook functions correctly without any additional arguments.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
cd playbook
```

**Step 2:**
```bash
[app]
    stapp01 ansible_user=tony ansible_ssh_password=Ir0nM@n
    stapp02 ansible_user=steve ansible_ssh_password=Am3ric@
    stapp03 ansible_user=banner ansible_ssh_password=BigGr33n

    [all:vars]
    ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

**Step 3:**
```bash
ansible-playbook -i inventory playbook.yml
```

**Step 4:**
```bash
ls -la /tmp
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 84](../week-12/day-84.md) | [Day 86 →](day-86.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
