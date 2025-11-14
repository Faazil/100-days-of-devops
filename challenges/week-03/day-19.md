# Challenge 19: Install and Configure Web Application

## 📊 Metadata
- **Day**: 19
- **Week**: 3
- **Day in Week**: 5/7
- **Category**: DevOps
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

xFusionCorp Industries is planning to host two static websites on their infra in Stratos Datacenter. The development of these websites is still in-progress, but we want to get the servers ready. Please perform the following steps to accomplish the task:

- Install `httpd` package and dependencies on `app server 3`.
- `Apache` should serve on port `6400`.
- There are two website's backups `/home/thor/official` and `/home/thor/games` on `jump_host`. Set them up on `Apache` in a way that official should work on the link `http://localhost:6400/official/` and games should work on link `http://localhost:6400/games/` on the mentioned app server.
- Once configured you should be able to access the website using curl command on the respective app server, i.e `curl http://localhost:6400/official/` and `curl http://localhost:6400/games/`


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Key Concepts**:
  - DevOps workflow and principles
  - CI/CD pipeline concepts
  - Automation strategies
  - Infrastructure management

**Foundation from Earlier Challenges:**
- Day 4: Script Execute Permissions (recommended)
- Day 10: Create a BASH Script (recommended)
- Day 13: IPtables Installation And Configuration (recommended)

**Required Skills:**
- ✅ Understand DevOps methodologies
- ✅ Integrate multiple tools
- ✅ Implement automation workflows

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Access App Server 3 and Install httpd

    ```sh
    sudo yum install -y httpd
    ```

2. Change Apache port:

    ```sh
    sudo cp /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.bak
    sudo sed -i 's/80/6400/g' /etc/httpd/conf/httpd.conf
    ```

3. Restart Apache Server

    ```sh
    sudo systemctl restart httpd
    ```

4. Copy backup from Jump Host to App Server

    ```sh
    scp -r /home/thor/official banner@stapp03:/home/banner
    scp -r /home/thor/games banner@stapp03:/home/banner/
    ```

5. Place websites

    ```sh
    sudo cp -r /home/banner/official /var/www/html/
    sudo cp -r /home/banner/games /var/www/html
    ```

6. Restart `httpd`

7. Verify result

    ```sh
    curl http://localhost:6400/games/
    curl http://localhost:6400/official/
    ```

    ```html
    <!DOCTYPE html>
    <html>
    <body>

    <h1>KodeKloud</h1>

    <p>This is a sample page for our official website</p>

    </body>
    </html>
    ```

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
```bash
```

