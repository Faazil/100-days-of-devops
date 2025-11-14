# Day 56: Deploy Nginx Web Server on Kubernetes Cluster

## Task Overview

Some of the Nautilus team developers are developing a static website and they want to deploy it on Kubernetes cluster. They want it to be highly available and scalable. Therefore, based on the requirements, the DevOps team has decided to create a deployment for it with multiple replicas. Below you can find more details about it:

- Create a deployment using nginx image with latest tag only and remember to mention the tag i.e nginx:latest. Name it as nginx-deployment. The container should be named as nginx-container, also make sure replica counts are 3.

- Create a NodePort type service named nginx-service. The nodePort should be 30011.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
kubectl apply -f k3s-deployment.yml
```

**Step 2:**
```bash
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
