# Day 62: Manage Secrets in Kubernetes

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

**Step 1:** Create the Kubernetes resource.

```sh
kubectl create secret generic media --from-file=/opt/media.txt
```

**Step 2:** Get detailed information about the resource.

```sh
kubectl describe secret media
```

**Step 3:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f k3s-pod.yaml
```

**Step 4:** Verify the resource was created and check its status.

```sh
kubectl get secret
    kubectl get pod
    kubectl exec -it secret-devops -c secret-container-devops -- cat /opt/cluster
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 61](day-61.md) | [Day 63 →](day-63.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
