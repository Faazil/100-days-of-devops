# Day 73: Jenkins Scheduled Jobs

## Task Overview

Install and configure Jenkins plugins to extend functionality. Plugins add capabilities for build tools, version control, and deployment targets.

**Plugin Management:**
- Access Jenkins plugin manager
- Search and select required plugins
- Install plugins
- Restart Jenkins if needed

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Connect to the target server using SSH.

```sh
echo "app-1-pass" | sudo -S yum install -y sshpass
    echo "app-1-pass" | sudo -S sshpass -p "storage-server-pass" scp -o StrictHostKeyChecking=no -r /var/log/httpd/* natasha@ststor01:/usr/src/itadmin
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 72](day-72.md) | [Day 74 →](day-74.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
