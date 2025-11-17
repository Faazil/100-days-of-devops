# Day 40: Docker Execution

## Task Overview

Build custom Docker images using Dockerfiles to package applications with their dependencies. Images serve as blueprints for creating containers.

**Image Creation:**
- Write Dockerfile with build instructions
- Define base image and dependencies
- Configure application setup
- Build and verify image

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** List running containers to verify deployment.

```sh
docker ps
```

**Step 2:** List running containers to verify deployment.

```shell
[tony@stapp01 ~]$ docker ps
    CONTAINER ID   IMAGE          COMMAND       CREATED         STATUS         PORTS     NAMES
    dcdc693d1175   ubuntu:18.04   "/bin/bash"   8 minutes ago   Up 8 minutes             kkloud
```

**Step 3:** Execute the command to complete this step.

```sh
docker exec -it kkloud /bin/bash
```

**Step 4:** Execute the command to complete this step.

```output
[tony@stapp01 ~]$ docker exec -it kkloud /bin/bash
    root@dcdc693d1175:/#
```

**Step 5:** Install packages using the package manager.

```sh
apt install apache2 vim -y
```

**Step 6:** Execute the command to complete this step.

```sh
vim /etc/apache2/ports.conf
```

**Step 7:** Execute the command to complete this step.

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

**Step 8:** Execute the command to complete this step.

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

**Step 9:** Execute the command to complete this step.

```sh
/usr/sbin/apache2ctl start
```

**Step 10:** Execute the command to complete this step.

```sh
ps aux | grep apache2
```

**Step 11:** Execute the command to complete this step.

```output
root@dcdc693d1175:~# ps aux | grep apache2
    root         116  0.0  0.0  73972  4632 ?        Ss   02:12   0:00 /usr/sbin/apache2 -k start
    www-data     117  0.0  0.0 2067072 4464 ?        Sl   02:12   0:00 /usr/sbin/apache2 -k start
    www-data     118  0.0  0.0 2067072 4464 ?        Sl   02:12   0:00 /usr/sbin/apache2 -k start
    root         174  0.0  0.0  11472  1076 pts/1    S+   02:13   0:00 grep --color=auto apache2
```

**Step 12:** Execute the command to complete this step.

```sh
curl localhost:6000
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 39](day-39.md) | [Day 41 →](day-41.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
