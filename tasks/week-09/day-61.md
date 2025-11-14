# Day 61: Init Containers in Kubernetes

## Task Overview

There are some applications that need to be deployed on Kubernetes cluster and these apps have some pre-requisites where some configurations need to be changed before deploying the app container. Some of these changes cannot be made inside the images so the DevOps team has come up with a solution to use init containers to perform these tasks during deployment. Below is a sample scenario that the team is going to test first.

- Create a Deployment named as `ic-deploy-devops`.

- Configure spec as `replicas` should be `1`, labels app should be `ic-devops`, template's metadata lables app should be the same `ic-devops`.

- The initContainers should be named as `ic-msg-devops`, use image `debian` with latest tag and use command `'/bin/bash', '-c' and 'echo Init Done - Welcome to xFusionCorp Industries > /ic/media'`. The volume mount should be named as `ic-volume-devops` and mount path should be `/ic`.

- Main container should be named as `ic-main-devops`, use image debian with latest tag and use command `'/bin/bash', '-c' and 'while true; do cat /ic/media; sleep 5; done'`. The volume mount should be named as `ic-volume-devops` and mount path should be `/ic`.

- Volume to be named as `ic-volume-devops` and it should be an `emptyDir` type.

> Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

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
    kubectl get pods
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 60](day-60.md) | [Day 62 →](day-62.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
