# 📦 Resources

This directory contains supporting materials for the 100 Days of DevOps challenges, including configuration files, scripts, and diagrams.

## 📂 Directory Structure

```
resources/
├── configs/          # Configuration files organized by technology
│   ├── docker/      # Docker Compose files and Dockerfiles
│   ├── kubernetes/  # Kubernetes manifests and deployments
│   ├── ansible/     # Ansible playbooks and roles
│   ├── terraform/   # Terraform configurations and modules
│   └── jenkins/     # Jenkins pipeline files
├── scripts/         # Helper scripts and utilities
└── diagrams/        # Architecture diagrams and visual aids
```

## 🐳 Docker Configurations

**Location**: `configs/docker/`

Production-ready Docker configurations including:
- **Dockerfiles**: For Apache, Python apps, and more
- **Docker Compose**: Multi-container application setups
- **Best Practices**: Optimized layer caching and security

[View Docker Configs](./configs/docker/README.md)

## ☸️ Kubernetes Manifests

**Location**: `configs/kubernetes/`

Kubernetes YAML files for:
- **Pods**: Basic pod configurations
- **Deployments**: Application deployments with replicas
- **Services**: ClusterIP, NodePort, LoadBalancer
- **Volumes**: Persistent volume configurations
- **Advanced**: Sidecar containers, init containers

[View Kubernetes Configs](./configs/kubernetes/README.md)

## 🤖 Ansible Playbooks

**Location**: `configs/ansible/`

Ansible automation playbooks for:
- **Package Management**: Installing and configuring packages
- **Configuration**: Server and application configuration
- **Templates**: Jinja2 templates for dynamic configs
- **Multi-Server**: Orchestrating across multiple servers

[View Ansible Playbooks](./configs/ansible/README.md)

## 🏗️ Terraform Configurations

**Location**: `configs/terraform/`

Infrastructure as Code with Terraform:
- **AWS Resources**: EC2, VPC, Security Groups
- **Networking**: Subnets, routing, NAT gateways
- **Monitoring**: CloudWatch alarms and dashboards
- **IAM**: Policies and role attachments

[View Terraform Configs](./configs/terraform/README.md)

## ⚙️ Jenkins Pipelines

**Location**: `configs/jenkins/`

CI/CD pipeline configurations:
- **Declarative Pipelines**: Modern Jenkins pipeline syntax
- **Multi-Stage**: Build, test, deploy stages
- **Parameterized**: Pipelines with user input
- **SCM Integration**: Git-triggered deployments

[View Jenkins Pipelines](./configs/jenkins/README.md)

## 📜 Scripts

**Location**: `scripts/`

Helper scripts and utilities:
- Automation scripts
- Setup and teardown scripts
- Testing utilities
- Deployment helpers

[View Scripts](./scripts/README.md)

## 📊 Diagrams

**Location**: `diagrams/`

Visual documentation including:
- Architecture diagrams
- Network topology
- Data flow diagrams
- Deployment workflows

---

## 💡 How to Use

### Copy and Modify
All configurations are templates that you can copy and customize:

```bash
# Example: Copy a Docker Compose file
cp resources/configs/docker/2-tier-app-docker-compose.yml my-app/

# Modify for your needs
vim my-app/2-tier-app-docker-compose.yml
```

### Learn by Example
Study the configurations to understand:
- Best practices for each technology
- Common patterns and anti-patterns
- Production-ready configurations
- Security considerations

### Reference During Challenges
Use these files as reference while working through challenges:
- Look up syntax
- Compare your solution
- Find alternative approaches
- Understand advanced features

---

## 📝 Contributing

Found an improvement or want to add more examples?
1. Create a new configuration file
2. Add detailed comments explaining each section
3. Include a usage example
4. Submit a pull request

---

## ⚖️ License

All configuration files are provided as examples for educational purposes.
Feel free to use and modify them for your own projects.

---

**Need Help?** Check the main [README](../README.md) or open a GitHub issue.
