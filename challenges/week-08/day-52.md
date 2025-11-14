# Challenge 52: Execute Rollback in Kubernetes Cluster

## 📊 Metadata
- **Day**: 52
- **Week**: 8
- **Day in Week**: 3/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

Earlier today, the Nautilus DevOps team deployed a new release for an application. However, a customer has reported a bug related to this recent release. Consequently, the team aims to revert to the previous version.

- There exists a deployment named nginx-deployment; initiate a rollback to the previous revision.


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
- Day 49: Deploy Applications with Kubernetes Deployments (recommended)
- Day 50: Set Resource Limits in Kubernetes Cluster (recommended)
- Day 51: Execute Rolling Updates in Kubernetes (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Let's see the deployments and pods

    ```sh
    kubectl get deployments.apps
    kubectl get pods
    ```

2. Let's see current container image version

    ```sh
    kubectl describe pods pod-name
    ```

3. To roll back the deployment to our last working version, we can use the following command:

    ```sh
    kubectl rollout undo deployments/nginx-deployment
    ```

    > It will move back to prevous version of deployments

## Good to Know?

### Rollback Operations

- **Purpose**: Revert to previous working version
- **Revision History**: Kubernetes maintains deployment history
- **Quick Recovery**: Fast recovery from failed deployments
- **Automatic**: Can be triggered by failed health checks

### Rollback Commands

- **Undo**: `kubectl rollout undo deployment/name`
- **Specific Revision**: `kubectl rollout undo deployment/name --to-revision=2`
- **History**: `kubectl rollout history deployment/name`
- **Revision Details**: `kubectl rollout history deployment/name --revision=3`

### Revision Management

- **Revision Limit**: Configure `revisionHistoryLimit`
- **Change Cause**: Use `--record` flag to track changes
- **Annotations**: Kubernetes tracks change causes
- **Cleanup**: Old ReplicaSets are retained for rollback

### Rollback Scenarios

- **Failed Deployment**: Application not starting correctly
- **Performance Issues**: New version causing problems
- **Bug Discovery**: Critical bugs found in production
- **Configuration Errors**: Incorrect environment variables

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

- **← Previous**: [Day 51 - Execute Rolling Updates in Kubernetes](./day-51.md)
- **Next →**: [Day 53 - Resolve VolumeMounts Issue in Kubernetes](../week-08/day-53.md)

### Similar Challenges (Kubernetes)
- [Day 48 - Deploy Pods in Kubernetes Cluster](../week-07/day-48.md)
- [Day 49 - Deploy Applications with Kubernetes Deployments](../week-07/day-49.md)
- [Day 50 - Set Resource Limits in Kubernetes Cluster](../week-08/day-50.md)

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

