# ☸️ Kubernetes Manifests

Production-ready Kubernetes configurations for deploying and managing containerized applications.

## 📁 Available Files

### Pods
- `k3s-pod.yml` - Basic pod configuration
- `k3s-pod-057.yaml` - Pod with resource limits
- `k3s-pod-060.yaml` - Multi-container pod
- `k3s-pod-062.yaml` - Pod with volume mounts

### Deployments
- `k3s-deployment-49d.yml` - Basic deployment
- `k3s-deployment-056.yaml` - Deployment with replicas
- `k3s-deployment-ic-061.yaml` - Init container deployment
- `k3s-grafana-deployment-058.yaml` - Grafana monitoring
- `k3s-mysql-deployment-066.yml` - MySQL database
- `k3s-redis-deployment-065.yml` - Redis cache
- `k3s-redis-master-deployment-067.yaml` - Redis master
- `k3s-redis-slave-deployment-067.yaml` - Redis slave
- `k3s-php-redis-deployment-067.yaml` - PHP with Redis
- `k3s-iron-gallery-deployment-63.yaml` - Application deployment

### Advanced Patterns
- `k3s-replicaset.yml` - ReplicaSet configuration
- `k3s-sidecar-containers-055.yaml` - Sidecar pattern
- `k3s-shared-volume.yml` - Shared volumes between containers

---

## 🚀 Quick Start

### Deploy a Pod

```bash
# Create a pod
kubectl apply -f k3s-pod.yml

# Check status
kubectl get pods

# View logs
kubectl logs <pod-name>

# Delete pod
kubectl delete -f k3s-pod.yml
```

### Deploy an Application

```bash
# Create deployment
kubectl apply -f k3s-deployment-056.yaml

# Check deployment
kubectl get deployments
kubectl get pods

# Scale deployment
kubectl scale deployment <deployment-name> --replicas=5

# Update deployment
kubectl set image deployment/<deployment-name> container=new-image:tag
```

---

## 📚 Learning Points

### Pod Basics

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: web
spec:
  containers:
  - name: nginx
    image: nginx:1.21
    ports:
    - containerPort: 80
```

### Deployment Patterns

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: nginx:1.21
        resources:
          limits:
            memory: "128Mi"
            cpu: "500m"
```

### Common Patterns

1. **Sidecar Container**: Helper container alongside main app
2. **Init Container**: Runs before main container starts
3. **Multi-Container Pod**: Multiple containers in one pod
4. **Shared Volumes**: Share data between containers

---

## 🔒 Best Practices

- ✅ Set resource limits and requests
- ✅ Use namespaces for organization
- ✅ Implement health checks (liveness/readiness)
- ✅ Use ConfigMaps for configuration
- ✅ Use Secrets for sensitive data
- ✅ Label everything consistently
- ✅ Use rolling updates
- ✅ Implement pod disruption budgets

---

## 📖 Related Challenges

- **Day 48-67**: Kubernetes challenges (Weeks 8-10)
- Topics: Pods, Deployments, Services, Volumes, Troubleshooting

---

## 🔗 Additional Resources

- [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [K3s Documentation](https://docs.k3s.io/)

---

[← Back to Resources](../README.md) | [Main README](../../../README.md)
