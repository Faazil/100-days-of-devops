# Day 19: Install and Configure Web Application

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
sudo yum install -y httpd
```

**Step 2:** Execute the command to complete this step.

```sh
sudo cp /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.bak
    sudo sed -i 's/80/6400/g' /etc/httpd/conf/httpd.conf
```

**Step 3:** Restart the service to apply changes.

```sh
sudo systemctl restart httpd
```

**Step 4:** Copy file to remote server using secure copy.

```sh
scp -r /home/thor/official banner@stapp03:/home/banner
    scp -r /home/thor/games banner@stapp03:/home/banner/
```

**Step 5:** Execute the command to complete this step.

```sh
sudo cp -r /home/banner/official /var/www/html/
    sudo cp -r /home/banner/games /var/www/html
```

**Step 6:** Test the web server by making HTTP request.

```sh
curl http://localhost:6400/games/
    curl http://localhost:6400/official/
```

**Step 7:** Execute the command to complete this step.

```html
<!DOCTYPE html>
    <html>
    <body>

    <h1>KodeKloud</h1>

    <p>This is a sample page for our official website</p>

    </body>
    </html>
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 18](day-18.md) | [Day 20 →](day-20.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
