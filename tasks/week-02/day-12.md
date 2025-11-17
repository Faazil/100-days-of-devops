# Day 12: Linux Network Services

## Task Overview

Execute Git version control operations for source code management. Track changes, collaborate, and maintain project history.

**Git Operations:**
- Configure Git settings
- Perform repository operations
- Manage commits and history
- Collaborate with remotes

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Check the service status to verify it's running.

```shell
tony@stapp01 ~]$ sudo systemctl status httpd
    ● httpd.service - The Apache HTTP Server
    Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset
    : disabled)
    Active: failed (Result: exit-code) since Wed 2025-08-06 01:38:21 UT
    C; 13min ago
        Docs: man:httpd.service(8)
    Process: 491 ExecStart=/usr/sbin/httpd $OPTIONS -DFOREGROUND (code=exit
    ed, status=1/FAILURE)
    Main PID: 491 (code=exited, status=1/FAILURE)
    Status: "Reading configuration..."

    Aug 06 01:38:21 stapp01.stratos.xfusioncorp.com httpd[491]: (98)Address already i
    n use: AH00072: make_sock: could not bind to address 0.0.0.0:3000
    Aug 06 01:38:21 stapp01.stratos.xfusioncorp.com httpd[491]: no listening sockets 
    available, shutting down
    top -
```

**Step 2:** Execute the command to complete this step.

```sh
sudo netstat -tlnup
```

**Step 3:** Execute the command to complete this step.

```txt
Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
    tcp        0      0 127.0.0.11:36025        0.0.0.0:*               LISTEN      -                   
    tcp        0      0 127.0.0.1:3000          0.0.0.0:*               LISTEN      430/sendmail: accep 
    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      298/sshd            
    tcp6       0      0 :::22                   :::*                    LISTEN      298/sshd            
    udp        0      0 127.0.0.11:56145        0.0.0.0:*                           -
```

**Step 4:** Execute the command to complete this step.

```sh
cd /etc/mail
    cp sendmail.mc sendmail.mc.bak
    vi sendmail.mc
```

**Step 5:** Execute the command to complete this step.

```sh
DAEMON_OPTIONS(`Port=3000,Addr=127.0.0.1, Name=MTA')dnl
```

**Step 6:** Restart the service to apply changes.

```sh
sudo systemctl restart sendmail
```

**Step 7:** Check the service status to verify it's running.

```sh
sudo netstat -tlnup
    sudo systemctl status httpd sendmail
```

**Step 8:** Test the web server by making HTTP request.

```sh
curl http://localhost:3000
```

**Step 9:** Test the web server by making HTTP request.

```sh
curl http://stapp01:3000
```

**Step 10:** Execute the command to complete this step.

```sh
sudo iptables -L -n
```

**Step 11:** Execute the command to complete this step.

```bash
sudo iptables -L -n
    Chain INPUT (policy ACCEPT)
    target     prot opt source               destination         
    ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0            state RELATED,ESTABLISHED
    ACCEPT     icmp --  0.0.0.0/0            0.0.0.0/0           
    ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           
    ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0            state NEW tcp dpt:22
    REJECT     all  --  0.0.0.0/0            0.0.0.0/0            reject-with icmp-host-prohibited

    Chain FORWARD (policy ACCEPT)
    target     prot opt source               destination         
    REJECT     all  --  0.0.0.0/0            0.0.0.0/0            reject-with icmp-host-prohibited

    Chain OUTPUT (policy ACCEPT)
    target     prot opt source               destination         
    # Warning: iptables-legacy tables present, use iptables-legacy to see them
```

**Step 12:** Execute the command to complete this step.

```sh
sudo iptables -I INPUT 4 -p tcp --dport 3000 -j ACCEPT
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 11](day-11.md) | [Day 13 →](day-13.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
