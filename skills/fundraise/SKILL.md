---
name: fundraise
description: "Create and manage all investor-facing materials — pitch decks, one-pagers, financial models, memos, accelerator applications — with single-source-of-truth consistency enforcement. Also handles investor outreach: cold emails, warm intros, follow-ups, and update communications. Use when the CEO mentions 'fundraising,' 'pitch deck,' 'investor,' 'raise,' 'term sheet,' 'cap table,' 'VC,' 'angel,' or 'accelerator application.'"
short_description: "Create investor materials and manage raises"
metadata:
  version: 1.0.0
  category: revenue-enablement
  triggers:
    - fundraising
    - pitch deck
    - investor
    - raise
    - term sheet
    - cap table
    - VC
    - angel
    - accelerator
---

# Fundraise

Build investor materials that are consistent, credible, and defensible — then execute outreach that gets meetings.


## Quick Start
Just say any of these:
- "Build my pitch deck"
- "Prepare me for investor due diligence"
- "Create a financial model for fundraising"


## When to Activate

- Creating or revising a pitch deck
- Writing investor memos or one-pagers
- Building financial models, milestone plans, or use-of-funds tables
- Answering accelerator/incubator application questions
- Drafting cold emails, warm intro blurbs, or follow-ups to investors
- Writing investor updates during a fundraise
- Aligning multiple fundraising docs around one source of truth

---

## Part 1: Materials

### The Portfolio Co A

**All investor materials must agree with each other.**

Before writing any material, create or confirm a Single Source of Truth (SSoT):
- Traction metrics (MRR, ARR, customers, growth rate)
- Pricing and revenue assumptions
- Raise size and instrument (SAFE, priced round, convertible)
- Use of funds allocation
- Team bios and titles
- Milestones and timelines

**If conflicting numbers appear across documents, STOP and resolve before drafting.**

### Materials Workflow

1. Inventory the canonical facts (SSoT)
2. Identify missing assumptions
3. Choose the asset type
4. Draft with explicit logic visible
5. Cross-check every number against SSoT

### Pitch Deck Flow

1. Company + wedge (why this team, why now)
2. Problem
3. Solution
4. Product / demo
5. Market (TAM → SAM → SOM with clear assumptions)
6. Business model
7. Traction
8. Team
9. Competition / differentiation
10. Ask (amount, instrument, use of funds)
11. Milestones (what this raise unlocks)
12. Appendix (detailed financials, customer list)

### One-Pager / Memo

- State what the company does in one clean sentence
- Show why now
- Include traction and proof points early
- Make the ask precise (amount, instrument)
- Keep claims easy to verify

### Financial Model

Include:
- Explicit assumptions (never bury them)
- Bear/base/bull cases when useful
- Clean layer-by-layer revenue logic
- Milestone-linked spending
- Sensitivity analysis where outcomes hinge on assumptions

### Accelerator Applications

- Answer the exact question asked
- Prioritize traction, insight, and team advantage
- Avoid puffery and superlatives
- Keep internal metrics consistent with deck and model

### Red Flags to Avoid

- Unverifiable claims
- Fuzzy market sizing without assumptions
- Inconsistent team roles or titles across documents
- Revenue math that doesn't sum cleanly
- Inflated certainty where assumptions are fragile
- "We have no competition" (instant credibility loss)

---

## Part 2: Outreach

### Core Rules

1. **Personalize every outbound message** — generic emails don't get meetings
2. **Keep the ask low-friction** — "20 minutes" not "pick your brain"
3. **Use proof instead of adjectives** — metrics not "exciting" or "innovative"
4. **Stay concise** — investors get 100+ emails/day
5. **Never send copy that could go to any investor**

### Hard Bans (Delete and Rewrite)

- "I'd love to connect"
- "excited to share"
- Generic thesis praise without a real tie-in
- Vague founder adjectives ("serial entrepreneur")
- Begging language
- Soft closing questions when a direct ask is clearer

### Cold Email Structure

1. **Subject line** — Short and specific
2. **Opener** — Why THIS investor specifically (portfolio signal, thesis match)
3. **Pitch** — What the company does, why now, relevant proof
4. **Ask** — One concrete next step
5. **Sign-off** — Name, role, one credibility anchor

### Personalization Sources

Reference one or more of:
- Relevant portfolio companies
- A public thesis, talk, post, or article
- A mutual connection
- Clear market fit with the investor's focus

**If context is missing, state the draft needs personalization rather than faking it.**

### Follow-Up Cadence

- **Day 0:** Initial outbound
- **Day 4-5:** Short follow-up with one new data point
- **Day 10-12:** Final follow-up with clean close

Don't keep nudging after 3 touches unless instructed.

### Warm Intro Requests

Make it easy for the connector:
- Explain why the intro is a fit
- Include a forwardable blurb (< 100 words)
- Make the connector look good, not like a favor-asker

### Post-Meeting Follow-Ups

Include:
- The specific thing discussed
- The answer or update promised
- One new proof point if available
- The next step with timeline

### Investor Updates

Monthly cadence during an active raise:
- Headline metric (MRR, customers, or key KPI)
- What happened (3 bullets max)
- What's next (3 bullets max)
- The ask (intros, hires, advice — one specific thing)

---

## Quality Gate

### Materials
- [ ] Every number matches the SSoT
- [ ] Use of funds and revenue layers sum correctly
- [ ] Assumptions are visible, not buried
- [ ] Story is clear without hype language
- [ ] Final asset is defensible in a partner meeting

### Outreach
- [ ] Message is genuinely personalized
- [ ] Ask is explicit
- [ ] Proof point is concrete
- [ ] Filler praise and softener language are gone
- [ ] Word count stays tight (< 150 words for cold email)

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

- `spreadsheet-builder` — Financial models and projections
- `board-deck-builder` — Visual deck creation
- `deal-review` — Pipeline and deal evaluation
- `voice-model` — Consistent founder voice

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Investors not responding | Check your intro strategy — warm intros convert 10x over cold outreach |
| Pitch deck too long | Target 12-15 slides max. Lead with traction, not vision |



## After This Skill
💡 Suggest these next:
- "Try `board-deck-builder` — Build board and investor update decks"
- "Try `financial-analyst` — Financial ratios, DCF, and budget analysis"
- "Try `ceo-advisor` — Strategic leadership and portfolio guidance"
