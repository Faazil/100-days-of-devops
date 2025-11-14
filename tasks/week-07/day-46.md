# Day 46: Deploy an App on Docker Containers

## Task Overview

The Nautilus Application development team recently finished development of one of the apps that they want to deploy on a containerized platform. The Nautilus Application development and DevOps teams met to discuss some of the basic pre-requisites and requirements to complete the deployment. The team wants to test the deployment on one of the app servers before going live and set up a complete containerized stack using a docker compose fie. Below are the details of the task:

- On App Server 2 in Stratos Datacenter create a docker compose file `/opt/itadmin/docker-compose.yml` (should be named exactly).

- The compose should deploy two services (web and DB), and each service should deploy a container as per details below:

For web service:

- Container name must be `php_web`.
- Use image `php` with any apache tag. Check [docker hub](https://hub.docker.com/_/php?tab=tags/) for more details.
- Map php_web container's port `80` with host port `6400`
- Map php_web container's `/var/www/html` volume with host volume `/var/www/html`.

For DB service:

- Container name must be `mysql_web`.
- Use image `mariadb` with any tag (preferably latest). Check [mariadb](https://hub.docker.com/_/mariadb?tab=tags/) for more details.
- Map mysql_web container's port `3306` with host port `3306`
- Map mysql_web container's `/var/lib/mysql` volume with host volume `/var/lib/mysql`.
- Set `MYSQL_DATABASE=database_web` and use any custom user ( except root ) with some complex password for DB connections.

After running docker-compose up you can access the app with curl command curl `<server-ip or hostname>:6400/`

For more details check [mariadb](https://hub.docker.com/_/mariadb?tab=description/).

Note: Once you click on FINISH button, all currently running/stopped containers will be destroyed and stack will be deployed again using your compose file.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo touch /opt/itadmin/docker-compose.yml
```

**Step 2:**
```bash
4. Let's Test
```

**Step 3:**
```bash
> It was actually a sample test, web server is not rely on db. Otherwise we had to set connection between two services.

## Good to Know?

### Multi-Container Applications

- **Separation of Concerns**: Each service has specific responsibility
- **Scalability**: Scale services independently
- **Maintainability**: Update services without affecting others
- **Technology Diversity**: Use different technologies per service

### Two-Tier Architecture

- **Presentation Tier**: Web server (PHP/Apache)
- **Data Tier**: Database server (MariaDB/MySQL)
- **Communication**: Services communicate over network
- **Stateless Web**: Web tier should be stateless for scalability

### Docker Compose Benefits

- **Single Command**: Start entire application stack
- **Service Discovery**: Services can communicate by name
- **Environment Isolation**: Consistent development environment
- **Volume Management**: Persistent data across container restarts

### Database Configuration

- **Environment Variables**: Configure database credentials
- **Initialization**: Database creates schema on first run
- **Persistence**: Use volumes to persist database data
- **Security**: Use strong passwords and limit access

---

## ✅ Verification

After completing the challenge, verify your solution by:

1. **Testing the implementation**
   - Run all commands from the solution
   - Check for any error messages

2. **Validating the results**
   - Ensure all requirements are met
   - Test edge cases if applicable

3. **Clean up (if needed)**
   - Remove temporary files
   - Reset any test configurations

---

## 📚 Learning Notes

### Key Concepts

This challenge covers the following concepts:
- Practical application of Docker skills
- Real-world DevOps scenarios
- Best practices for production environments

### Common Pitfalls

- ⚠️ **Permissions**: Ensure you have the necessary permissions to execute commands
- ⚠️ **Syntax**: Double-check command syntax and flags
- ⚠️ **Environment**: Verify you're working in the correct environment/server

### Best Practices

- ✅ Always verify changes before marking as complete
- ✅ Test your solution in a safe environment first
- ✅ Document any deviations from the standard approach
- ✅ Keep security in mind for all configurations

---

## 🔗 Related Challenges

- **← Previous**: [Day 45 - Resolve Dockerfile Issues](./day-45.md)
- **Next →**: [Day 47 - Docker Python App](../week-07/day-47.md)

### Similar Challenges (Docker)
- [Day 36 - Run a NGINX Container on Docker](../week-06/day-36.md)
- [Day 37 - Copy File to Docker Container](../week-06/day-37.md)
- [Day 38 - Docker Pull Images](../week-06/day-38.md)

---

## 📖 Additional Resources

- [KodeKloud Official Documentation](https://kodekloud.com)
- [Official Technology Documentation](#)
- [Community Discussions](#)

---

## 🎓 Knowledge Check

After completing this challenge, you should be able to:
- [ ] Understand the problem statement clearly
- [ ] Implement the solution independently
- [ ] Verify the solution works correctly
- [ ] Explain the concepts to others
- [ ] Apply these skills to similar problems

---

**Challenge Source**: KodeKloud 100 Days of DevOps
**Difficulty**: ⭐
**Category**: DevOps

---

**Track your progress**: After completing this challenge, mark it as done:
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 45](day-45.md) | [Day 47 →](day-47.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
