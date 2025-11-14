# Day 35: Setup Docker Installation

## Task Overview

The Nautilus DevOps team aims to containerize various applications following a recent meeting with the application development team. They intend to conduct testing with the following steps:

- Install docker-ce and docker compose packages on App Server 2.
- Initiate the docker service.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
cat /etc/os-release
    uname -a
```

**Step 2:**
```bash
[steve@stapp02 ~]$ cat /etc/os-release 
    NAME="CentOS Stream"
    VERSION="9"
    ID="centos"
    ID_LIKE="rhel fedora"
    VERSION_ID="9"
    PLATFORM_ID="platform:el9"
    PRETTY_NAME="CentOS Stream 9"
    ANSI_COLOR="0;31"
    LOGO="fedora-logo-icon"
    CPE_NAME="cpe:/o:centos:centos:9"
    HOME_URL="https://centos.org/"
    BUG_REPORT_URL="https://issues.redhat.com/"
    REDHAT_SUPPORT_PRODUCT="Red Hat Enterprise Linux 9"
    REDHAT_SUPPORT_PRODUCT_VERSION="CentOS Stream"
```

**Step 3:**
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
```

**Step 4:**
```bash
sudo systemctl enable docker.service
    sudo systemctl start docker.service
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 34](day-34.md) | [Day 36 →](../week-06/day-36.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
