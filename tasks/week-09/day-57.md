# Day 57: Print Environment Variables

## Task Overview

The Nautilus DevOps team is working on to setup some pre-requisites for an application that will send the greetings to different users. There is a sample deployment, that needs to be tested. Below is a scenario which needs to be configured on Kubernetes cluster. Please find below more details about it.

- Create a pod named `print-envars-greeting`.

- Configure spec as, the container name should be print-env-container and use bash image.

- Create three environment variables:

  - GREETING and its value should be Welcome to

  - COMPANY and its value should be xFusionCorp

  - GROUP and its value should be Group

- Use command ["/bin/sh", "-c", 'echo "$(GREETING) $(COMPANY) $(GROUP)"'] (please use this exact command), also set its restartPolicy policy to Never to avoid crash loop back.

- You may check the output using kubectl logs -f print-envars-greeting command.

> Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
kubectl apply -f k3s-pod.yml
```

**Step 2:**
```bash
kubectl logs -f print-env-greeting
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 56](../week-08/day-56.md) | [Day 58 →](day-58.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
