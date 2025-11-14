#!/usr/bin/env python3
"""
Update Prerequisites for 100 Days of DevOps Challenges

This script updates the prerequisites section in all challenge files with
task-specific requirements while preserving the KodeKloud platform emphasis
and our unique repository identity.

Usage:
    python3 update_prerequisites.py --preview    # Preview changes
    python3 update_prerequisites.py --apply      # Apply updates
    python3 update_prerequisites.py --day 50     # Update specific day
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional


class PrerequisiteUpdater:
    """Updates prerequisites sections in challenge markdown files."""

    def __init__(self, base_dir: str = None):
        """Initialize the updater with base directory."""
        if base_dir is None:
            # Get the script's directory and go up one level
            base_dir = Path(__file__).parent.parent
        self.base_dir = Path(base_dir)
        self.challenges_dir = self.base_dir / "challenges"
        self.tasks_file = self.base_dir / "tools" / "tasks.json"

        # Load task metadata
        self.tasks = self._load_tasks()

        # Load prerequisite templates
        self.prereq_templates = self._load_prerequisite_templates()

    def _load_tasks(self) -> Dict:
        """Load task metadata from tasks.json."""
        if self.tasks_file.exists():
            with open(self.tasks_file, 'r') as f:
                data = json.load(f)
                # Convert list to dict with day as key
                if isinstance(data, list):
                    return {str(task['day']): task for task in data}
                return data.get('tasks', {})
        return {}

    def _load_prerequisite_templates(self) -> Dict[str, Dict]:
        """
        Define prerequisite templates for each technology category.
        Each template includes specific tools, concepts, and skills needed.
        """
        return {
            "Linux": {
                "commands": ["ssh", "sudo", "useradd", "cat", "grep", "chmod", "chown"],
                "concepts": [
                    "SSH remote access",
                    "User and group management",
                    "File permissions and ownership",
                    "Linux file system hierarchy"
                ],
                "skills": [
                    "Execute commands with sudo privileges",
                    "Navigate Linux file system",
                    "Manage users and groups",
                    "Understand file permissions"
                ]
            },
            "Docker": {
                "commands": ["docker", "docker run", "docker ps", "docker build", "docker exec"],
                "concepts": [
                    "Container vs Image distinction",
                    "Container lifecycle management",
                    "Docker networking fundamentals",
                    "Volume mounting and persistence"
                ],
                "skills": [
                    "Build Docker images from Dockerfiles",
                    "Run and manage containers",
                    "Use port mapping and volumes",
                    "Execute commands in running containers"
                ],
                "requires": "Docker installed and running"
            },
            "Kubernetes": {
                "commands": ["kubectl", "kubectl apply", "kubectl get", "kubectl describe", "kubectl logs"],
                "concepts": [
                    "Kubernetes resources (Pods, Deployments, Services)",
                    "YAML manifest structure",
                    "Resource requests and limits",
                    "Labels and selectors",
                    "Namespaces"
                ],
                "skills": [
                    "Write Kubernetes YAML manifests",
                    "Deploy resources using kubectl",
                    "Debug pods and containers",
                    "Understand Kubernetes architecture"
                ],
                "requires": "kubectl configured to access Kubernetes cluster",
                "file_formats": ["YAML"]
            },
            "Git": {
                "commands": ["git", "git init", "git add", "git commit", "git push", "git clone", "git branch"],
                "concepts": [
                    "Version control fundamentals",
                    "Branching and merging strategies",
                    "Remote repositories",
                    "Commit history management"
                ],
                "skills": [
                    "Initialize and clone repositories",
                    "Create commits with meaningful messages",
                    "Manage branches effectively",
                    "Push and pull from remotes"
                ]
            },
            "Jenkins": {
                "commands": [],
                "concepts": [
                    "Jenkins UI navigation",
                    "Job configuration (Freestyle, Pipeline)",
                    "Plugin installation and management",
                    "Build triggers and scheduling",
                    "Credentials management"
                ],
                "skills": [
                    "Create and configure Jenkins jobs",
                    "Install and configure plugins",
                    "Manage credentials securely",
                    "Configure build parameters",
                    "Set up build triggers"
                ],
                "requires": "Access to Jenkins server",
                "credentials": "Jenkins admin credentials"
            },
            "Ansible": {
                "commands": ["ansible", "ansible-playbook"],
                "concepts": [
                    "Inventory file structure (INI/YAML)",
                    "Playbook anatomy (plays, tasks, modules)",
                    "Ansible modules (yum, apt, copy, file, etc.)",
                    "Variables and facts",
                    "Idempotency principles"
                ],
                "skills": [
                    "Write inventory files",
                    "Create playbooks with proper YAML syntax",
                    "Use Ansible modules effectively",
                    "Configure SSH connectivity",
                    "Handle privilege escalation (become)"
                ],
                "requires": "Ansible installed",
                "file_formats": ["YAML", "INI"]
            },
            "Terraform": {
                "commands": ["terraform", "terraform init", "terraform plan", "terraform apply", "terraform destroy"],
                "concepts": [
                    "Infrastructure as Code (IaC) principles",
                    "HCL syntax and structure",
                    "Resource blocks and attributes",
                    "State management",
                    "Provider configuration",
                    "Variables and outputs"
                ],
                "skills": [
                    "Write Terraform configuration files in HCL",
                    "Initialize Terraform working directories",
                    "Plan and apply infrastructure changes",
                    "Manage Terraform state",
                    "Use Terraform providers (AWS, Azure, etc.)"
                ],
                "requires": "Terraform installed",
                "file_formats": ["HCL (.tf files)"]
            },
            "Web Server": {
                "commands": ["curl", "systemctl", "httpd", "nginx"],
                "concepts": [
                    "Web server configuration",
                    "Virtual hosts setup",
                    "Service management with systemd",
                    "Port binding and listening"
                ],
                "skills": [
                    "Install and configure web servers",
                    "Manage services with systemctl",
                    "Test web server responses",
                    "Configure virtual hosts"
                ]
            },
            "Database": {
                "commands": ["mysql", "mariadb", "psql"],
                "concepts": [
                    "Database server installation",
                    "User and privilege management",
                    "Database creation and schema",
                    "SQL query fundamentals"
                ],
                "skills": [
                    "Install database servers",
                    "Create databases and users",
                    "Grant and manage privileges",
                    "Execute SQL commands"
                ]
            },
            "DevOps": {
                "commands": [],
                "concepts": [
                    "DevOps workflow and principles",
                    "CI/CD pipeline concepts",
                    "Automation strategies",
                    "Infrastructure management"
                ],
                "skills": [
                    "Understand DevOps methodologies",
                    "Integrate multiple tools",
                    "Implement automation workflows"
                ]
            }
        }

    def get_task_category(self, day: int) -> str:
        """Get the category for a specific day."""
        task_key = str(day)
        if task_key in self.tasks:
            return self.tasks[task_key].get('category', 'DevOps')
        return 'DevOps'

    def get_related_challenges(self, day: int, category: str) -> List[int]:
        """Find related challenges from earlier days in the same category."""
        related = []
        for d in range(max(1, day - 20), day):
            if self.get_task_category(d) == category:
                related.append(d)
        return related[-3:]  # Return last 3 related

    def generate_task_specific_prereqs(self, day: int, category: str,
                                      challenge_title: str) -> str:
        """
        Generate task-specific prerequisites content.

        This preserves the KodeKloud platform emphasis while adding
        technology-specific requirements.
        """
        template = self.prereq_templates.get(category, self.prereq_templates["DevOps"])

        # Start with KodeKloud platform section (PRESERVE THIS - OUR UNIQUE VALUE)
        prereqs = """## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
