---
name: cron-scheduler
description: Safely configure recurring local or cloud background tasks with GFV logging loops attached.
short_description: "Set up recurring background tasks"
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: Infrastructure
---

# /cron-scheduler

**Usage**: Utilize this skill when the CEO wants to automate a recurring execution loop (e.g., pulling a pipeline report every Friday, syncing memory daily).


## Quick Start
Just say any of these:
- "Set up a daily report at 8am"
- "Schedule a weekly database backup"
- "Create a recurring task that runs every hour"


## ⚠️ The Silent Failure Protocol

Unmonitored scheduled background jobs inevitably fail without notification. To comply with the GFV Execution Paradigm, the agent MUST construct crons using a **Verification Loop**, meaning the cron task must pipe its final status (Success/Fail) directly into `~/gtm-brain/logs` or send a Slack/Email output.

## Phase 1: Environment Definition
- Verify what OS the user is running (Mac/Linux `crontab`, Windows Task Scheduler).
- Evaluate if the script to be scheduled requires isolated dependencies (e.g., Python venv paths, active API environment variables).
- Formulate the absolute paths for the command logic.

## Phase 2: Generation of the Shell Output
- Generate a wrapping shell script that acts as the entry point. The script MUST contain a `try/catch` equivalent.
- `echo` the exact cron format expression out to the CEO.
- Include instructions on how the CEO can use `crontab -e` to install it, or offer to use the Terminal MCP to inject it directly if running locally.

## Phase 3: The Verification Pipeline
- Every scheduled task built automatically generates an artifact logging format. Upon running, if it fails, it must write a status text file that the `chief-of-staff` heartbeat capability can pick up the next morning.

## Phase 4: Silent Failure Diagnostics (Enhanced v1.1 — Cron Debugger Method)

When a cron job stops producing output, diagnose in this exact order:

### The 6-Layer Debug Checklist
1. **Crontab Registration** — Is the job actually in `crontab -l`? (Most common failure: it was never added.)
2. **Dispatcher Sync** — If using a dispatcher/scheduler, is it registered there AND in crontab?
3. **Python/Script Path** — Is the interpreter path absolute? Does it match the venv? Run `which python3` inside the cron environment.
4. **Missing Packages** — Does the script import packages only installed in a venv that cron doesn't activate?
5. **.env Loading** — Cron jobs do NOT inherit shell environment. Is `.env` loaded explicitly in the wrapper script?
6. **Stale Cache** — Python bytecode cache (`__pycache__`) can mask code changes. Clear and re-run.

### Diagnostic Output
```
[CRON DIAGNOSTIC: job_name]
Layer 1 - Crontab: ✅ Registered | ❌ Missing
Layer 2 - Dispatcher: ✅ Synced | ❌ Out of sync | ⚠️ No dispatcher
Layer 3 - Script Path: ✅ Absolute | ❌ Relative path
Layer 4 - Dependencies: ✅ All found | ❌ Missing: [list]
Layer 5 - Environment: ✅ .env loaded | ❌ Missing vars: [list]
Layer 6 - Cache: ✅ Clean | ❌ Stale bytecode detected
```

## Phase 5: Safe Registration Protocol (Enhanced v1.1 — Add Cron Job Method)

Before adding any new cron job, complete this checklist:

1. **Script Verification** — Run the script manually once. Confirm it produces expected output.
2. **Time Conflict Check** — Query existing crontab for jobs running at the same time. Avoid resource contention.
3. **Dispatcher Registration** — If a dispatcher exists, register there FIRST, then crontab.
4. **Dry Run** — Add the cron entry with output redirected to a test log. Wait for one cycle. Verify the log.
5. **Monitoring Hook** — Ensure the `chief-of-staff` heartbeat can detect if this job fails silently.

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

## <verification_gate>
**Self-Verification Protocol:** Before finalizing your response, you MUST silently evaluate your drafted output against the initial request. Have you provided concrete Action Items with ownership? Did you use the Bottom Line First formatting? Have you applied Confidence Tags to your claims? If not, rewrite the response before submitting.

## After This Skill
💡 Suggest these next:
- "Try `scheduling-infra` — Set up cron jobs and background automation"
- "Try `automation-recommender` — Find automation opportunities in your workflows"
- "Try `gfv-hooks` — Configure lifecycle hooks for your AI agent"
