# Day 19: Install and Configure Web Application

## Task Overview

xFusionCorp Industries is planning to host two static websites on their infra within the Stratos DC. The development of these websites is still in-progress, but we want to get the servers ready. Please perform the following steps to accomplish the task:

- Install `httpd` package and dependencies on `app server 3`.
- `Apache` should serve on port `6400`.
- There are two website's backups `/home/thor/official` and `/home/thor/games` on `jump_host`. Set them up on `Apache` in a way that official should work on the link `http://localhost:6400/official/` and games should work on link `http://localhost:6400/games/` on the mentioned app server.
- Once configured you should be able to access the website using curl command on the respective app server, i.e `curl http://localhost:6400/official/` and `curl http://localhost:6400/games/`

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo yum install -y httpd
```

**Step 2:**
```bash
sudo cp /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.bak
    sudo sed -i 's/80/6400/g' /etc/httpd/conf/httpd.conf
```

**Step 3:**
```bash
sudo systemctl restart httpd
```

**Step 4:**
```bash
scp -r /home/thor/official banner@stapp03:/home/banner
    scp -r /home/thor/games banner@stapp03:/home/banner/
```

**Step 5:**
```bash
sudo cp -r /home/banner/official /var/www/html/
    sudo cp -r /home/banner/games /var/www/html
```

**Step 6:**
```bash
curl http://localhost:6400/games/
    curl http://localhost:6400/official/
```

**Step 7:**
```bash
## Good to Know?

### Apache Virtual Hosts

- **Name-based**: Multiple sites on same IP using different hostnames
- **IP-based**: Different sites on different IP addresses
- **Port-based**: Different sites on different ports
- **Directory-based**: Different sites in subdirectories

### Document Root Structure

- **Main Document Root**: `/var/www/html/` (default)
- **Subdirectories**: Organize content in folders
- **Index Files**: `index.html`, `index.php` served automatically
- **Permissions**: Ensure Apache can read files (644 for files, 755 for directories)

### Apache Configuration

- **Main Config**: `/etc/httpd/conf/httpd.conf`
- **Virtual Hosts**: `/etc/httpd/conf.d/`
- **Modules**: Enable/disable Apache modules
- **Directory Directives**: Control access and behavior per directory

### Web Application Deployment

- **Static Content**: HTML, CSS, JavaScript, images
- **Dynamic Content**: PHP, Python, server-side processing
- **Security**: Disable directory browsing, hide sensitive files
- **Performance**: Enable compression, caching headers

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
- Practical application of DevOps skills
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

- **← Previous**: [Day 18 - Configure LAMP Server (LAMP Stack)](./day-18.md)
- **Next →**: [Day 20 - Configure Nginx + PHP-FPM Using Unix Sock](../week-03/day-20.md)

### Similar Challenges (DevOps)
- [Day 10 - Create a BASH Script](../week-02/day-10.md)
- [Day 13 - IPtables Installation And Configuration](../week-02/day-13.md)

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

[← Day 18](day-18.md) | [Day 20 →](day-20.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
