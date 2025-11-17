# Day 64: Fix Python App Deployed on Kubernetes Cluster

## Task Overview

Configure resource constraints for Kubernetes pods to prevent performance degradation. Define CPU and memory limits to ensure fair resource distribution and stable cluster operations.

**Resource Configuration:**
- Pod creation with resource specifications
- Memory requests and limits (Mi units)
- CPU requests and limits (millicores)
- Prevent resource contention across workloads

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Verify the resource was created and check its status.

```sh
kubectl get pods
    kubectl describe pod pod-name
```

**Step 2:** Execute the command to complete this step.

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

**Step 3:** Verify the resource was created and check its status.

```sh
kubectl get deployments.apps python-deployment-devops -o yaml > k3s-deployment.yaml
```

**Step 4:** Execute the command to complete this step.

```sh
vi k3s-deployment.yaml
```

**Step 5:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl delete deployments.apps python-deployment-devops
    kubectl apply -f k3s-deployment.yaml
```

**Step 6:** Verify the resource was created and check its status.

```sh
kubectl get pods
```

**Step 7:** Verify the resource was created and check its status.

```sh
kubectl get svc
```

**Step 8:** Verify the resource was created and check its status.

```output
kubectl get svc
    NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
    kubernetes              ClusterIP   10.96.0.1       <none>        443/TCP          23m
    python-service-devops   NodePort    10.96.109.187   <none>        8080:32345/TCP   12m
```

**Step 9:** Verify the resource was created and check its status.

```sh
kubectl get svc python-service-devops -o yaml > k3s-service.yaml
```

**Step 10:** Execute the command to complete this step.

```sh
vi k3s-service.yaml
```

**Step 11:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f k3s.-svc.yaml
```

**Step 12:** Verify the resource was created and check its status.

```sh
kubectl get svc
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 63](../week-09/day-63.md) | [Day 65 →](day-65.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
