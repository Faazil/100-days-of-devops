# Day 68: Set Up Jenkins Server

## Task Overview

Configure Jenkins pipeline for automated build and deployment workflows. Pipelines define CI/CD processes as code.

**Pipeline Configuration:**
- Create pipeline job in Jenkins
- Define pipeline stages
- Configure build and deployment steps
- Integrate with version control

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Connect to the target server using SSH.

```bash
ssh root@jenkins
```

**Step 2:** Execute the command to complete this step.

```shell
cat /etc/os-release 
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

**Step 3:** Install packages using the package manager.

```sh
yum update -y
    yum install -y wget
```

**Step 4:** Install packages using the package manager.

```sh
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
    sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
    sudo dnf upgrade -y
    # Add required dependencies for the jenkins package
    sudo dnf install fontconfig java-21-openjdk -y
    sudo dnf install jenkins -y
    sudo systemctl daemon-reload
```

**Step 5:** Enable service to start automatically on boot.

```sh
sudo systemctl enable --now jenkins
```

**Step 6:** Execute the command to complete this step.

```sh
cat /var/lib/jenkins/secrets/initialAdminPassword
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 67](day-67.md) | [Day 69 →](day-69.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
