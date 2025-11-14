# Day 86: Ansible Ping Module Usage

## Task Overview

The Nautilus DevOps team is planning to test several Ansible playbooks on different app servers in Stratos DC. Before that, some pre-requisites must be met. Essentially, the team needs to set up a password-less SSH connection between Ansible controller and Ansible managed nodes. One of the tickets is assigned to you; please fulfill this objective as per details mentioned below:

a. Jump host is our Ansible controller, and we are going to run Ansible playbooks through thor user from jump host.

b. An inventory file `/home/thor/ansible/inventory` on jump host. Using that inventory file test Ansible ping from jump host to App Server 3, make sure ping works.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
stapp01 ansible_host=172.16.238.10 ansible_user=tony ansible_ssh_pass=Ir0nM@n
    stapp02 ansible_host=172.16.238.11 ansible_user=steve ansible_ssh_pass=Am3ric@
    stapp03 ansible_host=172.16.238.12 ansible_user=banner ansible_ssh_pass=BigGr33n

    [all:vars]
    ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

**Step 2:**
```bash
ansible all -i inventory -m ping
```

**Step 3:**
```bash
ansible stapp03 -i inventory -m ping
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 85](day-85.md) | [Day 87 →](day-87.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
