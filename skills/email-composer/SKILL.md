---
name: email-composer
description: "Write emails in the CEO's authentic voice — no buzzwords, no AI smell. Loads voice model, checks CRM context, drafts with banned-word enforcement, and NEVER auto-sends. Use when drafting any outbound email, follow-up, intro, client communication, or prospect outreach."
short_description: "Draft emails in your authentic voice"
metadata:
  version: 2.0.0
  category: daily-operations
  origin: GFV v1 + clawchief EA templates + auto-resolver draft-first pattern
  triggers:
    - draft email
    - write email
    - follow up email
    - intro email
    - send email
---

# Email Composer

Write outbound emails that sound like *you* wrote them — not a chatbot. **Never auto-send. Never.**


## Quick Start
Just say any of these:
- "Draft an email to [Name] about [topic]"
- "Write a follow-up email to the investor I met yesterday"
- "Reply to this email in my voice" (paste the thread)

## When to Activate

- Drafting prospect outreach
- Following up after meetings
- Client communications
- Intro emails connecting two people
- Any email that represents the CEO or GFV

## How It Works

### Step 1: Load Voice Model
Read voice-model.md before drafting. This contains:
- Word choices and phrases you actually use
- Sentence structures and patterns
- Formality levels by audience
- Anti-patterns (words/phrases you'd never say)

### Step 2: Gather Context (Source-of-Truth Rule)

**Never draft from memory alone.** Check live systems:

| Source | What to Look For |
|--------|-----------------|
| **HubSpot** | Deal status, last interaction, open tasks, relationship stage |
| **Email history** | When you last emailed this person, what was said, any open threads |
| **Calendar** | Recent or upcoming meetings with this contact |
| **Meeting notes** | Any unprocessed action items from recent meetings |
| **Local Memory** | Relationship context, entity history, past commitments |

### Step 3: Draft with Rules

**HTML Format:**
```html
<body style="font-family: Arial, Helvetica, sans-serif; font-size: 14px; color: #333; line-height: 1.5;">
  <!-- Email content here -->
</body>
```

**Core Rules:**
- Match the voice model's tone for THIS audience type
- Keep it concise — CEOs don't write novels
- Include a clear ask or next step
- CC relevant team members on client outreach
- Before intro emails: verify both parties don't already know each other
- Reference something concrete from context (meeting, deal, shared interest)

**Thread Rules (from clawchief):**
- For replies to existing threads → reply in-thread, not a new message with "Re:"
- Preserve real To/CC recipients
- Read the full thread before replying — don't miss context
- If cancelling/rescheduling → reply in-thread, don't start fresh

### Step 4: Auto-Resolve vs Draft-First

Apply the auto-resolver boundary:

| Email Type | Action |
|-----------|--------|
| Scheduling confirmation | ✅ Auto-draft (low risk, operational) |
| Meeting follow-up | ✅ Auto-draft (but CEO approves before send) |
| Cold prospect outreach | ✅ Auto-draft (voice model applied) |
| Investor/board email | 🟡 Draft-first (CEO must review wording carefully) |
| Legal/contract email | 🔴 Escalate (don't draft, surface the need) |
| Press/public-facing | 🔴 Escalate (CEO voice critical) |
| Emotionally sensitive | 🔴 Escalate (judgment call) |

### Step 5: High-Stakes Critique (3-Persona LLM-as-a-Judge)

For Investor/Board, Legal, or High-Value Prospect emails, **do not** just present a single draft. Employ the Reflexion Critique mechanism instead:
1. **Persona A (Requirements Validator):** CoVe (Chain-of-Verification) - Does this email meet the exact intent of the goal?
2. **Persona B (Solution Architect):** CoVe - Is this the right strategic angle/leverage?
3. **Persona C (Quality Reviewer):** CoVe - Is the tone exact? Does it strictly adhere to the banned words list?
If they disagree, synthesize an executive summary of the debate, and present the final perfected draft based on this strict critique.

**Death Loop Short-Circuit:** Maximum 2 critique loops allowed. If the 3 personas cannot reach consensus after 2 rewrite attempts, you MUST break the loop. Output the best draft labeled `[BLOCKED BY JUDGMENT LOOP]` and explicitly flag it for the CEO's manual intervention to prevent token burning.

### Step 6: Present for Approval

Show the full email inline. Wait for explicit **"send it"** before any action.

**Never auto-send. Never. This is the hardest rule and the most important one.**

## Banned Phrases (Always Enforced)

These words and phrases are NEVER acceptable in any email:
- "I wanted to reach out" / "reaching out"
- "circle back" / "touch base"
- "align" (as verb) / "leverage" (as verb)
- "unlock" / "seamlessly" / "holistic"
- "transformative" / "game-changer" / "robust"
- "empower" / "move the needle"
- "synergy" / "at the end of the day"
- "excited to" / "thrilled to"
- "I hope this email finds you well"

## Reply Templates (from clawchief)

### Offer Times
```
Hey [NAME] —

Here are a few times that work:
- [OPTION 1]
- [OPTION 2]
- [OPTION 3]

If one works, I'll send the invite. If not, send a couple windows that do.

— the CEO
```

### Short Follow-Up
```
Hey [NAME] —

Following up on the note below in case it got buried.
Happy to move this forward whenever you're ready.

— the CEO
```

### Holding Reply
```
Got it — checking on this and will get back to you shortly.
```

## Quality Gate

Before presenting:
- [ ] Sounds like a real person, not an AI
- [ ] Has a specific ask or next step
- [ ] References something concrete (meeting, deal, shared context)
- [ ] No banned words or AI-sounding filler
- [ ] Appropriate length for the relationship stage
- [ ] CC list is correct
- [ ] Context gathered from live systems (not assumptions)
- [ ] Thread context preserved (if replying)
- [ ] Voice model applied for this audience type

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

- `voice-model` — The source of truth for how the CEO writes
- `outreach-sequence` — For multi-touch sequences (email-composer handles individual emails)
- `post-meeting-brief` — Generates the follow-up email after meetings
- `chief-of-staff` — Triggers email drafting from inbox sweeps

## After This Skill
💡 Suggest these next steps:
- "Want me to prep for a meeting with them?" → `/meeting-prep`
- "Want me to build a full outreach sequence?" → `/outreach-sequence`
- "Want me to log this outreach?" → `/decision-logger`

## Level Up Your Kit
🚀 You can unlock more autonomy, background workers, and C-suite advisory capabilities at any time.
- **Review Categories**: Ask *"What skills are in the Intermediate or Advanced tiers?"*
- **How to Upgrade**: Run `./bootstrap.sh` in the repository root and select your new tier.
