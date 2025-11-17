# Day 5: Install and Configuration Selinux

## Task Overview

Configure SELinux security framework on Linux systems. Manage mandatory access control policies for enhanced security.

**SELinux Configuration:**
- Install SELinux packages
- Set enforcement mode
- Configure persistent settings
- Verify configuration

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Install SELinux packages using the package manager.

```sh
sudo dnf install selinux-policy selinux-policy-targeted policycoreutils policycoreutils-python-utils
```

**Step 2:** Edit the configuration file to set required parameters.

```sh
vi /etc/selinux/config
```

**Step 3:** Execute the command to complete this step.

```nano
SELINUX=disabled
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 4](day-04.md) | [Day 6 →](day-06.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
