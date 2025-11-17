# Day 85: Create Files on App Servers using Ansible

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
```

**Step 2:** Connect to the target server using SSH.

```ini
[app]
    stapp01 ansible_user=tony ansible_ssh_password=Ir0nM@n
    stapp02 ansible_user=steve ansible_ssh_password=Am3ric@
    stapp03 ansible_user=banner ansible_ssh_password=BigGr33n

    [all:vars]
    ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

**Step 3:** Execute the Ansible playbook to configure hosts.

```sh
ansible-playbook -i inventory playbook.yml
```

**Step 4:** Execute the command to complete this step.

```sh
ls -la /tmp
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 84](../week-12/day-84.md) | [Day 86 →](day-86.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
