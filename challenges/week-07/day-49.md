# Challenge 49: Deploy Applications with Kubernetes Deployments

## 📊 Metadata
- **Day**: 49
- **Week**: 7
- **Day in Week**: 7/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team is delving into Kubernetes for app management. One team member needs to create a deployment following these details:

Create a deployment named nginx to deploy the application nginx using the image nginx:latest (ensure to specify the tag)

Note: The kubectl utility on jump_host is set up to interact with the Kubernetes cluster.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

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
- Day 48: Deploy Pods in Kubernetes Cluster (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

Let's create the `k3s-deployment.yml` file with these contents:

```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  labels:
    app: nginx

spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 1
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:latest
          ports:
          - containerPort: 80
```

- Run the following commands to create the deployment:

  ```sh
  kubectl apply -f k3s-deployment.yml
  ```

- Verify Deployments

  ```sh
  kubectl get deployments.apps
  ```

## Good to Know?

### Kubernetes Deployments

- **Purpose**: Manage stateless applications with declarative updates
- **ReplicaSets**: Deployments create and manage ReplicaSets
- **Rolling Updates**: Zero-downtime application updates
- **Rollback**: Easy rollback to previous versions

### Deployment Components

- **Selector**: Matches pods using labels
- **Replicas**: Desired number of pod instances
- **Template**: Pod specification for creating instances
- **Strategy**: Update strategy (RollingUpdate, Recreate)

### Labels and Selectors

- **Labels**: Key-value pairs attached to objects
- **Selectors**: Query labels to identify objects
- **Loose Coupling**: Flexible object relationships
- **Organization**: Group and categorize resources

### Best Practices

- **Resource Limits**: Set CPU and memory limits
- **Health Checks**: Configure liveness and readiness probes
- **Image Tags**: Use specific tags, avoid 'latest'
- **Naming**: Use descriptive names for resources

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

- **← Previous**: [Day 48 - Deploy Pods in Kubernetes Cluster](./day-48.md)
- **Next →**: [Day 50 - Set Resource Limits in Kubernetes Cluster](../week-08/day-50.md)

### Similar Challenges (Kubernetes)
- [Day 48 - Deploy Pods in Kubernetes Cluster](../week-07/day-48.md)
- [Day 50 - Set Resource Limits in Kubernetes Cluster](../week-08/day-50.md)
- [Day 51 - Execute Rolling Updates in Kubernetes](../week-08/day-51.md)

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

