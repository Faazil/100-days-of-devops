# Challenge 44: Creating a Docker Compose File

## 📊 Metadata
- **Day**: 44
- **Week**: 7
- **Day in Week**: 2/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus application development team shared static website content that needs to be hosted on the httpd web server using a containerised platform. The team has shared details with the DevOps team, and we need to set up an environment according to those guidelines. Below are the details:

- On App Server 3 in Stratos DC create a container named `httpd` using a docker compose file `/opt/docker/docker-compose.yml` (please use the exact name for file).

- Use `httpd` (preferably latest tag) image for container and make sure container is named as `httpd`; you can use any name for `service`.

- Map `80` number port of container with port `3003` of docker host.

- Map container's `/usr/local/apache2/htdocs` volume with `/opt/itadmin` volume of docker host which is already there. (please do not modify any data within these locations).


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

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
- Day 41: Create a Docker File (recommended)
- Day 42: Create Docker Network (recommended)
- Day 43: Docker Ports Mapping (recommended)

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Login into App Server 3
2. Make sure docker is running and accessible, you can check simply runing:

    ```sh
    docker ps
    ```

3. Let's create the `/opt/docker/docker-compose.yml` file:

    ```sh
    sudo touch /opt/docker/docker-compose.yml
    ```

    - Open the file in editor and copy paste the contents from this [file](../scripts/compose.yml)

4. Let's run the compose file

    ```sh
    docker compose -f /opt/docker/docker-compose.yml up -d
    ```

5. Let's verify if it's running or not

    ```sh
    docker ps
    ```

    > It should display the output like this:

    ```shell
    banner@stapp03 ~]$ docker ps
    CONTAINER ID   IMAGE          COMMAND              CREATED          STATUS          PORTS                  NAMES
    31c6d90cafa8   httpd:latest   "httpd-foreground"   37 seconds ago   Up 35 seconds   0.0.0.0:3003->80/tcp   httpd
    ```

## Good to Know?

### Docker Compose

- **Purpose**: Define and run multi-container Docker applications
- **YAML Configuration**: Declarative service definitions
- **Orchestration**: Manage multiple containers as single application
- **Development**: Simplify local development environments

### Compose File Structure

- **version**: Compose file format version
- **services**: Define application containers
- **networks**: Custom network configuration
- **volumes**: Persistent data storage

### Service Configuration

- **image**: Docker image to use for container
- **container_name**: Custom name for container
- **ports**: Port mapping between host and container
- **volumes**: Mount host directories or named volumes
- **environment**: Set environment variables

### Compose Commands

- **Up**: `docker-compose up -d` (start services)
- **Down**: `docker-compose down` (stop and remove)
- **Logs**: `docker-compose logs` (view service logs)
- **Scale**: `docker-compose up --scale service=3`

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

- **← Previous**: [Day 43 - Docker Ports Mapping](./day-43.md)
- **Next →**: [Day 45 - Resolve Dockerfile Issues](../week-07/day-45.md)

### Similar Challenges (Docker)
- [Day 35 - Setup Docker Installation](../week-05/day-35.md)
- [Day 36 - Run a NGINX Container on Docker](../week-06/day-36.md)
- [Day 37 - Copy File to Docker Container](../week-06/day-37.md)

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
```bash
```

