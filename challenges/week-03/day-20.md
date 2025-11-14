# Challenge 20: Configure Nginx + PHP-FPM Using Unix Sock

## 📊 Metadata
- **Day**: 20
- **Week**: 3
- **Day in Week**: 6/7
- **Category**: Web Server
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus application development team is planning to launch a new PHP-based application, which they want to deploy on Nautilus infra in Stratos DC. The development team had a meeting with the production support team and they have shared some requirements regarding the infrastructure. Below are the requirements they shared:

- Install `nginx` on `app server 1` , configure it to use port `8093` and its document `root` should be `/var/www/html`.
- Install `php-fpm` version `8.2` on `app server 1`, it must use the unix socket `/var/run/php-fpm/default.sock` (create the parent directories if don't exist).
- Configure `php-fpm` and `nginx` to work together.
- Once configured correctly, you can test the website using `curl http://stapp01:8093/index.php` command from jump host.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `curl`, `systemctl`, `httpd`, `nginx`
- **Key Concepts**:
  - Web server configuration
  - Virtual hosts setup
  - Service management with systemd
  - Port binding and listening

**Foundation from Earlier Challenges:**
- Day 15: Setup SSL for NGINX (recommended)
- Day 16: Install and Configure NGINX as Load Balancer (recommended)

**Required Skills:**
- ✅ Install and configure web servers
- ✅ Manage services with systemctl
- ✅ Test web server responses
- ✅ Configure virtual hosts

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Login into App Server and run the following commands:

    ```sh
    sudo dnf update -y
    sudo dnf install nginx -y
    sudo dnf module install php:8.2 -y # change version here if requires
    ```

    - It will update packge repo
    - Install nginx and php with expected version

2. Configure php-fpm config:

    ```sh
    sudo mkdir -p /var/run/php-fpm
    sudo vi /etc/php-fpm.d/www.conf
    ```

    - `listen = /run/php-fpm/www.sock` update this line with expected directory. It should be `listen = /var/run/php-fpm/default.sock`

3. Configure nginx

    ```sh
    sudo vi /etc/nginx/nginx.conf
    ```

    - change port 80 to `8093`

4. Configure php with nginx

    ```sh
    sudo vi /etc/nginx/default.d/php.conf
    ```

    - Update `fastcgi_pass php-fpm;` to this: `fastcgi_pass unix:/var/run/php-fpm/default.sock;`

5. Restart php-fpm and nginx

    ```sh
    sudo systemctl enable --now nginx
    sudo systemctl enable --now php-fpm
    ```

6. Test: `curl http://stapp01:8093/index.php`

## Good to Know?

### PHP-FPM (FastCGI Process Manager)

- **Purpose**: High-performance PHP FastCGI implementation
- **Process Management**: Manages PHP worker processes
- **Performance**: Better than mod_php for high-traffic sites
- **Isolation**: Separate processes for different applications

### Communication Methods

- **Unix Sockets**: Faster, local communication only
- **TCP Sockets**: Network communication, can be remote
- **Performance**: Unix sockets generally faster for local communication
- **Security**: Unix sockets more secure (filesystem permissions)

### NGINX + PHP-FPM Benefits

- **Scalability**: Handle more concurrent connections
- **Resource Efficiency**: Lower memory usage
- **Stability**: PHP crashes don't affect web server
- **Flexibility**: Different PHP versions per application

### Configuration Best Practices

- **Process Management**: Configure pm.max_children appropriately
- **Socket Permissions**: Ensure NGINX can access PHP-FPM socket
- **Security**: Run PHP-FPM as dedicated user
- **Monitoring**: Enable status page for monitoring

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

- **← Previous**: [Day 19 - Install and Configure Web Application](./day-19.md)
- **Next →**: [Day 21 - Setup Git Repository on Server](../week-03/day-21.md)

### Similar Challenges (Web Server)
- [Day 15 - Setup SSL for NGINX](../week-03/day-15.md)
- [Day 16 - Install and Configure NGINX as Load Balancer](../week-03/day-16.md)

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

