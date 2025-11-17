# Day 15: Setup SSL for NGINX

## Task Overview

Execute Git version control operations for source code management. Track changes, collaborate, and maintain project history.

**Git Operations:**
- Configure Git settings
- Perform repository operations
- Manage commits and history
- Collaborate with remotes

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Install packages using the package manager.

```sh
sudo yum install nginx -y
```

**Step 2:** Execute the command to complete this step.

```sh
echo "Welcome!" | sudo tee /usr/share/nginx/html/index.html
```

**Step 3:** Restart the service to apply changes.

```sh
sudo systemctl restart nginx
    curl http://stapp03
```

**Step 4:** Create the required directory.

```sh
sudo mkdir -p /etc/certs
    sudo cp /tmp/nautilus.* /etc/certs
```

**Step 5:** Edit the configuration file to set required parameters.

```sh
sudo vi /etc/nginx/nginx.conf
```

**Step 6:** Execute the command to complete this step.

```shell
return 301 https://$host$request_uri;
```

**Step 7:** Execute the command to complete this step.

```nginx
ssl_certificate     /etc/certs/nautilus.crt;
    ssl_certificate_key /etc/certs/nautilus.key;
```

**Step 8:** Execute the command to complete this step.

```sh
sudo nginx -t
```

**Step 9:** Restart the service to apply changes.

```sh
sudo systemctl restart nginx
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 14](../week-02/day-14.md) | [Day 16 →](day-16.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
