# Day 12: Linux Network Services

## Task Overview

Our monitoring tool has reported an issue in Stratos Datacenter. One of our app servers has an issue, as its Apache service is not reachable on port 3000 (which is the Apache port). The service itself could be down, the firewall could be at fault, or something else could be causing the issue.

- Use tools like telnet, netstat, etc. to find and fix the issue. Also make sure Apache is reachable from the jump host without compromising any security settings.

- Once fixed, you can test the same using command `curl http://stapp01:3000` command from jump host.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
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

**Step 2:**
```bash
sudo netstat -tlnup
```

**Step 3:**
```bash
Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
    tcp        0      0 127.0.0.11:36025        0.0.0.0:*               LISTEN      -                   
    tcp        0      0 127.0.0.1:3000          0.0.0.0:*               LISTEN      430/sendmail: accep 
    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      298/sshd            
    tcp6       0      0 :::22                   :::*                    LISTEN      298/sshd            
    udp        0      0 127.0.0.11:56145        0.0.0.0:*                           -
```

**Step 4:**
```bash
cd /etc/mail
    cp sendmail.mc sendmail.mc.bak
    vi sendmail.mc
```

**Step 5:**
```bash
DAEMON_OPTIONS(`Port=3000,Addr=127.0.0.1, Name=MTA')dnl
```

**Step 6:**
```bash
sudo systemctl restart sendmail
```

**Step 7:**
```bash
sudo netstat -tlnup
    sudo systemctl status httpd sendmail
```

**Step 8:**
```bash
curl http://localhost:3000
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 11](day-11.md) | [Day 13 →](day-13.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
