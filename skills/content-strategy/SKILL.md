---
name: content-strategy
description: "Plan, prioritize, and execute content strategy — topic pillars, content calendars, keyword mapping by buyer stage, ideation from multiple sources (forums, competitors, sales calls, surveys), and prioritization scoring. Use when the CEO mentions 'content strategy,' 'what should we write about,' 'content calendar,' 'blog strategy,' 'content pillars,' 'editorial calendar,' or 'content plan.'"
short_description: "Plan and execute your content calendar"
metadata:
  version: 1.0.0
  category: growth-engine
  triggers:
    - content strategy
    - content calendar
    - blog strategy
    - content pillars
    - editorial calendar
    - content plan
    - what should we write about
---

# Content Strategy

Build a content strategy that drives decisions, not just pageviews.


## Quick Start
Just say any of these:
- "Plan my content calendar for the next quarter"
- "What topics should I be creating content about?"
- "Audit my existing content — what's working?"


## When to Activate

- Planning what content to create and why
- Building content pillars and topic clusters
- Creating an editorial calendar
- Mapping keywords to buyer journey stages
- Prioritizing content ideas by business impact
- Identifying content gaps vs. competitors
- Repurposing existing content into new formats

## Before Starting

Gather this context (ask if not provided):

1. **Business Context** — What do you sell? Who's your ICP?
2. **Current Content** — What exists already? What performs?
3. **Goals** — Traffic? Leads? Brand awareness? Thought leadership?
4. **Resources** — Who writes? How often can you publish?
5. **Competitors** — Who's winning at content in your space?

## Content Pillars

Content pillars are the 3-5 core topics your brand will own. Each pillar spawns a cluster of related content.

### How to Identify Pillars

1. **Product-led**: What problems does your product solve?
2. **Audience-led**: What does your ICP need to learn?
3. **Search-led**: What topics have volume in your space?
4. **Competitor-led**: What are competitors ranking for?

### Pillar Structure

```
Pillar Topic (Hub)
├── Subtopic Cluster 1
│   ├── Article A
│   ├── Article B
│   └── Article C
├── Subtopic Cluster 2
│   ├── Article D
│   ├── Article E
│   └── Article F
└── Subtopic Cluster 3
    ├── Article G
    └── Article H
```

### Pillar Criteria

Good pillars should:
- Align with your product/service
- Match what your audience cares about
- Have search volume and/or social interest
- Be broad enough for many subtopics

## Keyword Research by Buyer Stage

Map topics to the buyer's journey:

| Stage | Modifiers | Example |
|-------|-----------|---------|
| **Awareness** | "what is," "how to," "guide to" | "What is HVAC maintenance" |
| **Consideration** | "best," "vs," "alternatives," "comparison" | "Best HVAC companies Salt Lake City" |
| **Decision** | "pricing," "reviews," "near me," "cost" | "Portfolio Co A HVAC reviews" |
| **Implementation** | "templates," "tutorial," "how to use" | "HVAC maintenance checklist" |

## Content Ideation Sources

### 1. Customer Conversations
- Questions from sales calls → FAQ content
- Pain points → problem-focused articles
- Objections → content to address proactively
- Language patterns → voice of customer data

### 2. Keyword Data
If keyword exports available (SEMrush, Ahrefs, GSC):
- Topic clusters (group related keywords)
- Quick wins (low competition + decent volume + high relevance)
- Content gaps (keywords competitors rank for that you don't)

### 3. Competitor Analysis
- Top-performing competitor posts
- Topics they cover repeatedly
- Gaps they haven't covered
- Outdated content to improve on

### 4. Forum Research
- Reddit: `site:reddit.com [topic]`
- Quora, Hacker News, industry forums
- Extract: FAQs, misconceptions, debates, terminology

## Content Types That Work

**Problem-Solution Content** — Address real problems customers face before they know you exist.

**Expert Roundups** — 15-30 experts answering one specific question. Built-in distribution.

**Case Studies** — Challenge → Solution → Results → Key learnings.

**Data-Driven Content** — Original research, product data analysis, industry benchmarking.

**Meta Content** — Behind-the-scenes transparency. "How We Got Our First 100 Customers."

## Prioritization Framework

Score each content idea on four factors:

| Factor | Weight | What to Evaluate |
|--------|--------|-------------------|
| **Customer Impact** | 40% | Frequency of topic in research, % of customers facing this |
| **Content-Market Fit** | 30% | Alignment with product, unique insights available |
| **Search Potential** | 20% | Monthly volume, competition level, growth trend |
| **Resource Requirements** | 10% | Expertise available, research needed, assets required |

### Prioritization Output

| Idea | Customer Impact | Content-Market Fit | Search Potential | Resources | Total |
|------|----------------|-------------------|-----------------|-----------|-------|
| Topic A | 8 | 9 | 7 | 6 | 8.0 |
| Topic B | 6 | 7 | 9 | 8 | 7.1 |

## Output Format

### Deliverables

1. **Content Pillars** — 3-5 pillars with rationale and subtopic clusters
2. **Priority Topics** — Ranked list with keyword, buyer stage, content type, rationale
3. **Topic Cluster Map** — Visual representation of how content interconnects
4. **Calendar** — Monthly/weekly publishing schedule mapped to pillars

## Quality Gate

Before delivering:
- [ ] Pillars align with business goals, not just search volume
- [ ] Every topic has a clear "why" tied to customer research
- [ ] Buyer stages are covered (not all awareness-stage content)
- [ ] Calendar is realistic for stated resources
- [ ] Content gaps vs. competitors are addressed

## A/B Hook Testing (Enhanced v1.1 — content-engine Method)

### The Hook Testing Protocol
Every high-stakes piece of content should test multiple hooks before committing:

1. **Generate 3 Hook Variants** per content piece:
   - **Data Hook**: Lead with a surprising statistic or number.
   - **Story Hook**: Lead with a micro-narrative (2 sentences max).
   - **Contrarian Hook**: Lead with a commonly-held belief, then challenge it.

2. **Rapid Test Across Channels**:
   - Post each hook variant on a different platform (or at different times on the same platform).
   - Measure: Click-through rate, time-on-page, engagement rate.
   - Minimum sample: 48 hours before declaring a winner.

3. **Winner Becomes the Template**:
   - The winning hook structure becomes the default for that content pillar.
   - Feed into `larry-loop` for doubling-down.
   - Archive losing hooks in `decision-logger` to avoid repeating failures.

### Content Experiment Log
Maintain a running log of hook tests:
```
| Date | Content | Data Hook CTR | Story Hook CTR | Contrarian Hook CTR | Winner |
```

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

- `competitive-intel` — Deep competitive research
- `outreach-sequence` — Email-based distribution
- `voice-model` — Brand voice consistency
- `social-engine` — Social media content
- `larry-loop` — Content doubling-down engine
- `ai-search-optimizer` — AI search optimization

## Troubleshooting

| Problem | Fix |
|---------|-----|
| No content ideas | Start with competitor analysis — see what's ranking for them but not you |
| Calendar feels overwhelming | Focus on 2-3 cornerstone pieces per month, repurpose across channels |



## After This Skill
💡 Suggest these next:
- "Try `eeat-content-pod` — Execute the prioritized content with E-E-A-T generation"
- "Try `seo-growth` — Audit and optimize SEO — technical and content"
- "Try `social-engine` — Create platform-native social media content"
- "Try `copy-master` — Write world-class marketing copy"
