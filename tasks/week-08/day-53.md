# Day 53: Resolve VolumeMounts Issue in Kubernetes

## Task Overview

We encountered an issue with our Nginx and PHP-FPM setup on the Kubernetes cluster this morning, which halted its functionality. Investigate and rectify the issue:

- The pod name is `nginx-phpfpm` and configmap name is `nginx-config`. Identify and fix the problem.

- Once resolved, copy `/home/thor/index.php` file from the jump host to the `nginx-container` within the nginx document root. After this, you should be able to access the website using Website button on the top bar.

> Note: The kubectl utility on jump_host is configured to operate with the Kubernetes cluster.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
kubectl get pod nginx-phpfpm -o yaml > nginx-phpfpm.yml
```

**Step 2:**
```bash
vi nginx-phpfpm.yml
```

**Step 3:**
```bash
> Which volume path is the right one? To be confirmed the right mount path let's see the data of `nginx-config` configmap.

    ![shared-path-issue](../screenshots/kubernetes_shared_file_path_issue.png)

3. To see the configmap data:
```

**Step 5:**
```bash
> we can see our nginx root directory is: `/var/www/html`. So let's update the mount path of nginx container with this. Once we updated the `nginx-phpfpm.yml`, let's move into the next steps.

4. Let's re-create the pod
```

**Step 6:**
```bash
5. Now, let's copy `index.php`
```

**Step 7:**
```bash
6. Test:
```

**Step 8:**
```bash
## Good to Know?

### Volume Troubleshooting

- **Mount Path Mismatch**: Containers must share same mount path
- **ConfigMap Issues**: Verify ConfigMap exists and is correctly named
- **Permission Problems**: Check file system permissions
- **Volume Types**: emptyDir, hostPath, PVC, ConfigMap, Secret

### Multi-Container Pods

- **Shared Volumes**: Containers share volumes within pod
- **Sidecar Pattern**: Helper containers alongside main application
- **Data Sharing**: Share files between containers
- **Log Aggregation**: Collect logs from multiple containers

### ConfigMap Volumes

- **Configuration Files**: Mount config files into containers
- **subPath**: Mount specific files from ConfigMap
- **File Mode**: Set file permissions for mounted files
- **Updates**: ConfigMap changes reflect in mounted volumes

### Debugging Techniques

- **Describe Pod**: `kubectl describe pod` shows events and issues
- **Pod Logs**: `kubectl logs pod-name -c container-name`
- **Exec into Pod**: `kubectl exec -it pod-name -c container -- /bin/sh`
- **Volume Inspection**: Check mount points and file contents

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

- **← Previous**: [Day 52 - Execute Rollback in Kubernetes Cluster](./day-52.md)
- **Next →**: [Day 54 - Kubernetes Shared Volumes](../week-08/day-54.md)

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
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 52](day-52.md) | [Day 54 →](day-54.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
