# Challenge 63: Deploy Iron Gallery App on Kubernetes

## 📊 Metadata
- **Day**: 63
- **Week**: 9
- **Day in Week**: 7/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

There is an iron gallery app that the Nautilus DevOps team was developing. They have recently customized the app and are going to deploy the same on the Kubernetes cluster. Below you can find more details:

- Create a namespace `iron-namespace-xfusion`

- Create a deployment `iron-gallery-deployment-xfusion` for iron gallery under the same namespace you created.

  - Labels `run` should be `iron-gallery`.

  - Replicas count should be `1`.

  - Selector's matchLabels `run` should be `iron-gallery`.

  - Template labels `run` should be `iron-gallery` under metadata.

  - The container should be named as `iron-gallery-container-xfusion`, use `kodekloud/irongallery:2.0` image ( use exact image name / tag ).

  - Resources limits for memory should be `100Mi` and for CPU should be `50m`.

  - First volumeMount name should be `config`, its mountPath should be `/usr/share/nginx/html/data`.

  - Second volumeMount name should be `images`, its mountPath should be `/usr/share/nginx/html/uploads`.

  - First volume name should be `config` and give it `emptyDir` and second volume name should be `images`, also give it `emptyDir`.

- Create a deployment `iron-db-deployment-xfusion` for iron db under the same namespace.

  - Labels `db` should be `mariadb`.

  - Replicas count should be `1`.

  - Selector's matchLabels `db` should be `mariadb`.

  - Template labels `db` should be `mariadb` under metadata.

  - The container name should be `iron-db-container-xfusion`, use `kodekloud/irondb:2.0 image` ( use exact image name / tag ).

  - Define environment, set `MYSQL_DATABASE` its value should be `database_blog`, set `MYSQL_ROOT_PASSWORD` and `MYSQL_PASSWORD` value should be with some complex passwords for DB connections, and `MYSQL_USER` value should be any custom user ( except root ).

  - Volume mount name should be `db` and its mountPath should be `/var/lib/mysql`. Volume name should be `db` and give it an `emptyDir`.

- Create a service for iron db which should be named `iron-db-service-xfusion` under the same namespace. Configure spec as selector's db should be `mariadb`. Protocol should be TCP, port and targetPort should be `3306`and its type should be `ClusterIP`.

- Create a service for iron gallery which should be `named iron-gallery-service-xfusion` under the same namespace. Configure spec as selector's run should be `iron-gallery`. Protocol should be TCP, port and targetPort should be 80, nodePort should be `32678` and its type should be `NodePort`.

- Note:
  - We don't need to make connection b/w database and front-end now, if the installation page is coming up it should be enough for now.
  - The kubectl on jump_host has been configured to work with the kubernetes cluster.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

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
- Day 59: Troubleshoot Deployment Issues in Kubernetes (recommended)
- Day 60: Persistent Volumes in Kubernetes (recommended)
- Day 62: Manage Secrets in Kubernetes (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Let's create the namespace first:

    ```sh
    kubectl create ns iron-namespace-xfusion
    kubectl get ns
    ```

    > We can see our namespace in the list

2. Create `k3s-iron-gallery.yaml` file and copy-paste contents from this [YAML file](../files/k3s-iron-gallery-deployment-63.yaml)

3. Let's run the deployment

    ```sh
    kubectl apply -f k3s-iron-gallery.yaml
    ```

    > This single yaml file wile create two deployments, and two services

4. Verify results

    ```sh
    kubectl get ns
    kubectl get deployments.apps -n iron-namespace-xfusion
    kubectl get pods -n iron-namespace-xfusion
    kubectl get svc -n iron-namespace-xfusion
    ```

## Good to Know?

### Kubernetes Namespaces

- **Purpose**: Virtual clusters within physical cluster
- **Resource Isolation**: Separate resources by environment/team
- **RBAC**: Fine-grained access control per namespace
- **Resource Quotas**: Limit resource usage per namespace

### Multi-Tier Applications

- **Frontend**: User interface layer (web servers)
- **Backend**: Business logic and APIs
- **Database**: Data persistence layer
- **Service Communication**: Inter-service networking

### Application Architecture

- **Microservices**: Decompose application into services
- **Service Discovery**: Services find each other via DNS
- **Load Balancing**: Distribute traffic across replicas
- **Data Persistence**: Separate stateful and stateless components

### Deployment Strategies

- **Environment Variables**: Configure service connections
- **ConfigMaps**: External configuration management
- **Secrets**: Secure credential management
- **Health Checks**: Ensure service availability

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

- **← Previous**: [Day 62 - Manage Secrets in Kubernetes](./day-62.md)
- **Next →**: [Day 64 - Fix Python App Deployed on Kubernetes Cluster](../week-10/day-64.md)

### Similar Challenges (Kubernetes)
- [Day 53 - Resolve VolumeMounts Issue in Kubernetes](../week-08/day-53.md)
- [Day 54 - Kubernetes Shared Volumes](../week-08/day-54.md)
- [Day 58 - Deploy Grafana on Kubernetes Cluster](../week-09/day-58.md)

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
**Difficulty**: {get_difficulty_emoji(day)}
**Category**: {task_info['category']}

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
python3 ../../tools/progress.py --complete {day}
```

