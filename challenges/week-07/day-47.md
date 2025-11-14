# Challenge 47: Docker Python App

## 📊 Metadata
- **Day**: 47
- **Week**: 7
- **Day in Week**: 5/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

A python app needed to be Dockerized, and then it needs to be deployed on App Server 3. We have already copied a requirements.txt file (having the app dependencies) under /python_app/src/ directory on App Server 3. Further complete this task as per details mentioned below:

- Create a Dockerfile under /python_app directory:

  - Use any python image as the base image.
  - Install the dependencies using requirements.txt file.
  - Expose the port 6300.
  - Run the server.py script using CMD.

- Build an image named nautilus/python-app using this Dockerfile.

- Once image is built, create a container named pythonapp_nautilus:

  - Map port 6300 of the container to the host port 8096.

- Once deployed, you can test the app using curl command on App Server 3.


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
- Day 44: Creating a Docker Compose File (recommended)
- Day 45: Resolve Dockerfile Issues (recommended)
- Day 46: Deploy an App on Docker Containers (recommended)

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Access App server and move into directory

    ```sh
    sudo -i
    cd /pythona_app
    ```

2. Create Docker file and copy paste the contents:

    ```sh
    sudo vi Dockerfile
    ```

    ```Dockerfile

    FROM python:3.9.23-slim

    WORKDIR /app

    COPY ./src/* /app/

    RUN pip install -r requirements.txt

    EXPOSE 6300

    CMD ["python", "server.py"]
    ```

3. Build Docker Image

    ```sh
    docker build -t nautilus/python-app .
    ```

4. Run the container

    ```sh
    docker run -d --name pythonapp_nautilus -p 8096:6300 nautilus/python-app
    ```

5. Verify

    ```sh
    docker ps
    curl http://localhost:8096
    ```

## Good to Know?

### Python Application Containerization

- **Dependency Management**: requirements.txt defines Python packages
- **Virtual Environment**: Container provides isolated Python environment
- **Reproducibility**: Same dependencies across all environments
- **Portability**: Run anywhere Docker is available

### Python Docker Images

- **Official Images**: python:3.9, python:3.9-slim, python:3.9-alpine
- **Size Optimization**: Slim images exclude unnecessary packages
- **Alpine**: Minimal Linux distribution for smallest images
- **Version Pinning**: Use specific versions for consistency

### Dockerfile Best Practices

- **WORKDIR**: Set working directory for organization
- **COPY Order**: Copy requirements.txt first for better caching
- **Layer Optimization**: Combine RUN commands when possible
- **EXPOSE**: Document which ports application uses

### Application Deployment

- **Port Mapping**: Map container port to host port
- **Health Checks**: Verify application is responding
- **Logging**: Configure application logging
- **Environment Variables**: Use for configuration

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

- **← Previous**: [Day 46 - Deploy an App on Docker Containers](./day-46.md)
- **Next →**: [Day 48 - Deploy Pods in Kubernetes Cluster](../week-07/day-48.md)

### Similar Challenges (Docker)
- [Day 37 - Copy File to Docker Container](../week-06/day-37.md)
- [Day 38 - Docker Pull Images](../week-06/day-38.md)
- [Day 39 - Create a Docker Image From a Container](../week-06/day-39.md)

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

