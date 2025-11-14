# Day 60: Persistent Volumes in Kubernetes

## Task Overview

The Nautilus DevOps team is working on a Kubernetes template to deploy a web application on the cluster. There are some requirements to create/use persistent volumes to store the application code, and the template needs to be designed accordingly. Please find more details below:

- Create a `PersistentVolume` named as `pv-xfusion`. Configure the `spec` as storage class should be `manual`, set capacity to `3Gi`, set access mode to `ReadWriteOnce`, volume type should be `hostPath` and set path to `/mnt/security` (this directory is already created, you might not be able to access it directly, so you need not to worry about it).
- Create a `PersistentVolumeClaim` named as `pvc-xfusion`. Configure the spec as storage class should be `manual`, request `3Gi` of the storage, set access mode to `ReadWriteOnce`.
- Create a `pod` named as `pod-xfusion`, mount the persistent volume you created with claim name `pvc-xfusion` at document root of the web server, the container within the pod should be named as `container-xfusion` using image `httpd` with latest tag only (remember to mention the tag i.e `httpd:latest`).
- Create a node port type service named `web-xfusion` using node port `30008` to expose the web server running within the pod.

> Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
> Create the volume:
```

**Step 2:**
```bash
2. Create the persistent volume claim `k3s-pvc.yaml` with this following content:
```

**Step 3:**
```bash
To create the pvc:
```

**Step 4:**
```bash
3. Create the pod `k3s-pod.yaml`:
```

**Step 5:**
```bash
> run the pod
```

**Step 6:**
```bash
4. And finally, create the service `k3s-svc.yaml`:
```

**Step 8:**
```bash
5. We can put all in one file [k3s-pod.yaml](../files/k3s-pod-060.yaml)

## Good to Know?

### Persistent Volumes (PV)

- **Purpose**: Cluster-wide storage resources
- **Lifecycle**: Independent of pod lifecycle
- **Storage Classes**: Different types of storage (SSD, HDD, NFS)
- **Access Modes**: ReadWriteOnce, ReadOnlyMany, ReadWriteMany

### Persistent Volume Claims (PVC)

- **Purpose**: Request for storage by pods
- **Binding**: PVC binds to suitable PV
- **Dynamic Provisioning**: Automatic PV creation
- **Storage Classes**: Specify storage requirements

### Volume Types

- **hostPath**: Mount directory from host (development only)
- **nfs**: Network File System
- **awsElasticBlockStore**: AWS EBS volumes
- **gcePersistentDisk**: Google Cloud persistent disks
- **azureDisk**: Azure disk storage

### Best Practices

- **Storage Classes**: Use storage classes for dynamic provisioning
- **Backup**: Regular backup of persistent data
- **Monitoring**: Monitor storage usage and performance
- **Security**: Encrypt sensitive data at rest

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

- **← Previous**: [Day 59 - Troubleshoot Deployment Issues in Kubernetes](./day-59.md)
- **Next →**: [Day 61 - Init Containers in Kubernetes](../week-09/day-61.md)

### Similar Challenges (Kubernetes)
- [Day 50 - Set Resource Limits in Kubernetes Cluster](../week-08/day-50.md)
- [Day 51 - Execute Rolling Updates in Kubernetes](../week-08/day-51.md)
- [Day 52 - Execute Rollback in Kubernetes Cluster](../week-08/day-52.md)

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

[← Day 59](day-59.md) | [Day 61 →](day-61.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
