# Challenge 46: Deploy an App on Docker Containers

## 📊 Metadata
- **Day**: 46
- **Week**: 7
- **Day in Week**: 4/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

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


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Docker installed and configured
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `docker`, `docker run`, `docker ps`, `docker build`, `docker exec`
- **Key Concepts**:
  - Container vs Image distinction
  - Container lifecycle management
  - Docker networking fundamentals
  - Volume mounting and persistence
- **Environment**: Docker installed and running

**Foundation from Earlier Challenges:**
- Day 43: Docker Ports Mapping (recommended)
- Day 44: Creating a Docker Compose File (recommended)
- Day 45: Resolve Dockerfile Issues (recommended)

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

In this daily challenge, we are going to dockerized a 2-tier application. We have to create a docker compose file bundled with frontend and database containers. let's start...

1. Login into App Server 2
2. Create a docker compose file

    ```sh
    sudo touch /opt/itadmin/docker-compose.yml
    ```

3. Copy-paste the following contents inside `/opt/itadmin/docker-compose.yml`

    ```yaml
    services:
        web:
            image: php:apache
            container_name: php_web
            ports:
                - 6400:80
            volumes:
                - /var/www/html:/var/www/html
        
        db:
            image: mariadb:latest
            container_name: mysql_web
            ports:
                - 3306:3306
            volumes:
                - /var/lib/mysql:/var/lib/mysql
            environment:
                - MARIADB_DATABASE=database_web
                - MARIADB_USER=kkloud
                - MARIADB_PASSWORD=your-user-password
                - MARIADB_ROOT_PASSWORD=your-root-password
    ```

4. Let's Test

    ```sh
    docker compose -f /opt/itadmin/docker-compose.yml
    ```

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
**Difficulty**: {get_difficulty_emoji(day)}
**Category**: {task_info['category']}

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
python3 ../../tools/progress.py --complete {day}
```

