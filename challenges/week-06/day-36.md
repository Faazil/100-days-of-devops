# Challenge 36: Run a NGINX Container on Docker

## 📊 Metadata
- **Day**: 36
- **Week**: 6
- **Day in Week**: 1/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team is conducting application deployment tests on selected application servers. They require a nginx container deployment on Application Server 1. Complete the task with the following instructions:

On Application Server 1 create a container named nginx_1 using the nginx image with the alpine tag. Ensure container is in a running state.


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
- Day 35: Setup Docker Installation (recommended)

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

Lets run the following command to run a docker container:

```sh
sudo docker run -d --name nginx_1 -p 80:80 nginx:alpine
```

## Good to Know?

### Docker Container Basics

- **Container**: Running instance of Docker image
- **Image**: Read-only template for creating containers
- **Lightweight**: Share host OS kernel, faster than VMs
- **Isolation**: Process and filesystem isolation

### Docker Run Options

- **-d**: Detached mode (run in background)
- **--name**: Assign custom name to container
- **-p**: Port mapping (host:container)
- **-v**: Volume mounting for persistent data

### NGINX Alpine

- **Alpine Linux**: Minimal Linux distribution (~5MB)
- **Security**: Reduced attack surface
- **Performance**: Faster startup and lower resource usage
- **Production**: Ideal for production deployments

### Container Management

- **List**: `docker ps` (running), `docker ps -a` (all)
- **Stop**: `docker stop container-name`
- **Start**: `docker start container-name`
- **Remove**: `docker rm container-name`

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

- **← Previous**: [Day 35 - Setup Docker Installation](./day-35.md)
- **Next →**: [Day 37 - Copy File to Docker Container](../week-06/day-37.md)

### Similar Challenges (Docker)
- [Day 35 - Setup Docker Installation](../week-05/day-35.md)
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
```bash
```

