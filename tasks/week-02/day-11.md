# Day 11: Install and Configure Apache Tomcat

## Task Overview

Nautilus dev team members have completed a beta release of their Java application, scheduled for deployment on one of the app servers in Stratos DC. Following team discussions, the decision was made to utilize the Tomcat application server.

**Requirements:**
- Deploy Tomcat on App Server 1
- Set it to listen on port 8086
- Deploy the `ROOT.war` file from Jump host at location `/tmp`
- Ensure the webpage works at the root URL: `curl http://stapp01:8086`

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
ssh <your-username>@<app-server-1>
```

**Step 2:**
```bash
sudo yum install java-1.8.0-openjdk-devel -y
```

**Step 3:**
```bash
java -version
```

**Step 4:**
```bash
openjdk version "1.8.0_362"
OpenJDK Runtime Environment (build 1.8.0_362-b09)
OpenJDK 64-Bit Server VM (build 25.362-b09, mixed mode)
```

**Step 5:**
```bash
sudo groupadd tomcat
sudo useradd -M -U -d /opt/tomcat -s /bin/nologin -g tomcat tomcat
```

**Step 6:**
```bash
sudo mkdir /opt/tomcat
```

**Step 7:**
```bash
wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.80/bin/apache-tomcat-9.0.80.tar.gz
sudo tar -xf apache-tomcat-9.0.80.tar.gz -C /opt/tomcat --strip-components=1
```

**Step 8:**
```bash
wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.80/bin/apache-tomcat-9.0.80.tar.gz
sudo tar -xf apache-tomcat-9.0.80.tar.gz -C /opt/tomcat --strip-components=1
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 10](day-10.md) | [Day 12 →](day-12.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
