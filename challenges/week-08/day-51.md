# Challenge 51: Execute Rolling Updates in Kubernetes

## 📊 Metadata
- **Day**: 51
- **Week**: 8
- **Day in Week**: 2/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

An application currently running on the Kubernetes cluster employs the nginx web server. The Nautilus application development team has introduced some recent changes that need deployment. They've crafted an image nginx:1.18 with the latest updates.

- Execute a rolling update for this application, integrating the nginx:1.18 image. The deployment is named nginx-deployment.

- Ensure all pods are operational post-update.

> Note: The kubectl utility on jump_host is set up to operate with the Kubernetes cluster


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
- Day 48: Deploy Pods in Kubernetes Cluster (recommended)
- Day 49: Deploy Applications with Kubernetes Deployments (recommended)
- Day 50: Set Resource Limits in Kubernetes Cluster (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Let's get the deployments, and pods

    ```sh
    kubectl get deployments.apps
    NAME               READY   UP-TO-DATE   AVAILABLE   AGE
    nginx-deployment   3/3     3            3           4m33s
    ```

    ```sh
    kubectl get pods
    NAME                               READY   STATUS    RESTARTS   AGE
    nginx-deployment-989f57c54-mnznk   1/1     Running   0          4m52s
    nginx-deployment-989f57c54-sqf5h   1/1     Running   0          4m52s
    nginx-deployment-989f57c54-vgjd8   1/1     Running   0          4m52s
    ```

2. Let's find details of the deployments for any pod

    ```sh
    kubectl describe pods nginx-deployment-989f57c54-mnznk
    ```

    ```shell
    Name:             nginx-deployment-989f57c54-mnznk
    Namespace:        default
    Priority:         0
    Service Account:  default
    Node:             kodekloud-control-plane/172.17.0.2
    Start Time:       Mon, 15 Sep 2025 10:38:31 +0000
    Labels:           app=nginx-app
                    pod-template-hash=989f57c54
    Annotations:      <none>
    Status:           Running
    IP:               10.244.0.6
    IPs:
    IP:           10.244.0.6
    Controlled By:  ReplicaSet/nginx-deployment-989f57c54
    Containers:
    nginx-container:
        Container ID:   containerd://5928ff11805390e2ac2b10bbaee9a5dcb540d6c534d162ca49c975c270280d11
        Image:          nginx:1.16
        Image ID:       docker.io/library/nginx@sha256:d20aa6d1cae56fd17cd458f4807e0de462caf2336f0b70b5eeb69fcaaf30dd9c
        Port:           <none>
        Host Port:      <none>
        State:          Running
        Started:      Mon, 15 Sep 2025 10:38:38 +0000
        Ready:          True
        Restart Count:  0
        Environment:    <none>
        Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-v2jf9 (ro)
    Conditions:
    Type              Status
    Initialized       True 
    Ready             True 
    ContainersReady   True 
    PodScheduled      True 
    Volumes:
    kube-api-access-v2jf9:
        Type:                    Projected (a volume that contains injected data from multiple sources)
        TokenExpirationSeconds:  3607
        ConfigMapName:           kube-root-ca.crt
        ConfigMapOptional:       <nil>
        DownwardAPI:             true
    QoS Class:                   BestEffort
    Node-Selectors:              <none>
    Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                                node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
    Events:
    Type    Reason     Age    From               Message
    ----    ------     ----   ----               -------
    Normal  Scheduled  10m    default-scheduler  Successfully assigned default/nginx-deployment-989f57c54-mnznk to kodekloud-control-plane
    Normal  Pulling    10m    kubelet            Pulling image "nginx:1.16"
    Normal  Pulled     9m57s  kubelet            Successfully pulled image "nginx:1.16" in 5.385304195s (5.385392439s including waiting)
    Normal  Created    9m57s  kubelet            Created container nginx-container
    Normal  Started    9m57s  kubelet            Started container nginx-container
    ```

    > We can see the current image version: 1.16

3. Let's update image version:

    ```sh
    kubectl set image deployments/nginx-deployment nginx-container=nginx:1.18
    ```

    > We have to use `set image` command with **deployment name** and **container name**

4. Let's verify the rollout status

    ```sh
    kubectl rollout status deployments/nginx-deployment
    ```

## Good to Know?

### Rolling Updates

- **Zero Downtime**: Update applications without service interruption
- **Gradual Replacement**: Replace pods incrementally
- **Health Checks**: Ensure new pods are ready before proceeding
- **Automatic Rollback**: Rollback on failure detection

### Update Strategies

- **RollingUpdate**: Default strategy, gradual replacement
- **Recreate**: Terminate all pods before creating new ones
- **MaxUnavailable**: Maximum pods that can be unavailable
- **MaxSurge**: Maximum pods that can be created above desired

### Rollout Commands

- **Set Image**: `kubectl set image deployment/name container=image:tag`
- **Status**: `kubectl rollout status deployment/name`
- **History**: `kubectl rollout history deployment/name`
- **Undo**: `kubectl rollout undo deployment/name`

### Best Practices

- **Health Probes**: Configure readiness and liveness probes
- **Resource Limits**: Ensure adequate resources for updates
- **Testing**: Test updates in staging environment
- **Monitoring**: Monitor application during rollout

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

- **← Previous**: [Day 50 - Set Resource Limits in Kubernetes Cluster](./day-50.md)
- **Next →**: [Day 52 - Execute Rollback in Kubernetes Cluster](../week-08/day-52.md)

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
**Difficulty**: {get_difficulty_emoji(day)}
**Category**: {task_info['category']}

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
python3 ../../tools/progress.py --complete {day}
```

