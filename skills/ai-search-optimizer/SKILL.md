---
name: ai-search-optimizer
description: Answer Engine Optimization — get AI assistants like ChatGPT, Perplexity, and Gemini to recommend your brand when users ask questions in your category.
short_description: "Optimize your content for AI search engines"
license: MIT
metadata:
  author: GFV Proactive Intelligence
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

## Security Constraints
- Never fabricate reviews, fake citations, or create astroturfed content.
- All third-party signal building must be authentic and transparent.

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
- "Try `seo-growth` — Audit and optimize SEO — technical and content"
- "Try `content-strategy` — Plan and execute your content calendar"
- "Try `competitive-intel` — Track competitors and market positioning"
