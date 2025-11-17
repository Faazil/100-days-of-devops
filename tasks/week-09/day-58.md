# Day 58: Deploy Grafana on Kubernetes Cluster

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

**Step 1:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f k3s-deployment.yaml
```

**Step 2:** Verify the resource was created and check its status.

```sh
kubectl get deployments.apps
    kubectl get svc
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 57](day-57.md) | [Day 59 →](day-59.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
