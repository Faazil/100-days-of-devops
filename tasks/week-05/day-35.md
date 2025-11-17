# Day 35: Setup Docker Installation

## Task Overview

Create a Docker Compose configuration file to orchestrate multi-container applications. Docker Compose defines services, networks, and volumes in a single YAML file.

**Compose Configuration:**
- Define services and their configurations
- Specify container images and build contexts
- Configure ports, volumes, and networks
- Enable multi-container application deployment

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Perform the initial setup or connection.

```sh
cat /etc/os-release
    uname -a
```

**Step 2:** Execute the command to complete this step.

```shell
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

**Step 3:** Execute the command to complete this step.

```sh
curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
```

**Step 4:** Enable service to start automatically on boot.

```sh
sudo systemctl enable docker.service
    sudo systemctl start docker.service
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 34](day-34.md) | [Day 36 →](../week-06/day-36.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
