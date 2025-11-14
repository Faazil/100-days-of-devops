# Challenge 6: Setup a Cron Job

## 📊 Metadata
- **Day**: 6
- **Week**: 1
- **Day in Week**: 6/7
- **Category**: Linux
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The `Nautilus` system admins team has prepared scripts to automate several day-to-day tasks. They want them to be deployed on all app servers in `Stratos DC` on a set schedule. Before that they need to test similar functionality with a sample cron job. Therefore, perform the steps below:

- Install `cronie` package on all `Nautilus` app servers and start `crond` service.
- Add a cron `*/5 * * * * echo hello > /tmp/cron_text` for `root` user.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `ssh`, `sudo`, `useradd`, `cat`, `grep`
- **Key Concepts**:
  - SSH remote access
  - User and group management
  - File permissions and ownership
  - Linux file system hierarchy

**Foundation from Earlier Challenges:**
- Day 2: Temporary User Setup with Expiry Date (recommended)
- Day 3: Secure SSH Root Access (recommended)
- Day 5: Install and Configuration Selinux (recommended)

**Required Skills:**
- ✅ Execute commands with sudo privileges
- ✅ Navigate Linux file system
- ✅ Manage users and groups
- ✅ Understand file permissions

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Login into each server using ssh (check [day01](./001.md))
2. Install `cronie` package into centos:

    ```sh
    sudo yum install cronie -y
    ```

3. Start crond service

    ```sh
    sudo systemctl enable crond
    sudo systemctl start crond
    ```

4. Create cron schedule:

    ```sh
    sudo crontab -e
    */5 * * * * echo hello > /tmp/cron_text
    ```

5. Verify crontab:

    ```sh
    sudo crontab -l
    ```

    and wait 5 minutes to check cron_text in /tmp/

## Automation Script

```sh
#!/bin/sh

# setup_cron_job.sh
# Script to setup cron job on CentOS for Nautilus app servers

set -e  # Exit on any error

echo "=== Setting up Cron Job on CentOS ==="

# Step 1: Install cronie package
echo "Installing cronie package..."
if ! rpm -q cronie &>/dev/null; then
    sudo yum install cronie -y
    echo "✓ cronie package installed successfully"
else
    echo "✓ cronie package already installed"
fi

# Step 2: Start and enable crond service
echo "Starting and enabling crond service..."
sudo systemctl start crond
sudo systemctl enable crond

# Verify service is running
if systemctl is-active --quiet crond; then
    echo "✓ crond service is running"
else
    echo "✗ Failed to start crond service"
    exit 1
fi

# Step 3: Add cron job for root user
echo "Adding cron job for root user..."

# Define the cron job
CRON_JOB="*/5 * * * * echo hello > /tmp/cron_text"

# Check if cron job already exists
if sudo crontab -l 2>/dev/null | grep -q "echo hello > /tmp/cron_text"; then
    echo "✓ Cron job already exists"
else
    # Add the cron job
    (sudo crontab -l 2>/dev/null || true; echo "$CRON_JOB") | sudo crontab -
    echo "✓ Cron job added successfully"
fi

# Step 4: Verify the setup
echo "Verifying cron job setup..."
echo "Current cron jobs for root user:"
sudo crontab -l

echo ""
echo "=== Setup Complete ==="
echo "The cron job will run every 5 minutes and write 'hello' to /tmp/cron_text"
echo "To monitor: sudo tail -f /var/log/cron"
echo "To check output: cat /tmp/cron_text (after 5+ minutes)"

# Optional: Show service status
echo ""
echo "Crond service status:"
sudo systemctl status crond --no-pager -l
```

## Good to Know?

### Cron Job Scheduling

- **Format**: `minute hour day month weekday command`
- **Ranges**: 0-59 (min), 0-23 (hour), 1-31 (day), 1-12 (month), 0-7 (weekday)
- **Special Characters**: `*` (any), `,` (list), `-` (range), `/` (step)
- **Examples**: `0 2 * * *` (daily 2 AM), `*/15 * * * *` (every 15 min)

### Cron Types

- **User Crontab**: `crontab -e` (per-user scheduling)
- **System Crontab**: `/etc/crontab` (system-wide)
- **Cron Directories**: `/etc/cron.d/`, `/etc/cron.daily/`

### Best Practices

- **Absolute Paths**: Always use full paths in cron jobs
- **Environment**: Set PATH, SHELL, MAILTO variables
- **Logging**: Redirect output to files for debugging
- **Testing**: Test commands manually before scheduling

### Troubleshooting

- **Logs**: Check `/var/log/cron` for execution history
- **Environment**: Cron runs with minimal environment
- **Permissions**: Ensure user has execute permissions

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
- Practical application of Linux skills
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

- **← Previous**: [Day 5 - Install and Configuration Selinux](./day-05.md)
- **Next →**: [Day 7 - Linux SSH Automation](../week-01/day-07.md)

### Similar Challenges (Linux)
- [Day 1 - Linux User Setup with Non-interactive Shell](../week-01/day-01.md)
- [Day 2 - Temporary User Setup with Expiry Date](../week-01/day-02.md)
- [Day 3 - Secure SSH Root Access](../week-01/day-03.md)

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

