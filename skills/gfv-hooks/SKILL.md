---
name: gfv-hooks
short_description: "Configure lifecycle hooks for your AI agent"
  Use when: The executive requests execution of this domain.
  Skip when: The task is outside the scope of this module.
description: >
  Event-driven lifecycle automation for AI-native companies. Provides a complete hooks
  infrastructure with session persistence, decision audit trails, safety gates, and
  notification systems. Use when onboarding a new portfolio company, setting up agent
  governance, or implementing quality controls on AI operations. Triggers on "set up hooks",
  "configure governance", "audit trail", "session persistence", or "agent safety".
---

# GFV Hooks Infrastructure

**Adapted from:** claude-code-best-practice hooks system
**Purpose:** Give every portfolio company event-driven AI governance out of the box.

---


## Quick Start
Just say any of these:
- "Configure my session start/stop hooks"
- "Set up pre-send review for all messages"
- "How do I customize my AI's lifecycle hooks?"


## What Are Hooks?

Hooks are lifecycle events fired by your AI coding agent at specific moments during execution.
They let you:
- **Log** every action for compliance and audit
- **Block** dangerous operations before they execute
- **Persist** session context so nothing is lost
- **Notify** the team when important events occur
- **Gate** quality by requiring validation before proceeding

---

## Architecture

```
┌──────────────────────────────────────────┐
│  AI Agent Session                        │
│                                          │
│  ┌─────────┐    ┌─────────────────────┐  │
│  │ Action  │───▶│ Hook Event Fired    │  │
│  └─────────┘    └──────────┬──────────┘  │
│                            │             │
│                   ┌────────▼────────┐    │
│                   │ hooks_handler.py │    │
│                   └────────┬────────┘    │
│                            │             │
│              ┌─────────────┼─────────────┤
│              │             │             │
│        ┌─────▼───┐  ┌─────▼───┐  ┌──────▼──────┐
│        │  Log    │  │ Decide  │  │  Notify     │
│        │ (JSONL) │  │ (Gate)  │  │ (Alert)     │
│        └─────────┘  └─────────┘  └─────────────┘
└──────────────────────────────────────────┘
```

---

## Hook Events Reference (27 Events)

### Session Lifecycle

| Event | Fires When | CEO Use Case |
|-------|-----------|-------------|
| `SessionStart` | Agent session begins | Auto-load company context, check stale data |
| `SessionEnd` | Agent session ends | Persist session summary, write to decision log |
| `Setup` | First-time agent initialization | Run onboarding checks |
| `PreCompact` | Before context compaction | Save critical context before compression |
| `PostCompact` | After context compaction | Verify nothing important was lost |

### Tool Execution

| Event | Fires When | CEO Use Case |
|-------|-----------|-------------|
| `PreToolUse` | Before any tool executes | Block destructive ops, require approval for sends |
| `PostToolUse` | After any tool completes | Log action to audit trail, update decision memory |
| `PostToolUseFailure` | When a tool fails | Alert on API failures, trigger retry logic |
| `PermissionRequest` | Agent asks for permission | Auto-approve safe ops, escalate dangerous ones |
| `PermissionDenied` | User denies a tool | Log denied actions for pattern analysis |

### Agent Orchestration

| Event | Fires When | CEO Use Case |
|-------|-----------|-------------|
| `SubagentStart` | Sub-agent spawns | Track which advisors are consulted |
| `SubagentStop` | Sub-agent completes | Collect sub-agent outputs for synthesis |
| `TeammateIdle` | Background agent goes idle | Reassign or wake idle agents |
| `TaskCreated` | New background task created | Log task creation for tracking |
| `TaskCompleted` | Background task finishes | Collect results, update dashboard |

### User Interaction

| Event | Fires When | CEO Use Case |
|-------|-----------|-------------|
| `UserPromptSubmit` | User sends a message | Log all CEO inputs for context reconstruction |
| `Notification` | System notification fires | Route to Slack/email based on severity |
| `Stop` | Agent stops responding | Trigger session save, alert if unexpected |
| `Elicitation` | MCP server requests input | Auto-respond in headless mode |
| `ElicitationResult` | User responds to MCP | Log MCP interactions |

### Configuration

| Event | Fires When | CEO Use Case |
|-------|-----------|-------------|
| `ConfigChange` | Settings modified | Detect unauthorized config changes |
| `FileChanged` | Watched file modified | Alert on `.env` or credential changes |
| `InstructionsLoaded` | CLAUDE.md loaded | Verify correct instructions loaded |
| `CwdChanged` | Working directory changes | Track context switches |
| `WorktreeCreate` | Git worktree created | Log parallel execution branches |
| `WorktreeRemove` | Git worktree removed | Clean up resources |
| `StopFailure` | Agent fails to stop | Force-terminate, alert team |

