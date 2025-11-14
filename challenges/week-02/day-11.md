# Challenge 11: Install and Setup Tomcat Server

## 📊 Metadata
- **Day**: 11
- **Week**: 2
- **Day in Week**: 4/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus application development team recently finished the beta version of one of their Java-based applications, which they are planning to deploy on one of the app servers in Stratos DC. After an internal team meeting, they have decided to use the tomcat application server. Based on the requirements mentioned below complete the task:

- Install tomcat server on `App Server 1`.
- Configure it to run on port `8086`.
- There is a `ROOT.war` file on Jump host at location `/tmp`.

Deploy it on this tomcat server and make sure the webpage works directly on base URL i.e `curl http://stapp01:8086`


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `ssh`, `sudo`, `useradd`, `cat`, `grep`
- **Key Concepts**:
  - SSH remote access
  - User and group management
  - File permissions and ownership
  - Linux file system hierarchy

**Foundation from Earlier Challenges:**
- Day 5: Install and Configuration Selinux (recommended)
- Day 6: Setup a Cron Job (recommended)
- Day 7: Linux SSH Automation (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Install JVM

    ```sh
    sudo yum install java-1.8.0-openjdk-devel -y
    ```

2. Create `tomcat` user

    ```sh
    sudo groupadd tomcat
    sudo useradd -M -U -d /opt/tomcat -s /bin/nologin -g tomcat tomcat
    ```

3. Create `/opt/tomcat` directory

    ```sh
    sudo mkdir /opt/tomcat
    ```

4. Download tomcat and Extract

    ```sh
    wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.80/bin/apache-tomcat-9.0.80.tar.gz

    sudo tar -xf apache-tomcat-9.0.80.tar.gz -C /opt/tomcat --strip-components=1
    ```

5. Set Permissions

    ```sh
    sudo chown -R tomcat:tomcat /opt/tomcat
    ```

6. Create a systemd service

    ```sh
    sudo vi /etc/systemd/system/tomcat.service
    ```

    Copy and paste the following lines:

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

7. Start daemon service

    ```sh
    sudo systemctl daemon-reload
    sudo systemctl enable tomcat
    sudo systemctl start tomcat
    ```

8. Setup firewall, you can skip this step

    ```sh
    sudo firewall-cmd --permanent --zone=public --add-port=8080/tcp
    sudo firewall-cmd --reload
    ```

9. Test you can access using `curl http://stapp01:8080`. Now lets modify the port and deploy ROOT.war

10. To modify the port edit the `/opt/tomcat/conf/server.xml` and change port 8080 to 8086

    ```sh
    vi /opt/tomcat/conf/server.xml
    ```

    ```xml
     <Connector port="8086" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443"
               maxParameterCount="1000"
               />
    ```

11. Take backup of `/opt/tomcat/webapps/ROOT`

    ```sh
    cd /opt/tomcat/webapps
    mv ROOT ROOT.bak
    ```

12. Copy `/tmp/ROOT.war` from jump host server to app server.

    ```sh
    scp /tmp/ROOT.war tony@stapp01:/home/tony/
    ```

13. Unzip the ROOT.war

    ```sh
    unzip /home/tony/ROOT.war -d /opt/tomcat/webapps/ROOT
    ```

14. Restart tomcat service

    ```sh
    systemctl restart tomcat
    ```

15. Test

    ```sh
    curl http://stapp01:8086
    ```

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

## Good to Know?

### Apache Tomcat Fundamentals

- **Purpose**: Java servlet container and web server
- **Architecture**: Catalina (servlet container), Coyote (HTTP connector), Jasper (JSP engine)
- **Default Port**: 8080 (HTTP), 8443 (HTTPS), 8005 (shutdown)
- **Directory Structure**: `/bin` (scripts), `/conf` (config), `/webapps` (applications)

### Java Application Deployment

- **WAR Files**: Web Application Archive containing servlets, JSPs, static files
- **ROOT Application**: Default application served at context root `/`
- **Context Path**: URL path where application is accessible
- **Hot Deployment**: Deploy without stopping server

### Tomcat Configuration

- **server.xml**: Main configuration file
- **web.xml**: Web application descriptor
- **tomcat-users.xml**: User authentication
- **catalina.properties**: System properties

### Security Best Practices

- **Dedicated User**: Run Tomcat as non-root user
- **File Permissions**: Restrict access to configuration files
- **Manager App**: Secure or remove default applications
- **SSL/TLS**: Enable HTTPS for production

---

## ✅ Verification

After completing the challenge, verify your solution by:

1. **Testing the implementation**
   - Run all commands from the solution
   - Check for any error messages

2. **Validating the results**
   - Ensure all requirements are met
   - Test edge cases if applicable

3. **Clean up (if needed)**
   - Remove temporary files
   - Reset any test configurations

---

## 📚 Learning Notes

### Key Concepts

This challenge covers the following concepts:
- Practical application of Linux skills
- Real-world DevOps scenarios
- Best practices for production environments

### Common Pitfalls

- ⚠️ **Permissions**: Ensure you have the necessary permissions to execute commands
- ⚠️ **Syntax**: Double-check command syntax and flags
- ⚠️ **Environment**: Verify you're working in the correct environment/server

### Best Practices

- ✅ Always verify changes before marking as complete
- ✅ Test your solution in a safe environment first
- ✅ Document any deviations from the standard approach
- ✅ Keep security in mind for all configurations

---

## 🔗 Related Challenges

- **← Previous**: [Day 10 - Create a BASH Script](./day-10.md)
- **Next →**: [Day 12 - Linux Network Services](../week-02/day-12.md)

### Similar Challenges (Linux)
- [Day 1 - Linux User Setup with Non-interactive Shell](../week-01/day-01.md)
- [Day 2 - Temporary User Setup with Expiry Date](../week-01/day-02.md)
- [Day 3 - Secure SSH Root Access](../week-01/day-03.md)

---

## 📖 Additional Resources

- [KodeKloud Official Documentation](https://kodekloud.com)
- [Official Technology Documentation](#)
- [Community Discussions](#)

---

## 🎓 Knowledge Check

After completing this challenge, you should be able to:
- [ ] Understand the problem statement clearly
- [ ] Implement the solution independently
- [ ] Verify the solution works correctly
- [ ] Explain the concepts to others
- [ ] Apply these skills to similar problems

---

**Challenge Source**: KodeKloud 100 Days of DevOps
**Difficulty**: {get_difficulty_emoji(day)}
**Category**: {task_info['category']}

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
python3 ../../tools/progress.py --complete {day}
```

