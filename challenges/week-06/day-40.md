# Challenge 40: Docker Execution

## 📊 Metadata
- **Day**: 40
- **Week**: 6
- **Day in Week**: 5/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

One of the Nautilus DevOps team members was working to configure services on a kkloud container that is running on App Server 1 in Stratos Datacenter. Due to some personal work he is on PTO for the rest of the week, but we need to finish his pending work ASAP. Please complete the remaining work as per details given below:

- Install `apache2` in `kkloud` container using apt that is running on `App Server 1` in Stratos Datacenter.

- Configure `Apache` to listen on port `6000` instead of default http port. Do not bind it to listen on specific IP or hostname only, i.e it should listen on localhost, 127.0.0.1, container ip, etc.

- Make sure Apache service is up and running inside the container. Keep the container in running state at the end.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Docker installed and configured
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `docker`, `docker run`, `docker ps`, `docker build`, `docker exec`
- **Key Concepts**:
  - Container vs Image distinction
  - Container lifecycle management
  - Docker networking fundamentals
  - Volume mounting and persistence
- **Environment**: Docker installed and running

**Foundation from Earlier Challenges:**
- Day 37: Copy File to Docker Container (recommended)
- Day 38: Docker Pull Images (recommended)
- Day 39: Create a Docker Image From a Container (recommended)

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Login into App Server using SSH
2. Let's check the running containers

    ```sh
    docker ps
    ```

    ```shell
    [tony@stapp01 ~]$ docker ps
    CONTAINER ID   IMAGE          COMMAND       CREATED         STATUS         PORTS     NAMES
    dcdc693d1175   ubuntu:18.04   "/bin/bash"   8 minutes ago   Up 8 minutes             kkloud
    ```

3. Login inside the container

    ```sh
    docker exec -it kkloud /bin/bash
    ```

    ```output
    [tony@stapp01 ~]$ docker exec -it kkloud /bin/bash
    root@dcdc693d1175:/#
    ```

4. Install apache2 inside the container

    So, we are already inside the container. lets run the following command to install apache2:

    ```sh
    apt install apache2 vim -y
    ```

    > We have installed apache2 and vim

5. Configure Apache2

    We have installed apache2 and vim so far. Now let's configure Apache2 to change the default port 80 to 6000.

    To modify port, we have to edit file in `/etc/apache2/ports.conf`:

    ```sh
    vim /etc/apache2/ports.conf
    ```

    ```conf
    # If you just change the port or add more ports here, you will likely also
    # have to change the VirtualHost statement in
    # /etc/apache2/sites-enabled/000-default.conf

    Listen 80

    <IfModule ssl_module>
            Listen 443
    </IfModule>

    <IfModule mod_gnutls.c>
            Listen 443
    </IfModule>

    # vim: syntax=apache ts=4 sw=4 sts=4 sr noet
    ```

    > just change 80 to 6000

    Another part is to update the `000-default.conf`.
    Just changed 80 to 6000:

    ```conf
    <VirtualHost *:6000>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
    </VirtualHost>

    # vim: syntax=apache ts=4 sw=4 sts=4 sr noet
    ```

6. Let's start the apache2 service

    To run apache2 service inside the container:

    ```sh
    /usr/sbin/apache2ctl start
    ```

    To verify if apache2 is started or not:

    ```sh
    ps aux | grep apache2
    ```

    > It will show running process of apache2

    ```output
    root@dcdc693d1175:~# ps aux | grep apache2
    root         116  0.0  0.0  73972  4632 ?        Ss   02:12   0:00 /usr/sbin/apache2 -k start
    www-data     117  0.0  0.0 2067072 4464 ?        Sl   02:12   0:00 /usr/sbin/apache2 -k start
    www-data     118  0.0  0.0 2067072 4464 ?        Sl   02:12   0:00 /usr/sbin/apache2 -k start
    root         174  0.0  0.0  11472  1076 pts/1    S+   02:13   0:00 grep --color=auto apache2
    ```

    To test if apache2 is running or not:

    ```sh
    curl localhost:6000
    ```

## Good to Know?

### Docker Exec

- **Purpose**: Execute commands in running containers
- **Interactive**: `-it` flags for interactive terminal
- **Non-interactive**: Run commands without terminal
- **Multiple Sessions**: Can have multiple exec sessions

### Container Configuration

- **Runtime Changes**: Modify running container configuration
- **Service Management**: Start/stop services inside container
- **Package Installation**: Install software in running containers
- **Debugging**: Troubleshoot container issues

### Apache Configuration

- **Port Changes**: Modify listening ports in configuration files
- **Virtual Hosts**: Configure multiple sites
- **Modules**: Enable/disable Apache modules
- **Security**: Configure SSL, authentication

### Container Persistence

- **Ephemeral**: Container changes lost when container stops
- **Volumes**: Use volumes for persistent data
- **Image Creation**: Commit changes to new image
- **Configuration Management**: Use external config files

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
- Practical application of Docker skills
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

- **← Previous**: [Day 39 - Create a Docker Image From a Container](./day-39.md)
- **Next →**: [Day 41 - Create a Docker File](../week-06/day-41.md)

### Similar Challenges (Docker)
- [Day 35 - Setup Docker Installation](../week-05/day-35.md)
- [Day 36 - Run a NGINX Container on Docker](../week-06/day-36.md)
- [Day 37 - Copy File to Docker Container](../week-06/day-37.md)

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

