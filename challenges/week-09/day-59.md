# Challenge 59: Troubleshoot Deployment Issues in Kubernetes

## 📊 Metadata
- **Day**: 59
- **Week**: 9
- **Day in Week**: 3/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

Last week, the Nautilus DevOps team deployed a redis app on Kubernetes cluster, which was working fine so far. This morning one of the team members was making some changes in this existing setup, but he made some mistakes and the app went down. Next, fix this as soon as possible. Please take a look.

- The deployment name is `redis-deployment`. The pods are not in running state right now, so please look into the issue and fix the same.

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
- Day 53: Resolve VolumeMounts Issue in Kubernetes (recommended)
- Day 54: Kubernetes Shared Volumes (recommended)
- Day 58: Deploy Grafana on Kubernetes Cluster (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Review the pod in details

    ```sh
    kubectl describe pod redis-deployment-pod-name
    ```

    ```shell
    thor@jumphost ~$ kubectl describe pod redis-deployment-6fd9d5fcb-k9n65
    Name:             redis-deployment-6fd9d5fcb-k9n65
    Namespace:        default
    Priority:         0
    Service Account:  default
    Node:             kodekloud-control-plane/172.17.0.2
    Start Time:       Mon, 22 Sep 2025 16:42:08 +0000
    Labels:           app=redis
                    pod-template-hash=6fd9d5fcb
    Annotations:      <none>
    Status:           Pending
    IP:               
    IPs:              <none>
    Controlled By:    ReplicaSet/redis-deployment-6fd9d5fcb
    Containers:
    redis-container:
        Container ID:   
        Image:          redis:alpin
        Image ID:       
        Port:           6379/TCP
        Host Port:      0/TCP
        State:          Waiting
        Reason:       ContainerCreating
        Ready:          False
        Restart Count:  0
        Requests:
        cpu:        300m
        Environment:  <none>
        Mounts:
        /redis-master from config (rw)
        /redis-master-data from data (rw)
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-z6ndg (ro)
    Conditions:
    Type              Status
    Initialized       True 
    Ready             False 
    ContainersReady   False 
    PodScheduled      True 
    Volumes:
    data:
        Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
        Medium:     
        SizeLimit:  <unset>
    config:
        Type:      ConfigMap (a volume populated by a ConfigMap)
        Name:      redis-cofig
        Optional:  false
    kube-api-access-z6ndg:
        Type:                    Projected (a volume that contains injected data from multiple sources)
        TokenExpirationSeconds:  3607
        ConfigMapName:           kube-root-ca.crt
        ConfigMapOptional:       <nil>
        DownwardAPI:             true
    QoS Class:                   Burstable
    Node-Selectors:              <none>
    Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                                node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
    Events:
    Type     Reason       Age                 From               Message
    ----     ------       ----                ----               -------
    Normal   Scheduled    3m7s                default-scheduler  Successfully assigned default/redis-deployment-6fd9d5fcb-k9n65 to kodekloud-control-plane
    Warning  FailedMount  64s                 kubelet            Unable to attach or mount volumes: unmounted volumes=[config], unattached volumes=[], failed to process volumes=[]: timed out waiting for the condition
    Warning  FailedMount  59s (x9 over 3m7s)  kubelet            MountVolume.SetUp failed for volume "config" : configmap "redis-cofig" not found
    ```

    > It seems the pod is looking for a config-map that's not available or soemthing wrong

2. Let's see the list of configmaps

    ```sh
    kubectl get cm
    ```

    ```shell
    thor@jumphost ~$ kubectl get cm
    NAME               DATA   AGE
    kube-root-ca.crt   1      27m
    redis-config       2      8m16s
    ```

3. If you notice carefully, there is mismatch between name. The actual config-map name is: `redis-config` but pod is lokking for `redis-cofig`

4. Let's extract the deployment into a YAML file and fix it there

    ```sh
    kubectl get deployment.apps redis-deployment -o yaml > redis-deployment.yaml
    ```

5. Let's fix the deployment file `cofig` to `config` in volumes
6. Let's run the deployment

    ```sh
    kubectl apply -f redis-deployment.yaml
    ```

7. Check pod status

    ```sh
    kubectl get pods
    ```

    > new error:

    ```shell
    thor@jumphost ~$ kubectl get pods
    NAME                                READY   STATUS              RESTARTS   AGE
    redis-deployment-5bcd4c7d64-rmcxj   0/1     ImagePullBackOff    0          4m9s
    ```

8. Let's fix the image tag `alpin` to `alpine`
9. Recreate the deployment

    ```sh
    kubectl delete deployments.apps redis-deployment
    kubectl apply -f redis-deployment
    ```

10. Verify the results

    ```kubectl get pods
    ```

## Good to Know?

### Kubernetes Troubleshooting

- **Pod States**: Pending, Running, Succeeded, Failed, Unknown
- **Container States**: Waiting, Running, Terminated
- **Events**: Kubernetes events show what happened
- **Logs**: Container logs provide application-level info

### Common Issues

- **Image Pull Errors**: Wrong image name or registry access
- **Resource Constraints**: Insufficient CPU/memory
- **ConfigMap/Secret Missing**: Referenced resources don't exist
- **Volume Mount Issues**: Incorrect paths or permissions

### Debugging Commands

- **Describe**: `kubectl describe pod/deployment/service`
- **Logs**: `kubectl logs pod-name -c container-name`
- **Events**: `kubectl get events --sort-by=.metadata.creationTimestamp`
- **Exec**: `kubectl exec -it pod-name -- /bin/sh`

### Systematic Approach

- **Check Pod Status**: `kubectl get pods`
- **Examine Events**: `kubectl describe pod`
- **Review Logs**: `kubectl logs`
- **Validate Config**: Check YAML syntax and references
- **Test Connectivity**: Network and service discovery

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

- **← Previous**: [Day 58 - Deploy Grafana on Kubernetes Cluster](./day-58.md)
- **Next →**: [Day 60 - Persistent Volumes in Kubernetes](../week-09/day-60.md)

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
**Difficulty**: ⭐
**Category**: DevOps

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
```

