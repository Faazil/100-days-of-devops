# Day 14: Linux Process Troubleshooting

## Task Overview

The operations team at xFusionCorp Industries has deployed some of the latest monitoring tools to keep an eye on every service, application, etc. running on the systems. One of the monitoring systems reported about Apache service unavailability on one of the app servers in Stratos DC.

> Identify the faulty app host and fix the issue. Ensure Apache service is up and running on all app hosts. They might not have hosted any code yet on these servers, so you don’t need to worry if Apache isn’t serving any pages. Just make sure the service is up and running. Also, make sure Apache is running on port ***`3004`*** on all app servers.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
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

**Step 2:**
```bash
Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com httpd[1003]: (98)Address already in use: AH0007...4
    Aug 08 05:04:33 stapp01.stratos.xfusioncorp.com httpd[1003]: no listening sockets available, sh...n
```

**Step 3:**
```bash
sudo netstat -tlnup
```

**Step 4:**
```bash
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

**Step 5:**
```bash
curl http://stapp01:3004 # from jump host
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 13](day-13.md) | [Day 15 →](../week-03/day-15.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
