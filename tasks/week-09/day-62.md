# Day 62: Manage Secrets in Kubernetes

## Task Overview

The Nautilus DevOps team is working to deploy some tools in Kubernetes cluster. Some of the tools are licence based so that licence information needs to be stored securely within Kubernetes cluster. Therefore, the team wants to utilize Kubernetes secrets to store those secrets. Below you can find more details about the requirements:

- We already have a secret key file `media.txt` under `/opt` location on jump host. Create a generic secret named `media`, it should contain the password/license-number present in `media.txt` file.

- Also create a pod named `secret-devops`.

- Configure pod's spec as container name should be `secret-container-devops`, image should be `debian` with latest tag (remember to mention the tag with image). Use sleep command for container so that it remains in running state. Consume the created secret and mount it under `/opt/cluster` within the container.

- To verify you can exec into the container `secret-container-devops`, to check the secret key under the mounted path `/opt/cluster`. Before hitting the Check button please make sure pod/pods are in running state, also validation can take some time to complete so keep patience.

> Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
kubectl create secret generic media --from-file=/opt/media.txt
```

**Step 2:**
```bash
kubectl describe secret media
```

**Step 3:**
```bash
kubectl apply -f k3s-pod.yaml
```

**Step 4:**
```bash
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
