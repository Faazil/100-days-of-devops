# Challenge 64: Fix Python App Deployed on Kubernetes Cluster

## 📊 Metadata
- **Day**: 64
- **Week**: 10
- **Day in Week**: 1/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

One of the DevOps engineers was trying to deploy a python app on Kubernetes cluster. Unfortunately, due to some mis-configuration, the application is not coming up. Please take a look into it and fix the issues. Application should be accessible on the specified nodePort.

- The deployment name is `python-deployment-devops`, its using `poroko/flask-demo-appimage`. The deployment and service of this app is already deployed.
- nodePort should be `32345` and `targetPort` should be python flask app's default port.

> Note: The kubectl on jump_host has been configured to work with the kubernetes cluster.


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
- Day 60: Persistent Volumes in Kubernetes (recommended)
- Day 62: Manage Secrets in Kubernetes (recommended)
- Day 63: Deploy Iron Gallery App on Kubernetes (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Let's see the pod status

    ```sh
    kubectl get pods
    kubectl describe pod pod-name
    ```

    > In my case the eorror is look like this:

    ```output
    Events:
    Type     Reason     Age                    From               Message
    ----     ------     ----                   ----               -------
    Normal   Scheduled  37m                    default-scheduler  Successfully assigned default/python-deployment-devops-678b746b7-f25jg to kodekloud-control-plane
    Normal   Pulling    36m (x4 over 37m)      kubelet            Pulling image "poroko/flask-app-demo"
    Warning  Failed     36m (x4 over 37m)      kubelet            Failed to pull image "poroko/flask-app-demo": rpc error: code = Unknown desc = failed to pull and unpack image "docker.io/poroko/flask-app-demo:latest": failed to resolve reference "docker.io/poroko/flask-app-demo:latest": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
    Warning  Failed     36m (x4 over 37m)      kubelet            Error: ErrImagePull
    Warning  Failed     36m (x6 over 37m)      kubelet            Error: ImagePullBackOff
    Normal   BackOff    2m45s (x152 over 37m)  kubelet            Back-off pulling
    ```

    > `docker.io/poroko/flask-app-demo:latest` the dpeloyment using wrong docker image

2. Let's create a `k3s-deployment.yaml` file from existing deployment

    ```sh
    kubectl get deployments.apps python-deployment-devops -o yaml > k3s-deployment.yaml
    ```

3. Let's fix the docker image

    ```sh
    vi k3s-deployment.yaml
    ```

    > replace docker image in container section with accurate image

4. Recreate the deployment

    ```sh
    kubectl delete deployments.apps python-deployment-devops
    kubectl apply -f k3s-deployment.yaml
    ```

    > wait for 1-2 minutes and check status

    ```sh
    kubectl get pods
    ```

    > try to access app, but its not working.

5. Now let's check the service state

    ```sh
    kubectl get svc
    ```

    ```output
     kubectl get svc
    NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
    kubernetes              ClusterIP   10.96.0.1       <none>        443/TCP          23m
    python-service-devops   NodePort    10.96.109.187   <none>        8080:32345/TCP   12m
    ```

    > So service is already running but it's mapped with wrong target port. let's fix that

6. Fixing service

    ```sh
    kubectl get svc python-service-devops -o yaml > k3s-service.yaml
    ```

    > let's change the target port in `k3s-service.yaml` file

    ```sh
    vi k3s-service.yaml
    ```

    > configure service

    ```sh
    kubectl apply -f k3s.-svc.yaml
    ```

7. Verify results

    ```sh
    kubectl get svc
    ```

## Good to Know?

### Application Debugging

- **Image Issues**: Verify correct image names and tags
- **Service Configuration**: Check port mappings and selectors
- **Network Connectivity**: Test service-to-service communication
- **Resource Constraints**: Ensure adequate resources

### Common Misconfigurations

- **Wrong Image**: Typos in image names or tags
- **Port Mismatch**: Service targetPort doesn't match container port
- **Label Mismatch**: Service selector doesn't match pod labels
- **Resource Limits**: Insufficient CPU/memory allocation

### Debugging Workflow

- **Check Pod Status**: Verify pods are running
- **Examine Events**: Look for error messages
- **Validate Configuration**: Review YAML specifications
- **Test Connectivity**: Use port-forward or exec
- **Check Logs**: Application and system logs

### Service Troubleshooting

- **Endpoints**: `kubectl get endpoints` shows service targets
- **Port Forward**: `kubectl port-forward` for direct access
- **Service Discovery**: Test DNS resolution within cluster
- **Network Policies**: Check if network policies block traffic

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

- **← Previous**: [Day 63 - Deploy Iron Gallery App on Kubernetes](./day-63.md)
- **Next →**: [Day 65 - Deploy Redis Deployment on Kubernetes](../week-10/day-65.md)

### Similar Challenges (Kubernetes)
- [Day 54 - Kubernetes Shared Volumes](../week-08/day-54.md)
- [Day 58 - Deploy Grafana on Kubernetes Cluster](../week-09/day-58.md)
- [Day 59 - Troubleshoot Deployment Issues in Kubernetes](../week-09/day-59.md)

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

