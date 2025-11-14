# Day 15: Setup SSL for NGINX

## Task Overview

The system admins team of xFusionCorp Industries needs to deploy a new application on App Server 3 within the Stratos DC. They have some pre-requites to get ready that server for application deployment. Prepare the server as per requirements shared below:

1. Install and configure `nginx` on `App Server 3`.

2. On App Server 3 A self signed SSL certificate and key present at location `/tmp/nautilus.crt` and `/tmp/nautilus.key`. Move them to some appropriate location and deploy the same in Nginx.

3. Create an `index.html` file with content `Welcome!` under Nginx document root.

4. For final testing try to access the App Server 3 link (either hostname or IP) from jump host using curl command. For example `curl -Ik https://<app-server-ip>/`.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo yum install nginx -y
```

**Step 2:**
```bash
echo "Welcome!" | sudo tee /usr/share/nginx/html/index.html
```

**Step 3:**
```bash
sudo systemctl restart nginx
    curl http://stapp03
```

**Step 4:**
```bash
sudo mkdir -p /etc/certs
    sudo cp /tmp/nautilus.* /etc/certs
```

**Step 5:**
```bash
sudo vi /etc/nginx/nginx.conf
```

**Step 6:**
```bash
return 301 https://$host$request_uri;
```

**Step 7:**
```bash
If you need to update anything else do respectively. Before restart the `ngninx` server make sure you are testin it using:
```

**Step 8:**
```bash
If it returns successful, you are ready to restart nginx:
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 14](../week-02/day-14.md) | [Day 16 →](day-16.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
