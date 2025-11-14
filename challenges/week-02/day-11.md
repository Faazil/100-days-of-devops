# Challenge 11: Install and Configure Apache Tomcat

## 📊 Metadata
- **Day**: 11
- **Week**: 2
- **Day in Week**: 4/7
- **Category**: Linux
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 40-50 minutes

---

## 🎯 Challenge Scenario

The Nautilus application development team recently finished the beta version of one of their Java-based applications, which they are planning to deploy on one of the app servers in Stratos DC. After an internal team meeting, they have decided to use the Tomcat application server.

**Requirements:**
- Install Tomcat server on App Server 1
- Configure it to run on port 8086
- Deploy the `ROOT.war` file from Jump host at location `/tmp`
- Ensure the webpage works directly on base URL: `curl http://stapp01:8086`

> **Lab Environment**: Complete this challenge on [KodeKloud Engineer](https://engineer.kodekloud.com/practice) platform with pre-configured lab infrastructure.

---

## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ App Server 1 and Jump host
- ✅ ROOT.war file at `/tmp` on Jump host
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `wget`, `tar`, `systemctl`, `scp`, `unzip`
- **Key Concepts**:
  - Java application servers
  - WAR file deployment
  - Systemd service creation
  - File permissions and ownership
  - Port configuration

**Required Skills:**
- ✅ Install and configure Java (JDK/JRE)
- ✅ Download and extract archives
- ✅ Create systemd service units
- ✅ Deploy Java web applications
- ✅ Troubleshoot service issues

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

## 💡 Understanding the Task

**What is Apache Tomcat?**

Tomcat is an open-source Java servlet container and web server developed by the Apache Software Foundation. It's the go-to choice for hosting Java web applications, JSPs (JavaServer Pages), and servlets.

**Why Tomcat?**
- **Lightweight**: No full Java EE stack overhead
- **Popular**: Industry-standard for Java web apps
- **Easy to deploy**: Drop WAR files and go
- **Open source**: Free and well-documented

**WAR Files Explained:**

WAR (Web Application Archive) files are:
- Packaged Java web applications
- Contain servlets, JSPs, HTML, JavaScript, CSS
- Deployed by dropping into Tomcat's `webapps/` directory
- Automatically extracted and deployed by Tomcat

**ROOT Application:**

The `ROOT` web application in Tomcat is special:
- Accessible at the root URL (`http://server:port/`)
- No context path needed
- Default application for the server

---

## 📝 Solution

### Step 1: Connect to App Server 1

SSH into the target app server:

```bash
ssh <your-username>@<app-server-1>
```

💡 **Example:** `ssh tony@stapp01`

---

### Step 2: Install Java Development Kit

Tomcat requires Java to run. Install OpenJDK:

```bash
sudo yum install java-1.8.0-openjdk-devel -y
```

💡 **Example:** `sudo yum install java-1.8.0-openjdk-devel -y`

**What this installs:**
- Java Runtime Environment (JRE) - to run Java apps
- Java Development Kit (JDK) - includes development tools
- Version 1.8.0 (Java 8) - stable, widely supported

**Verify installation:**
```bash
java -version
```

**Expected output:**
```
openjdk version "1.8.0_362"
OpenJDK Runtime Environment (build 1.8.0_362-b09)
OpenJDK 64-Bit Server VM (build 25.362-b09, mixed mode)
```

---

### Step 3: Create Tomcat User

Create a dedicated user to run Tomcat (security best practice):

```bash
sudo groupadd tomcat
sudo useradd -M -U -d /opt/tomcat -s /bin/nologin -g tomcat tomcat
```

💡 **Example:** `sudo groupadd tomcat && sudo useradd -M -U -d /opt/tomcat -s /bin/nologin -g tomcat tomcat`

**What these options mean:**
- `-M` - Don't create a home directory
- `-U` - Create a group with the same name as the user
- `-d /opt/tomcat` - Set home directory (but don't create it)
- `-s /bin/nologin` - Non-interactive shell (can't login directly)
- `-g tomcat` - Primary group is 'tomcat'

**Why a dedicated user?**
- Security: Limited privileges
- Isolation: Separate from other services
- Best practice: Don't run services as root

---

### Step 4: Create Tomcat Directory

Create the directory where Tomcat will live:

```bash
sudo mkdir /opt/tomcat
```

💡 **Example:** `sudo mkdir /opt/tomcat`

---

### Step 5: Download and Extract Tomcat

Download Tomcat 9 and extract it:

```bash
wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.80/bin/apache-tomcat-9.0.80.tar.gz
sudo tar -xf apache-tomcat-9.0.80.tar.gz -C /opt/tomcat --strip-components=1
```

💡 **Example:**
```bash
wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.80/bin/apache-tomcat-9.0.80.tar.gz
sudo tar -xf apache-tomcat-9.0.80.tar.gz -C /opt/tomcat --strip-components=1
```

**What these commands do:**
- `wget` - Download Tomcat archive from Apache
- `tar -xf` - Extract the tar.gz file
- `-C /opt/tomcat` - Extract to this directory
- `--strip-components=1` - Remove the top-level directory from archive (so files go directly into /opt/tomcat, not /opt/tomcat/apache-tomcat-9.0.80/)

---

### Step 6: Set Ownership and Permissions

Give the tomcat user ownership of the installation:

```bash
sudo chown -R tomcat:tomcat /opt/tomcat
```

💡 **Example:** `sudo chown -R tomcat:tomcat /opt/tomcat`

**Why this matters:**
- Tomcat process runs as 'tomcat' user
- Must be able to read/write its own files
- Security: Other users can't modify Tomcat files

---

### Step 7: Find Java Home Path

Tomcat needs to know where Java is installed:

```bash
sudo find /usr/lib/jvm -name "java-1.8.0-openjdk*" -type d
```

💡 **Example:** `sudo find /usr/lib/jvm -name "java-1.8.0-openjdk*" -type d`

**Expected output:**
```
/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.362.b09-4.el9.x86_64
```

Copy this path - you'll need it in the next step.

---

### Step 8: Create Systemd Service File

Create a systemd unit file to manage Tomcat as a service:

```bash
sudo vi /etc/systemd/system/tomcat.service
```

**Add the following content:**

```ini
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

**Important:** Replace the `JAVA_HOME` path with the actual path from Step 7!

**What this file does:**
- `[Unit]` - Service metadata
- `After=network.target` - Start after network is available
- `Type=forking` - Tomcat forks background processes
- `User=tomcat` - Run as tomcat user
- `Environment` - Set required environment variables
- `ExecStart` - Command to start Tomcat
- `ExecStop` - Command to stop Tomcat
- `Restart=always` - Auto-restart if it crashes
- `WantedBy=multi-user.target` - Enable on boot

---

### Step 9: Start and Enable Tomcat

Reload systemd, enable, and start Tomcat:

```bash
sudo systemctl daemon-reload
sudo systemctl enable tomcat
sudo systemctl start tomcat
```

💡 **Example:** `sudo systemctl daemon-reload && sudo systemctl enable tomcat && sudo systemctl start tomcat`

**Verify it's running:**
```bash
sudo systemctl status tomcat
```

**Expected output:**
```
● tomcat.service - Apache Tomcat Web Application Container
   Loaded: loaded (/etc/systemd/system/tomcat.service; enabled; vendor preset: disabled)
   Active: active (running) since Sun 2025-08-10 12:30:45 UTC; 5s ago
  Process: 1234 ExecStart=/opt/tomcat/bin/startup.sh (code=exited, status=0/SUCCESS)
 Main PID: 1235 (java)
```

Look for `Active: active (running)` - that's success!

---

### Step 10: Test Default Tomcat (Port 8080)

Tomcat starts on port 8080 by default. Test it:

```bash
curl http://localhost:8080
```

💡 **Example:** `curl http://localhost:8080`

You should see HTML output from Tomcat's default page.

---

### Step 11: Change Tomcat Port to 8086

Edit the server configuration to change the port:

```bash
sudo vi /opt/tomcat/conf/server.xml
```

**Find this line (around line 69):**
```xml
<Connector port="8080" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="8443"
           maxParameterCount="1000" />
```

**Change `8080` to `8086`:**
```xml
<Connector port="8086" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="8443"
           maxParameterCount="1000" />
```

Save and exit.

---

### Step 12: Backup Default ROOT Application

Tomcat comes with a default ROOT app. Back it up:

```bash
cd /opt/tomcat/webapps
sudo mv ROOT ROOT.bak
```

💡 **Example:** `cd /opt/tomcat/webapps && sudo mv ROOT ROOT.bak`

---

### Step 13: Copy ROOT.war from Jump Host

From the **jump host**, copy the WAR file to the app server:

```bash
scp /tmp/ROOT.war tony@stapp01:/home/tony/
```

💡 **Example:** `scp /tmp/ROOT.war tony@stapp01:/home/tony/`

---

### Step 14: Deploy the WAR File

Back on **App Server 1**, deploy the WAR file:

**Option A: Let Tomcat auto-extract (recommended):**
```bash
sudo cp /home/tony/ROOT.war /opt/tomcat/webapps/
sudo chown tomcat:tomcat /opt/tomcat/webapps/ROOT.war
```

Tomcat will automatically extract ROOT.war to a ROOT directory.

**Option B: Manual extraction:**
```bash
sudo mkdir /opt/tomcat/webapps/ROOT
sudo unzip /home/tony/ROOT.war -d /opt/tomcat/webapps/ROOT
sudo chown -R tomcat:tomcat /opt/tomcat/webapps/ROOT
```

---

### Step 15: Restart Tomcat

Apply all changes by restarting Tomcat:

```bash
sudo systemctl restart tomcat
```

💡 **Example:** `sudo systemctl restart tomcat`

Wait 5-10 seconds for Tomcat to fully start.

---

### Step 16: Test the Deployment

Test from the app server:

```bash
curl http://localhost:8086
```

Test from the jump host:

```bash
curl http://stapp01:8086
```

💡 **Example:** `curl http://stapp01:8086`

**Expected output:**
```html
<!DOCTYPE html>
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

Success! Your Java application is deployed and running!

---

## ✅ Verification Checklist

Before marking this challenge complete, verify:

- [ ] Java 1.8.0 installed (`java -version`)
- [ ] Tomcat user created (`id tomcat`)
- [ ] Tomcat installed in `/opt/tomcat`
- [ ] Systemd service created and enabled (`systemctl is-enabled tomcat`)
- [ ] Tomcat is running (`systemctl status tomcat`)
- [ ] Port changed to 8086 (check `/opt/tomcat/conf/server.xml`)
- [ ] ROOT.war deployed in `/opt/tomcat/webapps/`
- [ ] Application accessible on port 8086 (`curl http://stapp01:8086`)
- [ ] HTML output displays correctly
- [ ] KodeKloud validation passes

---

## 🔧 Troubleshooting

**Tomcat won't start:**
- Check Java is installed: `java -version`
- Check JAVA_HOME path in service file matches: `cat /etc/systemd/system/tomcat.service`
- View logs: `sudo journalctl -u tomcat -n 50`
- Check Tomcat logs: `sudo tail -f /opt/tomcat/logs/catalina.out`

**Port 8086 not accessible:**
- Verify Tomcat is listening: `sudo netstat -tlnp | grep 8086`
- Check firewall: `sudo firewall-cmd --list-ports` (may need to allow port)
- Ensure server.xml has correct port
- Restart after config changes: `sudo systemctl restart tomcat`

**ROOT.war not deploying:**
- Check file exists: `ls -l /opt/tomcat/webapps/ROOT.war`
- Check permissions: Should be owned by tomcat:tomcat
- Check Tomcat logs for errors: `sudo tail -f /opt/tomcat/logs/catalina.out`
- Manually extract if auto-deploy fails

**Application shows error page:**
- Check WAR file isn't corrupted: `file /opt/tomcat/webapps/ROOT.war`
- Verify extraction: `ls -la /opt/tomcat/webapps/ROOT/`
- Check application logs: `sudo tail -f /opt/tomcat/logs/localhost.*.log`

**Permission denied errors:**
- Ensure tomcat user owns all files: `sudo chown -R tomcat:tomcat /opt/tomcat`
- Check execute permissions on scripts: `ls -l /opt/tomcat/bin/*.sh`
- Fix if needed: `sudo chmod +x /opt/tomcat/bin/*.sh`

---

## 💡 Good to Know

**Tomcat Directory Structure:**

```
/opt/tomcat/
├── bin/          # Scripts (startup.sh, shutdown.sh)
├── conf/         # Configuration files (server.xml, web.xml)
├── lib/          # Java libraries
├── logs/         # Log files (catalina.out, access logs)
├── temp/         # Temporary files
├── webapps/      # Web applications (deploy WARs here)
└── work/         # Compiled JSPs, working files
```

**Important Configuration Files:**

```bash
# Main server configuration
/opt/tomcat/conf/server.xml

# Web application defaults
/opt/tomcat/conf/web.xml

# User authentication (manager app)
/opt/tomcat/conf/tomcat-users.xml

# Logging configuration
/opt/tomcat/conf/logging.properties
```

**Useful Tomcat Commands:**

```bash
# View live logs
sudo tail -f /opt/tomcat/logs/catalina.out

# Check Java processes
ps aux | grep tomcat

# See what port Tomcat is using
sudo netstat -tlnp | grep java

# Restart Tomcat
sudo systemctl restart tomcat

# Stop Tomcat
sudo systemctl stop tomcat

# Start Tomcat
sudo systemctl start tomcat
```

**Multiple Applications:**

Deploy additional apps alongside ROOT:

```bash
# Copy WAR file
sudo cp myapp.war /opt/tomcat/webapps/

# Accessible at:
# http://server:8086/myapp/
```

**Production Hardening:**

```bash
# Remove default apps
sudo rm -rf /opt/tomcat/webapps/docs
sudo rm -rf /opt/tomcat/webapps/examples
sudo rm -rf /opt/tomcat/webapps/host-manager
sudo rm -rf /opt/tomcat/webapps/manager

# Enable SSL (HTTPS)
# Edit /opt/tomcat/conf/server.xml
# Add HTTPS Connector on port 8443

# Limit memory usage
# Add to tomcat.service:
Environment="CATALINA_OPTS=-Xms512M -Xmx1024M"
```

**Real-World Usage:**

In production environments:
- Use Tomcat behind a reverse proxy (Nginx/Apache)
- Enable SSL/TLS for HTTPS
- Configure connection pooling
- Set up log rotation
- Monitor with tools like JMX
- Use Tomcat clustering for high availability
- Implement CI/CD pipelines for deployments

---

## 📚 Navigation

- **← Previous**: [Day 10 - Create Backup Script with SSH](./day-10.md)
- **Next →**: [Day 12 - Linux Network Services](./day-12.md)

**🔗 Challenge Source**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

---

*Java applications deployed - Tomcat is serving!*