"""

        # Add category-specific provisions from KodeKloud
        if category == "Docker":
            prereqs += "- ✅ Docker installed and configured\n"
        elif category == "Kubernetes":
            prereqs += "- ✅ Kubernetes cluster with kubectl configured\n"
        elif category == "Jenkins":
            prereqs += "- ✅ Jenkins server with admin access\n"
        elif category == "Ansible":
            prereqs += "- ✅ Ansible installed with target servers configured\n"
        elif category == "Terraform":
            prereqs += "- ✅ Terraform installed with cloud provider access\n"
        else:
            prereqs += "- ✅ Required servers and infrastructure\n"

        prereqs += """- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

"""

        # Add task-specific knowledge requirements
        prereqs += "**What You Need to Know:**\n"

        # Add CLI commands if applicable
        if template.get("commands"):
            commands = template["commands"][:5]  # Limit to 5 most important
            prereqs += f"- **Command Line Tools**: `{'`, `'.join(commands)}`\n"

        # Add concepts
        if template.get("concepts"):
            concepts = template["concepts"][:4]  # Top 4 concepts
            prereqs += "- **Key Concepts**:\n"
            for concept in concepts:
                prereqs += f"  - {concept}\n"

        # Add file format knowledge if applicable
        if template.get("file_formats"):
            formats = template["file_formats"]
            prereqs += f"- **File Formats**: {', '.join(formats)} syntax and structure\n"

        # Add special requirements
        if template.get("requires"):
            prereqs += f"- **Environment**: {template['requires']}\n"

        if template.get("credentials"):
            prereqs += f"- **Access**: {template['credentials']}\n"

        # Add related challenges if any
        related = self.get_related_challenges(day, category)
        if related:
            prereqs += "\n**Foundation from Earlier Challenges:**\n"
            for rel_day in related:
                if str(rel_day) in self.tasks:
                    rel_title = self.tasks[str(rel_day)].get('title', f'Day {rel_day}')
                    week = (rel_day - 1) // 7 + 1
                    prereqs += f"- Day {rel_day}: {rel_title} (recommended)\n"

        # Add required skills checklist
        prereqs += "\n**Required Skills:**\n"
        if template.get("skills"):
            skills = template["skills"][:5]  # Top 5 skills
            for skill in skills:
                prereqs += f"- ✅ {skill}\n"

        # Add the KodeKloud link at the end
        prereqs += """
