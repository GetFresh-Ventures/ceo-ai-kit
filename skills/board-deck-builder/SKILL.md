---
name: board-deck-builder
description: "Assembles comprehensive board and investor update decks by pulling data from live systems. Use when preparing board meetings, investor updates, quarterly business reviews, or fundraising narratives. Covers structure, narrative framework, bad news delivery, and common mistakes."
short_description: "Build board and investor update decks"
attribution: Adapted from alirezarezvani/claude-skills (MIT License), tuned for GFV portfolio context.
---

# Board Deck Builder

Build board decks that tell a story — not just show data. Every section has an owner, a narrative, and a "so what."


## Quick Start
Just say any of these:
- "Build my quarterly board deck"
- "Create an investor update for this month"
- "What metrics should I present to the board?"


## How This Skill Works

### Mode 1: Quarterly Board Deck
Full deck, all sections, 20-30 slides. Sent 48 hours in advance.

### Mode 2: Monthly Investor Update
Condensed — metrics dashboard, financials, pipeline, top risks. 8-12 slides.

### Mode 3: Fundraising Deck
Opens with market/vision, closes with ask. Designed to earn a follow-up meeting.

---

## Deck Structure (Standard Order)
Every section follows: **Headline → Data → Narrative → Ask/Next**

### 1. Executive Summary (CEO)
3 sentences. No more.
- Where we are
- Biggest thing that happened this period
- Where we're going next

*Bad:* "We had a good quarter with lots of progress across all areas."
*Good:* "We closed Q3 at $2.4M revenue (+22% QoQ), signed our largest contract, and enter Q4 with 14 months runway."

### 2. Key Metrics Dashboard
6-8 metrics max. Use a table with: Metric | This Period | Last Period | Target | Status (✅/🟡/❌)

### 3. Financial Update
- P&L summary: Revenue, COGS, Gross margin, OpEx, Net burn
- Cash position and runway (months)
- Variance to plan (what was different and WHY)
- Forecast update for next quarter

### 4. Revenue & Pipeline
- Revenue waterfall: starting → new → expansion → churn → ending
- Pipeline by stage (in $, not just count)
- Forecast with confidence level
- Top 3 deals: name/amount/close date/risk

### 5. Growth & Marketing
- CAC by channel
- Pipeline contribution by channel ($)
- What's working, what's being cut, what's being tested

### 6. Team & People
- Headcount: actual vs plan
- Key hires and open roles
- Attrition: regrettable vs non-regrettable

### 7. Strategic Outlook
- Next quarter priorities (3-5 items, ranked)
- Key decisions needed from the board
- **Asks** (the most important slide — be specific)

## Narrative Framework
**The 4-Act Structure:**
1. **Where we said we'd be** (last quarter's targets)
2. **Where we actually are** (honest assessment)
3. **Why the gap exists** (one cause per variance)
4. **What we're doing about it** (specific, dated actions)

## Delivering Bad News
1. **State it plainly** — "We missed target by $300K (12% gap)"
2. **Own the cause** — don't blame "market conditions"
3. **Show you understand it** — "We analyzed 8 deals; the pattern is X"
4. **Present the fix** — specific, dated changes
5. **Update the forecast** — with bottom-up build

## Common Board Deck Mistakes
| Mistake | Fix |
|---------|-----|
| Too many slides (>25) | Cut ruthlessly |
| Metrics without targets | Every metric needs a target and status |
| No narrative | Data without story forces boards to draw their own conclusions |
| Burying bad news | Lead with it, own it, fix it |
| Vague asks | Specific, actionable, person-assigned asks only |
| No variance explanation | Every gap needs one-sentence cause |

## Live Integration Hooks
| System | Board Section | Skill |
|--------|-------------|-------|
| QuickBooks | Financials — P&L, cash, runway | quickbooks-api |
| HubSpot | Pipeline — deals, velocity, forecast | hubspot-api |
| Google Ads | Marketing — spend, CPA, ROAS | google-ads-connector |
| GA4 | Marketing — traffic, conversions | ga4-connector |
| Field Service Platform | Revenue — job data, avg ticket | field-service-connector |
| Linear | Product/Eng — sprint velocity, delivery | linear-mcp-server |

## Proactive Triggers
- **Board meeting in < 1 week with no deck** → start assembly now
- **Key metrics missing from data sources** → flag data gaps before assembly
- **Bad news detected in financials** → prep the bad-news delivery framework
- **No asks slide prepared** → boards expect asks, push for specifics
- **Last deck reused with just number updates** → narrative must be fresh

## Output Artifacts
| Request | You Produce |
|---------|-------------|
| "Build the board deck" | Full deck with all sections populated from live data |
| "Monthly investor update" | Condensed update with key metrics + narrative |
| "Fundraising deck" | Vision + market + metrics + ask |
| "How do I deliver bad news?" | Bad-news framework with specific scripts |

## Communication
- **Boards see 10+ decks per quarter — yours needs a through-line**
- **Confidence tagging** — 🟢 verified / 🟡 medium / 🔴 assumed
- **Opening frame:** Board should know the key message by slide 3

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

## Related Skills
- **ceo-advisor**: Use for strategic direction that informs the deck. NOT for deck assembly.
- **cfo-advisor**: Use for financial section depth. NOT for full deck coordination.
- **executive-mentor**: Use for stress-testing the deck before presenting. NOT for building it.
- **gfv-report-builder**: Use for generating branded visual slides. NOT for narrative strategy.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Board asks questions I can't answer | Include an appendix with detailed backup data for each key metric |
| Deck takes too long to build | Template it — same structure each quarter, just update the numbers |



## After This Skill
💡 Suggest these next:
- "Try `fundraise` — Create investor materials and manage raises"
- "Try `financial-analyst` — Financial ratios, DCF, and budget analysis"
- "Try `google-doc-creation` — Create professional Google Docs in Drive"
