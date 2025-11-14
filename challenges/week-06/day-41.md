# Challenge 41: Create a Docker File

## 📊 Metadata
- **Day**: 41
- **Week**: 6
- **Day in Week**: 6/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

As per recent requirements shared by the Nautilus application development team, they need custom images created for one of their projects. Several of the initial testing requirements are already been shared with DevOps team. Therefore, create a docker file `/opt/docker/Dockerfile` (please keep D capital of Dockerfile) on `App server 2` in Stratos DC and configure to build an image with the following requirements:

- Use `ubuntu:24.04` as the base image.

- Install `apache2` and configure it to work on `5002` port. (do not update any other Apache configuration settings like document root etc).


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
- Day 38: Docker Pull Images (recommended)
- Day 39: Create a Docker Image From a Container (recommended)
- Day 40: Docker Execution (recommended)

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

[Dockerfile](../scripts/Dockerfile)

## Good to Know?

### Dockerfile Fundamentals

- **Purpose**: Text file with instructions to build Docker images
- **Automation**: Reproducible image creation process
- **Layered**: Each instruction creates a new layer
- **Caching**: Docker caches layers for faster builds

### Common Dockerfile Instructions

- **FROM**: Base image to start from
- **RUN**: Execute commands during build
- **COPY/ADD**: Copy files from host to image
- **WORKDIR**: Set working directory
- **EXPOSE**: Document which ports the container uses
- **CMD/ENTRYPOINT**: Default command when container starts

### Best Practices

- **Minimal Base**: Use smallest possible base image
- **Layer Optimization**: Combine RUN commands to reduce layers
- **Cache Efficiency**: Order instructions by change frequency
- **Security**: Don't run as root, use specific versions

### Apache in Docker

- **Port Configuration**: Modify default port 80 to custom port
- **Configuration Files**: Update httpd.conf for custom settings
- **Document Root**: Set appropriate web content directory
- **Process Management**: Ensure Apache runs in foreground

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

- **← Previous**: [Day 40 - Docker Execution](./day-40.md)
- **Next →**: [Day 42 - Create Docker Network](../week-06/day-42.md)

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

