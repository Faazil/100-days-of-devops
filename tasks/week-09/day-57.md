# Day 57: Print Environment Variables

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

**Step 1:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f k3s-pod.yml
```

**Step 2:** Execute the command to complete this step.

```sh
kubectl logs -f print-env-greeting
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 56](../week-08/day-56.md) | [Day 58 →](day-58.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
