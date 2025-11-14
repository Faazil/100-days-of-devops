# Challenge 14: Linux Process Troubleshooting

## 📊 Metadata
- **Day**: 14
- **Week**: 2
- **Day in Week**: 7/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The production support team of xFusionCorp Industries has deployed some of the latest monitoring tools to keep an eye on every service, application, etc. running on the systems. One of the monitoring systems reported about Apache service unavailability on one of the app servers in Stratos DC.

> Identify the faulty app host and fix the issue. Make sure Apache service is up and running on all app hosts. They might not have hosted any code yet on these servers, so you don’t need to worry if Apache isn’t serving any pages. Just make sure the service is up and running. Also, make sure Apache is running on port ***`3004`*** on all app servers.


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
- Day 7: Linux SSH Automation (recommended)
- Day 11: Install and Setup Tomcat Server (recommended)
- Day 12: Linux Network Services (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Login into App server
2. Check httpd status

    ```sh
    root@stapp01 ~]# systemctl status httpd.service
    ● httpd.service - The Apache HTTP Server
    Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
    Active: failed (Result: exit-code) since Fri 2025-08-08 05:04:33 UTC; 12s ago
        Docs: man:httpd(8)
            man:apachectl(8)
    Process: 1004 ExecStop=/bin/kill -WINCH ${MAINPID} (code=exited, status=1/FAILURE)
    Process: 1003 ExecStart=/usr/sbin/httpd $OPTIONS -DFOREGROUND (code=exited, status=1/FAILURE)
    Main PID: 1003 (code=exited, status=1/FAILURE)

    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com systemd[1]: Starting The Apache HTTP Server...
    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com httpd[1003]: (98)Address already in use: AH0007...4
    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com httpd[1003]: no listening sockets available, sh...n
    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com httpd[1003]: AH00015: Unable to open logs
    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com systemd[1]: httpd.service: main process exited,...E
    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com kill[1004]: kill: cannot find process ""
    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com systemd[1]: httpd.service: control process exit...1
    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com systemd[1]: Failed to start The Apache HTTP Server.
    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com systemd[1]: Unit httpd.service entered failed s....
    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com systemd[1]: httpd.service failed.
    Hint: Some lines were ellipsized, use -l to show in full.
    ```

    I see two problems:

    ```shell
    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com httpd[1003]: (98)Address already in use: AH0007...4
    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com httpd[1003]: no listening sockets available, sh...n
    ```

3. Lets check the port status

    ```sh
    sudo netstat -tlnup
    ```

    ```shell
    Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
    tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      1/init              
    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      443/sshd            
    tcp        0      0 127.0.0.11:35047        0.0.0.0:*               LISTEN      -                   
    tcp        0      0 127.0.0.1:3004          0.0.0.0:*               LISTEN      680/sendmail: accep 
    tcp6       0      0 :::111                  :::*                    LISTEN      424/rpcbind         
    tcp6       0      0 :::22                   :::*                    LISTEN      443/sshd            
    udp        0      0 0.0.0.0:111             0.0.0.0:*                           1/init              
    udp        0      0 0.0.0.0:1021            0.0.0.0:*                           424/rpcbind         
    udp        0      0 127.0.0.11:35464        0.0.0.0:*                           -                   
    udp6       0      0 :::111                  :::*                                424/rpcbind         
    udp6       0      0 :::1021                 :::*                                424/rpcbind         
    ```

    So `3004` port already being used by sendmail. We already fixed this port conflict in the [previous day](./012.md). Lets fix the issue using the same way describe there.

4. Verify the status:

    ```sh
    curl http://stapp01:3004 # from jump host
    ```

## Good to Know?

### Process Troubleshooting

- **Service Status**: `systemctl status service-name`
- **Service Logs**: `journalctl -u service-name -f`
- **Process List**: `ps aux | grep process-name`
- **Resource Usage**: `top`, `htop`, `ps aux --sort=-%cpu`

### Port Conflict Diagnosis

- **Active Ports**: `netstat -tlnup` or `ss -tlnup`
- **Process by Port**: `lsof -i :port-number`
- **Kill Process**: `kill -9 PID` (force kill)
- **Service Stop**: `systemctl stop service-name`

### Apache/HTTP Troubleshooting

- **Configuration Test**: `httpd -t` or `nginx -t`
- **Error Logs**: `/var/log/httpd/error_log`
- **Access Logs**: `/var/log/httpd/access_log`
- **Module Status**: `httpd -M` (loaded modules)

### Common Service Issues

- **Port Conflicts**: Multiple services trying to use same port
- **Permission Issues**: Service can't access required files
- **Configuration Errors**: Syntax errors in config files
- **Resource Limits**: Insufficient memory or file descriptors

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

- **← Previous**: [Day 13 - IPtables Installation And Configuration](./day-13.md)
- **Next →**: [Day 15 - Setup SSL for NGINX](../week-03/day-15.md)

### Similar Challenges (Linux)
- [Day 5 - Install and Configuration Selinux](../week-01/day-05.md)
- [Day 6 - Setup a Cron Job](../week-01/day-06.md)
- [Day 7 - Linux SSH Automation](../week-01/day-07.md)

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

