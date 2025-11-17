# Day 3: Secure SSH Root Access

## Task Overview

Complete the secure ssh root access task according to the specifications provided in the KodeKloud Engineer platform.

**Task Focus:**
- Follow lab environment instructions
- Execute configuration steps
- Verify successful completion
- Test functionality

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Modify SSH configuration to disable root login.

```sh
sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config
    sudo systemctl restart sshd
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 2](day-02.md) | [Day 4 →](day-04.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
