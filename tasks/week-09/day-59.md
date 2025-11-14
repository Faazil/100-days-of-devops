# Day 59: Troubleshoot Deployment Issues in Kubernetes

## Task Overview

Last week, the Nautilus DevOps team deployed a redis app on Kubernetes cluster, which was working fine so far. This morning one of the team members was making some changes in this existing setup, but he made some mistakes and the app went down. Next, fix this as soon as possible. Please take a look.

- The deployment name is `redis-deployment`. The pods are not in running state right now, so please look into the issue and fix the same.

> Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
kubectl describe pod redis-deployment-pod-name
```

**Step 2:**
```bash
thor@jumphost ~$ kubectl describe pod redis-deployment-6fd9d5fcb-k9n65
    Name:             redis-deployment-6fd9d5fcb-k9n65
    Namespace:        default
    Priority:         0
    Service Account:  default
    Node:             kodekloud-control-plane/172.17.0.2
    Start Time:       Mon, 22 Sep 2025 16:42:08 +0000
    Labels:           app=redis
                    pod-template-hash=6fd9d5fcb
    Annotations:      <none>
    Status:           Pending
    IP:               
    IPs:              <none>
    Controlled By:    ReplicaSet/redis-deployment-6fd9d5fcb
    Containers:
    redis-container:
        Container ID:   
        Image:          redis:alpin
        Image ID:       
        Port:           6379/TCP
        Host Port:      0/TCP
        State:          Waiting
        Reason:       ContainerCreating
        Ready:          False
        Restart Count:  0
        Requests:
        cpu:        300m
        Environment:  <none>
        Mounts:
        /redis-master from config (rw)
        /redis-master-data from data (rw)
        /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-z6ndg (ro)
    Conditions:
    Type              Status
    Initialized       True 
    Ready             False 
    ContainersReady   False 
    PodScheduled      True 
    Volumes:
    data:
        Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
        Medium:     
        SizeLimit:  <unset>
    config:
        Type:      ConfigMap (a volume populated by a ConfigMap)
        Name:      redis-cofig
        Optional:  false
    kube-api-access-z6ndg:
        Type:                    Projected (a volume that contains injected data from multiple sources)
        TokenExpirationSeconds:  3607
        ConfigMapName:           kube-root-ca.crt
        ConfigMapOptional:       <nil>
        DownwardAPI:             true
    QoS Class:                   Burstable
    Node-Selectors:              <none>
    Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                                node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
    Events:
    Type     Reason       Age                 From               Message
    ----     ------       ----                ----               -------
    Normal   Scheduled    3m7s                default-scheduler  Successfully assigned default/redis-deployment-6fd9d5fcb-k9n65 to kodekloud-control-plane
    Warning  FailedMount  64s                 kubelet            Unable to attach or mount volumes: unmounted volumes=[config], unattached volumes=[], failed to process volumes=[]: timed out waiting for the condition
    Warning  FailedMount  59s (x9 over 3m7s)  kubelet            MountVolume.SetUp failed for volume "config" : configmap "redis-cofig" not found
```

**Step 3:**
```bash
kubectl get cm
```

**Step 4:**
```bash
thor@jumphost ~$ kubectl get cm
    NAME               DATA   AGE
    kube-root-ca.crt   1      27m
    redis-config       2      8m16s
```

**Step 5:**
```bash
kubectl get deployment.apps redis-deployment -o yaml > redis-deployment.yaml
```

**Step 6:**
```bash
kubectl apply -f redis-deployment.yaml
```

**Step 7:**
```bash
kubectl get pods
```

**Step 8:**
```bash
thor@jumphost ~$ kubectl get pods
    NAME                                READY   STATUS              RESTARTS   AGE
    redis-deployment-5bcd4c7d64-rmcxj   0/1     ImagePullBackOff    0          4m9s
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 58](day-58.md) | [Day 60 →](day-60.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
