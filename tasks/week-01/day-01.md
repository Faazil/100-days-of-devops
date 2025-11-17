# Day 1: Linux User Setup with Non-interactive Shell

## Task Overview

Configure a system user account with shell access disabled. This type of account serves automation workflows and service operations that don't need interactive terminal sessions.

**Technical Specifications:**
- User account: service/system user type
- Shell assignment: /usr/sbin/nologin (prevents interactive login)
- Home directory: automatically created
- Access level: restricted (no shell access)

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Connect to the target server using SSH.

```sh
ssh user@app-server-ip or ssh user@server-name
```

**Step 2:** Create a system user with non-interactive shell access disabled.

```sh
sudo useradd -m -s /usr/sbin/nologin user-name
```

**Step 3:** Verify the user was created and check its configuration.

```sh
cat /etc/passwd
```

**Step 4:** Attempt to switch to the user and verify login is blocked.

```sh
sudo su user-name
```

**Step 5:** Verify the user was created and check its configuration.

```bash
# List all users with nologin shell
grep nologin /etc/passwd

# Check user details
id username

# Remove user if needed
sudo userdel -r username
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[Day 2 →](day-02.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
