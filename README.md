# 🚀 100 Days of DevOps - KodeKloud Companion Guide

> **Your comprehensive companion guide for the KodeKloud Engineer 100 Days of DevOps challenge!** This repository provides detailed solutions, explanations, and learning resources to help you succeed in your DevOps journey on the KodeKloud platform.

[![100 Days](https://img.shields.io/badge/100%20Days-DevOps-blue?style=for-the-badge)](https://github.com/yourusername/100-days-of-devops)
[![KodeKloud](https://img.shields.io/badge/KodeKloud-Engineer-orange?style=for-the-badge)](https://kodekloud.com/kodekloud-engineer)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## ⚡ Start Your Journey on KodeKloud Engineer!

**👉 [Sign Up for KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer) 👈**

This repository is designed to be used **alongside** the KodeKloud Engineer platform where you'll get:
- 🎮 **Real hands-on labs** with actual servers and environments
- ✅ **Automated validation** of your solutions
- 🏆 **Points and achievements** as you progress
- 💼 **Resume-worthy projects** and certifications
- 👥 **Community support** from fellow learners

> **Important**: While this repository provides solutions and guidance, the real learning happens by doing the challenges on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**!

---

## 📖 About This Repository

This repository is a **companion guide** for the [KodeKloud Engineer 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer) challenge. It provides comprehensive solutions and detailed explanations to help you understand and complete each challenge on the platform.

### What You'll Find Here:

- ✅ **Step-by-step implementation** with clear explanations
- ✅ **Production-ready configurations** with inline comments
- ✅ **Verification steps** to ensure success
- ✅ **Troubleshooting guides** for common issues
- ✅ **Learning notes** with concepts and best practices
- ✅ **Alternative approaches** where applicable

### 🎯 Why Use KodeKloud Engineer + This Guide?

**KodeKloud Engineer Platform Gives You:**
- 🎮 **Real Infrastructure**: Actual servers, Kubernetes clusters, databases
- ✅ **Auto-Validation**: Know immediately if your solution works
- 🏆 **Gamification**: Points, achievements, and leaderboards
- 💼 **Career Value**: Verified skills to showcase on your resume
- 🌐 **Community**: Active forums and peer support

**This Companion Guide Gives You:**
- 📚 **Rich Context**: Understand the *why*, not just the *how*
- 🏗️ **Week-Based Organization**: Structured learning in manageable chunks
- 🤖 **Progress Tracking**: Track your journey locally
- 🎓 **Learning Notes**: Deep explanations and best practices
- 💼 **Production Ready**: Industry-standard configurations and examples

> **Together**: KodeKloud Engineer + This Guide = Your Complete DevOps Learning System! 🚀

---

## 🗂️ Repository Structure

```
100-days-of-devops/
├── challenges/              # 100 challenges organized by weeks
│   ├── week-01/            # Days 1-7: Linux Fundamentals
│   ├── week-02/            # Days 8-14: Linux Administration
│   ├── week-03/            # Days 15-21: Git Basics
│   ├── ...
│   └── week-15/            # Days 99-100: Advanced IaC
├── resources/              # Supporting materials
│   ├── configs/            # Configuration files by technology
│   ├── scripts/            # Helper scripts
│   └── diagrams/           # Architecture diagrams
├── docs/                   # Additional documentation
│   ├── getting-started.md
│   ├── prerequisites.md
│   ├── troubleshooting.md
│   └── reference.md
└── tools/                  # Automation utilities
    ├── progress.py         # Track your progress
    ├── setup.py            # Environment setup
    └── validate.py         # Validate solutions
```

---

## 🚀 How to Use This Guide

### Step 1: Sign Up for KodeKloud Engineer 🎯

**👉 [Create Your Free Account on KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer) 👈**

This is where you'll do the actual hands-on challenges! KodeKloud provides:
- Real server environments (Linux, Kubernetes clusters, etc.)
- Automated verification of your solutions
- Points, badges, and leaderboards
- Community forums and support

### Step 2: Clone This Companion Repository 📚

```bash
git clone https://github.com/yourusername/100-days-of-devops.git
cd 100-days-of-devops
```

### Step 3: Set Up Your Local Environment 🛠️

```bash
python3 tools/setup.py --init
```

This will:
- ✅ Check prerequisites
- ✅ Initialize progress tracking
- ✅ Set up your learning environment

### Step 4: Start a Challenge 🚀

**Recommended Workflow:**

1. **Log into KodeKloud Engineer** and start a challenge
2. **Read the challenge description** on the platform
3. **Try solving it yourself first** (this is important!)
4. **If you get stuck**, refer to this repository for guidance:
   ```bash
   # Navigate to the week
   cd challenges/week-01

   # Read the solution guide
   cat day-01.md
   ```
5. **Complete the challenge** on KodeKloud Engineer platform
6. **Submit and get verified** by KodeKloud's automated system
7. **Track your progress** locally:
   ```bash
   python3 ../../tools/progress.py --complete 1
   ```

### Step 5: Keep Learning! 📈

```bash
# View your progress
python3 tools/progress.py --show

# Move to the next challenge on KodeKloud Engineer!
```

> **💡 Pro Tip**: Try to solve challenges yourself before looking at solutions. The struggle is where the real learning happens!

---

## 📚 Learning Path

### 🟢 Weeks 1-3: Linux & System Administration (Days 1-21)
Master Linux fundamentals, user management, SSH, shell scripting, web servers, and databases.

**Topics**: User Management • SSH • Bash Scripting • Cron Jobs • SELinux • SystemD • NGINX • Apache • PostgreSQL • MariaDB

### 🔵 Weeks 4-5: Version Control with Git (Days 22-35)
Learn Git workflows, branching strategies, merging, rebasing, and collaboration.

**Topics**: Git Basics • Branching • Merging • Rebasing • Stashing • Cherry-picking • Conflict Resolution • Git Hooks

### 🟣 Weeks 6-7: Containerization with Docker (Days 36-49)
Understand containers, images, Docker networking, volumes, and multi-container applications.

**Topics**: Docker Basics • Images • Containers • Dockerfile • Docker Compose • Networking • Volumes • Multi-tier Apps

### 🔴 Weeks 8-10: Kubernetes Orchestration (Days 50-70)
Deploy and manage containerized applications at scale with Kubernetes.

**Topics**: Pods • Deployments • Services • ReplicaSets • ConfigMaps • Secrets • Volumes • Troubleshooting • Scaling

### 🟠 Weeks 11-13: CI/CD & Automation (Days 71-93)
Implement continuous integration and delivery pipelines with Jenkins and Ansible.

**Topics**: Jenkins Pipelines • Jenkinsfile • Multi-stage Builds • Ansible Playbooks • Automation • Configuration Management

### 🟡 Weeks 14-15: Infrastructure as Code (Days 94-100)
Provision and manage cloud infrastructure using Terraform.

**Topics**: Terraform Basics • AWS Resources • EC2 • VPC • Security Groups • IAM • CloudWatch • DynamoDB

---

## 📊 Challenge Categories

| Category | Days | Difficulty | Technologies |
|----------|------|------------|--------------|
| 🐧 **Linux Administration** | 1-20 | ⭐ Beginner | Linux, Bash, SSH, SystemD |
| 🔀 **Version Control** | 21-34 | ⭐ Beginner | Git, GitHub |
| 🐳 **Containerization** | 35-47 | ⭐⭐ Intermediate | Docker, Docker Compose |
| ☸️ **Orchestration** | 48-67 | ⭐⭐⭐ Advanced | Kubernetes, kubectl |
| ⚙️ **CI/CD** | 68-86 | ⭐⭐ Intermediate | Jenkins, Pipelines |
| 🤖 **Automation** | 87-93 | ⭐⭐ Intermediate | Ansible, Playbooks |
| 🏗️ **Infrastructure as Code** | 94-100 | ⭐⭐⭐ Advanced | Terraform, AWS |

---

## 🛠️ Prerequisites

Before starting, ensure you have:

### Essential Tools
- ✅ **Linux/Unix environment** (Ubuntu, CentOS, macOS, WSL2)
- ✅ **Git** for version control
- ✅ **Python 3** for automation scripts
- ✅ **SSH client** for remote access
- ✅ **Text editor** (VS Code, Vim, etc.)

### Optional Tools (Install as needed)
- 🐳 **Docker** for containerization challenges
- ☸️ **kubectl** for Kubernetes challenges
- 🤖 **Ansible** for automation challenges
- 🏗️ **Terraform** for IaC challenges
- ⚙️ **Jenkins** (or Jenkins in Docker) for CI/CD challenges

**Check Prerequisites**: Run `python3 tools/setup.py --check` to verify your setup.

---

## 💡 How to Use This Repository

### For Beginners
1. Start with **Week 1** and progress sequentially
2. Read each challenge thoroughly
3. Try to solve it yourself first
4. Refer to the solution for guidance
5. Complete the verification steps
6. Mark challenges complete using the progress tracker

### For Experienced Users
1. Browse by **category** to focus on specific topics
2. Jump to areas you want to improve
3. Use solutions as reference implementations
4. Contribute alternative approaches
5. Share your own insights

### Self-Paced Learning
- **Intensive**: Complete 1-2 challenges per day (50-100 days)
- **Balanced**: Complete 3-4 challenges per week (6 months)
- **Casual**: Work at your own pace, focus on quality over speed

---

## 📈 Progress Tracking

This repository includes a powerful progress tracking system:

```bash
# Mark a challenge as complete
python3 tools/progress.py --complete 5

# View your progress with beautiful visualization
python3 tools/progress.py --show

# Get detailed statistics
python3 tools/progress.py --stats

# List what you've completed
python3 tools/progress.py --list-completed

# See what's remaining
python3 tools/progress.py --list-remaining
```

Your progress is saved locally in `.progress.json` (not tracked in git).

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute
- 🐛 **Report Issues**: Found an error? Let us know!
- ✨ **Improve Solutions**: Have a better approach? Share it!
- 📝 **Enhance Documentation**: Make it clearer for others
- 🆕 **Add Resources**: Share helpful links and references
- 💬 **Share Experience**: Help others in discussions

### Contribution Guidelines
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages
6. Push to your fork
7. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📚 Additional Resources

### 🏆 Primary Learning Platform
- 🎯 **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)** - The official hands-on lab platform where you complete challenges with real infrastructure
- 📺 **[KodeKloud Courses](https://kodekloud.com/courses/)** - Video courses to supplement your learning
- 💬 **[KodeKloud Community](https://kodekloud.com/community/)** - Get help from instructors and peers

### Official Documentation
- 🔗 [Docker Documentation](https://docs.docker.com)
- 🔗 [Kubernetes Documentation](https://kubernetes.io/docs)
- 🔗 [Ansible Documentation](https://docs.ansible.com)
- 🔗 [Terraform Documentation](https://www.terraform.io/docs)

### Learning Materials
- 📖 [Linux Command Line Basics](docs/reference.md#linux)
- 📖 [Git Cheat Sheet](docs/reference.md#git)
- 📖 [Docker Best Practices](docs/reference.md#docker)
- 📖 [Kubernetes Concepts](docs/reference.md#kubernetes)

> **Remember**: This repository is a companion guide. The actual hands-on practice happens on [KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)!

---

## 🎓 Achievements & Certification

After completing all 100 challenges on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**:

1. ✅ **Earn your KodeKloud Engineer badge** - Official recognition from KodeKloud
2. 📊 **Check your local progress**: `python3 tools/progress.py --show`
3. 🏆 **View your KodeKloud points and rank** on the platform leaderboard
4. 📱 **Share your achievement** on LinkedIn with your KodeKloud certificate
5. 💼 **Add to your resume** - Verified DevOps skills from a recognized platform
6. 🚀 **Continue learning** - KodeKloud offers many more advanced challenges!

> **Pro Tip**: Your KodeKloud Engineer profile serves as proof of your hands-on DevOps skills to potential employers!

---

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Attribution
- **Challenge Source**: [KodeKloud 100 Days of DevOps](https://kodekloud.com)
- **Solutions & Content**: This repository's contributors

---

## 🌟 Support This Project

If you find this repository helpful:
- ⭐ **Star this repository**
- 🔀 **Fork it** and create your own solutions
- 📢 **Share it** with others learning DevOps
- 💬 **Contribute** improvements and feedback

---

## 📞 Contact & Community

- 💬 **Discussions**: Use GitHub Discussions for questions
- 🐛 **Issues**: Report bugs or request features
- 📧 **Email**: [your-email@example.com]
- 🐦 **Twitter**: [@yourhandle]

---

## 🎯 Ready to Start Your DevOps Journey?

<div align="center">

### **👇 Take Action Now! 👇**

**Step 1**: [🚀 Sign Up for KodeKloud Engineer (Free)](https://kodekloud.com/kodekloud-engineer)

**Step 2**: [📚 Clone This Companion Guide](https://github.com/yourusername/100-days-of-devops)

**Step 3**: [🎓 Start Day 1 Challenge](challenges/week-01/day-01.md)

---

**Happy Learning! 🚀**

*Master DevOps one challenge at a time with hands-on practice on KodeKloud Engineer*

[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer) • [Get Started](challenges/week-01/day-01.md) • [Track Progress](#-progress-tracking) • [Contribute](#-contributing)

</div>

---

## 🗓️ Week-by-Week Overview

<details>
<summary><b>📅 Click to expand full weekly breakdown</b></summary>

### Week 1: Linux Fundamentals
- Day 1: Linux User Setup with Non-interactive Shell
- Day 2: Temporary User Setup with Expiry Date
- Day 3: Secure SSH Root Access
- Day 4: Script Execute Permissions
- Day 5: Install and Configuration SELinux
- Day 6: Setup a Cron Job
- Day 7: Linux SSH Automation

### Week 2: Linux System Administration
- Day 8: Setup Ansible
- Day 9: Debugging MariaDB Issues
- Day 10: Create a BASH Script
- Day 11: Install and Setup Tomcat Server
- Day 12: Linux Network Services
- Day 13: IPtables Installation And Configuration
- Day 14: Linux Process Troubleshooting

### Week 3: Web Servers & Databases
- Day 15: Setup SSL for NGINX
- Day 16: Install and Configure NGINX as Load Balancer
- Day 17: Install and Configure PostgreSQL
- Day 18: Configure LAMP Server
- Day 19: Install and Configure Web Application
- Day 20: Configure Nginx + PHP-FPM Using Unix Sock
- Day 21: Setup Git Repository on Server

### Week 4: Git Fundamentals
- Day 22: Clone Git Repository
- Day 23: Fork a Repository
- Day 24: Git Branch Create
- Day 25: Git Branch Merge
- Day 26: Git Manage Remotes
- Day 27: Git Revert Some Changes
- Day 28: Git Cherry Pick

### Week 5: Advanced Git
- Day 29: Git Pull Request
- Day 30: Git Reset Hard
- Day 31: Git Stash
- Day 32: Git Rebase
- Day 33: Git Merge Conflict Resolve
- Day 34: Configure Git Hook
- Day 35: Setup Docker Installation

### Week 6: Docker Basics
- Day 36: Run a NGINX Container on Docker
- Day 37: Copy File to Docker Container
- Day 38: Docker Pull Images
- Day 39: Create a Docker Image From a Container
- Day 40: Docker Execution
- Day 41: Create a Docker File
- Day 42: Create Docker Network

### Week 7: Advanced Docker
- Day 43: Docker Ports Mapping
- Day 44: Creating a Docker Compose File
- Day 45: Resolve Dockerfile Issues
- Day 46: Deploy an App on Docker Containers
- Day 47: Docker Python App
- Day 48: Deploy Pods in Kubernetes Cluster
- Day 49: Deploy Applications with Kubernetes Deployments

### Week 8: Kubernetes Fundamentals
- Day 50: Set Resource Limits in Kubernetes Cluster
- Days 51-56: Various Kubernetes challenges
- Day 57-63: Kubernetes advanced topics

### Week 9-10: Kubernetes Deep Dive
- Days 57-70: Advanced Kubernetes operations

### Week 11-13: CI/CD with Jenkins & Ansible
- Days 71-93: Jenkins Pipelines and Ansible Automation

### Week 14-15: Infrastructure as Code
- Days 94-100: Terraform and AWS infrastructure

</details>

---

*Last Updated: 2024 • Made with ❤️ for the DevOps Community*
