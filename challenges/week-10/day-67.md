# Challenge 67: Deploy Guest Book App on Kubernetes

## 📊 Metadata
- **Day**: 67
- **Week**: 10
- **Day in Week**: 4/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus Application development team has finished development of one of the applications and it is ready for deployment. It is a guestbook application that will be used to manage entries for guests/visitors. As per discussion with the DevOps team, they have finalized the infrastructure that will be deployed on Kubernetes cluster. Below you can find more details about it.


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
- Day 64: Fix Python App Deployed on Kubernetes Cluster (recommended)
- Day 65: Deploy Redis Deployment on Kubernetes (recommended)
- Day 66: Deploy MySQL on Kubernetes (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## BACKEND TIER

Create a deployment named `redis-master` for Redis master.

a. Replicas count should be `1`.

b. Container name should be `master-redis-devops` and it should use image `redis`.

c. Request resources as CPU should be `100m` and Memory should be `100Mi`.

d. Container port should be redis default port i.e `6379`.

Create a service named `redis-master` for Redis master. Port and targetPort should be Redis default port i.e `6379`.

Create another deployment named `redis-slave` for Redis slave.

a. Replicas count should be `2`.

b. Container name should be `slave-redis-devops` and it should use `gcr.io/google_samples/gb-redisslave:v3` image.

c. Requests resources as CPU should be `100m` and Memory should be `100Mi`.

d. Define an environment variable named `GET_HOSTS_FROM` and its value should be `dns`.

e. Container port should be Redis default port i.e `6379`.

Create another service named `redis-slave`. It should use Redis default port i.e `6379`.

## FRONTEND TIER

Create a deployment named `frontend`.

a. Replicas count should be `3`.

b. Container name should be `php-redis-devops` and it should use `gcr.io/google-samples/gb-frontend@sha256:a908df8486ff66f2c4daa0d3d8a2fa09846a1fc8efd65649c0109695c7c5cbff` image.

c. Request resources as CPU should be `100m` and Memory should be `100Mi`.

d. Define an environment variable named as `GET_HOSTS_FROM` and its value should be `dns`.

e. Container port should be `80`.

Create a service named `frontend`. Its type should be `NodePort`, port should be `80` and its nodePort should be `30009`.

Finally, you can check the guestbook app by clicking on App button.

You can use any labels as per your choice.

> Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.

## Steps

Let's summerize, we have to create?

- redis master and slave deployment as backend and php-redis deployment as frontend
- two services for redis master and slave and one service for frontend

1. Let's create `k3s-redis-master.yaml` file and copy-paste contents from this [Redis Master YAML file](../files/k3s-redis-master-deployment-067.yaml)

2. Let's create `k3s-redis-slave.yaml` file and copy-paste contents from this [Redis Salve YAML file](../files/k3s-redis-slave-deployment-067.yaml)

3. Let's create `k3s-php-redis.yaml` file and copy-paste contents from this [Php Redis YAML file](../files/k3s-php-redis-deployment-067.yaml)

4. Create all the deployment one by one

    ```sh
    kubectl apply -f k3s-redis-master.yaml
    ```

    > wait few seconds until pods are running

    ```sh
    kubectl apply -f k3s-redis-slave.yaml
    ```

    > wait few seconds until pods are running

    ```sh
    kubectl apply -f k3s-php-redis.yaml
    ```

    > wait few seconds until all the pods are running

5. Verify results

    Access the application from the UI button.

## Good to Know?

### Multi-Tier Application Architecture

- **Frontend Tier**: User interface (PHP web application)
- **Backend Tier**: Data layer (Redis master/slave)
- **Service Communication**: DNS-based service discovery
- **Scalability**: Independent scaling of each tier

### Redis Architecture

- **Master-Slave**: Master handles writes, slaves handle reads
- **Replication**: Data replicated from master to slaves
- **High Availability**: Multiple slaves for redundancy
- **Load Distribution**: Read operations distributed across slaves

### Service Discovery

- **DNS Names**: Services accessible by name within cluster
- **Environment Variables**: GET_HOSTS_FROM=dns enables DNS lookup
- **Service Mesh**: Advanced service-to-service communication
- **Load Balancing**: Kubernetes distributes traffic automatically

### Application Deployment

- **Resource Requests**: Ensure adequate resources for each component
- **Health Checks**: Configure liveness and readiness probes
- **Rolling Updates**: Update components without downtime
- **Monitoring**: Track application performance and health

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

- **← Previous**: [Day 66 - Deploy MySQL on Kubernetes](./day-66.md)
- **Next →**: [Day 68 - Set Up Jenkins Server](../week-10/day-68.md)

### Similar Challenges (Kubernetes)
- [Day 58 - Deploy Grafana on Kubernetes Cluster](../week-09/day-58.md)
- [Day 59 - Troubleshoot Deployment Issues in Kubernetes](../week-09/day-59.md)
- [Day 60 - Persistent Volumes in Kubernetes](../week-09/day-60.md)

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

