# Day 47: Docker Python App

## Task Overview

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

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
sudo -i
    cd /pythona_app
```

**Step 2:**
```bash
sudo vi Dockerfile
```

**Step 3:**
```bash
3. Build Docker Image
```

**Step 4:**
```bash
4. Run the container
```

**Step 5:**
```bash
5. Verify
```

**Step 6:**
```bash
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
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 46](day-46.md) | [Day 48 →](day-48.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
