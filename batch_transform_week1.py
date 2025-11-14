#!/usr/bin/env python3
"""
Batch transform Week 1 tasks (Days 2-7) to new format.
Day 1 is already done manually as the template.
"""

from pathlib import Path

# Define the base directory
base_dir = Path("/Users/nimesha/Dev/kk-projects/100-days-of-devops")
week1_dir = base_dir / "challenges" / "week-01"

# Task definitions with solutions
tasks = {
    2: {
        "title": "Temporary User Setup with Expiry Date",
        "scenario": """As part of the temporary assignment to the Nautilus project, a developer named yousuf requires access for a limited duration. To ensure smooth access management, a temporary user account with an expiry date is needed.

> Create a user named `yousuf` on `App Server 1` in Stratos Datacenter. Set the expiry date to `2024-01-28`, ensuring the user is created in lowercase as per standard protocol.""",
        "understanding": """**What's a Temporary User Account?**

A temporary user account is one that automatically expires after a set date. This is perfect for contractors, temporary employees, or time-limited project access.

**Common Use Cases:**
- Contractor or vendor access (limited duration)
- Temporary project team members
- Intern or trainee accounts
- Testing or demo accounts

**Why It Matters:** Reduces security risk by ensuring temporary access doesn't become permanent. No manual cleanup needed - the account auto-expires.""",
        "solution_steps": [
            {
                "title": "Connect to Your Server",
                "desc": "SSH into the target app server:",
                "command": "ssh <your-username>@<server-name>",
                "example": "ssh tony@stapp01",
                "note": "Enter your password when prompted."
            },
            {
                "title": "Create User with Expiry Date",
                "desc": "Create the user account with an expiration date:",
                "command": "sudo useradd -m -e 2024-01-28 yousuf",
                "example": "sudo useradd -m -e 2024-01-28 yousuf",
                "breakdown": [
                    "`sudo` - Run with administrator privileges",
                    "`useradd` - Command to create new user",
                    "`-m` - Create a home directory",
                    "`-e 2024-01-28` - Set account expiry date (YYYY-MM-DD format)",
                    "`yousuf` - Username to create"
                ],
                "note": "The account will be automatically disabled after the specified date."
            },
            {
                "title": "Verify User Creation",
                "desc": "Confirm the user was created successfully:",
                "command": "cat /etc/passwd | grep yousuf",
                "example": "cat /etc/passwd | grep yousuf",
                "expected": "yousuf:x:1002:1002::/home/yousuf:/bin/bash",
                "note": "You should see the user entry in the passwd file."
            },
            {
                "title": "Check Expiry Date",
                "desc": "Verify the expiration date was set correctly:",
                "command": "sudo chage -l yousuf",
                "example": "sudo chage -l yousuf",
                "expected": "Account expires: Jan 28, 2024",
                "note": "This shows all account aging information including expiry."
            }
        ],
        "verification": [
            "User appears in `/etc/passwd`",
            "`chage -l` shows correct expiry date",
            "Can switch to user before expiry: `sudo su - yousuf`",
            "KodeKloud validation passes"
        ],
        "troubleshooting": [
            ("Wrong date format", "Use YYYY-MM-DD format (e.g., 2024-01-28)"),
            ("User already exists", "Delete existing: `sudo userdel -r yousuf`"),
            ("Permission denied", "Make sure you're using `sudo`")
        ],
        "good_to_know": """**Checking Expiry Status:**
```bash
# View account expiry details
sudo chage -l <username>

# Change expiry date for existing user
sudo usermod -e 2024-12-31 <username>

# Remove expiry (set to never)
sudo usermod -e "" <username>
```

**Real-World Usage:**
Companies often use temporary accounts for:
- External consultants (30-90 day projects)
- Seasonal workers
- Trial or evaluation periods
- Security compliance (automatic access revocation)"""
    },
    # Day 3: SSH Root Access
    3: {
        "title": "Secure SSH Root Access",
        "scenario": "Disable all app server SSH root access.",
        "understanding": """**Why Disable Root SSH Login?**

Allowing direct root login via SSH is a major security risk. If attackers gain root access, they have complete control of your system.

**Security Benefits:**
- Forces use of regular accounts first
- Creates audit trail (who did what)
- Enables sudo logging
- Prevents brute-force attacks on root account

**Standard Practice:** Industry best practice is to NEVER allow direct root SSH login. Always use a regular account + sudo.""",
        "solution_steps": [
            {
                "title": "Connect to App Server",
                "desc": "SSH to each app server that needs configuration:",
                "command": "ssh <your-username>@<server-name>",
                "example": "ssh tony@stapp01",
                "note": "Repeat for all app servers in your environment."
            },
            {
                "title": "Modify SSH Configuration",
                "desc": "Update the SSH daemon configuration to disable root login:",
                "command": "sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config",
                "example": "sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config",
                "breakdown": [
                    "`sudo` - Run with admin privileges",
                    "`sed -i` - Edit file in-place",
                    "`'s/PermitRootLogin yes/PermitRootLogin no/g'` - Find and replace",
                    "`/etc/ssh/sshd_config` - SSH server configuration file"
                ],
                "note": "This changes the setting in the SSH config file."
            },
            {
                "title": "Restart SSH Service",
                "desc": "Restart the SSH daemon to apply changes:",
                "command": "sudo systemctl restart sshd",
                "example": "sudo systemctl restart sshd",
                "note": "Your current SSH session will stay connected."
            },
            {
                "title": "Verify Configuration",
                "desc": "Confirm root login is disabled:",
                "command": "grep PermitRootLogin /etc/ssh/sshd_config",
                "example": "grep PermitRootLogin /etc/ssh/sshd_config",
                "expected": "PermitRootLogin no",
                "note": "Should show 'no' instead of 'yes'."
            }
        ],
        "verification": [
            "SSH config shows `PermitRootLogin no`",
            "SSH service restarted successfully",
            "Attempting `ssh root@server` from another machine fails",
            "Can still connect as regular user"
        ],
        "troubleshooting": [
            ("Still can login as root", "Make sure you restarted sshd service"),
            ("Configuration not changed", "Check file permissions on /etc/ssh/sshd_config"),
            ("SSH service won't restart", "Check syntax: `sudo sshd -t`")
        ],
        "good_to_know": """**Manual Configuration Method:**
```bash
# Edit configuration file manually
sudo vi /etc/ssh/sshd_config

# Find this line:
#PermitRootLogin yes

# Change to:
PermitRootLogin no

# Test configuration before restarting
sudo sshd -t

# If no errors, restart
sudo systemctl restart sshd
```

**Additional Security Hardening:**
- Disable password authentication (use keys only)
- Change default SSH port from 22
- Use fail2ban to block brute force attempts
- Enable two-factor authentication"""
    }
}

# Add Days 4-7 here (truncated for brevity in this example)
# Would continue with full definitions...

print("Task definitions prepared. Run write operations next...")
print(f"Tasks ready: {list(tasks.keys())}")
