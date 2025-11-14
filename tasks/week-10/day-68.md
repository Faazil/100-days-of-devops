# Day 68: Set Up Jenkins Server

## Task Overview

The DevOps team at xFusionCorp Industries is initiating the setup of CI/CD pipelines and has decided to utilize Jenkins as their server. Execute the task according to the provided requirements:

1. Install Jenkins on the jenkins server using the yum utility only, and start its service.
    - If you face a timeout issue while starting the Jenkins service, refer to [this](https://www.jenkins.io/doc/book/system-administration/systemd-services/#starting-services).
2. Jenkin's admin user name should be `theadmin`, password should be `Adm!n321`, full name should be `John` and email should be `john@jenkins.stratos.xfusioncorp.com`.

Note:

1. To access the jenkins server, connect from the jump host using the `root` user with the password `S3curePass`.

2. After Jenkins server installation, click the Jenkins button on the top bar to access the Jenkins UI and follow on-screen instructions to create an admin user.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
ssh root@jenkins
```

**Step 2:**
```bash
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

**Step 3:**
```bash
yum update -y
    yum install -y wget
```

**Step 4:**
```bash
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
    sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
    sudo dnf upgrade -y
    # Add required dependencies for the jenkins package
    sudo dnf install fontconfig java-21-openjdk -y
    sudo dnf install jenkins -y
    sudo systemctl daemon-reload
```

**Step 5:**
```bash
sudo systemctl enable --now jenkins
```

**Step 6:**
```bash
cat /var/lib/jenkins/secrets/initialAdminPassword
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 67](day-67.md) | [Day 69 →](day-69.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
