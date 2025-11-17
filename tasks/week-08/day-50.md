# Day 50: Set Resource Limits in Kubernetes Cluster

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
apiVersion: v1
kind: Pod
metadata:
    name: httpd-pod
    labels:
        app: httpd_pod
spec:
    containers:
        - name: httpd-container
          image: httpd:latest
          ports:
            - containerPort: 80
          resources:
            limits:
                cpu: 100m
                memory: 20Mi
            requests:
                cpu: 100m
                memory: 15Mi
```

**Step 2:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f pod.yml
```

**Step 3:** Verify the resource was created and check its status.

```sh
kubectl get pods
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 49](../week-07/day-49.md) | [Day 51 →](day-51.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
