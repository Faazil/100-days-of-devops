# 🚀 Getting Started with 100 Days of DevOps

Welcome to your DevOps learning journey! This guide will help you get started with **KodeKloud Engineer** and use this companion repository effectively.

## 📋 Table of Contents

- [Sign Up for KodeKloud Engineer](#sign-up-for-kodekloud-engineer) ⭐
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
- [Repository Structure](#repository-structure)
- [How to Use This Repository](#how-to-use-this-repository)
- [Progress Tracking](#progress-tracking)
- [Getting Help](#getting-help)

---

## 🎯 Sign Up for KodeKloud Engineer

**👉 [Create Your Free Account Here](https://kodekloud.com/kodekloud-engineer) 👈**

### Why KodeKloud Engineer?

This is THE platform where you'll do the actual hands-on challenges. Here's what you get:

✅ **Real Infrastructure**
- Actual Linux servers (not simulations!)
- Real Kubernetes clusters
- Production-like environments

✅ **Automated Validation**
- Instant feedback on your solutions
- Know immediately if you got it right
- No guessing if your solution works

✅ **Career Benefits**
- Points and achievements to showcase
- Certificate of completion
- Verified skills for your resume
- Recognition from a known platform

✅ **Community & Support**
- Active forums
- Help from instructors
- Learn with peers
- Share experiences

> **Important**: While this GitHub repository provides guidance and explanations, the actual learning happens by doing challenges on KodeKloud Engineer with real infrastructure!

---

## Prerequisites

Before starting, ensure you have the basics covered. See [Prerequisites Guide](./prerequisites.md) for detailed instructions.

### Essential
- Linux/Unix environment (Ubuntu, CentOS, macOS, or WSL2)
- Git for version control
- Python 3.7+ for automation tools
- SSH client
- Text editor (VS Code, Vim, nano, etc.)

### Optional (Install as Needed)
- Docker for containerization
- kubectl for Kubernetes
- Ansible for automation
- Terraform for Infrastructure as Code
- Jenkins (or run in Docker)

---

## Environment Setup

### 1. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/yourusername/100-days-of-devops.git
cd 100-days-of-devops
```

### 2. Run the Setup Script

```bash
# Check prerequisites
python3 tools/setup.py --check

# Initialize environment
python3 tools/setup.py --init
```

This will:
- ✅ Verify all required tools are installed
- ✅ Initialize progress tracking
- ✅ Create necessary configuration files
- ✅ Display getting started guide

### 3. Test Your Setup

```bash
# View progress tracker
python3 tools/progress.py --show

# Check environment
python3 tools/validate.py --env
```

---

## Repository Structure

```
100-days-of-devops/
├── challenges/              # 100 challenges in 15 weeks
│   ├── week-01/            # Week 1: Linux Fundamentals
│   │   ├── README.md       # Week overview
│   │   ├── day-01.md       # Challenge 1
│   │   └── ...
│   └── week-15/            # Week 15: Advanced IaC
├── resources/              # Supporting materials
│   ├── configs/            # Configuration examples
│   │   ├── docker/        # Docker configs
│   │   ├── kubernetes/    # K8s manifests
│   │   ├── ansible/       # Playbooks
│   │   ├── terraform/     # IaC configs
│   │   └── jenkins/       # Pipelines
│   ├── scripts/           # Helper scripts
│   └── diagrams/          # Visual aids
├── docs/                  # Documentation
│   ├── getting-started.md # This file
│   ├── prerequisites.md   # Setup guide
│   ├── troubleshooting.md # Common issues
│   └── reference.md       # Quick reference
└── tools/                 # Automation tools
    ├── progress.py        # Progress tracker
    ├── setup.py           # Setup helper
    └── validate.py        # Solution validator
```

---

## How to Use This Repository

### Learning Paths

Choose your learning style:

#### 🏃 **Intensive Track** (50-100 days)
- Complete 1-2 challenges per day
- Best for: Career changers, bootcamp students
- Time commitment: 2-3 hours/day

#### 🚶 **Balanced Track** (6 months)
- Complete 3-4 challenges per week
- Best for: Working professionals
- Time commitment: 5-10 hours/week

#### 🧘 **Casual Track** (At your pace)
- Work through challenges as time allows
- Best for: Continuous learners
- Time commitment: Flexible

### Working Through a Challenge

#### The Recommended Workflow (KodeKloud First!)

**Step 1: Start on KodeKloud Engineer** 🎮

1. Log into [KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)
2. Navigate to "100 Days of DevOps"
3. Click "Start" on the challenge
4. **Read the challenge description carefully** on the platform

**Step 2: Try It Yourself** 💪

This is the most important step:
1. Think about the approach
2. Try to solve it independently on KodeKloud's lab environment
3. Don't rush to look at solutions!
4. The struggle is where real learning happens

**Step 3: Get Hints (If Needed)** 📖

If you're stuck after trying:
```bash
cd challenges/week-01
cat day-01.md  # Read our solution guide
```

Our guide includes:
- 📊 Metadata (difficulty, time, category)
- 🎯 Detailed explanations
- 🛠️ Step-by-step solution with reasoning
- 📚 Learning notes and best practices

**Step 4: Complete on KodeKloud** ✅

1. Implement the solution in KodeKloud's lab environment
2. Run the verification (KodeKloud validates automatically)
3. Get your points and achievement!
4. Review any mistakes or alternate approaches

**Step 5: Track Your Progress Locally** 📊

```bash
# Mark challenge as complete in your local tracker
python3 ../../tools/progress.py --complete 1

# View your progress
python3 ../../tools/progress.py --show
```

> **Remember**: Your KodeKloud Engineer profile is your official record. This local tracker is just for personal reference!

### Tips for Success

1. **Understand, Don't Memorize**
   - Focus on understanding concepts
   - Learn why commands work
   - Experiment with variations

2. **Hands-On Practice**
   - Actually type and run commands
   - Don't just read solutions
   - Break things and fix them

3. **Take Notes**
   - Document what you learn
   - Keep a DevOps journal
   - Build your own reference guide

4. **Ask Questions**
   - Use GitHub Discussions
   - Research unfamiliar concepts
   - Connect with other learners

5. **Build Projects**
   - Apply skills to personal projects
   - Combine multiple concepts
   - Create portfolio pieces

---

## Progress Tracking

### View Your Progress

```bash
# Show overview with progress bar
python3 tools/progress.py --show

# Get detailed statistics
python3 tools/progress.py --stats

# List completed challenges
python3 tools/progress.py --list-completed

# See what's remaining
python3 tools/progress.py --list-remaining
```

### Manage Progress

```bash
# Mark day 5 as complete
python3 tools/progress.py --complete 5

# Mark day 3 as incomplete
python3 tools/progress.py --incomplete 3

# Reset all progress (careful!)
python3 tools/progress.py --reset
```

Your progress is saved locally in `.progress.json` and not tracked in Git.

---

## Getting Help

### Documentation
- **Prerequisites**: [prerequisites.md](./prerequisites.md)
- **Troubleshooting**: [troubleshooting.md](./troubleshooting.md)
- **Reference**: [reference.md](./reference.md)

### Community
- **GitHub Discussions**: Ask questions and share knowledge
- **Issues**: Report bugs or request features
- **Pull Requests**: Contribute improvements

### External Resources
- KodeKloud official platform
- Technology-specific documentation
- DevOps community forums

---

## Next Steps

Ready to start? Here's your action plan:

1. ✅ **Complete Setup**: Run `python3 tools/setup.py --init`
2. ✅ **Review Prerequisites**: Check [prerequisites.md](./prerequisites.md)
3. ✅ **Start Week 1**: Navigate to `challenges/week-01/`
4. ✅ **Do Challenge 1**: Open `day-01.md` and begin!
5. ✅ **Track Progress**: Use the progress tracker

---

## FAQ

**Q: Do I need a KodeKloud Engineer account?**
A: **YES!** That's where the actual hands-on challenges are. This repository is just a companion guide. [Sign up here (free)](https://kodekloud.com/kodekloud-engineer).

**Q: Can I just use this repository without KodeKloud?**
A: You can read the solutions, but you'll miss out on:
- Real server environments and infrastructure
- Automated validation of your solutions
- Points, achievements, and certificates
- The actual hands-on learning experience

**Q: Is KodeKloud Engineer free?**
A: Yes! KodeKloud Engineer offers free access to many challenges. Some advanced features may require a subscription.

**Q: Do I need to complete challenges in order?**
A: It's recommended for beginners, but experienced users can jump to specific topics.

**Q: How long does each challenge take?**
A: Most challenges take 20-30 minutes on the KodeKloud platform.

**Q: What if I get stuck on KodeKloud?**
A:
1. Try to solve it yourself first (most important!)
2. Check this repository's solution guide
3. Ask in KodeKloud's community forums
4. Review the troubleshooting section

**Q: Do I need a cloud account?**
A: No! KodeKloud Engineer provides all the infrastructure. You just need an internet connection and a browser.

---

## 🎉 You're Ready!

### Your Action Plan:

**1. 🚀 [Sign Up for KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)** (If you haven't already)

**2. 📖 Browse [Week 1 Overview](../challenges/week-01/README.md)** to understand what's coming

**3. 🎯 Start Day 1 on KodeKloud Engineer** platform

**4. 📚 Use this repo as your companion guide** when you need help

**Remember**:
- The goal is learning, not speed. Take your time!
- Try solving challenges yourself before looking at solutions
- The real learning happens on KodeKloud Engineer with hands-on practice
- This repository is your study buddy, not a replacement for actual practice

---

### 🔥 Take the First Step Now!

**👉 [Launch KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer) 👈**

---

[← Back to Main README](../README.md) | [View Prerequisites →](./prerequisites.md)
