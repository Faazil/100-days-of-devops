# Day 3: Secure SSH Root Access

## Task Overview

Disable all app server SSH root access.

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
sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config
```

**Step 3:**
```bash
sudo systemctl restart sshd
```

**Step 4:**
```bash
grep PermitRootLogin /etc/ssh/sshd_config
```

**Step 5:**
```bash
PermitRootLogin no
```

**Step 6:**
```bash
# Edit file manually if you prefer
sudo vi /etc/ssh/sshd_config

# Find this line:
#PermitRootLogin yes

# Change to:
PermitRootLogin no

# Save and exit, then test config
sudo sshd -t

# If no errors, restart
sudo systemctl restart sshd
```

**Step 7:**
```bash
# Disable password authentication (use keys only)
PasswordAuthentication no

# Change default SSH port
Port 2222

# Limit users who can SSH
AllowUsers user1 user2

# Enable key-based authentication only
PubkeyAuthentication yes
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 2](day-02.md) | [Day 4 →](day-04.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
