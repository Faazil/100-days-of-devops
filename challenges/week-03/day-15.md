# Challenge 15: Setup SSL for NGINX

## 📊 Metadata
- **Day**: 15
- **Week**: 3
- **Day in Week**: 1/7
- **Category**: Web Server
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The system admins team of xFusionCorp Industries needs to deploy a new application on App Server 3 in Stratos Datacenter. They have some pre-requites to get ready that server for application deployment. Prepare the server as per requirements shared below:

1. Install and configure `nginx` on `App Server 3`.

2. On App Server 3 there is a self signed SSL certificate and key present at location `/tmp/nautilus.crt` and `/tmp/nautilus.key`. Move them to some appropriate location and deploy the same in Nginx.

3. Create an `index.html` file with content `Welcome!` under Nginx document root.

4. For final testing try to access the App Server 3 link (either hostname or IP) from jump host using curl command. For example `curl -Ik https://<app-server-ip>/`.


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

**Required Skills:**
- ✅ Install and configure web servers
- ✅ Manage services with systemctl
- ✅ Test web server responses
- ✅ Configure virtual hosts

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Install nginx

    ```sh
    sudo yum install nginx -y
    ```

2. Change default `index.html` content:

    ```sh
    echo "Welcome!" | sudo tee /usr/share/nginx/html/index.html
    ```

3. Restart and check if nginx is accesible from jump host:

    ```sh
    sudo systemctl restart nginx
    curl http://stapp03
    ```

4. Copy ssl from `/tmp`:

    ```sh
    sudo mkdir -p /etc/certs
    sudo cp /tmp/nautilus.* /etc/certs
    ```

5. Configure SSL:

    ```sh
    sudo vi /etc/nginx/nginx.conf
    ```

    We have to be cautious here, otherwise nginx could be broken.

    We need to add this line inside `server:80` just after `server_name`.

    ```shell
    return 301 https://$host$request_uri;
    ```

    Then we have to uncomment `server:443` and add following lines:

    ```nginx
    ssl_certificate     /etc/certs/nautilus.crt;
    ssl_certificate_key /etc/certs/nautilus.key;
    ```

    If you need to update anything else do respectively. Before restart the `ngninx` server make sure you are testin it using:

    ```sh
    sudo nginx -t
    ```

    If it returns successful, you are ready to restart nginx:

    ```sh
    sudo systemctl restart nginx
    ```

6. Finally test

    ```curl -k https://stapp03
    ```

## Good to Know?

### SSL/TLS Fundamentals

- **Purpose**: Encrypt data in transit, authenticate server identity
- **Certificates**: Digital certificates contain public key and identity info
- **Private Key**: Must be kept secure, used for decryption
- **Self-signed**: Not trusted by browsers, good for testing

### NGINX SSL Configuration

- **ssl_certificate**: Path to certificate file (.crt, .pem)
- **ssl_certificate_key**: Path to private key file (.key)
- **ssl_protocols**: Specify allowed TLS versions
- **ssl_ciphers**: Define encryption algorithms

### Security Best Practices

- **Strong Ciphers**: Use modern, secure cipher suites
- **HSTS**: HTTP Strict Transport Security header
- **Redirect HTTP**: Force HTTPS with 301 redirects
- **Key Security**: Protect private keys (600 permissions)

### Certificate Management

- **Let's Encrypt**: Free automated certificates
- **Certificate Authority**: Trusted third-party issuers
- **Expiration**: Monitor and renew certificates
- **Chain**: Include intermediate certificates

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

- **← Previous**: [Day 14 - Linux Process Troubleshooting](./day-14.md)
- **Next →**: [Day 16 - Install and Configure NGINX as Load Balancer](../week-03/day-16.md)

### Similar Challenges (Web Server)
- [Day 16 - Install and Configure NGINX as Load Balancer](../week-03/day-16.md)
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
```bash
```

