# Challenge 48: Deploy Pods in Kubernetes Cluster

## 📊 Metadata
- **Day**: 48
- **Week**: 7
- **Day in Week**: 6/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team is diving into Kubernetes for application management. One team member has a task to create a pod according to the details below:

- Create a pod named pod-httpd using the httpd image with the latest tag. Ensure to specify the tag as httpd:latest.

- Set the app label to httpd_app, and name the container as httpd-container.

> Note: The kubectl utility on jump_host is configured to operate with the Kubernetes cluster.


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

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

- Create a `k3s-pod.yml` file inside the jump host with this [contents](../files/k3s-pod.yml)
- Run the following command to create pod in kubernetes cluster:

    ```sh
    kubectl apply -f k3s-pod.yml
    ```

- Check if pod is running or not:

    ```sh
    kubectl get pods
    ```

## Good to Know?

### Kubernetes Pods

- **Smallest Unit**: Basic deployable unit in Kubernetes
- **Container Group**: One or more containers sharing resources
- **Shared Network**: Containers share IP address and ports
- **Shared Storage**: Volumes mounted to all containers in pod

### Pod Lifecycle

- **Pending**: Pod accepted but not yet scheduled
- **Running**: Pod bound to node and containers created
- **Succeeded**: All containers terminated successfully
- **Failed**: At least one container failed
- **Unknown**: Pod state cannot be determined

### YAML Manifest Structure

- **apiVersion**: Kubernetes API version
- **kind**: Resource type (Pod, Deployment, Service)
- **metadata**: Name, labels, annotations
- **spec**: Desired state specification

### kubectl Commands

- **Create**: `kubectl apply -f pod.yaml`
- **List**: `kubectl get pods`
- **Describe**: `kubectl describe pod pod-name`
- **Logs**: `kubectl logs pod-name`
- **Delete**: `kubectl delete pod pod-name`

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

- **← Previous**: [Day 47 - Docker Python App](./day-47.md)
- **Next →**: [Day 49 - Deploy Applications with Kubernetes Deployments](../week-07/day-49.md)

### Similar Challenges (Kubernetes)
- [Day 49 - Deploy Applications with Kubernetes Deployments](../week-07/day-49.md)
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

