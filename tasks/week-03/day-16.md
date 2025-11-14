# Day 16: Install and Configure NGINX as Load Balancer

## Task Overview

Day by day traffic is increasing on one of the websites managed by the Nautilus production support team. Therefore, the team has observed a degradation in website performance. Following discussions about this issue, the team has decided to deploy this application on a high availability stack i.e on Nautilus infra in Stratos DC. They started the migration last month and it is almost done, as only the LBR server configuration is pending. Configure LBR server as per the information given below:

- Install `nginx` on `LBR` server
- Configure load-balancing with the an http context making use of all App Servers. Ensure that you update only the main `Nginx` configuration file located at `/etc/nginx/nginx.conf`
- Ensure you do not update the apache port that is already defined in the apache configuration on all app servers, also make sure apache server is up and running on all app servers
- Once done, you can access the website using StaticApp button on the top bar

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo ss -tlnup
```

**Step 2:**
```bash
Netid     State      Recv-Q     Send-Q         Local Address:Port            Peer Address:Port     Process                                                                                            
    udp       UNCONN     0          0                 127.0.0.11:45089                0.0.0.0:*                                                                                                           
    tcp       LISTEN     0          511                  0.0.0.0:5001                 0.0.0.0:*         users:(("httpd",pid=1690,fd=3),("httpd",pid=1689,fd=3),("httpd",pid=1688,fd=3),("httpd",pid=1680,fd=3))
    tcp       LISTEN     0          128                  0.0.0.0:22                   0.0.0.0:*         users:(("sshd",pid=1102,fd=3))                                                                    
    tcp       LISTEN     0          4096              127.0.0.11:42483                0.0.0.0:*                                                                                                           
    tcp       LISTEN     0          128                     [::]:22                      [::]:*         users:(("sshd",pid=1102,fd=4))
```

**Step 3:**
```bash
sudo yum install nginx -y
    sudo systemctl enable nginx
    sudo systemctl start nginx
```

**Step 4:**
```bash
- Then redirect call to these server using `proxy_pass`, copy paste following lines inside `server:80`:
```

**Step 5:**
```bash
- Done, lets check config is okay and restart nginx server:
```

**Step 6:**
```bash
## Full NGINX LBR Configuration
```

**Step 7:**
```bash
## Good to Know?

### Load Balancing Fundamentals

- **Purpose**: Distribute incoming requests across multiple servers
- **Benefits**: High availability, scalability, fault tolerance
- **Algorithms**: Round-robin (default), least connections, IP hash
- **Health Checks**: Monitor backend server availability

### NGINX Load Balancing

- **Upstream Block**: Define backend server pool
- **Proxy Pass**: Forward requests to upstream servers
- **Load Methods**: `round_robin`, `least_conn`, `ip_hash`, `random`
- **Server Weights**: `server backend1:80 weight=3;`

### Proxy Headers

- **Host**: Preserve original host header
- **X-Real-IP**: Client's real IP address
- **X-Forwarded-For**: Chain of proxy IPs
- **X-Forwarded-Proto**: Original protocol (HTTP/HTTPS)

### High Availability Features

- **Backup Servers**: `server backend4:80 backup;`
- **Health Checks**: Automatic failure detection
- **Session Persistence**: Sticky sessions with `ip_hash`
- **SSL Termination**: Handle SSL at load balancer level

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
- Practical application of Web Server skills
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

- **← Previous**: [Day 15 - Setup SSL for NGINX](./day-15.md)
- **Next →**: [Day 17 - Install and Configure PostgreSQL](../week-03/day-17.md)

### Similar Challenges (Web Server)
- [Day 15 - Setup SSL for NGINX](../week-03/day-15.md)
- [Day 20 - Configure Nginx + PHP-FPM Using Unix Sock](../week-03/day-20.md)

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
**Difficulty**: ⭐
**Category**: DevOps

---

**Track your progress**: After completing this challenge, mark it as done:
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 15](day-15.md) | [Day 17 →](day-17.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
