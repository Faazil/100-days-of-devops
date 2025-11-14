# Day 50: Set Resource Limits in Kubernetes Cluster

## Task Overview

The Nautilus DevOps team has noticed performance issues in some Kubernetes-hosted applications due to resource constraints. To address this, they plan to set limits on resource utilization. Here are the details:

- Create a pod named `httpd-pod` with a container named `httpd-container`. Use the `httpd` image with the latest tag (specify as httpd:latest). Set the following resource limits:
- Requests: Memory: 15Mi, CPU: 100m
- Limits: Memory: 20Mi, CPU: 100m

> Note: The kubectl utility on jump_host is configured to operate with the Kubernetes cluster.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
- Let's create the pod:
```

**Step 2:**
```bash
- Verify pod:
```

**Step 3:**
```bash
## Good to Know?

### Resource Management

- **Requests**: Minimum resources guaranteed to container
- **Limits**: Maximum resources container can use
- **Quality of Service**: BestEffort, Burstable, Guaranteed
- **Resource Types**: CPU (cores), Memory (bytes), Storage

### CPU Resources

- **Units**: Cores (1000m = 1 core)
- **Fractional**: 100m = 0.1 core
- **Throttling**: CPU limits enforced by throttling
- **Scheduling**: Requests used for pod placement

### Memory Resources

- **Units**: Bytes (Ki, Mi, Gi)
- **OOM Killer**: Exceeding limits triggers container kill
- **Non-compressible**: Memory cannot be throttled
- **Eviction**: Node pressure can evict pods

### Resource Planning

- **Monitoring**: Track actual resource usage
- **Right-sizing**: Set appropriate requests and limits
- **Node Capacity**: Consider node resource availability
- **Cluster Autoscaling**: Scale nodes based on resource needs

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

- **← Previous**: [Day 49 - Deploy Applications with Kubernetes Deployments](./day-49.md)
- **Next →**: [Day 51 - Execute Rolling Updates in Kubernetes](../week-08/day-51.md)

### Similar Challenges (Kubernetes)
- [Day 48 - Deploy Pods in Kubernetes Cluster](../week-07/day-48.md)
- [Day 49 - Deploy Applications with Kubernetes Deployments](../week-07/day-49.md)
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
**Difficulty**: ⭐
**Category**: DevOps

---

**Track your progress**: After completing this challenge, mark it as done:
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 49](../week-07/day-49.md) | [Day 51 →](day-51.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
