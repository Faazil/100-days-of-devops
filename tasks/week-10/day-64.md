# Day 64: Fix Python App Deployed on Kubernetes Cluster

## Task Overview

One of the DevOps engineers was trying to deploy a python app on Kubernetes cluster. Unfortunately, due to some mis-configuration, the application is not coming up. Please take a look into it and fix the issues. Application should be accessible on the specified nodePort.

- The deployment name is `python-deployment-devops`, its using `poroko/flask-demo-appimage`. The deployment and service of this app is already deployed.
- nodePort should be `32345` and `targetPort` should be python flask app's default port.

> Note: The kubectl on jump_host has been configured to work with the kubernetes cluster.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
kubectl get pods
    kubectl describe pod pod-name
```

**Step 2:**
```bash
> `docker.io/poroko/flask-app-demo:latest` the dpeloyment using wrong docker image

2. Let's create a `k3s-deployment.yaml` file from existing deployment
```

**Step 3:**
```bash
3. Let's fix the docker image
```

**Step 4:**
```bash
> replace docker image in container section with accurate image

4. Recreate the deployment
```

**Step 5:**
```bash
> wait for 1-2 minutes and check status
```

**Step 6:**
```bash
> try to access app, but its not working.

5. Now let's check the service state
```

**Step 8:**
```bash
> So service is already running but it's mapped with wrong target port. let's fix that

6. Fixing service
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 63](../week-09/day-63.md) | [Day 65 →](day-65.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
