# Challenge 62: Manage Secrets in Kubernetes

## 📊 Metadata
- **Day**: 62
- **Week**: 9
- **Day in Week**: 6/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team is working to deploy some tools in Kubernetes cluster. Some of the tools are licence based so that licence information needs to be stored securely within Kubernetes cluster. Therefore, the team wants to utilize Kubernetes secrets to store those secrets. Below you can find more details about the requirements:

- We already have a secret key file `media.txt` under `/opt` location on jump host. Create a generic secret named `media`, it should contain the password/license-number present in `media.txt` file.

- Also create a pod named `secret-devops`.

- Configure pod's spec as container name should be `secret-container-devops`, image should be `debian` with latest tag (remember to mention the tag with image). Use sleep command for container so that it remains in running state. Consume the created secret and mount it under `/opt/cluster` within the container.

- To verify you can exec into the container `secret-container-devops`, to check the secret key under the mounted path `/opt/cluster`. Before hitting the Check button please make sure pod/pods are in running state, also validation can take some time to complete so keep patience.

> Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.


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
- Day 58: Deploy Grafana on Kubernetes Cluster (recommended)
- Day 59: Troubleshoot Deployment Issues in Kubernetes (recommended)
- Day 60: Persistent Volumes in Kubernetes (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. To create a generic secret from file:

    ```sh
    kubectl create secret generic media --from-file=/opt/media.txt
    ```

    > To check:

    ```sh
    kubectl describe secret media
    ```

2. Create the `k3s-pod.yaml` file, copy-paste contents from this [YAML file](../files/k3s-pod-062.yaml)

3. Run the pod

    ```sh
    kubectl apply -f k3s-pod.yaml
    ```

4. Verify results

    ```sh
    kubectl get secret
    kubectl get pod
    kubectl exec -it secret-devops -c secret-container-devops -- cat /opt/cluster
    ```

    > You can see secret data, running pods and execute the command to verify the secret is placed inside the container

## Good to Know?

### Kubernetes Secrets

- **Purpose**: Store sensitive information (passwords, tokens, keys)
- **Base64 Encoding**: Data is base64 encoded (not encrypted)
- **Namespace Scoped**: Secrets belong to specific namespace
- **Volume Mounts**: Mount secrets as files in containers

### Secret Types

- **generic**: Arbitrary user-defined data
- **docker-registry**: Docker registry credentials
- **tls**: TLS certificates and keys
- **service-account-token**: Service account tokens

### Secret Usage

- **Environment Variables**: Inject as env vars
- **Volume Mounts**: Mount as files in filesystem
- **Image Pull Secrets**: Authenticate to private registries
- **Service Account**: Automatic token injection

### Security Best Practices

- **RBAC**: Control access to secrets
- **Encryption at Rest**: Enable etcd encryption
- **Rotation**: Regularly rotate secrets
- **Least Privilege**: Grant minimal required access
- **External Systems**: Consider external secret management

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

- **← Previous**: [Day 61 - Init Containers in Kubernetes](./day-61.md)
- **Next →**: [Day 63 - Deploy Iron Gallery App on Kubernetes](../week-09/day-63.md)

### Similar Challenges (Kubernetes)
- [Day 52 - Execute Rollback in Kubernetes Cluster](../week-08/day-52.md)
- [Day 53 - Resolve VolumeMounts Issue in Kubernetes](../week-08/day-53.md)
- [Day 54 - Kubernetes Shared Volumes](../week-08/day-54.md)

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

