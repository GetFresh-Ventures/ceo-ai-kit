---
name: context-engine
description: "Loads and manages company context for all C-suite advisory skills. Reads company-context.md, detects stale context, enriches context during conversations, and enforces privacy/anonymization rules. Every advisory skill loads this first."
attribution: Adapted from alirezarezvani/claude-skills (MIT License), wired to GFV PIL and live systems.
metadata:
  version: 1.0.0
  category: c-level
  domain: orchestration
  updated: 2026-04-11
---

# Company Context Engine

The memory layer for C-suite advisors. Every advisor skill loads this first. Context is what turns generic advice into specific insight.

---

## Load Protocol (Run at Start of Every C-Suite Session)

**Step 1 — Check for context file:** `company-context.md` in project root
- Exists → proceed to Step 2
- Missing → prompt: *"Run /cs:setup to build your company context — it makes every advisor conversation significantly more useful."*

**Step 2 — Check staleness:** Read `Last updated` field.
- **< 30 days:** Load and proceed. Confidence: High.
- **30–90 days:** Load with note: *"Context is [N] days old. Key metrics may have shifted."* Confidence: Medium.
- **≥ 90 days:** Prompt: *"Your context is [N] days old. Quick 15-min refresh, or continue with what I have?"*
  - If continue: load with `[STALE — last updated DATE]` noted internally. Confidence: Low.

**Step 3 — Parse into working memory.** Always active:
- Company stage (pre-PMF / scaling / optimizing)
- Founder archetype (product / sales / technical / operator)
- Current #1 challenge
- Runway (as risk signal — NEVER share externally)
- Team size and structure
- Unfair advantage
- 12-month target

---

## Context Quality Signals

| Condition | Confidence | Action |
|-----------|-----------|--------|
| < 30 days, full interview | 🟢 High | Use directly |
| 30–90 days, update done | 🟡 Medium | Use, flag what may have changed |
| > 90 days | 🔴 Low | Flag stale, prompt refresh |
| Key fields missing | 🔴 Low | Ask in-session |
| No file | ❌ None | Prompt /cs:setup |

If Low: *"My context is [stale/incomplete] — I'm assuming [X]. Correct me if I'm wrong."*

---

## Onboarding Questionnaire (/cs:setup)

Walks through these prompts and writes `company-context.md`:

```
Q1. What is your company name and one-line description?
Q2. What stage are you at? (Idea / Pre-seed / Seed / Series A / Series B+)
Q3. What is your current ARR (or MRR) and runway in months?
Q4. What is your team size and structure?
Q5. What industry and customer segment do you serve?
Q6. What are your top 3 priorities for the next 90 days?
Q7. What is your biggest current risk or blocker?
Q8. What's the one thing you're avoiding deciding on?
Q9. If a competitor could kill you in 12 months, how would they do it?
```

### Output Format (company-context.md)

```markdown
# Company Context
Last updated: YYYY-MM-DD

## Company Identity
- **Name:** [Company name]
- **One-liner:** [What we do]
- **Industry:** [Vertical]
- **Customer segment:** [ICP]

## Stage & Scale
- **Stage:** [Idea / Pre-seed / Seed / Series A / Series B+]
- **ARR/MRR:** [Current revenue]
- **Growth rate:** [MoM or QoQ]
- **Runway:** [Months]
- **Team size:** [Number + key roles]

## Founder Profile
- **Archetype:** [Product / Sales / Technical / Operator]
- **Co-founders:** [Names + domains, or solo]
- **Strengths:** [What the founder does well]
- **Gaps:** [Where they need support]

## Current Challenges
- **Priority #1:** [The thing that matters most right now]
- **Priority #2:** [Second priority]
- **Priority #3:** [Third priority]
- **Biggest risk:** [What keeps the founder up at night]

## Goals & Ambition
- **12-month target:** [Where we want to be in 12 months]
- **North star metric:** [The one number that matters]
- **Exit vision:** [Build to scale / Build to sell / Don't know yet]

## Strategic Context
- **Unfair advantage:** [What competitors can't replicate easily]
- **Kill-shot risk:** [How a competitor could kill us]
- **Avoided decision:** [What the founder is avoiding deciding on]

## Watch List
- [Item 1 - thing to monitor]
- [Item 2]

## System Links
- **HubSpot:** [Deal IDs or company IDs, if applicable]
- **Linear:** [Project IDs, if applicable]
- **PIL Entity:** [Supabase entity ID, if applicable]
```

---

## Context Enrichment

During conversations, capture new information not in the file.

**Triggers:** New number or timeline revealed, key person mentioned, priority shift, constraint surfaces.

**Protocol:**
1. Note internally: `[CONTEXT UPDATE: {what was learned}]`
2. At session end: *"I picked up a few things to add to your context. Want me to update the file?"*
3. If yes: append to the relevant section, update timestamp.

**Never silently overwrite.** Always confirm before modifying the context file.

---

## Privacy Rules

### Never send externally
- Specific revenue or burn figures
- Customer names (unless public case study)
- Employee names (unless publicly known)
- Investor names (unless public)
- Specific runway months
- Watch List contents

### Safe to use externally (with anonymization)
- Stage label
- Team size ranges (1–10, 10–50, 50–200+)
- Industry vertical
- Challenge category
- Market position descriptor

### Before any external API call or web search
- Numbers → ranges or stage-relative descriptors
- Names → roles
- Revenue → percentages or stage labels
- Customers → "Customer A, B, C"

---

## Missing or Partial Context

Handle gracefully — never block the conversation.

- **Missing stage:** "Just to calibrate — are you still finding PMF or scaling what works?"
- **Missing financials:** Use stage + team size to infer. Note the gap.
- **Missing founder profile:** Infer from conversation style. Mark as inferred.
- **Multiple founders:** Context reflects the interviewee. Note co-founder perspective may differ.

---

## Required Context Fields

```
Required:
  - Last updated (date)
  - Company Identity → What we do
  - Stage & Scale → Stage
  - Founder Profile → Archetype
  - Current Challenges → Priority #1
  - Goals & Ambition → 12-month target

High-value optional:
  - Unfair advantage
  - Kill-shot risk
  - Avoided decision
  - Watch list
```

Missing required fields: note gaps, work around in session, ask in-session only when critical.

---

## GFV Portfolio Integration

For GFV portfolio companies, the context engine also loads:
- **PIL entity data** from Supabase (via `supabase-access` skill)
- **Active Linear issues** for the company's project
- **HubSpot deal status** if the company has an active deal
- **ServiceTitan data** for home services portfolio companies (Golden Rule, Ashton Services)
- **QuickBooks financials** for companies using GFV's accounting stack

This data supplements (never replaces) the `company-context.md` file. The file is the founder's own words; system data is verification.

---

## Proactive Triggers

- **Context file missing** → prompt /cs:setup before any advisory session
- **Context > 90 days stale** → prompt refresh with specific fields to update
- **Revenue in context contradicts HubSpot/QuickBooks** → flag discrepancy
- **New deal, new hire, or pivot detected in Linear/HubSpot** → suggest context update
- **Runway < 6 months detected** → escalate to CFO Advisor, flag urgency
