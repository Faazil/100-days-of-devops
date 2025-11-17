# Day 52: Execute Rollback in Kubernetes Cluster

## Task Overview

Deploy containerized applications using Kubernetes Deployment resources. Deployments manage replica sets and provide declarative updates for pods and containers.

**Deployment Specifications:**
- Create Deployment manifest
- Define replicas and container specs
- Configure image and ports
- Apply to cluster and verify status

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Verify the resource was created and check its status.

```sh
kubectl get deployments.apps
    kubectl get pods
```

**Step 2:** Get detailed information about the resource.

```sh
kubectl describe pods pod-name
```

**Step 3:** Execute the command to complete this step.

```sh
kubectl rollout undo deployments/nginx-deployment
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 51](day-51.md) | [Day 53 →](day-53.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
