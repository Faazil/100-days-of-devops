# Day 7: Linux SSH Automation

## Task Overview

Develop automation scripts for system administration tasks. Create bash scripts to streamline repetitive operations.

**Script Development:**
- Write bash script
- Implement required logic
- Set executable permissions
- Test script functionality

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Generate SSH key pair for password-less authentication.

```sh
ssh-keygen -t rsa -b 2048
```

**Step 2:** Create the required directory.

```sh
mkdir -p .ssh
    vi .ssh/authorized_keys
```

**Step 3:** Connect to the target server using SSH.

```sh
#!/bin/sh

ssh-copy-id user@host
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 6](day-06.md) | [Day 8 →](../week-02/day-08.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