---

## Implementation

### File Structure

```
.claude/
├── hooks/
│   ├── scripts/
│   │   └── hooks_handler.py     # Main event handler
│   ├── config/
│   │   ├── hooks-config.json    # Team config (committed)
│   │   └── hooks-config.local.json  # Personal overrides (git-ignored)
│   └── logs/
│       └── hooks-log.jsonl      # Audit trail (git-ignored)
└── settings.json                # Hook registration
```

### hooks_handler.py — Core Event Handler

```python
#!/usr/bin/env python3
"""
GFV Hooks Handler — Event-driven lifecycle automation for AI-native companies.
Zero dependencies. stdlib only. Runs on any CEO's machine.
"""

import sys
import json
import os
import subprocess
from pathlib import Path
from datetime import datetime, timezone


# ── Configuration ──────────────────────────────────────────────

HOOKS_DIR = Path(__file__).parent.parent  # .claude/hooks/
CONFIG_DIR = HOOKS_DIR / "config"
LOGS_DIR = HOOKS_DIR / "logs"

# Safety gates — tools that require explicit approval
GATED_TOOLS = {
    "send_email",
    "whatsapp_send",
    "slack_post",
    "git_push",
    "deploy",
    "delete",
    "drop",
    "rm",
}

# Events that trigger session persistence
PERSIST_EVENTS = {"SessionEnd", "Stop", "PreCompact"}

# Events that trigger notifications
NOTIFY_EVENTS = {"StopFailure", "PostToolUseFailure", "PermissionDenied"}


# ── Config Loading ─────────────────────────────────────────────

def load_config():
    """Load config with local override cascade."""
    config = {}

    default_path = CONFIG_DIR / "hooks-config.json"
    local_path = CONFIG_DIR / "hooks-config.local.json"

    if default_path.exists():
        with open(default_path, "r") as f:
            config = json.load(f)

    if local_path.exists():
        with open(local_path, "r") as f:
            local = json.load(f)
            config.update(local)  # Local overrides default

    return config


def is_hook_disabled(event_name, config):
    """Check if a specific hook is disabled."""
    key = f"disable{event_name}Hook"
    return config.get(key, False)


# ── Logging ────────────────────────────────────────────────────

def log_event(hook_data, action_taken=None):
    """Append event to JSONL audit log."""
    config = load_config()
    if config.get("disableLogging", False):
        return

    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": hook_data.get("hook_event_name", "unknown"),
        "tool": hook_data.get("tool_name", None),
        "action": action_taken,
    }

    # Strip large fields to keep log compact
    for key in ("transcript_path", "cwd"):
        hook_data.pop(key, None)

    entry["data"] = hook_data

    log_path = LOGS_DIR / "hooks-log.jsonl"
    with open(log_path, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ── Safety Gates ───────────────────────────────────────────────

def check_safety_gate(hook_data):
    """
    For PreToolUse events, check if the tool requires approval.
    Returns a decision dict if the tool should be blocked, None otherwise.
    """
    tool_name = hook_data.get("tool_name", "")
    tool_input = hook_data.get("tool_input", {})

    # Check direct tool name match
    if tool_name.lower() in GATED_TOOLS:
        return {
            "hookSpecificOutput": {
                "permissionDecision": "ask",
            }
        }

    # Check bash commands for dangerous patterns
    if tool_name == "Bash":
        command = tool_input.get("command", "")
        dangerous_patterns = [
            "rm -rf",
            "git reset --hard",
            "git push --force",
            "DROP TABLE",
            "DELETE FROM",
            "curl.*POST",  # Outbound HTTP posts
        ]
        for pattern in dangerous_patterns:
            if pattern.lower() in command.lower():
                return {
                    "hookSpecificOutput": {
                        "permissionDecision": "ask",
                    }
                }

    return None


# ── Session Persistence ───────────────────────────────────────

def persist_session(hook_data):
    """
    On session end, save a summary for cross-session continuity.
    This integrates with the decision-logger skill.
    """
    session_dir = Path.home() / ".gfv" / "sessions"
    session_dir.mkdir(parents=True, exist_ok=True)

    summary = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": hook_data.get("hook_event_name"),
        "session_id": hook_data.get("session_id", "unknown"),
    }

    summary_path = session_dir / "session-log.jsonl"
    with open(summary_path, "a") as f:
        f.write(json.dumps(summary, ensure_ascii=False) + "\n")


# ── Notifications ─────────────────────────────────────────────

def send_notification(hook_data):
    """
    Send a notification for critical events.
    Uses macOS native notifications. Extend for Slack/email as needed.
    """
    event = hook_data.get("hook_event_name", "Unknown")
    tool = hook_data.get("tool_name", "")
    message = f"GFV Agent Alert: {event}"
    if tool:
        message += f" ({tool})"

    # macOS notification
    try:
        subprocess.run(
            [
                "osascript", "-e",
                f'display notification "{message}" with title "GFV Agent"'
            ],
            capture_output=True,
            timeout=5,
        )
    except Exception:
        pass  # Fail silently — notifications are nice-to-have


# ── Main Handler ──────────────────────────────────────────────

def main():
    """
    Main hook handler. Reads event from stdin, routes to appropriate handler.
    Always exits 0 to never block the agent.
    """
    try:
        stdin_content = sys.stdin.read().strip()
        if not stdin_content:
            sys.exit(0)

        hook_data = json.loads(stdin_content)
        event_name = hook_data.get("hook_event_name", "")
        config = load_config()

        # Check if this hook is disabled
        if is_hook_disabled(event_name, config):
            sys.exit(0)

        # Always log (unless logging disabled)
        log_event(hook_data)

        # Safety gates for PreToolUse
        if event_name == "PreToolUse":
            decision = check_safety_gate(hook_data)
            if decision:
                log_event(hook_data, action_taken="safety_gate_triggered")
                print(json.dumps(decision))
                sys.exit(0)

        # Session persistence
        if event_name in PERSIST_EVENTS:
            persist_session(hook_data)

        # Notifications for critical events
        if event_name in NOTIFY_EVENTS:
            send_notification(hook_data)

        sys.exit(0)

    except json.JSONDecodeError:
        sys.exit(0)
    except Exception:
        sys.exit(0)  # Never block the agent


if __name__ == "__main__":
    main()
```

