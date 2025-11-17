# Day 80: Jenkins Chained Builds

## Task Overview

Configure Jenkins pipeline for automated build and deployment workflows. Pipelines define CI/CD processes as code.

**Pipeline Configuration:**
- Create pipeline job in Jenkins
- Define pipeline stages
- Configure build and deployment steps
- Integrate with version control

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Connect to the target server using SSH.

```sh
sshpass -p "Bl@kW" scp -r -o StrictHostKeyChecking=no ./* natasha@ststor01:/var/www/html
```

**Step 2:** Restart the service to apply changes.

```sh
echo 'app-server-password' | sudo -S systemctl restart httpd
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 79](day-79.md) | [Day 81 →](day-81.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
