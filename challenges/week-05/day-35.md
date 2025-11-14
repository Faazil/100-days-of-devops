# Challenge 35: Setup Docker Installation

## 📊 Metadata
- **Day**: 35
- **Week**: 5
- **Day in Week**: 7/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team aims to containerize various applications following a recent meeting with the application development team. They intend to conduct testing with the following steps:

- Install docker-ce and docker compose packages on App Server 2.
- Initiate the docker service.


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

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Login into App server 2 and find out the linux distros

    ```sh
    cat /etc/os-release
    uname -a
    ```

    ```shell
    [steve@stapp02 ~]$ cat /etc/os-release 
    NAME="CentOS Stream"
    VERSION="9"
    ID="centos"
    ID_LIKE="rhel fedora"
    VERSION_ID="9"
    PLATFORM_ID="platform:el9"
    PRETTY_NAME="CentOS Stream 9"
    ANSI_COLOR="0;31"
    LOGO="fedora-logo-icon"
    CPE_NAME="cpe:/o:centos:centos:9"
    HOME_URL="https://centos.org/"
    BUG_REPORT_URL="https://issues.redhat.com/"
    REDHAT_SUPPORT_PRODUCT="Red Hat Enterprise Linux 9"
    REDHAT_SUPPORT_PRODUCT_VERSION="CentOS Stream"
    ```

    > We can see it's CentOS 9 os
    > To install Docker on CentOS, follow the [official docs](https://docs.docker.com/engine/install/centos/)

2. Available Methods

    You can install docker in many ways, like using RPM repository, downloading the docker package, or using a bash script. I would recommended to install using rpm repository, or using one script solution.

3. Install Using BASH Script

    ```sh
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    ```

4. Enable Docker Service

    ```sh
    sudo systemctl enable docker.service
    sudo systemctl start docker.service
    ```

## Good to Know?

### Docker Fundamentals

- **Containerization**: Package applications with dependencies
- **Images**: Read-only templates for creating containers
- **Containers**: Running instances of Docker images
- **Dockerfile**: Text file with instructions to build images

### Docker Architecture

- **Docker Engine**: Core runtime for containers
- **Docker Daemon**: Background service managing containers
- **Docker CLI**: Command-line interface for Docker
- **Docker Registry**: Store and distribute Docker images

### Installation Methods

- **Repository**: Add Docker repo and install via package manager
- **Package**: Download and install .deb/.rpm packages
- **Script**: Automated installation script (convenience)
- **Docker Desktop**: GUI application for development

### Key Benefits

- **Portability**: Run anywhere Docker is installed
- **Consistency**: Same environment across dev/test/prod
- **Efficiency**: Share OS kernel, lightweight
- **Scalability**: Easy horizontal scaling

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

- **← Previous**: [Day 34 - Configure Git Hook](./day-34.md)
- **Next →**: [Day 36 - Run a NGINX Container on Docker](../week-06/day-36.md)

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

