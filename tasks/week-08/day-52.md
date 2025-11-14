# Day 52: Execute Rollback in Kubernetes Cluster

## Task Overview

Earlier today, the Nautilus DevOps team deployed a new release for an application. However, a customer has reported a bug related to this recent release. Consequently, the team aims to revert to the previous version.

- There exists a deployment named nginx-deployment; initiate a rollback to the previous revision.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
kubectl get deployments.apps
    kubectl get pods
```

**Step 2:**
```bash
kubectl describe pods pod-name
```

**Step 3:**
```bash
kubectl rollout undo deployments/nginx-deployment
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 51](day-51.md) | [Day 53 →](day-53.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
