# Challenge 66: Deploy MySQL on Kubernetes

## 📊 Metadata
- **Day**: 66
- **Week**: 10
- **Day in Week**: 3/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

A new MySQL server needs to be deployed on Kubernetes cluster. The Nautilus DevOps team was working on to gather the requirements. Recently they were able to finalize the requirements and shared them with the team members to start working on it. Below you can find the details:

1. Create a PersistentVolume `mysql-pv`, its capacity should be `250Mi`, set other parameters as per your preference.

2. Create a PersistentVolumeClaim to request this PersistentVolume storage. Name it as `mysql-pv-claim` and request a `250Mi` of storage. Set other parameters as per your preference.

3. Create a deployment named `mysql-deployment`, use any mysql image as per your preference. Mount the PersistentVolume at mount path `/var/lib/mysql`.

4. Create a NodePort type service named `mysql` and set `nodePort` to `30007`.

5. Create a secret named `mysql-root-pass` having a key pair value, where key is password and its value is `YUIidhb667`, create another secret named `mysql-user-pass` having some key pair values, where frist key is `username` and its value is `kodekloud_sam`, second key is `password` and value is `BruCStnMT5`, create one more secret named `mysql-db-url`, key name is `database` and value is `kodekloud_db8`

6. Define some Environment variables within the container:

   - name: `MYSQL_ROOT_PASSWORD`, should pick value from secretKeyRef name: `mysql-root-pass` and key: `password`

   - name: `MYSQL_DATABASE`, should pick value from secretKeyRef name: `mysql-db-url` and key: `database`

   - name: `MYSQL_USER`, should pick value from secretKeyRef name: `mysql-user-pass` key key: `username`

   - name: `MYSQL_PASSWORD`, should pick value from secretKeyRef name: `mysql-user-pass` and key: `password`

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
- Day 63: Deploy Iron Gallery App on Kubernetes (recommended)
- Day 64: Fix Python App Deployed on Kubernetes Cluster (recommended)
- Day 65: Deploy Redis Deployment on Kubernetes (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Let's create the `k3s-mysql-deployment.yml` and copy-paste the contents from this [YAML file](../files/k3s-mysql-deployment-066.yml)

2. Create a volume directory for persistent volume:

    ```sh
    mkdir -p /home/thor/pv
    ```

3. Create the deployment

    ```sh
    kubectl apply -f k3s-mysql-deployment.yml
    ```

4. Verify Results

    ```sh
    kubectl get deployments.apps
    kubectl describe deployments.apps mysql-deployment
    kubectl get pods
    kubectl get pv
    kubectl get pvc
    kubectl get svc
    kubectl get secrets
    ```

> Passing passwords in plain text are not allowed, that's why we have used `stringData` in secret.

## Good to Know?

### MySQL on Kubernetes

- **Stateful Application**: Requires persistent storage
- **Data Persistence**: Use PVCs for database files
- **Configuration**: Environment variables for database setup
- **Security**: Secrets for passwords and credentials

### Database Security

- **Root Password**: Strong password for root user
- **User Accounts**: Create specific users for applications
- **Network Security**: Limit access with network policies
- **Encryption**: Enable encryption at rest and in transit

### Persistent Storage

- **Data Directory**: Mount PVC at `/var/lib/mysql`
- **Backup Strategy**: Regular database backups
- **Storage Class**: Choose appropriate storage type
- **Volume Expansion**: Plan for storage growth

### Production Considerations

- **High Availability**: MySQL replication or clustering
- **Monitoring**: Database performance and health metrics
- **Backup**: Automated backup and restore procedures
- **Resource Limits**: Appropriate CPU and memory allocation

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

- **← Previous**: [Day 65 - Deploy Redis Deployment on Kubernetes](./day-65.md)
- **Next →**: [Day 67 - Deploy Guest Book App on Kubernetes](../week-10/day-67.md)

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

