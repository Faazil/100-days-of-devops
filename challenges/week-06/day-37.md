# Challenge 37: Copy File to Docker Container

## 📊 Metadata
- **Day**: 37
- **Week**: 6
- **Day in Week**: 2/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team is conducting application deployment tests on selected application servers. They require completing a task on app server 1.

On Application Server 1 a container named ubuntu_latest is running, you have to copy the encrypted file `/tmp/nautilus.tx.gpg` from docker hosts to container folder `/usr/src`.


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
- Day 36: Run a NGINX Container on Docker (recommended)

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

Login into App Server and run the following command:

```sh
docker cp /tmp/nautilus.txt.gpg ubuntu_latest:/usr/src/
```

## Good to Know?

### Docker Copy Operations

- **Purpose**: Transfer files between host and containers
- **Bidirectional**: Copy from host to container or vice versa
- **Running Containers**: Works with both running and stopped containers
- **Preserve Permissions**: Maintains file ownership and permissions

### Copy Command Syntax

- **Host to Container**: `docker cp /host/path container:/container/path`
- **Container to Host**: `docker cp container:/container/path /host/path`
- **Directory Copy**: Use `-a` flag to preserve attributes
- **Recursive**: Automatically copies directories recursively

### Use Cases

- **Configuration**: Deploy config files to containers
- **Logs**: Extract log files for analysis
- **Debugging**: Copy files for troubleshooting
- **Backup**: Extract data from containers

### Best Practices

- **Volume Mounts**: Prefer volumes for persistent data
- **Build Time**: Use COPY in Dockerfile for build-time files
- **Security**: Be cautious with file permissions
- **Temporary**: Use docker cp for temporary file transfers

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

- **← Previous**: [Day 36 - Run a NGINX Container on Docker](./day-36.md)
- **Next →**: [Day 38 - Docker Pull Images](../week-06/day-38.md)

### Similar Challenges (Docker)
- [Day 35 - Setup Docker Installation](../week-05/day-35.md)
- [Day 36 - Run a NGINX Container on Docker](../week-06/day-36.md)
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