---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)
"""

        return prereqs

    def find_prerequisite_section(self, content: str) -> tuple:
        """
        Find the prerequisites section in the markdown content.
        Returns (start_pos, end_pos) or (None, None) if not found.
        """
        # Match the prerequisites section
        pattern = r'## 📋 Prerequisites\n\n.*?(?=\n##|\Z)'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            return match.start(), match.end()
        return None, None

    def update_challenge_file(self, week: int, day: int, preview: bool = True) -> bool:
        """
        Update prerequisites in a single challenge file.

        Args:
            week: Week number (1-15)
            day: Day number (1-100)
            preview: If True, only show changes without applying

        Returns:
            True if update was successful, False otherwise
        """
        # Construct file path
        week_dir = self.challenges_dir / f"week-{week:02d}"
        day_file = week_dir / f"day-{day:02d}.md"

        if not day_file.exists():
            print(f"❌ File not found: {day_file}")
            return False

        # Read current content
        with open(day_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract category and title
        category = self.get_task_category(day)

        # Extract title from file
        title_match = re.search(r'^# Challenge \d+: (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else f"Day {day}"

        # Find current prerequisites section
        start_pos, end_pos = self.find_prerequisite_section(content)

        if start_pos is None:
            print(f"⚠️  Prerequisites section not found in day {day}")
            return False

        # Generate new prerequisites
        new_prereqs = self.generate_task_specific_prereqs(day, category, title)

        # Replace the section
        updated_content = content[:start_pos] + new_prereqs + content[end_pos:]

        if preview:
            print(f"\n{'='*80}")
            print(f"📄 Day {day:03d} - {title} ({category})")
            print(f"📁 {day_file}")
            print(f"{'='*80}")
            print("\n🔍 NEW PREREQUISITES SECTION:")
            print("-" * 80)
            print(new_prereqs)
            print("-" * 80)
            return True
        else:
            # Apply changes
            with open(day_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✅ Updated day {day:03d}: {title}")
            return True

    def update_all_challenges(self, preview: bool = True, auto_confirm: bool = False):
        """Update prerequisites in all 100 challenge files."""
        print(f"\n{'='*80}")
        print("🚀 Starting Prerequisites Update for 100 Days of DevOps")
        print(f"{'='*80}\n")

        if preview:
            print("🔍 PREVIEW MODE - No files will be modified")
            print("Run with --apply to actually update files\n")
        else:
            print("✏️  APPLY MODE - Files will be updated")
            if not auto_confirm:
                confirm = input("\n⚠️  Are you sure you want to update all files? (yes/no): ")
                if confirm.lower() != 'yes':
                    print("❌ Cancelled")
                    return
            else:
                print("✅ Auto-confirmed with --yes flag\n")

        stats = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'by_category': {}
        }

        # Process all 100 days
        for day in range(1, 101):
            week = (day - 1) // 7 + 1
            category = self.get_task_category(day)

            # Track by category
            if category not in stats['by_category']:
                stats['by_category'][category] = {'success': 0, 'failed': 0}

            stats['total'] += 1

            try:
                success = self.update_challenge_file(week, day, preview=preview)
                if success:
                    stats['success'] += 1
                    stats['by_category'][category]['success'] += 1
                else:
                    stats['failed'] += 1
                    stats['by_category'][category]['failed'] += 1
            except Exception as e:
                print(f"❌ Error processing day {day}: {e}")
                stats['failed'] += 1
                stats['by_category'][category]['failed'] += 1

        # Print summary
        print(f"\n{'='*80}")
        print("📊 UPDATE SUMMARY")
        print(f"{'='*80}")
        print(f"Total challenges: {stats['total']}")
        print(f"✅ Successful: {stats['success']}")
        print(f"❌ Failed: {stats['failed']}")

        print(f"\n📈 By Category:")
        for cat, counts in sorted(stats['by_category'].items()):
            total = counts['success'] + counts['failed']
            print(f"  {cat:15s}: {counts['success']:3d}/{total:3d} ✅")

        print(f"\n{'='*80}\n")

        if preview:
            print("💡 To apply these changes, run:")
            print("   python3 update_prerequisites.py --apply\n")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Update prerequisites in 100 Days of DevOps challenges",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Preview changes for all challenges
  python3 update_prerequisites.py --preview

  # Apply updates to all challenges
  python3 update_prerequisites.py --apply

  # Preview specific day
  python3 update_prerequisites.py --preview --day 50

  # Apply update to specific day
  python3 update_prerequisites.py --apply --day 50
        """
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--preview', action='store_true',
                      help='Preview changes without modifying files')
    group.add_argument('--apply', action='store_true',
                      help='Apply changes to files')

    parser.add_argument('--day', type=int, metavar='N',
                       help='Update specific day (1-100)')

    parser.add_argument('--base-dir', type=str,
                       help='Base directory of the repository (auto-detected by default)')

    parser.add_argument('--yes', action='store_true',
                       help='Auto-confirm updates without prompting')

    args = parser.parse_args()

    # Initialize updater
    updater = PrerequisiteUpdater(base_dir=args.base_dir)

    preview_mode = args.preview

    if args.day:
        # Update specific day
        if not 1 <= args.day <= 100:
            print(f"❌ Invalid day number: {args.day}. Must be between 1 and 100.")
            return

        week = (args.day - 1) // 7 + 1
        updater.update_challenge_file(week, args.day, preview=preview_mode)
    else:
        # Update all challenges
        updater.update_all_challenges(preview=preview_mode, auto_confirm=args.yes)


if __name__ == '__main__':
    main()
