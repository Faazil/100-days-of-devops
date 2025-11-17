# Day 54: Kubernetes Shared Volumes

## Task Overview

Launch pods in a Kubernetes cluster to run containerized workloads. Pods are the smallest deployable units that encapsulate one or more containers.

**Pod Configuration:**
- Define pod specifications
- Configure container images
- Set labels and metadata
- Deploy and verify pod status

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f k3s-pod.yml
```

**Step 2:** Execute the command to complete this step.

```sh
kubectl exec -it volume-share-nautilus -c volume-container-nautilus-1 /bin/sh
```

**Step 3:** Execute the command to complete this step.

```sh
touch /tmp/news/news.txt
```

**Step 4:** Execute the command to complete this step.

```sh
kubectl exec -it volume-share-nautilus -c volume-container-nautilus-2 /bin/sh
```

**Step 5:** Execute the command to complete this step.

```sh
ls /tmp/demo
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 53](day-53.md) | [Day 55 →](day-55.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
