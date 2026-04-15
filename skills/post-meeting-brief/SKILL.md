---
name: post-meeting-brief
description: "Extract action items, decisions, and follow-up tasks from meeting notes or transcripts. NOT 'handled' until all outputs are pushed into live systems (Linear, HubSpot, calendar). Use when meeting notes arrive from Fathom, manual notes, calendar events, or any transcript source."
short_description: "Extract action items from meeting notes"
metadata:
  version: 2.0.0
  category: execution-infrastructure
  origin: GFV v1 + clawchief meeting-notes ingestion pattern
  triggers:
    - meeting notes
    - post-meeting
    - meeting summary
    - action items
    - what came out of the meeting
    - process my notes
---

# Post-Meeting Brief

Turn meeting notes into system-level action within 15 minutes. A meeting note is NOT "handled" just because it was read — it's handled when all outputs are pushed into live systems.


## Quick Start
Just say any of these:
- "Here are my meeting notes — extract the action items" (paste notes)
- "Summarize what we decided in today's leadership meeting"
- "Turn these rough notes into a follow-up email and task list"

## When to Activate

- Immediately after any client, prospect, or partner meeting
- When Fathom/Otter transcript arrives
- When manual notes are provided (bullets, stream of consciousness)
- During heartbeat sweeps when unprocessed meeting notes are detected

## The Non-Negotiable Rule

**A meeting note is NOT handled until:**
- [ ] Tasks are created in Linear (with correct assignee and due date)
- [ ] Deal state is updated in HubSpot (stage, amount, close date)
- [ ] Follow-up events are on the calendar
- [ ] Follow-up email is drafted (using `email-composer` rules)
- [ ] Any commitments made are tracked

Reading ≠ Processing. Summarizing ≠ Processing. Only action counts.

## Processing Workflow

### Step 1: Ingest Meeting Content

Accept from any format:
- Fathom AI transcript/summary
- Manual bullet notes
- Stream of consciousness voice dump
- Calendar event + verbal debrief

### Step 2: Extract Intelligence

Look specifically for:
- **Explicit action items** — things someone said they'd do
- **Implied follow-ups** — things that clearly need to happen even if nobody said "action item"
- **Deadlines** — any dates or time commitments mentioned
- **Promises the CEO made** — commitments the CEO owes
- **Introductions to send** — people to connect
- **Documents/materials to share** — decks, proposals, files promised
- **Scheduling next steps** — when to meet again
- **Deal-state changes** — stage movement, pricing discussions, new information
- **Key learnings** — things about the prospect/client we didn't know before

### Step 3: Classify and Route

For each extracted item, classify through the priority map:
- **P0 items** → Create immediately, alert the CEO
- **P1 items** → Create task, include in summary
- **P2 items** → Create task with future due date
- **Auto-resolvable** → Handle directly (send intro, update tracker, schedule follow-up)

### Step 4: Update ALL Live Systems

In the same turn:
1. **Linear** → Create tasks with owner + deadline
2. **HubSpot** → Update deal stage/amount/close date if changed
3. **Calendar** → Book follow-up meeting if agreed
4. **Email** → Draft follow-up email for the CEO's approval
5. **PIL** → Log key relationship insights

### Step 5: Output Brief

```markdown
# Post-Meeting Brief: [Company] — [Date]

## Meeting Details
- **Attendees**: [names and roles]
- **Duration**: [length]
- **Type**: [Discovery / Follow-up / Negotiation / Close]

## Key Decisions Made
1. [Decision with context]

## Action Items Created

### Ours (commit tracker)
| Action | Owner | Deadline | System Updated |
|--------|-------|----------|----------------|
| [item] | the CEO | [date] | ✅ Linear GFV-XXX |

### Theirs (we verify)
| Action | Who | Expected By |
|--------|-----|-------------|

## Deal Impact
- **Stage change**: [Yes/No — Linear + HubSpot updated]
- **Amount change**: [Yes/No]
- **Close date**: [Confirmed / Moved / At risk]
- **Next meeting**: [Scheduled on calendar? When?]

## Key Insights (for PIL)
- [Learning about their business/needs]
- [Buying signal or concern]

## Follow-Up Email Draft
[Draft below — awaiting the CEO's "send it" approval]
```

## Auto-Resolve Bias

Meeting notes often contain operational follow-ups that can be auto-resolved:
- ✅ Add tasks for the CEO or the assistant
- ✅ Create follow-up reminders
- ✅ Update deal tracker after outcome is clear
- ✅ Schedule follow-up when time was agreed
- ❌ Draft-first: investor/board messaging, legal wording, pricing commitments
- ❌ Escalate: unclear commitments, ambiguous outcomes

## Quality Gate

Before marking a meeting note as processed:
- [ ] Every action item has an owner AND deadline
- [ ] All affected systems (Linear, HubSpot, Calendar) are updated
- [ ] Follow-up email references specific meeting content
- [ ] Deal impact is honestly assessed (not just "went well")
- [ ] Key insights logged for future reference
- [ ] CEO has received the brief with draft email for approval

## Related Skills

- `email-composer` — For follow-up email drafting
- `chief-of-staff` — For heartbeat-driven meeting note detection
- `meeting-prep` — For preparing BEFORE meetings
- `deal-review` — For evaluating deal impact from meetings

## After This Skill
💡 Suggest these next steps:
- "Want me to draft follow-up emails for each action item?" → `/email-composer`
- "Want me to update the pipeline with what we discussed?" → `/pipeline-pulse`
- "Want me to log the key decisions?" → `/decision-logger`

## Ready for More?
🚀 You're on the **Beginner** tier (18 skills). When you're ready for more:
- **Upgrade to Intermediate** (46 skills): adds CRM integration, content strategy, fundraising, and C-suite advisory
- **How**: Re-run `./bootstrap.sh` and select **[2] Intermediate**
- **Preview**: Try asking *"What's in the Intermediate tier?"* — I'll show you what unlocks
