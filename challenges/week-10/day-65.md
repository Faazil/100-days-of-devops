# Challenge 65: Deploy Redis Deployment on Kubernetes

## 📊 Metadata
- **Day**: 65
- **Week**: 10
- **Day in Week**: 2/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus application development team observed some performance issues with one of the application that is deployed in Kubernetes cluster. After looking into number of factors, the team has suggested to use some in-memory caching utility for DB service. After number of discussions, they have decided to use Redis. Initially they would like to deploy Redis on kubernetes cluster for testing and later they will move it to production. Please find below more details about the task:

- Create a redis deployment with following parameters:

- Create a config map called `my-redis-config` having maxmemory `2mb` in `redis-config`.

- Name of the deployment should be `redis-deployment`, it should use `redis:alpine` image and container name should be `redis-container`. Also make sure it has only `1 replica`.

- The container should request for `1 CPU`.

Mount 2 volumes:

a. An Empty directory volume called `data` at path `/redis-master-data`.

b. A configmap volume called `redis-config` at path `/redis-master`.

c. The container should expose the port `6379`.

Finally, `redis-deployment` should be in an up and running state.
Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Kubernetes cluster with kubectl configured
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `kubectl`, `kubectl apply`, `kubectl get`, `kubectl describe`, `kubectl logs`
- **Key Concepts**:
  - Kubernetes resources (Pods, Deployments, Services)
  - YAML manifest structure
  - Resource requests and limits
  - Labels and selectors
- **File Formats**: YAML syntax and structure
- **Environment**: kubectl configured to access Kubernetes cluster

**Foundation from Earlier Challenges:**
- Day 62: Manage Secrets in Kubernetes (recommended)
- Day 63: Deploy Iron Gallery App on Kubernetes (recommended)
- Day 64: Fix Python App Deployed on Kubernetes Cluster (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. create a `k3s-deployment.yaml` file and copy-paste the contents from this [YAML file](../files/k3s-redis-deployment-065.yml)

2. Run the deployment

    ```sh
    kubectl apply -f k3s-deployment.yaml
    ```

3. verify result

    ```sh
    kubectl get pods
    ```

## Good to Know?

### Redis on Kubernetes

- **In-Memory Database**: High-performance key-value store
- **Caching**: Improve application performance with caching
- **Data Structures**: Supports strings, hashes, lists, sets
- **Persistence**: Optional data persistence to disk

### ConfigMap Configuration

- **Redis Config**: Store Redis configuration in ConfigMap
- **Memory Limits**: Set maxmemory to prevent OOM
- **Eviction Policies**: Configure memory eviction strategies
- **Persistence**: Configure RDB or AOF persistence

### Resource Management

- **CPU Requests**: Redis is CPU-intensive for some operations
- **Memory Limits**: Set appropriate memory limits
- **Storage**: Use persistent volumes for data persistence
- **Monitoring**: Monitor memory usage and hit rates

### Production Considerations

- **High Availability**: Redis Sentinel or Cluster mode
- **Backup**: Regular backup of Redis data
- **Security**: Authentication and network policies
- **Scaling**: Horizontal scaling with Redis Cluster

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
- Practical application of Kubernetes skills
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

- **← Previous**: [Day 64 - Fix Python App Deployed on Kubernetes Cluster](./day-64.md)
- **Next →**: [Day 66 - Deploy MySQL on Kubernetes](../week-10/day-66.md)

### Similar Challenges (Kubernetes)
- [Day 58 - Deploy Grafana on Kubernetes Cluster](../week-09/day-58.md)
- [Day 59 - Troubleshoot Deployment Issues in Kubernetes](../week-09/day-59.md)
- [Day 60 - Persistent Volumes in Kubernetes](../week-09/day-60.md)

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

