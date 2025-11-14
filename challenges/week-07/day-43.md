# Challenge 43: Docker Ports Mapping

## 📊 Metadata
- **Day**: 43
- **Week**: 7
- **Day in Week**: 1/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team is planning to host an application on a nginx-based container. There are number of tickets already been created for similar tasks. One of the tickets has been assigned to set up a nginx container on Application Server 2 in Stratos Datacenter. Please perform the task as per details mentioned below:

- Pull `nginx:stable` docker image on Application Server 2.

- Create a container named `cluster` using the image you pulled.

- Map host port `5002` to container port `80`. Please keep the container in running state.


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
- Day 40: Docker Execution (recommended)
- Day 41: Create a Docker File (recommended)
- Day 42: Create Docker Network (recommended)

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Login into App Server 2
2. Pull the docker image

    ```sh
    docker pull nginx:stable
    ```

3. Create a container with port mapping

    ```sh
    docker run -d --name cluster -p 5002:80 nginx:stable
    ```

4. Make sure container is running

    ```sh
    docker ps
    ```

## Good to Know?

### Docker Port Mapping

- **Purpose**: Expose container services to host network
- **Traffic Routing**: Route host traffic to container ports
- **Service Access**: Make containerized services accessible
- **Load Balancing**: Distribute traffic across multiple containers

### Port Mapping Syntax

- **Basic**: `-p host_port:container_port`
- **IP Binding**: `-p host_ip:host_port:container_port`
- **Protocol**: `-p port:port/tcp` or `-p port:port/udp`
- **Random Port**: `-P` maps all exposed ports to random host ports

### NGINX Container

- **Web Server**: High-performance HTTP server and reverse proxy
- **Default Port**: Listens on port 80 inside container
- **Static Content**: Serves static files efficiently
- **Reverse Proxy**: Can proxy requests to backend services

### Container States

- **Running**: Container is actively executing
- **Stopped**: Container exists but not running
- **Paused**: Container processes are paused
- **Restarting**: Container is in restart loop

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

- **← Previous**: [Day 42 - Create Docker Network](./day-42.md)
- **Next →**: [Day 44 - Creating a Docker Compose File](../week-07/day-44.md)

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

