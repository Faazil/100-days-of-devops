# Challenge 58: Deploy Grafana on Kubernetes Cluster

## 📊 Metadata
- **Day**: 58
- **Week**: 9
- **Day in Week**: 2/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps teams is planning to set up a Grafana tool to collect and analyze analytics from some applications. They are planning to deploy it on Kubernetes cluster. Below you can find more details.

1. Create a deployment named `grafana-deployment-datacenter` using any grafana image for Grafana app. Set other parameters as per your choice.

2. Create NodePort type service with nodePort `32000` to expose the app.

> You need not to make any configuration changes inside the Grafana app once deployed, just make sure you are able to access the Grafana login page.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Kubernetes cluster with kubectl configured
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `kubectl`, `kubectl apply`, `kubectl get`, `kubectl describe`, `kubectl logs`
- **Key Concepts**:
  - Kubernetes resources (Pods, Deployments, Services)
  - YAML manifest structure
  - Resource requests and limits
  - Labels and selectors
- **File Formats**: YAML syntax and structure
- **Environment**: kubectl configured to access Kubernetes cluster

**Foundation from Earlier Challenges:**
- Day 52: Execute Rollback in Kubernetes Cluster (recommended)
- Day 53: Resolve VolumeMounts Issue in Kubernetes (recommended)
- Day 54: Kubernetes Shared Volumes (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Let's create `k3s-deployment.yaml` file and copy content from this [YAML file](../files/k3s-grafana-deployment-058.yaml)

2. Create deployment and services

    ```sh
    kubectl apply -f k3s-deployment.yaml
    ```

3. Verify results

    ```sh
    kubectl get deployments.apps
    kubectl get svc
    ```

## Good to Know?

### Application Deployment

- **Containerized Apps**: Package applications in containers
- **Declarative Config**: Define desired state in YAML
- **Service Exposure**: Make applications accessible
- **Scaling**: Adjust replicas based on demand

### Grafana on Kubernetes

- **Monitoring**: Visualize metrics and logs
- **Dashboards**: Create custom monitoring dashboards
- **Data Sources**: Connect to Prometheus, InfluxDB, etc.
- **Persistence**: Use PVCs for dashboard and config storage

### Service Exposure

- **NodePort**: Simple external access method
- **Ingress**: HTTP/HTTPS routing with domain names
- **LoadBalancer**: Cloud provider integration
- **Port Forwarding**: Development and debugging access

### Production Considerations

- **Persistent Storage**: Use PVCs for data persistence
- **Resource Limits**: Set appropriate CPU/memory limits
- **Security**: Configure authentication and authorization
- **High Availability**: Multiple replicas and anti-affinity

---

## ✅ Verification

After completing the challenge, verify your solution by:

1. **Testing the implementation**
   - Run all commands from the solution
   - Check for any error messages

2. **Validating the results**
   - Ensure all requirements are met
   - Test edge cases if applicable

3. **Clean up (if needed)**
   - Remove temporary files
   - Reset any test configurations

---

## 📚 Learning Notes

### Key Concepts

This challenge covers the following concepts:
- Practical application of Kubernetes skills
- Real-world DevOps scenarios
- Best practices for production environments

### Common Pitfalls

- ⚠️ **Permissions**: Ensure you have the necessary permissions to execute commands
- ⚠️ **Syntax**: Double-check command syntax and flags
- ⚠️ **Environment**: Verify you're working in the correct environment/server

### Best Practices

- ✅ Always verify changes before marking as complete
- ✅ Test your solution in a safe environment first
- ✅ Document any deviations from the standard approach
- ✅ Keep security in mind for all configurations

---

## 🔗 Related Challenges

- **← Previous**: [Day 57 - Print Environment Variables](./day-57.md)
- **Next →**: [Day 59 - Troubleshoot Deployment Issues in Kubernetes](../week-09/day-59.md)

### Similar Challenges (Kubernetes)
- [Day 48 - Deploy Pods in Kubernetes Cluster](../week-07/day-48.md)
- [Day 49 - Deploy Applications with Kubernetes Deployments](../week-07/day-49.md)
- [Day 50 - Set Resource Limits in Kubernetes Cluster](../week-08/day-50.md)

---

## 📖 Additional Resources

- [KodeKloud Official Documentation](https://kodekloud.com)
- [Official Technology Documentation](#)
- [Community Discussions](#)

---

## 🎓 Knowledge Check

After completing this challenge, you should be able to:
- [ ] Understand the problem statement clearly
- [ ] Implement the solution independently
- [ ] Verify the solution works correctly
- [ ] Explain the concepts to others
- [ ] Apply these skills to similar problems

---

**Challenge Source**: KodeKloud 100 Days of DevOps
**Difficulty**: ⭐
**Category**: DevOps

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
```

