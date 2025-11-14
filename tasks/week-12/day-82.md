# Day 82: Create Ansible Inventory for App Server Testing

## Task Overview

The Nautilus DevOps team is testing Ansible playbooks on various servers within their stack. They've placed some playbooks under /home/thor/playbook/ directory on the jump host and now intend to test them on app server 1 in Stratos DC. However, an inventory file needs creation for Ansible to connect to the respective app. Here are the requirements:

a. Create an ini type Ansible inventory file `/home/thor/playbook/inventory` on jump host.

b. Include App Server 1 in this inventory and necessary variables for proper functionality.

c. Ensure the inventory hostname corresponds to the server name as per the wiki, for example stapp01 for app server 1 in Stratos DC.

Note: Validation will execute the playbook using the command ansible-playbook -i inventory playbook.yml. Ensure the playbook functions properly without any extra arguments.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
cd playbook
    vi inventory
```

**Step 2:**
```bash
[app]
    stapp01

    [app:vars]
    ansible_user=tony
    ansible_ssh_pass=Ir0nM@n
    ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

**Step 3:**
```bash
ansible-playbook -i inventory playbook.yml
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 81](day-81.md) | [Day 83 →](day-83.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
