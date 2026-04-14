---
name: meeting-prep
description: "Build pre-meeting intelligence dossiers from CRM, email, calendar, PIL, and web research. Know who you're meeting, what matters to them, and what your angle is — before you walk in. Use when the CEO has an upcoming meeting, asks 'prep me for,' 'who am I meeting,' or 'get me ready for.'"
metadata:
  version: 2.0.0
  category: daily-operations
  origin: GFV v1 + clawchief EA workflow + autoagent simplicity criterion
  triggers:
    - meeting prep
    - prep me for
    - who am I meeting
    - get me ready for
    - meeting brief
    - upcoming meeting
---

# Meeting Prep

Build a pre-meeting brief that gives you genuine leverage — not a Wikipedia summary. Quick enough to scan in 5 minutes, deep enough to walk in informed.

## When to Activate

- Before any meeting with a prospect, client, partner, or investor
- Ideally 30-60 minutes before the meeting
- Can be triggered by heartbeat when upcoming meetings detected
- CEO explicitly asks "prep me for [meeting]"

## Processing Workflow

### Step 1: Identify the Meeting

From calendar (source of truth — not memory):
- Who's attending? (names + roles)
- What's the stated agenda?
- How long is it?
- Is this a first meeting or a follow-up?
- Was there a previous meeting? What happened?

### Step 2: Research Each Attendee

Pull from every available source:

| Source | What to Gather | Priority |
|--------|---------------|----------|
| **HubSpot** | Deal stage, amount, last interaction, open tasks, notes | P0 |
| **Email** | Last 3-5 emails, outstanding commitments (ours + theirs) | P0 |
| **PIL** | Entity relationships, prior meetings, known preferences | P0 |
| **Calendar** | Previous meetings with this person | P1 |
| **Fathom** | Transcripts from prior meetings | P1 |
| **LinkedIn** | Recent posts, job changes, company news | P1 |
| **Web** | Company news (last 30 days), funding, hiring, product launches | P2 |

**Source-of-truth rule:** Never present assumed data as fact. Tag confidence:
- 🟢 Verified from system
- 🟡 Inferred from context
- 🔴 Assumed / needs confirmation

### Step 3: Check for Unresolved Items

Before drafting the brief, sweep for open loops:
- Commitments WE made to them that aren't fulfilled
- Commitments THEY made to us that we're waiting on
- Action items from last meeting that are still open
- Follow-up emails we should have sent but didn't

**If unresolved items exist → flag them in the brief AND create tasks.**

### Step 4: Build the Brief

```markdown
# Meeting Brief: [Company Name]
**Date**: [date] | **Time**: [time] | **Duration**: [length]
**Type**: [Discovery / Follow-up / Negotiation / Check-in / Close]

## Attendees
| Name | Role | Last Contact | Relationship | Confidence |
|------|------|-------------|-------------|------------|
| [name] | [role] | [date] | [warm/cold/hot] | 🟢/🟡/🔴 |

## Context
[2-3 sentences: Why is this meeting happening? What stage are we at?]

## What We Know
- [Key fact 1 — 🟢 from HubSpot]
- [Key fact 2 — 🟢 from email]
- [Key fact 3 — 🟡 inferred from context]

## ⚠️ Open Loops (from previous interactions)
| Item | Owner | Status | Impact on This Meeting |
|------|-------|--------|----------------------|
| [commitment] | Us/Them | Overdue/Pending | [how it affects the meeting] |

## Their World (Recent Intel)
- [Company news / LinkedIn activity / market context — sourced, not assumed]

## Our Angle
[What's the strategic play here? What value can we offer specifically?]

## Talking Points
1. [Specific talking point WITH supporting data]
2. [Second talking point]
3. [Third talking point]

## Desired Outcome
[What does success look like after this meeting? Be specific.]

## Watch Out For
- [Potential objection — with prepared response]
- [Sensitive topic — with navigation strategy]

## Post-Meeting Handoff
After this meeting → trigger `post-meeting-brief` skill to:
- Extract action items
- Update HubSpot
- Draft follow-up email
- Create Linear tasks
```

## Simplicity Criterion

The brief MUST be scannable in 5 minutes or less. If it's longer than 1 page:
- Cut web research that doesn't directly affect the conversation
- Remove "nice to know" facts that don't change the approach
- Focus on what changes how the CEO walks into the room

## Quality Gate

Before delivering:
- [ ] All data sourced from live systems with confidence tags
- [ ] Open loops from previous interactions surfaced
- [ ] Talking points are specific (not "build rapport")
- [ ] Clear desired outcome defined
- [ ] Watch-outs have prepared responses
- [ ] Brief is < 1 page (scannable in 5 minutes)
- [ ] Post-meeting handoff instructions included

## Related Skills

- `post-meeting-brief` — The natural successor after the meeting
- `deal-review` — For pipeline context before prospect meetings
- `email-composer` — For any pre-meeting emails needed
- `chief-of-staff` — Triggers meeting-prep from heartbeat
