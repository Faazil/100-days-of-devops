# Day 79: Jenkins Deployment Job

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
rm -rf web
        git clone repo-url 
        cd web
        sshpass -p "storage-server-pass" scp -r -o StrictHostKeyChecking=no ./* natasha@ststor01:/var/www/html
```

**Step 2:** Change file ownership to the appropriate user.

```sh
sudo chown -R natasha:natasha /var/www/html
```

**Step 3:** Attempt to switch to the user and verify login is blocked.

```sh
sudo su sarah
    cd /home/sarah/web
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 78](day-78.md) | [Day 80 →](day-80.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
