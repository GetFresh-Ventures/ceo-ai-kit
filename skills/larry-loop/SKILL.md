---
name: larry-loop
description: An autonomous content validation system. Focuses on distribution, iteration, and algorithmic doubling down over raw creativity.
short_description: "Autonomous content validation system"
license: MIT
metadata:
  author: GFV Growth by Design
  version: 1.0.0
  category: marketing-automation
---

# /larry-loop

**Usage**: Utilize this skill when the CEO wants to scale their social or marketing content systematically rather than relying on manual, creative one-offs.


## Quick Start
Just say any of these:
- "Validate my content against distribution targets"
- "Run a content quality loop on [asset]"
- "Check if this content meets our standards"


## The Paradigm: System over Creativity
The core secret of the "Larry" architecture is that automation alone will not save a bad hook. The system leverages:
**Speed + Consistency + Distribution > Creativity at Scale**.

When executing the `/larry-loop`, strictly follow this 4-step execution chain without skipping steps.

## Phase 1: Audience & Hook Research
- **Do not randomly generate.** Use available search or web-scraping MCP tools to scan the specific niche (e.g. LinkedIn, X, or TikTok).
- Identify what formats the algorithm currently favors (e.g., Slideshows, long-form threads, short-form video hooks).
- Pinpoint the winning positioning and the specific pain point of the audience.

## Phase 2: Generative Variations
- Take the validated hooked concept and systematically generate variations.
- Produce structured content matrices (e.g., 5 hooks, 3 bodies, 2 CTAs) rather than a single perfect post. 
- All outputs must be formatted natively for the platform's requirements.

## Phase 3: High-Velocity Distribution Setup
- Package the outputs in a format that the CEO can schedule instantly, or (if a scheduler MCP is active) stage the posts for distribution in the backend. 
- Consistency is the primary KPI. Ensure the volume of the generated variations can sustain a daily or sub-daily posting schedule.

## Phase 4: The Algorithmic Prune
- When reviewing data after a cycle, ruthlessly kill formats and topics that didn't drive engagement or revenue (integrating with QuickBooks/HubSpot/GA4 if possible for attribution).
- Evolve the few winning hooks into the baseline for the next week's Phase 1 loop.
- **Double down on winners.**

## Winner Scoring System (Enhanced v1.1 — Marketing Experiments Method)

### Quantitative Winner Criteria
Every content piece gets scored on a 100-point scale:

| Metric | Weight | Scoring |
|--------|--------|---------|
| Engagement Rate | 30 | Top 10% = 30, Top 25% = 20, Below avg = 5 |
| Conversion Signal | 25 | Lead captured = 25, Click to site = 15, None = 0 |
| Virality | 20 | Shared/reposted = 20, Saved = 10, Neither = 0 |
| Audience Fit | 15 | ICP engagement = 15, Mixed = 8, Off-target = 0 |
| Production Cost | 10 | Auto-generated = 10, Light edit = 7, Heavy = 3 |

### Format Trend Detection
Track which content FORMATS are winning algorithmically RIGHT NOW:
- Monitor: carousel vs. text-only vs. video vs. slideshow vs. poll vs. thread.
- Update weekly. The algorithm shifts frequently.
- Never commit to a format permanently — commit to testing formats.

### Cross-Platform Winner Migration
When a post wins on one platform, automatically adapt for others:
1. LinkedIn winner → Repurpose as X thread via `social-engine`.
2. X thread winner → Convert to newsletter via `email-composer`.
3. Video winner → Extract hook for static posts via `social-scheduler`.
4. Blog winner → Slice into carousel slides via `ugc-video`.

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
- "Try `content-strategy` — Plan and execute your content calendar"
- "Try `seo-growth` — Audit and optimize SEO — technical and content"
- "Try `voice-model` — Build your personal writing voice model"

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
