# Day 67: Deploy Guest Book App on Kubernetes

## Task Overview

Nautilus dev team members has finished development of one of the applications and it is ready for deployment. It is a guestbook application that will be used to manage entries for guests/visitors. As per discussion with the DevOps team, they have finalized the infrastructure that will be deployed on Kubernetes cluster. Below you can find more details about it.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
kubectl apply -f k3s-redis-master.yaml
```

**Step 2:**
```bash
kubectl apply -f k3s-redis-slave.yaml
```

**Step 3:**
```bash
kubectl apply -f k3s-php-redis.yaml
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 66](day-66.md) | [Day 68 →](day-68.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
