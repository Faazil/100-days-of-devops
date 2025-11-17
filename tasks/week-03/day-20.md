# Day 20: Configure Nginx + PHP-FPM Using Unix Sock

## Task Overview

Install and configure web server software for hosting applications. Set up HTTP service with custom port and configuration.

**Web Server Setup:**
- Install web server package
- Configure server settings
- Adjust ports and document root
- Start and enable service

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Install packages using the package manager.

```sh
sudo dnf update -y
    sudo dnf install nginx -y
    sudo dnf module install php:8.2 -y # change version here if requires
```

**Step 2:** Edit the configuration file to set required parameters.

```sh
sudo mkdir -p /var/run/php-fpm
    sudo vi /etc/php-fpm.d/www.conf
```

**Step 3:** Edit the configuration file to set required parameters.

```sh
sudo vi /etc/nginx/nginx.conf
```

**Step 4:** Edit the configuration file to set required parameters.

```sh
sudo vi /etc/nginx/default.d/php.conf
```

**Step 5:** Enable service to start automatically on boot.

```sh
sudo systemctl enable --now nginx
    sudo systemctl enable --now php-fpm
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 19](day-19.md) | [Day 21 →](day-21.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
