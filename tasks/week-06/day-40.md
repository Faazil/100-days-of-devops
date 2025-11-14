# Day 40: Docker Execution

## Task Overview

One of the Nautilus DevOps team members was working to configure services on a kkloud container that is running on App Server 1 in Stratos Datacenter. Due to some personal work he is on PTO for the rest of the week, but we need to finish his pending work ASAP. Please complete the remaining work as per details given below:

- Install `apache2` in `kkloud` container using apt that is running on `App Server 1` in Stratos Datacenter.

- Configure `Apache` to listen on port `6000` instead of default http port. Do not bind it to listen on specific IP or hostname only, i.e it should listen on localhost, 127.0.0.1, container ip, etc.

- Ensure Apache service is up and running inside the container. Keep the container in running state at the end.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
docker ps
```

**Step 2:**
```bash
[tony@stapp01 ~]$ docker ps
    CONTAINER ID   IMAGE          COMMAND       CREATED         STATUS         PORTS     NAMES
    dcdc693d1175   ubuntu:18.04   "/bin/bash"   8 minutes ago   Up 8 minutes             kkloud
```

**Step 3:**
```bash
docker exec -it kkloud /bin/bash
```

**Step 4:**
```bash
4. Install apache2 inside the container

    So, we are already inside the container. lets run the following command to install apache2:
```

**Step 5:**
```bash
> We have installed apache2 and vim

5. Configure Apache2

    We have installed apache2 and vim so far. Now let's configure Apache2 to change the default port 80 to 6000.

    To modify port, we have to edit file in `/etc/apache2/ports.conf`:
```

**Step 7:**
```bash
> just change 80 to 6000

    Another part is to update the `000-default.conf`.
    Just changed 80 to 6000:
```

**Step 8:**
```bash
6. Let's start the apache2 service

    To run apache2 service inside the container:
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 39](day-39.md) | [Day 41 →](day-41.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
