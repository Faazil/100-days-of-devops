# Day 66: Deploy MySQL on Kubernetes

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

**Step 1:** Create the required directory.

```sh
mkdir -p /home/thor/pv
```

**Step 2:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f k3s-mysql-deployment.yml
```

**Step 3:** Verify the resource was created and check its status.

```sh
kubectl get deployments.apps
    kubectl describe deployments.apps mysql-deployment
    kubectl get pods
    kubectl get pv
    kubectl get pvc
    kubectl get svc
    kubectl get secrets
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 65](day-65.md) | [Day 67 →](day-67.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
