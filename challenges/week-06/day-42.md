# Challenge 42: Create Docker Network

## 📊 Metadata
- **Day**: 42
- **Week**: 6
- **Day in Week**: 7/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team needs to set up several docker environments for different applications. One of the team members has been assigned a ticket where he has been asked to create some docker networks to be used later. Complete the task based on the following ticket description:

- Create a docker network named as `blog` on App Server 2 in Stratos DC.
- Configure it to use `macvlan` drivers.
- Set it to use subnet `10.10.1.0/24` and iprange `10.10.1.0/24`.


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
- Day 39: Create a Docker Image From a Container (recommended)
- Day 40: Docker Execution (recommended)
- Day 41: Create a Docker File (recommended)

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

Login into app server 2 and run the following command:

```sh
docker network create blog -d macvlan --ip-range 10.10.1.0/24 --subnet 10.10.1.0/24
```

To verify run the following command:

```sh
docker network ls
```

If you need to understand more on `docker network` command, you can use `help`:

```sh
docker network --help
```

## Good to Know?

### Docker Networking

- **Purpose**: Enable communication between containers and external networks
- **Isolation**: Network segmentation for security
- **Service Discovery**: Containers can find each other by name
- **Load Balancing**: Distribute traffic across container instances

### Network Drivers

- **bridge**: Default driver for single-host networking
- **host**: Remove network isolation, use host networking
- **overlay**: Multi-host networking for swarm mode
- **macvlan**: Assign MAC addresses to containers
- **none**: Disable networking for container

### MACVLAN Driver

- **Purpose**: Make containers appear as physical devices on network
- **MAC Addresses**: Each container gets unique MAC address
- **VLAN Support**: Support for VLAN tagging
- **Performance**: Direct access to physical network

### Network Configuration

- **Subnet**: IP address range for the network
- **IP Range**: Subset of subnet for container assignment
- **Gateway**: Default route for network traffic
- **DNS**: Custom DNS configuration for containers

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

- **← Previous**: [Day 41 - Create a Docker File](./day-41.md)
- **Next →**: [Day 43 - Docker Ports Mapping](../week-07/day-43.md)

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

