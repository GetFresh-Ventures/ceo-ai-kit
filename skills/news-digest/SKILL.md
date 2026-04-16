---
name: news-digest
description: "Extract intelligence from news, industry feeds, and market signals relevant to the CEO's active portfolio and pipeline. Use for morning intel, competitive monitoring, or when the user asks 'what's happening in [industry]'."
short_description: "Extract intelligence from news and feeds"
---

# News Digest

Produce a curated intelligence brief — not a raw RSS dump. Every item must be relevant to the CEO's active companies, deals, or competitive landscape.


## Quick Start
Just say any of these:
- "What's happening in [my industry] today?"
- "Build me a weekly industry digest"
- "Track news about [competitor]"


## When to Use

- Morning sweep (via `/chief-of-staff`)
- "What's happening in [industry/market]?"
- "Any news about [company/competitor]?"
- Pre-meeting research on a prospect or partner

## Step 1: Define the Watch List

Pull from the CEO's active context:

```bash
# Portfolio companies (from ~/gtm-brain/pipeline.md or CRM)
# Competitors (from ~/gtm-brain/competitive-landscape.md)
# Industries: home services, SaaS, AI/ML, private equity
# Key people: prospect CEOs, partner contacts
```

If no watch list exists, ask:
> "What companies, industries, or topics should I monitor? I'll build your watch list."

## Step 2: Source Intelligence

Use available tools in priority order:

| Source | Tool | What to extract |
|--------|------|----------------|
| Web search | `search_web` | Breaking news, funding rounds, acquisitions |
| Firecrawl | Firecrawl web scraping | Deep scrape of industry publications |
| HubSpot | CRM MCP tools | Prospect company news (for meeting prep) |
| Google News | `search_web` with `site:news.google.com` | General market signals |

**Query patterns:**
```
"[Company Name]" funding OR acquisition OR launch OR partnership
"[Industry]" market trends 2026
"[Competitor]" product launch OR pricing OR layoffs
```

## Step 3: Score Relevance

Every news item gets a relevance score:

| Score | Criteria | Action |
|-------|----------|--------|
| 🔴 **Direct** (5) | Mentions a portfolio company or active deal by name | Always include |
| 🟠 **Adjacent** (4) | Mentions a direct competitor or partner | Include with context |
| 🟡 **Market** (3) | Industry trend affecting the CEO's sectors | Include if actionable |
| ⚪ **Noise** (1-2) | General tech/business news | Exclude |

**Only items scoring 3+ make the digest.**

## Step 4: Format the Digest

```markdown
## Intelligence Digest — [Date]

### 🔴 Direct Impact
- **[Headline]** — [Source, Date]
  [1-sentence summary]. **Relevance:** [Why this matters to the CEO].
  **Action:** [What the CEO should consider doing]

### 🟠 Competitive Signals
- **[Headline]** — [Source, Date]
  [1-sentence summary]. **Watch:** [What to monitor next]

### 🟡 Market Trends
- **[Headline]** — [Source, Date]
  [1-sentence summary].

---
*[N] sources checked. [M] items scored 3+. Next digest: [tomorrow/date].*
```

## Rules

1. **No more than 7 items** — CEOs don't read newsletters, they scan
2. **Every item has a "why it matters" sentence** — raw headlines are useless
3. **Direct Impact items get an action suggestion** — "Consider reaching out to..."
4. **Date everything** — news loses value fast
5. **Never fabricate news** — if search returns nothing relevant, say "No significant signals today"

## Integration

- Feeds into `/audio-briefing` for the market section
- Triggered by `/chief-of-staff` morning sweep
- Items can feed `/meeting-prep` for upcoming calls with mentioned companies
- Save output to `~/ceo-brain/digests/` for trend tracking

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Too much noise | Narrow your keywords — be specific to your niche, not just industry |
| Missing important stories | Add competitor names and key executive names to your watch list |

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
💡 Suggest these next:
- "Try `competitive-intel` — Track competitors and market positioning"
- "Try `content-strategy` — Plan and execute your content calendar"
- "Try `chief-of-staff` — Your always-on executive AI assistant"
