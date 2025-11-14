# Day 4: Script Execute Permissions

## Task Overview

In a bid to automate backup processes, the xFusionCorp Industries sysadmin team has developed a new bash script named `xfusioncorp.sh`. While the script has been distributed to all necessary servers, it lacks executable permissions on App Server 1 within the Stratos Datacenter.

Your task is to grant executable permissions to the `/tmp/xfusioncorp.sh` script on App Server 1. Additionally, ensure that all users have the capability to execute it.

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
ls -la /tmp/xfusioncorp.sh
```

**Step 3:**
```bash
---------- 1 root root 40 Nov 14 10:30 /tmp/xfusioncorp.sh
```

**Step 4:**
```bash
chmod 755 /tmp/xfusioncorp.sh
```

**Step 5:**
```bash
ls -la /tmp/xfusioncorp.sh
```

**Step 6:**
```bash
-rwxr-xr-x 1 root root 40 Nov 14 10:30 /tmp/xfusioncorp.sh
```

**Step 7:**
```bash
Owner  Group  Others
 7      5      5
rwx    r-x    r-x

Numbers mean:
4 = read (r)
2 = write (w)
1 = execute (x)

Add them up:
7 = 4+2+1 = rwx (all permissions)
5 = 4+1 = r-x (read + execute)
6 = 4+2 = rw- (read + write)
```

**Step 8:**
```bash
chmod 755 script.sh   # Standard executable
chmod 644 file.txt    # Standard file (no execute)
chmod 600 secret.txt  # Private file (owner only)
chmod 777 file.sh     # Full access (dangerous!)
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 3](day-03.md) | [Day 5 →](day-05.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
