# Day 20: Configure Nginx + PHP-FPM Using Unix Sock

## Task Overview

The Nautilus application development team is planning to launch a new PHP-based application, which they want to deploy on Nautilus infra in Stratos DC. The development team had a meeting with the production support team and they have shared some requirements regarding the infrastructure. Below are the requirements they shared:

- Install `nginx` on `app server 1` , configure it to use port `8093` and its document `root` should be `/var/www/html`.
- Install `php-fpm` version `8.2` on `app server 1`, it must use the unix socket `/var/run/php-fpm/default.sock` (create the parent directories if don't exist).
- Configure `php-fpm` and `nginx` to work together.
- Once configured correctly, you can test the website using `curl http://stapp01:8093/index.php` command from jump host.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo dnf update -y
    sudo dnf install nginx -y
    sudo dnf module install php:8.2 -y # change version here if requires
```

**Step 2:**
```bash
sudo mkdir -p /var/run/php-fpm
    sudo vi /etc/php-fpm.d/www.conf
```

**Step 3:**
```bash
sudo vi /etc/nginx/nginx.conf
```

**Step 4:**
```bash
sudo vi /etc/nginx/default.d/php.conf
```

**Step 5:**
```bash
sudo systemctl enable --now nginx
    sudo systemctl enable --now php-fpm
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 19](day-19.md) | [Day 21 →](day-21.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