### hooks-config.json — Team Configuration

```json
{
  "disableSessionStartHook": false,
  "disableSessionEndHook": false,
  "disablePreToolUseHook": false,
  "disablePostToolUseHook": false,
  "disablePostToolUseFailureHook": false,
  "disableStopHook": false,
  "disableSubagentStartHook": false,
  "disableSubagentStopHook": false,
  "disablePreCompactHook": false,
  "disablePostCompactHook": false,
  "disableNotificationHook": false,
  "disablePermissionRequestHook": false,
  "disablePermissionDeniedHook": false,
  "disableConfigChangeHook": false,
  "disableFileChangedHook": false,
  "disableLogging": false,
  "safetyGatesEnabled": true,
  "notificationsEnabled": true,
  "sessionPersistenceEnabled": true
}
```

### settings.json — Hook Registration

Register hooks in `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": ".*",
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/hooks/task_manager.py",
        "timeout": 5000
      }]
    }],
    "PostToolUse": [{
      "matcher": ".*",
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/hooks/task_manager.py",
        "timeout": 5000,
        "async": true
      }]
    }],
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/hooks/task_manager.py",
        "timeout": 5000,
        "async": true,
        "once": true
      }]
    }],
    "SessionEnd": [{
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/hooks/task_manager.py",
        "timeout": 5000,
        "async": true,
        "once": true
      }]
    }],
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/hooks/task_manager.py",
        "timeout": 5000,
        "async": true
      }]
    }],
    "PreCompact": [{
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/hooks/task_manager.py",
        "timeout": 5000,
        "async": true,
        "once": true
      }]
    }],
    "FileChanged": [{
      "matcher": ".envrc|.env|.env.local",
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/hooks/task_manager.py",
        "timeout": 5000,
        "async": true
      }]
    }]
  }
}
```

---

## Onboarding a Portfolio Company

### Step 1: Copy hooks infrastructure

```bash
mkdir -p .claude/hooks/{scripts,config,logs}
cp hooks_handler.py .claude/hooks/scripts/
cp hooks-config.json .claude/hooks/config/
echo "hooks-log.jsonl" >> .claude/hooks/logs/.gitignore
echo "hooks-config.local.json" >> .claude/hooks/config/.gitignore
```

### Step 2: Register hooks in settings.json

Copy the `hooks` block from the settings.json template above into the company's `.claude/settings.json`.

### Step 3: Customize safety gates

Edit `GATED_TOOLS` in `hooks_handler.py` to match the company's risk profile:

