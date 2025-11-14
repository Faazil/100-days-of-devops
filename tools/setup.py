#!/usr/bin/env python3
"""
Setup Script for 100 Days of DevOps
Initialize your learning environment and check prerequisites
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
import argparse


def check_command(command):
    """Check if a command exists"""
    return shutil.which(command) is not None


def get_version(command, *args):
    """Get version of a command"""
    try:
        result = subprocess.run(
            [command, *args],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip() or result.stderr.strip()
    except:
        return "Unknown"


def check_prerequisites():
    """Check if all required tools are installed"""
    print("\n" + "="*60)
    print("🔍 CHECKING PREREQUISITES")
    print("="*60 + "\n")

    tools = {
        "Essential": [
            ("git", ["--version"], "Git for version control"),
            ("python3", ["--version"], "Python 3 for scripting"),
        ],
        "Linux/Shell": [
            ("bash", ["--version"], "Bash shell"),
            ("ssh", ["-V"], "SSH client"),
        ],
        "Containers": [
            ("docker", ["--version"], "Docker for containerization"),
            ("docker-compose", ["--version"], "Docker Compose (optional)"),
        ],
        "Kubernetes": [
            ("kubectl", ["version", "--client"], "Kubernetes CLI (optional)"),
        ],
        "Configuration Management": [
            ("ansible", ["--version"], "Ansible (optional)"),
            ("terraform", ["--version"], "Terraform (optional)"),
        ],
    }

    missing_required = []
    missing_optional = []

    for category, tool_list in tools.items():
        print(f"\n📦 {category}:")
        print("-" * 60)

        for tool, args, description in tool_list:
            if check_command(tool):
                version = get_version(tool, *args)
                version_short = version.split('\n')[0][:50]
                print(f"  ✅ {tool:15} {version_short}")
            else:
                print(f"  ❌ {tool:15} Not found - {description}")
                if "optional" in description.lower():
                    missing_optional.append(tool)
                else:
                    missing_required.append(tool)

    print("\n" + "="*60)

    if missing_required:
        print("\n⚠️  Missing Required Tools:")
        for tool in missing_required:
            print(f"   - {tool}")
        print("\nPlease install the required tools before continuing.")
        return False
    elif missing_optional:
        print("\nℹ️  Some optional tools are missing:")
        for tool in missing_optional:
            print(f"   - {tool}")
        print("\nYou can install them as needed for specific challenges.")
        return True
    else:
        print("\n✅ All prerequisites are installed!")
        return True


def init_environment():
    """Initialize the learning environment"""
    print("\n" + "="*60)
    print("🚀 INITIALIZING ENVIRONMENT")
    print("="*60 + "\n")

    root_dir = Path(__file__).parent.parent

    # Create .progress.json if it doesn't exist
    progress_file = root_dir / ".progress.json"
    if not progress_file.exists():
        print("📝 Creating progress tracking file...")
        subprocess.run([sys.executable, str(root_dir / "tools" / "progress.py"), "--show"])
        print("✅ Progress tracker initialized")
    else:
        print("✅ Progress tracker already initialized")

    # Create .gitignore if it doesn't exist
    gitignore_file = root_dir / ".gitignore"
    if not gitignore_file.exists():
        print("📝 Creating .gitignore...")
        with open(gitignore_file, 'w') as f:
            f.write("""# Progress tracking (personal)
.progress.json

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Temporary files
*.tmp
*.log
.terraform/
*.tfstate
*.tfstate.backup
""")
        print("✅ .gitignore created")
    else:
        print("✅ .gitignore already exists")

    print("\n" + "="*60)
    print("✅ Environment initialized successfully!")
    print("="*60)


def show_getting_started():
    """Show getting started guide"""
    print("\n" + "="*60)
    print("📚 GETTING STARTED")
    print("="*60 + "\n")

    print("""
Welcome to 100 Days of DevOps! Here's how to get started:

1️⃣  Explore the Challenges
   cd challenges/week-01
   cat day-01.md

2️⃣  Work Through a Challenge
   - Read the challenge description
   - Follow the step-by-step solution
   - Try the verification steps

3️⃣  Track Your Progress
   python3 tools/progress.py --complete 1
   python3 tools/progress.py --show

4️⃣  Browse by Week
   Week 1-3:   Linux Fundamentals
   Week 4-5:   Git Version Control
   Week 6-7:   Docker Containers
   Week 8-10:  Kubernetes
   Week 11-13: CI/CD & Automation
   Week 14-15: Infrastructure as Code

5️⃣  Get Help
   - Check docs/ for detailed guides
   - Review resources/ for configuration examples
   - Visit the README.md for full documentation

Happy Learning! 🚀
    """)


def main():
    parser = argparse.ArgumentParser(
        description='Setup and initialize 100 Days of DevOps environment',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--check', action='store_true', help='Check prerequisites')
    parser.add_argument('--init', action='store_true', help='Initialize environment')
    parser.add_argument('--guide', action='store_true', help='Show getting started guide')

    args = parser.parse_args()

    if args.check:
        check_prerequisites()
    elif args.init:
        if check_prerequisites():
            init_environment()
            show_getting_started()
    elif args.guide:
        show_getting_started()
    else:
        # Default: run full setup
        if check_prerequisites():
            print("\n")
            init_response = input("Would you like to initialize the environment? (yes/no): ")
            if init_response.lower() in ['yes', 'y']:
                init_environment()
                show_getting_started()


if __name__ == "__main__":
    main()
