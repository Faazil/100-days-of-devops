# Challenge 39: Create a Docker Image From a Container

## 📊 Metadata
- **Day**: 39
- **Week**: 6
- **Day in Week**: 4/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

One of the Nautilus developer was working to test new changes on a container. He wants to keep a backup of his changes to the container. A new request has been raised for the DevOps team to create a new image from this container. Below are more details about it:

- Create an image `ecommerce:nautilus` on `Application Server 3` from a container `ubuntu_latest` that is running on same server.


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
- Day 36: Run a NGINX Container on Docker (recommended)
- Day 37: Copy File to Docker Container (recommended)
- Day 38: Docker Pull Images (recommended)

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

To create a docker image from a running container, we can use the following command:

```sh
docker commit container-name image-repository:tag
```

In this case, the actual command is:

```sh
docker commit ubuntu_latest ecommerce:nautilus
```

## Good to Know?

### Docker Commit

- **Purpose**: Create new image from container's changes
- **Snapshot**: Captures current state of container
- **Layer Addition**: Adds new layer on top of base image
- **Persistence**: Preserves modifications made to container

### When to Use Commit

- **Quick Prototyping**: Rapid image creation during development
- **Manual Changes**: Capture manual configurations
- **Debugging**: Save state for later analysis
- **Backup**: Create checkpoint of working container

### Commit vs Dockerfile

- **Dockerfile**: Preferred for production (reproducible, version-controlled)
- **Commit**: Good for experimentation and quick fixes
- **Transparency**: Dockerfile shows exact build steps
- **Automation**: Dockerfile enables automated builds

### Best Practices

- **Documentation**: Add commit message explaining changes
- **Minimize Layers**: Avoid excessive commits
- **Clean State**: Remove temporary files before commit
- **Dockerfile Migration**: Convert successful commits to Dockerfile

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

- **← Previous**: [Day 38 - Docker Pull Images](./day-38.md)
- **Next →**: [Day 40 - Docker Execution](../week-06/day-40.md)

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

