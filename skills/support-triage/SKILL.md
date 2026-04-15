---
name: support-triage
description: "Classify, prioritize, and route inbound support requests from any channel. Use when monitoring social mentions, customer emails, or support tickets."
short_description: "Classify and route inbound support requests"
---

# Support Triage

Classify incoming support items by severity and route them to the right system. Don't just flag things — resolve what you can, escalate what you can't.


## Quick Start
Just say any of these:
- "Triage these support emails" (paste or describe them)
- "Classify and prioritize these customer requests"
- "What support issues need my personal attention?"

## When to Use

- Batch processing unread support emails
- Social media mention monitoring
- Customer complaint escalation
- "Check for any fires" requests

## Step 1: Ingest

Pull unread items from available channels:

| Channel | How to pull | What to extract |
|---------|------------|-----------------|
| Email (IMAP) | Google Workspace API | Subject, sender, body snippet, date |
| HubSpot tickets | CRM MCP tools | Ticket ID, contact, subject, priority |
| Social mentions | `search_web` with brand names | Platform, author, sentiment, content |
| Linear issues | Linear MCP tools | Issue ID, title, assignee, state |

## Step 2: Classify

Every inbound item gets classified on two dimensions:

### Severity Matrix

| Level | Criteria | SLA |
|-------|----------|-----|
| 🔴 **P0 — Outage** | Service is down, data loss, security breach | Respond in 15 minutes |
| 🟠 **P1 — Broken** | Feature not working, customer blocked, revenue impact | Respond in 1 hour |
| 🟡 **P2 — Degraded** | Workaround exists, minor bug, feature request | Respond in 24 hours |
| ⚪ **P3 — Noise** | General inquiry, spam, already resolved | Batch weekly or ignore |

### Category

| Category | Keywords / Signals | Route to |
|----------|-------------------|----------|
| **Billing** | invoice, charge, payment, refund | Finance / QuickBooks |
| **Technical** | error, crash, bug, broken, 500 | Engineering / Linear |
| **Onboarding** | setup, getting started, how to, access | Customer Success |
| **Feature Request** | would be nice, can you add, wish | Product / Linear backlog |
| **Complaint** | frustrated, disappointed, cancel, leaving | CEO escalation |
| **Praise** | love, amazing, thank you, great | Marketing (testimonial) |

## Step 3: Auto-Resolve (when possible)

Before escalating, check if the item can be resolved immediately:

| Pattern | Auto-resolution |
|---------|----------------|
| "How do I...?" | Search docs, draft response with answer |
| Password reset request | Send reset link procedure |
| Known bug (matches existing Linear issue) | Reply with workaround + link to tracking issue |
| Duplicate of another ticket | Merge and reply "being tracked in [ID]" |

**Never auto-send responses.** Draft them and present for CEO approval.

## Step 4: Route

For items that can't be auto-resolved:

```markdown
### Triage Report — [Date]

**Items processed:** [N]
**Auto-resolved:** [M]
**Needs attention:** [K]

#### 🔴 P0 — Immediate
- **[Item: Subject]** from [sender]
  - **Category:** [Technical/Billing/etc.]
  - **Summary:** [1 sentence]
  - **Action:** [Create Linear issue / Escalate to CEO / Draft response]

#### 🟠 P1 — Today
- ...

#### 🟡 P2 — This Week
- ...

#### Auto-Resolved
- [Item]: Responded with [summary of response] — awaiting CEO approval to send
```

## Step 5: Create Tracking Items

For P0/P1 items, create tracking artifacts:

```bash
# Create Linear issue for technical items
# → Use Linear MCP: save_issue with appropriate team, priority, labels

# Log in CRM for customer-facing items
# → Use HubSpot MCP: create note on contact record

# Alert CEO for complaints
# → Draft a 2-sentence alert with recommended action
```

## Red Flags

- 3+ items from the same customer → escalate as churn risk
- P0 item from a top-5 revenue customer → interrupt the CEO immediately
- Complaint mentions "lawyer" or "legal" → flag for immediate CEO review
- Social mention going viral (10+ replies) → PR response needed

## Integration

- Feeds from `/chief-of-staff` background sweep
- Creates issues via Linear MCP tools
- Logs interactions via HubSpot MCP tools
- Drafts responses via `/email-composer`

## After This Skill
💡 Suggest these next steps:
- "Want me to draft a response to the urgent items?" → `/email-composer`
- "Want me to log these as decisions?" → `/decision-logger`

## Ready for More?
🚀 You're on the **Beginner** tier (18 skills). When you're ready for more:
- **Upgrade to Intermediate** (46 skills): adds CRM integration, content strategy, fundraising, and C-suite advisory
- **How**: Re-run `./bootstrap.sh` and select **[2] Intermediate**
- **Preview**: Try asking *"What's in the Intermediate tier?"* — I'll show you what unlocks
