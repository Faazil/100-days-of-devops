# Day 11: Install and Setup Tomcat Server

## Task Overview

Install and configure web server software for hosting applications. Set up HTTP service with custom port and configuration.

**Web Server Setup:**
- Install web server package
- Configure server settings
- Adjust ports and document root
- Start and enable service

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Install packages using the package manager.

```sh
sudo yum install java-1.8.0-openjdk-devel -y
```

**Step 2:** Create a system user with non-interactive shell access disabled.

```sh
sudo groupadd tomcat
    sudo useradd -M -U -d /opt/tomcat -s /bin/nologin -g tomcat tomcat
```

**Step 3:** Create the required directory.

```sh
sudo mkdir /opt/tomcat
```

**Step 4:** Download the required file from the internet.

```sh
wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.80/bin/apache-tomcat-9.0.80.tar.gz

    sudo tar -xf apache-tomcat-9.0.80.tar.gz -C /opt/tomcat --strip-components=1
```

**Step 5:** Change file ownership to the appropriate user.

```sh
sudo chown -R tomcat:tomcat /opt/tomcat
```

**Step 6:** Edit the configuration file to set required parameters.

```sh
sudo vi /etc/systemd/system/tomcat.service
```

**Step 7:** Execute the command to complete this step.

```text
[Unit]
    Description=Apache Tomcat Web Application Container
    After=network.target

    [Service]
    Type=forking
    User=tomcat
    Group=tomcat
    Environment="JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.362.b09-4.el9.x86_64"
    Environment="CATALINA_PID=/opt/tomcat/temp/tomcat.pid"
    Environment="CATALINA_HOME=/opt/tomcat"
    Environment="CATALINA_BASE=/opt/tomcat"
    ExecStart=/opt/tomcat/bin/startup.sh
    ExecStop=/opt/tomcat/bin/shutdown.sh
    RestartSec=10
    Restart=always

    [Install]
    WantedBy=multi-user.target
```

**Step 8:** Enable service to start automatically on boot.

```sh
sudo systemctl daemon-reload
    sudo systemctl enable tomcat
    sudo systemctl start tomcat
```

**Step 9:** Configure firewall to allow traffic on the specified port.

```sh
sudo firewall-cmd --permanent --zone=public --add-port=8080/tcp
    sudo firewall-cmd --reload
```

**Step 10:** Execute the command to complete this step.

```sh
vi /opt/tomcat/conf/server.xml
```

**Step 11:** Configure the resource with required specifications.

```xml
<Connector port="8086" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443"
               maxParameterCount="1000"
               />
```

**Step 12:** Execute the command to complete this step.

```sh
cd /opt/tomcat/webapps
    mv ROOT ROOT.bak
```

**Step 13:** Copy file to remote server using secure copy.

```sh
scp /tmp/ROOT.war tony@stapp01:/home/tony/
```

**Step 14:** Create compressed archive of the directory.

```sh
unzip /home/tony/ROOT.war -d /opt/tomcat/webapps/ROOT
```

**Step 15:** Restart the service to apply changes.

```sh
systemctl restart tomcat
```

**Step 16:** Test the web server by making HTTP request.

```sh
curl http://stapp01:8086
```

**Step 17:** Execute the command to complete this step.

```html
<!DOCTYPE html>
    <!--
    To change this license header, choose License Headers in Project Properties.
    To change this template file, choose Tools | Templates
    and open the template in the editor.
    -->
    <html>
        <head>
            <title>SampleWebApp</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body>
            <h2>Welcome to xFusionCorp Industries!</h2>
            <br>
        
        </body>
    </html>
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 10](day-10.md) | [Day 12 →](day-12.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
