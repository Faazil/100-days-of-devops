# Challenge 54: Kubernetes Shared Volumes

## 📊 Metadata
- **Day**: 54
- **Week**: 8
- **Day in Week**: 5/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

We are working on an application that will be deployed on multiple containers within a pod on Kubernetes cluster. There is a requirement to share a volume among the containers to save some temporary data. The Nautilus DevOps team is developing a similar template to replicate the scenario. Below you can find more details about it.

- Create a pod named `volume-share-nautilus`.

- For the first container, use image `fedora` with `latest` tag only and remember to mention the tag i.e `fedora:latest`, container should be named as `volume-container-nautilus-1`, and run a sleep command for it so that it remains in running state. Volume `volume-share` should be mounted at path `/tmp/news`.

- For the second container, use image fedora with the latest tag only and remember to mention the tag i.e `fedora:latest`, container should be named as `volume-container-nautilus-2`, and again run a sleep command for it so that it remains in running state. Volume `volume-share` should be mounted at path `/tmp/demo`.

- Volume name should be `volume-share` of type `emptyDir`.

- After creating the pod, exec into the first container i.e `volume-container-nautilus-1`, and just for testing create a file `news.txt` with any content under the mounted path of first container i.e `/tmp/news`.

- The file `news.txt` should be present under the mounted path `/tmp/demo` on the second container `volume-container-nautilus-2` as well, since they are using a shared volume.

> Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.


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
- Day 51: Execute Rolling Updates in Kubernetes (recommended)
- Day 52: Execute Rollback in Kubernetes Cluster (recommended)
- Day 53: Resolve VolumeMounts Issue in Kubernetes (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Let's create the `k3s-pod.yml` file using the [contnets](../files/k3s-shared-volume.yml)

2. Create the pod

    ```sh
    kubectl apply -f k3s-pod.yml
    ```

3. Execute the first container

    ```sh
    kubectl exec -it volume-share-nautilus -c volume-container-nautilus-1 /bin/sh
    ```

    > Create `news.txt` file

    ```sh
    touch /tmp/news/news.txt
    ```

4. Execute the 2nd container

    ```sh
    kubectl exec -it volume-share-nautilus -c volume-container-nautilus-2 /bin/sh
    ```

    > Verify the created files under shared directory

    ```sh
    ls /tmp/demo
    ```

## Good to Know?

### Shared Volumes

- **emptyDir**: Temporary storage shared between containers
- **Pod Lifetime**: Volume exists for pod's lifetime
- **Memory Storage**: Can use memory as storage medium
- **Data Sharing**: Enable inter-container communication

### Volume Types

- **emptyDir**: Empty directory, deleted when pod removed
- **hostPath**: Mount directory from host node
- **persistentVolumeClaim**: Persistent storage
- **configMap/secret**: Configuration and sensitive data

### Multi-Container Use Cases

- **Log Shipping**: Sidecar collects and ships logs
- **Data Processing**: One container produces, another consumes
- **Configuration Sharing**: Share config files between containers
- **Backup Operations**: Backup container accesses main app data

### Container Communication

- **Shared Filesystem**: Files written by one, read by another
- **Localhost Network**: Containers share network namespace
- **Process Signals**: Containers can send signals to each other
- **Resource Sharing**: Share CPU, memory, and storage resources

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

- **← Previous**: [Day 53 - Resolve VolumeMounts Issue in Kubernetes](./day-53.md)
- **Next →**: [Day 55 - Kubernetes Sidecar Containers](../week-08/day-55.md)

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

