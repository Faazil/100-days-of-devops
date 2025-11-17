# Day 4: Script Execute Permissions

## Task Overview

Execute Git version control operations for source code management. Track changes, collaborate, and maintain project history.

**Git Operations:**
- Configure Git settings
- Perform repository operations
- Manage commits and history
- Collaborate with remotes

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Perform the initial setup or connection.

```sh
ls -la /tmp
```

**Step 2:** Execute the command to complete this step.

```txt
4 ---------- 1 root root   40 Jul 30 02:21 xfusioncorp.sh
```

**Step 3:** Make the script executable for all users.

```sh
chmod 755 /tmp/xfusioncorp.sh
```

**Step 4:** Execute the command to complete this step.

```sh
ls -la /tmp
```

**Step 5:** Execute the command to complete this step.

```txt
4 -rwxr-xr-x 1 root root   40 Jul 30 02:21 xfusioncorp.sh
```

**Step 6:** Set appropriate file permissions.

```sh
chmod u=rwx,g=rx,o=r test.sh
```

**Step 7:** Set appropriate file permissions.

```sh
chmod g+w test.sh     # Add write permission for group
    chmod o-r test.sh     # Remove read permission for others
```

**Step 8:** Set appropriate file permissions.

```sh
chmod 754 test.sh
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 3](day-03.md) | [Day 5 →](day-05.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
