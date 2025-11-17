# Day 6: Setup a Cron Job

## Task Overview

Set up automated task scheduling using cron. Configure recurring jobs for system maintenance and automation.

**Cron Configuration:**
- Install cron service
- Create crontab entries
- Define schedule patterns
- Verify job execution

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Install cron service using the package manager.

```sh
sudo yum install cronie -y
```

**Step 2:** Enable service to start automatically on boot.

```sh
sudo systemctl enable crond
    sudo systemctl start crond
```

**Step 3:** Open the crontab editor to add scheduled jobs.

```sh
sudo crontab -e
    */5 * * * * echo hello > /tmp/cron_text
```

**Step 4:** Add or verify the cron job schedule.

```sh
sudo crontab -l
```

**Step 5:** Check the service status to verify it's running.

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

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 5](day-05.md) | [Day 7 →](day-07.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
