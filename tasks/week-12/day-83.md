# Day 83: Troubleshoot and Create Ansible Playbook

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
cd ansible
    ls
```

**Step 2:** Define inventory file with target hosts and connection details.

```ini
stapp02 ansible_host=172.238.16.204 ansible_user=steve ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

**Step 3:** Connect to the target server using SSH.

```ini
stapp02 ansible_host=stapp02 ansible_user=steve ansible_ssh_password=Am3ric@ ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

**Step 4:** Execute the Ansible playbook to configure hosts.

```sh
ansible-playbook -i inventory playbook.yml
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 82](day-82.md) | [Day 84 →](day-84.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
