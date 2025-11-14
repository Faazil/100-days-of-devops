# Day 58: Deploy Grafana on Kubernetes Cluster

## Task Overview

The Nautilus DevOps teams is planning to set up a Grafana tool to collect and analyze analytics from some applications. They are planning to deploy it on Kubernetes cluster. Below you can find more details.

1. Create a deployment named `grafana-deployment-datacenter` using any grafana image for Grafana app. Set other parameters as per your choice.

2. Create NodePort type service with nodePort `32000` to expose the app.

> You need not to make any configuration changes inside the Grafana app once deployed, just make sure you are able to access the Grafana login page.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
kubectl apply -f k3s-deployment.yaml
```

**Step 2:**
```bash
kubectl get deployments.apps
    kubectl get svc
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 57](day-57.md) | [Day 59 →](day-59.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
