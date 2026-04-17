---
name: weekly-ceo-brief
description: "Synthesize the week into a CEO-level summary — pipeline movement, key meetings, commitments, wins, risks, and priorities for next week. Resolves open items during synthesis, doesn't just report them. Use when the CEO asks 'how was the week,' 'weekly update,' 'board summary,' or on Friday afternoon."
short_description: "Synthesize your week into a CEO summary"
metadata:
  version: 2.0.0
  category: daily-operations
  origin: GFV v1 + clawchief priority map + autoagent simplicity criterion
  triggers:
    - weekly brief
    - how was the week
    - weekly update
    - board summary
    - end of week
---

# Weekly CEO Brief

Your week distilled into what actually matters — with open items resolved, not just listed.


## Quick Start
Just say any of these:
- "Write my weekly CEO brief"
- "Summarize this week — what moved, what's stuck, what's next?"
- "Build my Monday morning briefing"

## When to Activate

- Friday afternoon / Sunday evening
- Before weekly leadership standup
- For investor or board reporting
- Any time the CEO asks "how was the week"

## The Resolve-First Rule

**Don't just report the week — close loops during the synthesis.**

| Bad Brief | Good Brief |
|-----------|------------|
| "Deal X had no activity" | "Deal X stalled 12 days. Follow-up drafted and task created (GFV-XXX). Recommend sending Monday." |
| "Meeting with Acme happened" | "Met Acme. They're interested. Follow-up email drafted. HubSpot updated to Qualified. Next meeting Thursday." |
| "We had 3 risks" | "3 risks identified. Risk A mitigated (changed approach). Risk B needs your decision by Tuesday. Risk C is monitoring only." |

## Data Sources

Pull from (in priority order) — **never from memory alone:**
1. **HubSpot** — deal movement, new opportunities, stage changes
2. **Linear** — tasks completed, tasks created, blockers
3. **Calendar** — meetings attended this week
4. **Email** — commitments made, follow-ups pending
5. **Previous brief** — week-over-week comparison (is pipeline growing?)
6. **Memory** — relationship context, entity history

## Output Format

```markdown
# CEO Brief — Week of [Date]

## 🎯 This Week in One Sentence
[The single most important thing]

## Pipeline
- **New opportunities**: X ($X)
- **Deals progressed**: X
- **Deals won**: X ($X)
- **Deals lost**: X ($X)
- **Net change**: +/- $X vs last week
- **Total active pipeline**: $X (↑/↓ from $X)

## Key Meetings (What Mattered)
| Meeting | With | Outcome | Next Step | System Updated? |
|---------|------|---------|-----------|----------------|
| [meeting] | [who] | [what happened] | [specific next] | ✅ Linear/HubSpot |

## Commitments Tracker
### We Owe
| What | To Whom | By When | Status | Action Taken |
|------|---------|---------|--------|--------------|

### They Owe Us
| What | From Whom | Expected | Status | Follow-up Created? |
|------|-----------|----------|--------|-------------------|

## Wins 🎉
- [Concrete win with numbers and attribution]

## Risks ⚠️
| Risk | Severity | Mitigation | Owner | Status |
|------|----------|-----------|-------|--------|
| [risk] | 🔴/🟡 | [specific action] | [who] | [done/pending/needs decision] |

## Open Loops Resolved This Synthesis
- [x] Created follow-up task for Deal X (GFV-XXX)
- [x] Drafted follow-up email for Acme meeting
- [ ] Needs the CEO: Decision on Risk B by Tuesday

## Next Week Priorities
1. [Most important — tied to revenue]
2. [Second — what moves the needle]
3. [Third — what prevents regression]
```

## Rules

1. **Lead with "so what"** — not a data dump
2. **Every risk must have a mitigation plan with an owner** — not just "risk exists"
3. **Every commitment must have a deadline and status** — not just "we owe them"
4. **Compare against last week** — is pipeline growing or shrinking?
5. **Be honest about losses** — don't bury them
6. **Resolve during synthesis** — create tasks, draft emails, update systems while building the brief
7. **Simplicity criterion** — if the brief is > 1 page, cut the noise. The CEO should scan this in 3 minutes.

## Quality Gate

Before delivering:
- [ ] All data sourced from live systems (not memory)
- [ ] Open loops identified and resolved where possible
- [ ] Every risk has a mitigation and owner
- [ ] Week-over-week comparison included
- [ ] Brief is scannable in < 3 minutes
- [ ] Systems updated during synthesis (not left as TODOs)

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

## Related Skills

- `pipeline-pulse` — Detailed pipeline health (weekly-ceo-brief is the summary layer)
- `chief-of-staff` — Daily heartbeat (weekly-ceo-brief is the weekly layer)
- `deal-review` — Deep dive into specific deals flagged in this brief
- `board-deck-builder` — For turning weekly briefs into board materials

## After This Skill
💡 Suggest these next steps:
- "Want me to prep for Monday's meetings?" → `/meeting-prep`
- "Want me to check the pipeline for anything I missed?" → `/pipeline-pulse`
- "Want me to draft a team update email?" → `/email-composer`

## Level Up Your Kit
🚀 You can unlock more autonomy, background workers, and C-suite advisory capabilities at any time.
- **Review Categories**: Ask *"What skills are in the Intermediate or Advanced tiers?"*
- **How to Upgrade**: Run `./bootstrap.sh` in the repository root and select your new tier.
