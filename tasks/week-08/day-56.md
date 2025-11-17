# Day 56: Deploy Nginx Web Server on Kubernetes Cluster

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

**Step 1:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f k3s-deployment.yml
```

**Step 2:** Verify the resource was created and check its status.

```sh
kubectl get deployment.apps
    kubectl get pods
    kubectl get svc
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 55](day-55.md) | [Day 57 →](../week-09/day-57.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
