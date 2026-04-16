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

## Live Integration Hooks

| System | What It Provides | How to Access |
|--------|-----------------|---------------|
| PIL | Cross-session intelligence | `pil-memory-bus` / `gfv-brain-search.py` |
| HubSpot / CRM | Real-time pipeline state | `hubspot-api` |

> **GFV Rule:** Check PIL and live systems to verify claims before submitting answers.

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
- 🟡 **Medium** — Deduced from PIL/memory or recent but not validated real-time data.
- 🔴 **Assumed** — No source available, utilizing best-judgment baseline.

## <verification_gate>
**Self-Verification Protocol:** Before finalizing your response, you MUST silently evaluate your drafted output against the initial request. Have you provided concrete Action Items with ownership? Did you use the Bottom Line First formatting? Have you applied Confidence Tags to your claims? If not, rewrite the response before submitting.

## After This Skill
💡 Suggest these next steps:
- "Want me to draft a response to the urgent items?" → `/email-composer`
- "Want me to log these as decisions?" → `/decision-logger`

## Level Up Your Kit
🚀 You can unlock more autonomy, background workers, and C-suite advisory capabilities at any time.
- **Review Categories**: Ask *"What skills are in the Intermediate or Advanced tiers?"*
- **How to Upgrade**: Run `./bootstrap.sh` in the repository root and select your new tier.