| Company Stage | Safety Gates |
|---------------|-------------|
| Pre-seed | Minimal — `git push --force`, `rm -rf` only |
| Seed | Add `deploy`, `send_email` |
| Series A+ | Add financial tools, API calls, database mutations |
| Enterprise | Full gate suite with approval workflows |

### Step 4: Set up local overrides

Each team member creates `.claude/hooks/config/hooks-config.local.json`:

```json
{
  "disableLogging": false,
  "notificationsEnabled": true,
  "safetyGatesEnabled": true
}
```

---

## Extending the System

### Adding Custom Hooks

To add company-specific behavior, extend `main()` in `hooks_handler.py`:

```python
# Example: Auto-create Linear issue on tool failure
if event_name == "PostToolUseFailure":
    tool = hook_data.get("tool_name", "")
    error = hook_data.get("error", "")
    # Create Linear issue via API
    create_linear_issue(
        title=f"Agent tool failure: {tool}",
        description=f"Error: {error}",
        team="engineering",
        priority=2
    )
```

### Adding Slack Notifications

```python
def send_slack_alert(message, channel="#ops-alerts"):
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        return
    subprocess.run(
        ["curl", "-X", "POST", "-H", "Content-type: application/json",
         "-d", json.dumps({"text": message, "channel": channel}),
         webhook_url],
        capture_output=True, timeout=10
    )
```

---

## Security Considerations

1. **Logs are git-ignored** — JSONL audit files never enter version control
2. **Local overrides are git-ignored** — Personal preferences stay local
3. **Safety gates are non-blocking** — They trigger `ask` mode, not `deny`
4. **No secrets in config** — All credentials come from environment or keychain
5. **Fail-open design** — Hooks always exit 0; never block the agent on error

## Live Integration Hooks

| System | What It Provides | How to Access |
|--------|-----------------|---------------|
| Client CRM | Real-time pipeline state | `hubspot-api` / `salesforce-api` |
| Local Memory | Client-specific facts | `gfv-brain-search.py` |

> **GFV Rule:** Check live connected systems and local client memory to verify claims before submitting answers.

## Proactive Triggers

Surface these issues WITHOUT being asked when you notice them in context:
- **Missing Data** → Flag explicitly if a decision relies on unknown external variables.
- **Scope Creep** → Alert if the requested operation spans beyond immediate context goals.
- **Executive Bottlenecks** → Warn if the action plan relies entirely on unassigned human approval gates.
- **Financial Risk** → Call out actions that may trigger unexpected OPEX burn (e.g. infinite LLM agent loops).

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| Process Map | A mermaid.js chronological diagram |
| Executive Decision | BOTTOM LINE FIRST layout with options + trade-offs |
| Data Audit | A structured table grouping issues by severity |
| Code Execution | Isolated, copy-ready code blocks + terminal commands |

## Confidence Tagging

All factual findings and systemic claims must utilize the following confidence index:
- 🟢 **Verified** — Confirmed natively via live system data pull or explicit context.
- 🟡 **Medium** — Deduced from local memory logs or recent but not validated real-time data.
- 🔴 **Assumed** — No source available, utilizing best-judgment baseline.

## 
## When to Trigger
- When requested by the Executive.
- When the task aligns with the core competency of this skill.

## When to Skip
- When the data or answers already exist in the PIL memory bus.
- When the task requires physical intervention or manual approval before drafting.

## GFV Integration
**Credentials** — Never use `.env` files. All secrets live in macOS Keychain:
`security find-generic-password -s "<service>" -a "<account>" -w`
**Data Sources** — Before querying external APIs, check PIL first (`search_pil`, `gfv_memory.db`).
**Output** — Save results to `~/Documents/Code/gfv-brain/`. Never send external messages without the Executive`s explicit "send it" approval.

## Anti-Patterns
- **Summarizing instead of resolving**: Do not just summarize what needs to be done. Do the work.
- **Bypassing the Gate**: Do not execute risky actions without human-in-the-loop validation.

## References
- **GFV Standard**: GetFresh Ventures Growth by Design CEO AI Kit Architecture

<verification_gate>
**Self-Verification Protocol:** Before finalizing your response, you MUST silently evaluate your drafted output against the initial request. Have you provided concrete Action Items with ownership? Did you use the Bottom Line First formatting? Have you applied Confidence Tags to your claims? If not, rewrite the response before submitting.

## After This Skill
💡 Suggest these next:
- "Try `create-skill` — Create a new skill from scratch"
- "Try `scheduling-infra` — Set up cron jobs and background automation"
- "Try `project-release` — Governed release workflow with version bumps"

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
