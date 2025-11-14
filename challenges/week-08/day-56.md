# Challenge 56: Deploy Nginx Web Server on Kubernetes Cluster

## 📊 Metadata
- **Day**: 56
- **Week**: 8
- **Day in Week**: 7/7
- **Category**: Linux
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

Some of the Nautilus team developers are developing a static website and they want to deploy it on Kubernetes cluster. They want it to be highly available and scalable. Therefore, based on the requirements, the DevOps team has decided to create a deployment for it with multiple replicas. Below you can find more details about it:

- Create a deployment using nginx image with latest tag only and remember to mention the tag i.e nginx:latest. Name it as nginx-deployment. The container should be named as nginx-container, also make sure replica counts are 3.

- Create a NodePort type service named nginx-service. The nodePort should be 30011.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `ssh`, `sudo`, `useradd`, `cat`, `grep`
- **Key Concepts**:
  - SSH remote access
  - User and group management
  - File permissions and ownership
  - Linux file system hierarchy

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Create a `k3s-deployment.yml` using this [YAML file](../files/k3s-deployment-056.yaml)
2. Execute command to create deployment and service:

    ```sh
    kubectl apply -f k3s-deployment.yml
    ```

3. Verify results:

    ```sh
    kubectl get deployment.apps
    kubectl get pods
    kubectl get svc
    ```

## Good to Know?

### Kubernetes Services

- **Purpose**: Stable network endpoint for pods
- **Service Discovery**: Find and connect to services
- **Load Balancing**: Distribute traffic across pod replicas
- **Abstraction**: Decouple clients from pod implementation

### Service Types

- **ClusterIP**: Internal cluster communication (default)
- **NodePort**: Expose service on each node's IP
- **LoadBalancer**: Cloud provider load balancer
- **ExternalName**: DNS CNAME record for external services

### High Availability

- **Multiple Replicas**: Run multiple pod instances
- **Health Checks**: Automatic failure detection and recovery
- **Rolling Updates**: Zero-downtime deployments
- **Pod Distribution**: Spread pods across nodes

### NodePort Services

- **Port Range**: 30000-32767 (default range)
- **External Access**: Access service from outside cluster
- **Node IP**: Service accessible on all node IPs
- **Firewall**: Ensure nodePort is open in firewall

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
- Practical application of Linux skills
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

- **← Previous**: [Day 55 - Kubernetes Sidecar Containers](./day-55.md)
- **Next →**: [Day 57 - Print Environment Variables](../week-09/day-57.md)

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

