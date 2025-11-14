# Day 8: Install Ansible with pip3

## Task Overview

During the weekly meeting, the Nautilus DevOps team discussed automation and configuration management solutions. After considering several options, the team decided to go with Ansible due to its simple setup and minimal prerequisites. They want to start testing using Ansible, with the jump host as an Ansible controller to test different tasks on the other servers.

Install ansible version 4.8.0 on Jump host using pip3 only. Ensure Ansible binary is available globally on this system, so all users can run Ansible commands.

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
ssh <your-username>@<jump-host>
```

**Step 2:**
```bash
sudo pip3 install ansible==4.8.0
```

**Step 3:**
```bash
Collecting ansible==4.8.0
  Downloading ansible-4.8.0.tar.gz (35.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.6/35.6 MB 50.0 MB/s eta 0:00:00
Collecting ansible-core~=2.11.6
  Downloading ansible-core-2.11.12.tar.gz (7.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 80.0 MB/s eta 0:00:00
...
Successfully installed ansible-4.8.0 ansible-core-2.11.12
```

**Step 4:**
```bash
ansible --version
```

**Step 5:**
```bash
ansible [core 2.11.12]
  config file = None
  configured module search path = ['/home/thor/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.9/site-packages/ansible
  ansible collection location = /home/thor/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/local/bin/ansible
  python version = 3.9.18 (main, Jan 24 2024, 00:00:00) [GCC 11.4.1 20230605 (Red Hat 11.4.1-2)]
  jinja version = 3.1.3
  libyaml = True
```

**Step 6:**
```bash
which ansible
```

**Step 7:**
```bash
/usr/local/bin/ansible
```

**Step 8:**
```bash
# OS package manager (may not have exact version)
sudo yum install ansible           # RHEL/CentOS
sudo apt install ansible           # Ubuntu/Debian

# Python virtual environment (isolated installation)
python3 -m venv ansible-env
source ansible-env/bin/activate
pip install ansible==4.8.0

# From source (for development)
git clone https://github.com/ansible/ansible.git
cd ansible
pip install -e .
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 7](../week-01/day-07.md) | [Day 9 →](day-09.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
