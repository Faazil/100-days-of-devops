# Day 49: Deploy Applications with Kubernetes Deployments

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

**Step 1:** Perform the initial setup or connection.

```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  labels:
    app: nginx

spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 1
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:latest
          ports:
          - containerPort: 80
```

**Step 2:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f k3s-deployment.yml
```

**Step 3:** Verify the resource was created and check its status.

```sh
kubectl get deployments.apps
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 48](day-48.md) | [Day 50 →](../week-08/day-50.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
