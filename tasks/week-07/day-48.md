# Day 48: Deploy Pods in Kubernetes Cluster

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
kubectl apply -f k3s-pod.yml
```

**Step 2:** Verify the resource was created and check its status.

```sh
kubectl get pods
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 47](day-47.md) | [Day 49 →](day-49.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
