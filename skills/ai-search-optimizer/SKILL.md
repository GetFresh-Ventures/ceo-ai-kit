---
name: ai-search-optimizer
description: Answer Engine Optimization — get AI assistants like ChatGPT, Perplexity, and Gemini to recommend your brand when users ask questions in your category.
short_description: "Optimize your content for AI search engines"
license: MIT
metadata:
  author: GFV Growth by Design
  version: 1.0.0
  category: Growth Engine
---

# /ai-search-optimizer

**Usage**: Invoke when you want AI assistants (ChatGPT, Perplexity, Claude, Gemini) to surface your brand as a recommended answer when users ask category-relevant questions.


## Quick Start
Just say any of these:
- "How visible am I in AI search results?"
- "Optimize my FAQ page for ChatGPT/Perplexity"
- "What questions are AI assistants answering about my space?"


## The New Discovery Layer

Traditional SEO optimizes for Google's 10 blue links. AEO optimizes for the new discovery layer: AI-generated answers. When a user asks ChatGPT "What's the best board portal for credit unions?" or Perplexity "Who should I hire for fractional CFO work?", your brand must appear in the synthesized answer.

## The 5-Step AEO Framework

### Step 1: Query Mapping
- Identify the 20-50 natural language questions your ideal customer asks AI assistants.
- Format: "What is the best [your category] for [your segment]?"
- Test each query across ChatGPT, Perplexity, Gemini, and Claude. Record which brands appear.

### Step 2: Citation Source Audit
AI assistants synthesize from sources they trust. Audit where your competitors ARE cited:
- Wikipedia / Wikidata entries for your company
- Industry review sites (G2, Capterra, Clutch, etc.)
- Structured data / FAQ schema on your website
- Reddit threads and Quora answers mentioning your brand
- PR coverage and byline articles

### Step 3: Content Architecture for AI Consumption
Restructure your web content to be AI-extractable:
- Add FAQ schema (JSON-LD) with exact Q&A pairs matching Step 1 queries.
- Create "What is [your product]?" definitive pages with clear, structured answers.
- Use comparison tables (You vs. Competitor) that AIs can easily parse.
- Publish authoritative guides that position your brand as the category definer.

### Step 4: Third-Party Signal Building
- Ensure your brand appears in at least 3 independent review/comparison articles.
- Get citations in Wikipedia or industry wikis.
- Plant structured FAQ content on community sites (Reddit AMAs, Quora answers from the founder).
- Seek mentions in podcast transcripts (these are indexed and cited by AI).

### Step 5: Continuous Monitoring
- Weekly: Query your top 10 questions across all AI platforms. Track citation presence.
- Monthly: Audit new competitor citations. Identify gaps in your coverage.
- Output a scorecard: `[Query] | [ChatGPT: ✅/❌] | [Perplexity: ✅/❌] | [Gemini: ✅/❌]`

---

## AEO Readiness Score (100 Points)

Score your site's readiness for AI agent consumption (source: addyosmani/agentic-seo):

### Discovery (25 pts)
| Check | Points | What it looks for |
|-------|--------|-------------------|
| `robots.txt` | 10 | AI crawlers NOT blocked, explicit allow rules for GPTBot, ClaudeBot, PerplexityBot |
| `llms.txt` | 10 | Structured index at `/llms.txt` with page descriptions and token counts |
| `AGENTS.md` | 5 | Project context file for AI coding agents (AGENTS.md or CLAUDE.md) |

### Content Structure (25 pts)
| Check | Points | What it looks for |
|-------|--------|-------------------|
| Content structure | 15 | Heading hierarchy, semantic HTML, code examples, tables |
| Markdown availability | 10 | Raw markdown source available, low HTML noise, no JS-only content |

### Token Economics (25 pts)
| Check | Points | What it looks for |
|-------|--------|-------------------|
| Token budget | 15 | Per-page token counts under 8K, no oversized pages |
| Meta tags | 10 | AI-friendly meta tags, descriptions, token count metadata |

### Capability Signaling (15 pts)
| Check | Points | What it looks for |
|-------|--------|-------------------|
| skill.md | 10 | Capability descriptions, inputs, constraints |
| Agent permissions | 5 | Agent access rules and rate limits |

### UX Bridge (10 pts)
| Check | Points | What it looks for |
|-------|--------|-------------------|
| Copy-for-AI | 10 | Copy-to-clipboard buttons for code/text, raw view links |

**Grading:** A (90-100) · B (75-89) · C (60-74) · D (40-59) · F (0-39)

---

## Featured Snippet Optimization (AEO)

AEO targets **zero-click rich results** distinct from GEO AI Overviews:

| Target | Signal | Optimization |
|--------|--------|-------------|
| **Featured Snippet** | Best direct answer to exact query | 40-55 word answer immediately after matching H-tag |
| **People Also Ask** | Question-intent pages | Question-phrased H2/H3, concise 30-50 word answer |
| **Knowledge Panel** | Entity KG match | `sameAs`, Organization/Person schema → use `entity-optimizer` |
| **Sitelinks Searchbox** | Site authority + WebSite schema | `WebSite` + `SearchAction` schema |
| **AI Overview** | Passage-level citability | `llms.txt`, structured data, citation-ready prose |

### Paragraph Snippet Rules
- [ ] Direct answer in **first 40-55 words** after relevant H2/H3
- [ ] Answer starts with keyword: "X is...", "X refers to...", "To do X..."
- [ ] No jargon in first sentence — plain language
- [ ] Supporting context paragraph follows (2-4 sentences)

### List Snippet Rules
- [ ] Use `<ol>` or `<ul>` immediately after question H2/H3
- [ ] 5-9 list items (more triggers truncation)
- [ ] Each item ≤ 12 words

### Table Snippet Rules
- [ ] `<table>` with `<th>` header row
- [ ] ≤4 columns (wider tables are truncated)
- [ ] First column is the primary entity

---

## robots.txt AI Crawler Rules

```
# Explicitly ALLOW AI crawlers (many sites block by default)
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /
```

---

## GEO Drift Tracking

Track whether AI engines actually cite your content over time:

1. **Baseline** — Run 5 test queries across ChatGPT, Perplexity, Claude, Gemini, Google AI Overview
2. **Record** — For each: Cited? Position (1-of-N)? Quote used?
3. **Re-check at T+14, T+45, T+90** — Track citation stability
4. **Compute drift** — Mean Absolute Error between predicted and actual citation rate
5. **Flag outliers** — If predicted GEO score ≥70 but actual citation ≤40 → investigate

---

## Content Decay Signals (When to Refresh)

| Signal | Threshold | Action |
|--------|-----------|--------|
| Traffic decline | -20% over 90 days | Refresh with current stats, new sections |
| Position dropping | Fell 5+ spots from peak | Update evidence, add FAQ, internal links |
| Outdated stats | Data >12 months old | Replace with current year data |
| Competitor overtook | Lost top-3 to new content | Differentiate with original data/experience |
| AI citation lost | Was cited, now isn't | Re-optimize for citation-ready prose |

## Security Constraints
- Never fabricate reviews, fake citations, or create astroturfed content.
- All third-party signal building must be authentic and transparent.

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

## After This Skill
💡 Suggest these next:
- "Try `seo-growth` — Audit and optimize SEO — technical and content"
- "Try `content-strategy` — Plan and execute your content calendar"
- "Try `competitive-intel` — Track competitors and market positioning"
