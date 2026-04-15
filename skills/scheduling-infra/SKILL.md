---
name: scheduling-infra
description: "Set up scheduled tasks, cron jobs, and background automation on macOS and Linux. Use when the user needs something to run on a schedule — backups, reports, data syncs, health checks."
short_description: "Set up cron jobs and background automation"
---

# Scheduling Infrastructure

Set up reliable, persistent scheduled tasks. Every scheduled job must have health monitoring — a silent failure is worse than no automation.


## Quick Start
Just say any of these:
- "Set up my background automation infrastructure"
- "Configure cron jobs for [tasks]"
- "Build a task scheduling system"


## When to Use

- "Run this script every morning at 8am"
- "Set up a daily backup"
- "Schedule a weekly report"
- "Automate this data sync"
- Any recurring task that shouldn't require manual triggering

## macOS: launchd (Preferred)

macOS uses `launchd` instead of cron for persistent scheduling. Plist files go in `~/Library/LaunchAgents/`.

### Create a Scheduled Job

```bash
# Create the plist
cat > ~/Library/LaunchAgents/com.gfv.daily-sync.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.gfv.daily-sync</string>

    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/USERNAME/scripts/daily_sync.py</string>
    </array>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>8</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>/tmp/daily-sync.stdout.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/daily-sync.stderr.log</string>

    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
EOF

# Load it
launchctl load ~/Library/LaunchAgents/com.gfv.daily-sync.plist

# Verify it's loaded
launchctl list | grep gfv
```

### Common Schedules

| Schedule | launchd `StartCalendarInterval` |
|----------|-------------------------------|
| Every day at 8am | `<key>Hour</key><integer>8</integer><key>Minute</key><integer>0</integer>` |
| Every Monday at 9am | Add `<key>Weekday</key><integer>1</integer>` (0=Sunday) |
| Every hour | `<key>Minute</key><integer>0</integer>` |
| Every 5 minutes | Use `StartInterval` instead: `<key>StartInterval</key><integer>300</integer>` |

### Manage Jobs

```bash
# List active jobs
launchctl list | grep gfv

# Stop a job
launchctl unload ~/Library/LaunchAgents/com.gfv.daily-sync.plist

# Remove a job
launchctl unload ~/Library/LaunchAgents/com.gfv.daily-sync.plist
rm ~/Library/LaunchAgents/com.gfv.daily-sync.plist

# Run immediately (test)
launchctl start com.gfv.daily-sync

# Check logs
tail -20 /tmp/daily-sync.stderr.log
```

## Linux: systemd Timers (Preferred over cron)

### Create a Timer + Service Pair

```bash
# Service unit (what to run)
sudo cat > /etc/systemd/user/daily-sync.service << 'EOF'
[Unit]
Description=Daily data sync

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /home/user/scripts/daily_sync.py
StandardOutput=journal
StandardError=journal
EOF

# Timer unit (when to run)
sudo cat > /etc/systemd/user/daily-sync.timer << 'EOF'
[Unit]
Description=Run daily sync at 8am

[Timer]
OnCalendar=*-*-* 08:00:00
Persistent=true

[Install]
WantedBy=timers.target
EOF

# Enable and start
systemctl --user enable --now daily-sync.timer

# Verify
systemctl --user list-timers
```

## Cron (Universal Fallback)

```bash
# Edit crontab
crontab -e

# Format: minute hour day month weekday command
# ┌───────────── minute (0-59)
# │ ┌───────────── hour (0-23)
# │ │ ┌───────────── day of month (1-31)
# │ │ │ ┌───────────── month (1-12)
# │ │ │ │ ┌───────────── day of week (0-6, Sunday=0)
# │ │ │ │ │
# * * * * * command

# Examples:
0 8 * * *     /usr/bin/python3 ~/scripts/daily_sync.py >> /tmp/sync.log 2>&1
0 9 * * 1     /usr/bin/python3 ~/scripts/weekly_report.py >> /tmp/report.log 2>&1
*/5 * * * *   /usr/bin/python3 ~/scripts/health_check.py >> /tmp/health.log 2>&1
0 0 1 * *     /usr/bin/python3 ~/scripts/monthly_backup.py >> /tmp/backup.log 2>&1
```

## Health Monitoring (MANDATORY)

Every scheduled job MUST have health checks:

```python
#!/usr/bin/env python3
"""Wrapper for any scheduled job with health logging."""
import subprocess, datetime, json, sys

JOB_NAME = "daily-sync"
LOG_FILE = f"/tmp/{JOB_NAME}-health.jsonl"

start = datetime.datetime.now()
try:
    result = subprocess.run(
        [sys.executable, "/path/to/actual/script.py"],
        capture_output=True, text=True, timeout=300
    )
    status = "success" if result.returncode == 0 else "failure"
    error = result.stderr[:500] if result.returncode != 0 else None
except subprocess.TimeoutExpired:
    status = "timeout"
    error = "Exceeded 300s timeout"
except Exception as e:
    status = "crash"
    error = str(e)

duration = (datetime.datetime.now() - start).total_seconds()
log_entry = json.dumps({
    "job": JOB_NAME,
    "timestamp": start.isoformat(),
    "status": status,
    "duration_seconds": round(duration, 2),
    "error": error
})

with open(LOG_FILE, "a") as f:
    f.write(log_entry + "\n")

# Exit with same code as the actual job
sys.exit(0 if status == "success" else 1)
```

```bash
# Quick health check — last 5 runs
tail -5 /tmp/daily-sync-health.jsonl | python3 -m json.tool
```

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Job doesn't run | Not loaded/enabled | `launchctl list \| grep name` or `systemctl --user list-timers` |
| Runs but fails silently | No log output | Add `StandardOutPath`/`StandardErrorPath` to plist |
| PATH issues | Cron has minimal PATH | Use absolute paths for everything: `/usr/bin/python3`, not `python3` |
| Permission denied | Script not executable | `chmod +x script.py` |
| macOS kills the job | App Nap | Add `ProcessType: Interactive` to plist |

## Integration

- Used by `/chief-of-staff` to set up morning sweeps
- Used by `/cron-scheduler` for task scheduling
- Health logs feed into `/verify-execution` for monitoring


## After This Skill
💡 Suggest these next:
- "Try `cron-scheduler` — Set up recurring background tasks"
- "Try `automation-recommender` — Find automation opportunities in your workflows"
- "Try `agent-orchestrator` — Coordinate multi-agent task pipelines"
