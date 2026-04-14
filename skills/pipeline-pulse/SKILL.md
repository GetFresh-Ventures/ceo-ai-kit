---
name: pipeline-pulse
description: "Active pipeline management — not just reporting, but resolving. Monitor deal movement, auto-resolve obvious next steps, escalate stalled deals, and maintain the outreach tracker as a live source of truth. Use when the CEO asks 'what's happening in the pipeline,' 'are we closing anything,' 'what deals are stuck,' 'weekly pipeline,' or any deal-state monitoring."
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

## Related Skills

- `deal-review` — Deep dive on specific deals
- `outreach-sequence` — Email cadence management
- `chief-of-staff` — Heartbeat integration
- `weekly-ceo-brief` — Weekly summary report
- `experiment-loop` — Testing pipeline optimizations
