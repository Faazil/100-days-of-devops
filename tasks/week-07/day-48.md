# Day 48: Deploy Pods in Kubernetes Cluster

## Task Overview

The Nautilus DevOps team is diving into Kubernetes for application management. One team member has a task to create a pod according to the details below:

- Create a pod named pod-httpd using the httpd image with the latest tag. Ensure to specify the tag as httpd:latest.

- Set the app label to httpd_app, and name the container as httpd-container.

> Note: The kubectl utility on jump_host is configured to operate with the Kubernetes cluster.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
kubectl apply -f k3s-pod.yml
```

**Step 2:**
```bash
kubectl get pods
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 47](day-47.md) | [Day 49 →](day-49.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
