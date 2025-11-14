# Day 5: Install and Configuration Selinux

## Task Overview

Following a security audit, the xFusionCorp Industries security team has opted to enhance application and server security with SELinux. To initiate testing, the following requirements have been established for App server 2 in the Stratos Datacenter:

- Install the required SELinux packages
- Permanently disable SELinux for the time being (it will be re-enabled after necessary configuration changes)
- No need to reboot the server (a scheduled maintenance reboot is planned for tonight)
- Disregard the current status via command line; the final status after reboot should be disabled

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
ssh <your-username>@<server-name>
```

**Step 2:**
```bash
sudo dnf install selinux-policy selinux-policy-targeted policycoreutils policycoreutils-python-utils -y
```

**Step 3:**
```bash
sudo vi /etc/selinux/config
```

**Step 4:**
```bash
SELINUX=enforcing
```

**Step 5:**
```bash
SELINUX=disabled
```

**Step 6:**
```bash
cat /etc/selinux/config | grep SELINUX=
```

**Step 7:**
```bash
SELINUX=disabled
```

**Step 8:**
```bash
# Using nano (easier for beginners)
sudo nano /etc/selinux/config

# Using sed (one-liner)
sudo sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 4](day-04.md) | [Day 6 →](day-06.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
