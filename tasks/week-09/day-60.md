# Day 60: Persistent Volumes in Kubernetes

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
    kind: PersistentVolume
    metadata:
    name: pv-xfusion
    spec:
    capacity:
        storage: 3Gi
    accessModes:
        - ReadWriteOnce
    storageClassName: manual
    hostPath:
        path: /mnt/security
```

**Step 2:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f k3s-pv.yaml
```

**Step 3:** Execute the command to complete this step.

```YAML
apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
    name: pvc-xfusion
    spec:
    accessModes:
        - ReadWriteOnce
    resources:
        requests:
        storage: 3Gi
    storageClassName: manual
```

**Step 4:** Execute the command to complete this step.

```sh
kubectl k3s-pvc.yaml
```

**Step 5:** Execute the command to complete this step.

```YAML
apiVersion: v1
    kind: Pod
    metadata:
    name: pod-xfusion
    labels:
        app: xfusion
    spec:
    containers:
        - name: container-xfusion
        image: httpd:latest
        volumeMounts:
            - name: xfusion-volume
            mountPath: /mnt/security
        resources:
            limits:
            memory: "128Mi"
            cpu: "500m"
            requests:
            memory: "64Mi"
            cpu: "250m"
    volumes:
        - name: xfusion-volume
        persistentVolumeClaim:
            claimName: pvc-xfusion
```

**Step 6:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f k3s-pod.yaml
```

**Step 7:** Execute the command to complete this step.

```YAML
apiVersion: v1
    kind: Service
    metadata:
    name: web-xfusion
    labels:
        app: xfusion
    spec:
    type: NodePort
    ports:
        - port: 80
        targetPort: 80
        nodePort: 30008
    selector:
        app: xfusion
```

**Step 8:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl apply -f k3s-svc.yaml
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 59](day-59.md) | [Day 61 →](day-61.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
