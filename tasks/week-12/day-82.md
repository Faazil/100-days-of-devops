# Day 82: Create Ansible Inventory for App Server Testing

## Task Overview

Develop Ansible playbooks to automate configuration management tasks. Playbooks define desired system states using YAML syntax.

**Playbook Development:**
- Write playbook with tasks
- Define hosts and variables
- Configure modules and parameters
- Execute and verify playbook

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Perform the initial setup or connection.

```sh
cd playbook
    vi inventory
```

**Step 2:** Connect to the target server using SSH.

```ini
[app]
    stapp01

    [app:vars]
    ansible_user=tony
    ansible_ssh_pass=Ir0nM@n
    ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

**Step 3:** Execute the Ansible playbook to configure hosts.

```sh
ansible-playbook -i inventory playbook.yml
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 81](day-81.md) | [Day 83 →](day-83.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
