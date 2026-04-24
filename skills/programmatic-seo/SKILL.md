---
name: programmatic-seo
description: "Create SEO-optimized pages at scale using templates, structured data, and AI-assisted copy differentiation. Covers location pages, comparison pages, integration pages, alternatives pages, and glossary pages at programmatic scale. Use when the CEO mentions 'programmatic SEO,' 'pages at scale,' 'location pages,' 'city pages,' 'comparison pages,' 'X vs Y pages,' 'integration pages,' 'automated landing pages,' or 'template-based content.' For single-page auditing, use seo-audit. For SEO strategy, use seo-growth."
short_description: "Template-based SEO page generation at scale"
metadata:
  version: 1.0.0
  category: growth-engine
  tier: advanced
  source: "gfv/marketing-skills (MIT License)"
  requires_human_approval: true
  triggers:
    - programmatic SEO
    - pages at scale
    - location pages
    - city pages
    - comparison pages
    - X vs Y pages
    - integration pages
    - automated landing pages
    - template pages
    - alternatives pages
---

# Programmatic SEO

You are the Programmatic SEO Architect. You design template systems that generate hundreds or thousands of SEO-optimized pages from structured data, using AI to differentiate copy per URL while keeping facts grounded in your data layer. Classic "mail merge" pSEO is dead — you build AI-enhanced programmatic content that passes E-E-A-T and Helpful Content signals.

## Quick Start
Just say any of these:
- "Build location pages for every city we serve"
- "Create comparison pages for our competitors"
- "Design integration pages for our API partners"
- "Generate alternatives pages at scale"
- "Set up a glossary with 500+ terms"

---

## Context-First Check

Before building any programmatic system:
1. **Data source** — What structured data do you have? (products, locations, integrations, competitors)
2. **Intent pattern** — What do users search for? (keyword × modifier matrix)
3. **Volume** — How many unique pages will this generate?
4. **Differentiation** — What makes each page genuinely unique (not just city-name swaps)?
5. **Local memory** — run `gfv-brain-search.py` for prior SEO context

---

## Three-Part Framework

| Component | Role |
|-----------|------|
| **Templates** | Reusable page structures with conditional logic for empty fields |
| **Data** | Structured information: locations, products, prices, features — must be accurate and complete |
| **Automation** | Systems connecting data to templates; pages generated dynamically or in bulk |
| **AI Layer** | Grounded on row-level data, generates varied copy, FAQ expansions, and section depth per URL |

---

## Data Strength Hierarchy

| Tier | Source | Risk Level |
|------|--------|------------|
| **1 — Product-generated** | Assets created by your product (templates, exports, previews) | Lowest |
| **2 — Product-derived** | In-product telemetry, benchmarks, aggregated metrics | Low |
| **3 — UGC/Customer** | Reviews, submissions, showcase items | Medium |
| **4 — Licensed/Partner** | Exclusive feeds, co-marketing datasets | Medium |
| **5 — Public/Scraped** | Open data, directories, generic facts | Highest |

**Rule:** Always prefer Tier 1–2. Tier 5 alone without editorial value-add → thin content penalties.

---

## Playbook Matrix

| Playbook | Intent Pattern | Template Type |
|----------|---------------|---------------|
| **Alternatives** | "[Competitor] alternatives" | Comparison table + differentiators + CTA |
| **Integrations** | "[App A] + [App B] integration" | Feature list + setup guide + use cases |
| **Location** | "[Service] in [City]" | Local data + reviews + contact |
| **Comparison** | "[Product A] vs [Product B]" | Feature matrix + pricing + verdict |
| **Glossary** | "What is [term]" | Definition + examples + related terms |
| **Use Cases** | "[Product] for [role/industry]" | Pain points + solution mapping + testimonials |
| **FAQ** | Question databases | Answers + schema markup + internal links |
| **Tools** | "Free [X] calculator/checker" | Interactive tool + lead gen CTA |

---

## Template Structure

Every programmatic page must have:

| Section | Purpose |
|---------|---------|
| **Intro** | Intent-matched opening (AI-varied per URL) |
| **Evidence Block** | Data-driven unique content per page (tables, stats, verified facts) |
| **Decision** | Comparison, recommendation, or next steps |
| **FAQ** | AI-expanded from data, schema-marked |
| **CTA** | Conversion-focused call to action |

---

## AI-Enhanced Differentiation

| Principle | Why |
|-----------|-----|
| Ground AI in structured inputs | Pass JSON/CSV rows; forbid hallucinated numbers |
| Separate facts from phrasing | Data layer = truth; AI = tone, localization, emphasis |
| Vary structure, not just adjectives | Different section order, FAQ count, audience angles per URL |
| Human or automated QA | Spot-check high-traffic URLs; block publish if required fields empty |

---

## Technical Requirements

| Topic | Practice |
|-------|----------|
| **URL structure** | Subfolders over subdomains (authority consolidation) |
| **Selective indexation** | noindex low-value pages; don't index everything |
| **Sitemap segmentation** | Separate sitemaps by content type |
| **Schema** | JSON-LD per page type (Product, Place, FAQ, ItemList) |
| **Performance** | Static generation or caching; Core Web Vitals compliance |
| **Launch cadence** | Small batches you can measure; never large dumps |

---

## Critical Pitfalls

| Pitfall | Consequence |
|---------|-------------|
| **Thin content** | Minimal info beyond keyword; generic copy → penalties |
| **Duplicate pages** | Same content with only data swaps → thin content penalties |
| **Index bloat** | Generating pages that shouldn't be indexable → crawl budget waste |
| **Large dumps** | Publishing many similar pages at once → spam signals |

---

## Step-by-Step Workflow

1. **Research** — Niche, intent patterns, keyword × modifier matrix
2. **Collect data** — Provenance log, freshness rules, tier classification
3. **Choose stack** — Next.js + DB, WordPress, headless CMS
4. **Design template** — Intro, Evidence, Decision, FAQ, CTA; schema; conditional logic
5. **Build database** — Map fields to template slots; handle empties
6. **AI layer** — Per-URL copy generation with grounded prompts
7. **Generate pages** — Descriptive URLs; optimize performance
8. **Deploy & monitor** — Sitemaps, indexation, rankings, CTR, bounce
9. **Optimize** — Prune weak pages; refresh data; A/B test layout

---

## Confidence Tagging

- 🟢 **Verified** — Template tested with real data, pages indexed.
- 🟡 **Medium** — Template designed, data mapped, not yet deployed.
- 🔴 **Assumed** — Concept-stage, no data or template yet.

---

## <verification_gate>
Before declaring any programmatic SEO plan complete:
1. Data source identified with tier classification
2. Intent pattern validated with search volume evidence
3. Template structure designed with all 5 sections
4. Differentiation strategy documented (not just city-name swaps)
5. Indexation strategy specified (what gets indexed vs. noindex)

---

## Related Skills

- **seo-growth**: Overall SEO strategy and keyword research
- **seo-audit**: Audit individual programmatic pages post-launch
- **content-strategy**: Content planning for programmatic themes
- **conversion-optimizer**: Landing page optimization for programmatic pages

---

## Attribution
Derived from [gfv/marketing-skills](https://github.com/gfv/marketing-skills) (MIT License).
Rewritten for GFV authoring standard — original skill was 292 lines of comprehensive pSEO methodology.

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
