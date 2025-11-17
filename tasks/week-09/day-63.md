# Day 63: Deploy Iron Gallery App on Kubernetes

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
kubectl create ns iron-namespace-xfusion
    kubectl get ns
```

**Step 2:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f k3s-iron-gallery.yaml
```

**Step 3:** Verify the resource was created and check its status.

```sh
kubectl get ns
    kubectl get deployments.apps -n iron-namespace-xfusion
    kubectl get pods -n iron-namespace-xfusion
    kubectl get svc -n iron-namespace-xfusion
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 62](day-62.md) | [Day 64 →](../week-10/day-64.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
