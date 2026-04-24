---
name: pipeline-pulse
description: "Active pipeline management — not just reporting, but resolving. Monitor deal movement, auto-resolve obvious next steps, escalate stalled deals, and maintain the outreach tracker as a live source of truth. Use when the CEO asks 'what's happening in the pipeline,' 'are we closing anything,' 'what deals are stuck,' 'weekly pipeline,' or any deal-state monitoring."
short_description: "Active pipeline management and deal tracking"
metadata:
  version: 2.0.0
  category: revenue-enablement
  origin: GFV v1 + clawchief business-development pattern
  triggers:
    - pipeline
    - deals
    - what's closing
    - what deals are stuck
    - pipeline review
    - deal status
    - weekly pipeline
---

# Pipeline Pulse

Your pipeline health monitor — with teeth. Don't just report, resolve.


## Quick Start
Just say any of these:
- "What's happening in my pipeline?"
- "Give me a pipeline health check"
- "Show me deals at risk and what to do about them"

## When to Activate

- End of week pipeline review (Friday)
- Before weekly standup or team meeting
- Monthly/quarterly business reviews
- Investor update preparation
- Any time the CEO asks "what's happening in the pipeline"

## The Resolve-First Rule

**From clawchief:** Don't just summarize pipeline state — resolve what you can in the same turn.

| Signal | Bad Response | Good Response |
|--------|-------------|---------------|
| Deal stuck 14+ days | "Deal X is stalled" | "Deal X stalled 14 days. Follow-up drafted. Recommend sending today." |
| Prospect replied positively | "Prospect Y is interested" | "Prospect Y interested. Meeting booked for Thursday. HubSpot updated to 'Qualified'." |
| No activity on deal | "Deal Z has no activity" | "Deal Z: last touch 21 days ago. Created follow-up task GFV-XXX due tomorrow." |

## Pipeline Dashboard

```markdown
# Pipeline Pulse — Week of [Date]

## This Week at a Glance
- **Pipeline value**: $X (↑/↓ $X from last week)
- **Weighted pipeline**: $X
- **Deals won**: X ($X)
- **Deals lost**: X ($X)
- **New opportunities**: X ($X)

## Stage Distribution
| Stage | Count | Value | Avg Days in Stage | Health |
|-------|-------|-------|-------------------|--------|
| Lead | X | $X | X days | 🟢/🟡/🔴 |
| Qualified | X | $X | X days | 🟢/🟡/🔴 |
| Proposal | X | $X | X days | 🟢/🟡/🔴 |
| Negotiation | X | $X | X days | 🟢/🟡/🔴 |

## Velocity Metrics
- **Average deal cycle**: X days
- **Win rate (30d)**: X%
- **Average deal size**: $X

## What Moved This Week
### Forward ✅
- [Deal] → [New Stage] — [what triggered the move]

### Backward ⚠️
- [Deal] → [Regression reason] — [recommended action]

### New 🆕
- [Deal] — [Source/Channel] — [quality assessment]

### Closed Won 🎉
- [Deal] — $X — [what we can learn]

### Closed Lost 💀
- [Deal] — [Root cause, not just "lost"]

## Stalled Deals (Needs Action)
| Deal | Days Stalled | Last Touch | Recommended Action | Status |
|------|-------------|------------|-------------------|--------|
| [Deal] | 14 | Apr 1 | Send follow-up | ✅ Drafted |

## Actions Taken This Sweep
- [ ] Follow-up drafted for Deal X → awaiting the CEO approval
- [x] HubSpot updated: Deal Y moved to Qualified
- [x] Follow-up task created: GFV-XXX
```

## Follow-Up Cadence (Default)

For unanswered outreach:
- **First follow-up**: ~2 days after last unanswered outbound
- **Second follow-up**: ~5 days after previous follow-up
- **Third follow-up**: ~7 days after previous follow-up
- **After third**: Stop auto-sequence, escalate if deal still matters

Rules:
- Reset clock after each new outbound
- Record each follow-up in tracker notes
- Don't auto-follow-up when thread is sensitive, closed, or CEO said stop

## Data Sources

Pull from (in priority order):
1. **HubSpot** — Deal pipeline, stage, amount, activity
2. **Linear** — Related tasks and blockers
3. **Calendar** — Upcoming meetings with prospects
4. **Email** — Recent outbound and replies
5. **Previous pulse** — Week-over-week comparison

## Source-of-Truth Rule

The CRM/tracker is the live source of truth — not local files, not memory.
- Always read current state before reporting
- Update the tracker as part of the sweep, not as an afterthought
- If pipeline state changes during the sweep, update immediately in the same turn

## Quality Gate

Before delivering pipeline pulse:
- [ ] Every stalled deal has a recommended action
- [ ] Forward movement is attributed (what caused it)
- [ ] Losses have root cause analysis (not just "lost")
- [ ] Actions were taken (not just reported)
- [ ] Week-over-week comparison is included
- [ ] Next week priorities are specific, not generic

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

- `deal-review` — Deep dive on specific deals
- `outreach-sequence` — Email cadence management
- `chief-of-staff` — Heartbeat integration
- `weekly-ceo-brief` — Weekly summary report
- `experiment-loop` — Testing pipeline optimizations

## After This Skill
💡 Suggest these next steps:
- "Want me to deep-dive on a specific deal?" → `/deal-review [deal name]`
- "Want me to draft follow-ups for stale deals?" → `/email-composer`
- "Want me to write this up as a weekly brief?" → `/weekly-ceo-brief`

## Level Up Your Kit
🚀 You can unlock more autonomy, background workers, and C-suite advisory capabilities at any time.
- **Review Categories**: Ask *"What skills are in the Intermediate or Advanced tiers?"*
- **How to Upgrade**: Run `./bootstrap.sh` in the repository root and select your new tier.

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
