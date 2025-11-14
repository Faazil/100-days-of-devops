# Challenge 61: Init Containers in Kubernetes

## 📊 Metadata
- **Day**: 61
- **Week**: 9
- **Day in Week**: 5/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

There are some applications that need to be deployed on Kubernetes cluster and these apps have some pre-requisites where some configurations need to be changed before deploying the app container. Some of these changes cannot be made inside the images so the DevOps team has come up with a solution to use init containers to perform these tasks during deployment. Below is a sample scenario that the team is going to test first.

- Create a Deployment named as `ic-deploy-devops`.

- Configure spec as `replicas` should be `1`, labels app should be `ic-devops`, template's metadata lables app should be the same `ic-devops`.

- The initContainers should be named as `ic-msg-devops`, use image `debian` with latest tag and use command `'/bin/bash', '-c' and 'echo Init Done - Welcome to xFusionCorp Industries > /ic/media'`. The volume mount should be named as `ic-volume-devops` and mount path should be `/ic`.

- Main container should be named as `ic-main-devops`, use image debian with latest tag and use command `'/bin/bash', '-c' and 'while true; do cat /ic/media; sleep 5; done'`. The volume mount should be named as `ic-volume-devops` and mount path should be `/ic`.

- Volume to be named as `ic-volume-devops` and it should be an `emptyDir` type.

> Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.


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
- Day 46: Deploy an App on Docker Containers (recommended)
- Day 47: Docker Python App (recommended)
- Day 55: Kubernetes Sidecar Containers (recommended)

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Create the `k3s-deployment.yaml` using the content from this [YAML file](../files/k3s-deployment-ic-061.yaml)

2. Run deployment:

    ```sh
    kubectl apply -f k3s-deployment.yaml
    ```

3. Verify resuls:

    ```sh
    kubectl get deployments.apps
    kubectl get pods
    ```

## Good to Know?

### Init Containers

- **Purpose**: Run before main application containers
- **Sequential Execution**: Run one after another, not parallel
- **Completion Required**: Must complete successfully before main containers start
- **Shared Resources**: Share volumes and network with main containers

### Use Cases

- **Setup Tasks**: Database schema creation, file downloads
- **Dependency Checks**: Wait for services to be available
- **Configuration**: Generate config files, set permissions
- **Security**: Fetch certificates, decrypt secrets

### Init Container Behavior

- **Restart Policy**: Always restart on failure
- **Resource Sharing**: Share volumes with main containers
- **Network**: Same network namespace as main containers
- **Failure Handling**: Pod won't start if init container fails

### Best Practices

- **Idempotent**: Init containers should be safe to run multiple times
- **Fast Execution**: Keep init tasks quick to reduce startup time
- **Error Handling**: Proper error handling and logging
- **Resource Limits**: Set appropriate resource limits

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

- **← Previous**: [Day 60 - Persistent Volumes in Kubernetes](./day-60.md)
- **Next →**: [Day 62 - Manage Secrets in Kubernetes](../week-09/day-62.md)

### Similar Challenges (Docker)
- [Day 55 - Kubernetes Sidecar Containers](../week-08/day-55.md)

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

