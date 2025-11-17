# Day 16: Install and Configure NGINX as Load Balancer

## Task Overview

Configure NGINX as a load balancer to distribute traffic across multiple backend servers. Improve availability and performance through request distribution.

**Load Balancer Setup:**
- Install NGINX
- Configure upstream servers
- Define load balancing algorithm
- Test traffic distribution

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Perform the initial setup or connection.

```sh
sudo ss -tlnup
```

**Step 2:** Execute the command to complete this step.

```shell
Netid     State      Recv-Q     Send-Q         Local Address:Port            Peer Address:Port     Process                                                                                            
    udp       UNCONN     0          0                 127.0.0.11:45089                0.0.0.0:*                                                                                                           
    tcp       LISTEN     0          511                  0.0.0.0:5001                 0.0.0.0:*         users:(("httpd",pid=1690,fd=3),("httpd",pid=1689,fd=3),("httpd",pid=1688,fd=3),("httpd",pid=1680,fd=3))
    tcp       LISTEN     0          128                  0.0.0.0:22                   0.0.0.0:*         users:(("sshd",pid=1102,fd=3))                                                                    
    tcp       LISTEN     0          4096              127.0.0.11:42483                0.0.0.0:*                                                                                                           
    tcp       LISTEN     0          128                     [::]:22                      [::]:*         users:(("sshd",pid=1102,fd=4))
```

**Step 3:** Install packages using the package manager.

```sh
sudo yum install nginx -y
    sudo systemctl enable nginx
    sudo systemctl start nginx
```

**Step 4:** Execute the command to complete this step.

```conf
upstream stapp {
            server stapp01:5001;
            server stapp02:5001;
            server stapp03:5001;
        }
```

**Step 5:** Execute the command to complete this step.

```conf
location / {
            proxy_pass http://stapp;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";

            proxy_connect_timeout 5s;
            proxy_read_timeout 60s;
        }
```

**Step 6:** Restart the service to apply changes.

```sh
sudo nginx -t
        sudo systemctl restart nginx
```

**Step 7:** Execute the command to complete this step.

```conf
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}


http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 4096;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    upstream stapp {
        server stapp01:5001;
        server stapp02:5001;
        server stapp03:5001;
    }

    server {
        listen       80;
        listen       [::]:80;
        server_name  _;
        #root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        error_page 404 /404.html;
        location = /404.html {
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
        }

        location / {
            proxy_pass http://stapp;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";

            proxy_connect_timeout 5s;
            proxy_read_timeout 60s;
        }
    }

# Settings for a TLS enabled server.
#
#    server {
#        listen       443 ssl http2;
#        listen       [::]:443 ssl http2;
#        server_name  _;
#        root         /usr/share/nginx/html;
#
#        ssl_certificate "/etc/pki/nginx/server.crt";
#        ssl_certificate_key "/etc/pki/nginx/private/server.key";
#        ssl_session_cache shared:SSL:1m;
#        ssl_session_timeout  10m;
#        ssl_ciphers PROFILE=SYSTEM;
#        ssl_prefer_server_ciphers on;
#
#        # Load configuration files for the default server block.
#        include /etc/nginx/default.d/*.conf;
#
#        error_page 404 /404.html;
#            location = /40x.html {
#        }
#
#        error_page 500 502 503 504 /50x.html;
#            location = /50x.html {
#        }
#    }

}
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 15](day-15.md) | [Day 17 →](day-17.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
