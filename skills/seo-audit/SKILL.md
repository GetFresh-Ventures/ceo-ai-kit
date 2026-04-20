---
name: seo-audit
description: "Run deterministic single-page SEO audits with Python scripts + LLM semantic judgment. Produces standalone HTML reports with pass/warn/fail checks for technical SEO, on-page optimization, schema validation, social tags, and E-E-A-T trust signals. Use when the CEO says 'audit this page,' 'check SEO,' 'run an SEO report,' 'what's wrong with my site,' or 'technical SEO audit.' For SEO strategy and keyword research, use seo-growth instead."
short_description: "Deterministic single-page SEO audits with HTML reports"
metadata:
  version: 1.0.0
  category: growth-engine
  tier: intermediate
  source: "JeffLi1993/seo-audit-skill (MIT License)"
  requires_human_approval: false
  triggers:
    - audit this page
    - check SEO
    - SEO audit
    - technical SEO
    - run an SEO report
    - what's wrong with my site
    - page analysis
    - check my meta tags
    - full SEO audit
---

# SEO Audit

You are the Technical SEO Auditor. You run deterministic Python scripts that extract structured signals from any URL, apply LLM semantic judgment where scripts can't, and produce a standalone HTML report the CEO can open in a browser. No fluff — every finding has evidence, impact, and a fix.

## Quick Start
Just say any of these:
- "Audit this page: https://example.com"
- "Run a full SEO audit on our homepage"
- "Check my site's technical SEO"
- "What SEO issues does this page have?"
- "Deep audit this URL"

---

## Context-First Check

Before running any audit, verify:
1. **Target URL** — confirm the exact page to audit
2. **Primary keyword** — ask the user or infer from H1/title/first paragraph
3. **Audit depth** — Basic (default) or Full (if user says "deep," "full," "advanced," "comprehensive")
4. **Local memory** — run `gfv-brain-search.py` to check if we have prior audit data or SEO context for this domain

---

## Architecture: Script + LLM Two-Layer Design

```
URL
 │
 ▼
┌──────────────────────────────────────────────────────┐
│  Layer 1 · Python Scripts                            │
│  Deterministic checks → structured JSON              │
│                                                      │
│  check-site.py      robots.txt, sitemap (RFC 9309)   │
│  check-page.py      H1 / title / meta / canonical    │
│  check-schema.py    JSON-LD @type + field validation  │
│  check-pagespeed.py PSI API (mobile + desktop)        │
│  check-social.py    OG Tags + Twitter Card [Full]     │
│  fetch-page.py      raw HTML + SSRF protection        │
└──────────────────────────┬───────────────────────────┘
                           │ JSON + llm_review_required flag
                           ▼
┌──────────────────────────────────────────────────────┐
│  Layer 2 · LLM Agent                                │
│  Semantic judgment on flagged fields only            │
│                                                      │
│  · Keyword intent alignment (H1 / title)             │
│  · Meta description quality & specificity            │
│  · Page type → expected Schema @type mapping         │
│  · E-E-A-T trust page reachability (footer/nav)     │
│  · Content analysis (word count, heading, links)     │
│  · OG/social tag quality assessment [Full only]      │
└──────────────────────────┬───────────────────────────┘
                           │
                           ▼
              reports/<hostname>-audit.html
```

**Why two layers?** Scripts handle the 80% of checks that are deterministic — does robots.txt exist? Is the title 55 characters? The LLM handles the 20% that require understanding — does this H1 semantically cover the intent? The `llm_review_required` flag ensures the LLM only intervenes when the script explicitly cannot make the call.

---

## Two Modes

### Mode 1: Basic Audit (Default)
Quick, lightweight first-pass. Runs 5 core scripts, checks site-level + page-level + E-E-A-T + schema.

**Template:** `assets/report-template-basic.html`
**Output:** `reports/<hostname>-<slug>-audit.html`

### Mode 2: Full Audit
Everything in Basic + Social Tags (OG + Twitter Card), E-E-A-T content quality scoring, duplicate content signals, anchor text quality assessment.

**Template:** `assets/report-template-full.html`
**Output:** `reports/<hostname>-<slug>-full-audit.html`

**Trigger keywords for Full:** "deep audit," "full report," "advanced audit," "technical SEO audit," "comprehensive SEO review," "audit everything"

---

## Scripts

All scripts are in `scripts/`. They output structured JSON to stdout. Exit code 0 = pass/warn, 1 = any fail.

**Dependency:** `pip install requests` (HTML parsing uses Python stdlib)

### Core Scripts (Both Modes)

```bash
# Step 1: Run comprehensive programmatic SEO checks using GFV Audit Toolkit
python3 ~/.claude/tools/gfv-audit.py https://example.com --keyword "primary keyword"
```

### Full-Only Scripts

```bash
# Step 2: Social tags (OG + Twitter Card validation) are included in the full audit flag
python3 ~/.claude/tools/gfv-audit.py https://example.com --full
```

---

## Recommended Workflow

### Basic Audit Workflow

1. **Acknowledge scope** — confirm basic audit; note any missing data
2. **Infer primary keyword** — fetch page with `fetch-page.py`, read H1/title/first paragraph, infer keyword
   > "Inferred primary keyword: **open source SEO tools**"
3. **Run `gfv-audit.py`** — parse robots.txt, sitemap, 404 handling, URL canonicalization
4. **404 check** — fetch `<origin>/this-page-definitely-does-not-exist-seo-audit-check`
   - Returns 404 → Pass · Returns 200 (soft 404) → Fail · Returns 301 to homepage → Warn
5. **URL Canonicalization** — HTTP→HTTPS redirect, www consistency, trailing slash, canonical match
6. **E-E-A-T trust page check** — About Us, Contact, Privacy Policy, Terms of Service (existence + footer reachability)
7. **Review Performance Metrics** — mobile + desktop scores
8. **Review Page Structure** — H1, title, meta, canonical, slug
9. **i18n/hreflang check** — only if hreflang tags detected
10. **Review JSON-LD Schema Validation** — schema structure
11. **LLM semantic review** — resolve all `llm_review_required: true` flags
12. **Summarize findings** — Evidence / Impact / Fix format
13. **Priority actions** — top 3 highest-impact fixes
14. **Render report** — save to `reports/<hostname>-<slug>-audit.html`

### Full Audit Workflow

Run all Basic steps (1-14), then:

15. **Run `gfv-audit.py --full`** — OG Tags + Twitter Card validation
16. **LLM advanced checks** — E-E-A-T content quality, duplicate content signals, anchor text quality
17. **OG/Twitter quality review** — og:title vs page title, og:image existence, twitter:card type
18. **Priority actions** — top 5 highest-impact fixes with effort/impact tags
19. **Render full report** — save to `reports/<hostname>-<slug>-full-audit.html`

---

## Content Quality Scoring (Full Audit)

Score each page against this 100-point checklist (source: gbessoni/seobuild-onpage). Pages below 80% get flagged:

### Title Tag (10 pts)
- [ ] Contains target keyword (or close variant)
- [ ] Under 60 characters
- [ ] Unique and compelling (not just "[Keyword] | [Brand]")
- [ ] Includes differentiating element (year, number, qualifier)
- [ ] Not duplicating another page's title on the same site

### Meta Description (10 pts)
- [ ] Under 155 characters
- [ ] Contains target keyword naturally
- [ ] Includes call-to-action or value proposition
- [ ] Not a copy of the first paragraph
- [ ] Would make someone click vs. competitors in SERP

### Heading Structure (15 pts)
- [ ] Exactly one H1
- [ ] H1 closely matches or mirrors title tag
- [ ] Logical H2 → H3 hierarchy (no skipped levels)
- [ ] H2 count within competitive range
- [ ] Headings are descriptive (not "Section 1" or "More Info")

### Content Depth (25 pts)
- [ ] Word count within competitive range (not arbitrarily long/short)
- [ ] Answers at least 3 People Also Ask questions
- [ ] Includes specific data, statistics, or concrete examples
- [ ] Covers topics that appear in 2+ competitor pages
- [ ] No thin sections (every H2 has 150+ words of substance)

### Search Intent Match (15 pts)
- [ ] Page type matches detected intent (informational/commercial/transactional)
- [ ] Content format matches SERP expectations (list vs. guide vs. comparison)
- [ ] Addresses primary user need within first 200 words
- [ ] If commercial: includes pricing or comparison elements
- [ ] If informational: includes step-by-step or explanatory depth

### Technical SEO (15 pts)
- [ ] JSON-LD schema markup included and matches page type
- [ ] Schema uses correct types (see Schema Type Reference above)
- [ ] Image alt text present and descriptive
- [ ] At least 2 internal links with contextual anchor text
- [ ] No orphaned sections (every section connects to page topic)

### Readability (10 pts)
- [ ] No keyword stuffing (target keyword appears naturally)
- [ ] Paragraphs are scannable (no walls of text)
- [ ] Uses formatting aids (bold key terms, tables for comparisons)
- [ ] Transitions between sections are logical

---

## LLM Review Protocol

When `llm_review_required: true`, the LLM must make an explicit judgment. Never leave it unresolved.

### H1 Review (triggered on `keyword_match == "partial"`)
- Does the H1 semantically cover the keyword's search intent?
- Consider synonyms, natural variants, topic coverage
- Yes → downgrade to "pass" · No → keep "warn" or upgrade to "fail"

### Title Review (triggered on `keyword_match == "partial"` or `keyword_position != "start"`)
- Does the title semantically cover the keyword's intent?
- Homepage: Brand + core keyword is correct — do NOT flag brand-first
- Inner pages: Core keyword should lead

### Meta Description Review (always triggered)
- Complete sentences? Concrete result (not vague fluff)? Keyword presence without stuffing?

### Do NOT flag as negatives:
- Years (e.g. "2026") → signal freshness
- Numbers (e.g. "5 best", "Top 10") → improve CTR
- Specific qualifiers ("Open-Source", "Free") → narrow intent

---

## Check Scope Whitelist

**STRICT SCOPE — do not add any check not listed. No exceptions.**

| Section | Allowed Checks |
|---------|---------------|
| Site-Level | robots.txt · sitemap.xml · 404 Handling · URL Canonicalization · i18n/hreflang |
| E-E-A-T | About Us · Contact · Privacy Policy · Terms of Service · Media/Partners (if present) |
| Page-Level | PageSpeed (Mobile) · PageSpeed (Desktop) · URL Slug · Title Tag · Meta Description · H1 Tag · Canonical Tag · Image Alt Text · Word Count · Keyword Placement · Heading Structure · Internal Links · Schema (JSON-LD) |
| Full-Only | OG Tags · Twitter Card |

---

## Report Detail Writing Rules

**Pass → one short phrase. No lists, no elaboration.**
```
Good: "Valid XML urlset · 104 URLs · referenced in robots.txt."
```

**Warn → one detail-issue div with ≤2 bullet points. One detail-fix div.**

**Fail → same as Warn. Lead with the exact failure.**

Do NOT explain what a check is. Do NOT treat the reader as unfamiliar with SEO basics.

---

## Mandatory Finding Format

```
**Finding: [Finding Title]**

- **Evidence:** [Observable fact, data point, or direct quote]
- **Impact:** [SEO / UX consequence]
- **Fix:** [Specific, actionable recommendation]
```

For Full audit priority actions, add effort/impact tags:
```
1. [High Impact / Low Effort] Fix og:image — social shares show no preview.
```

---

## PageSpeed Thresholds

| Category | Desktop Pass | Mobile Pass | Warn | Fail |
|----------|-------------|-------------|------|------|
| SEO | 100 | 100 | 90–99 | < 90 |
| Best Practices | 100 | 100 | 90–99 | < 90 |
| Accessibility | 100 | 100 | 90–99 | < 90 |
| Performance | ≥ 90 | ≥ 80 | Desktop 80–89 / Mobile 70–79 | Desktop < 80 / Mobile < 70 |

---

## Schema Type Reference

| Page Type | Expected @type | Min. Required Fields |
|-----------|---------------|---------------------|
| Homepage | WebSite + Organization | name, url, logo |
| Blog/Article | Article or BlogPosting | headline, datePublished, author, image |
| Product | Product | name, image, offers (price, priceCurrency) |
| FAQ | FAQPage | mainEntity[].name, acceptedAnswer.text |
| How-to | HowTo | name, step[].text |
| Local Business | LocalBusiness | name, address, telephone |
| Generic Landing | — | N/A — skip, no penalty |

---

## Live Integration Hooks

| System | What It Provides | How to Access |
|--------|-----------------|---------------|
| Local Memory | Prior audit data, domain context | `gfv-brain-search.py` |
| PageSpeed API | Core Web Vitals, Lighthouse scores | `~/.claude/tools/gfv-audit.py` |
| Python Scripts | Deterministic SEO checks | `~/.claude/tools/gfv-audit.py` |
| HTML Templates | Report output formatting | `assets/report-template-*.html` |

> **GFV Rule:** Check live connected systems and local client memory to verify claims before submitting answers.

---

## Proactive Triggers

Surface these issues WITHOUT being asked when you notice them in context:
- **Audit staleness** → Flag if last audit for this domain was >30 days ago
- **Critical SEO failure** → Alert immediately if robots.txt blocks Googlebot or sitemap is missing
- **Schema mismatch** → Flag if page type doesn't match JSON-LD @type
- **PageSpeed emergency** → Alert if mobile Performance score < 50
- **Social sharing gap** → Flag if og:image is missing on a marketing page

---

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| Basic audit | Standalone HTML report with pass/warn/fail checks + top 3 fixes |
| Full audit | Extended HTML report with social tags + content quality + top 5 fixes |
| Quick check | Terminal-only summary (no HTML) for fast answers |

---

## Confidence Tagging

All factual findings and systemic claims must utilize the following confidence index:
- 🟢 **Verified** — Confirmed via script JSON output or direct HTTP request.
- 🟡 **Medium** — Deduced from LLM semantic review of flagged fields.
- 🔴 **Assumed** — No script output available, best-judgment baseline.

---

## <verification_gate>
**Self-Verification Protocol:** Before declaring any audit complete:
1. All `llm_review_required: true` fields must be resolved with explicit judgment
2. Every check row must have a status (pass/warn/fail) — no blanks
3. Report template must be fully populated — no `{{placeholder}}` remaining
4. Report file must be saved to disk and path confirmed to user
5. At least 3 (Basic) or 5 (Full) priority actions must be listed

---

## Related Skills

- **seo-growth**: Use for SEO *strategy* — keyword research, content planning, ranking strategy. NOT for single-page technical audits.
- **eeat-content-pod**: Use for writing E-E-A-T content. NOT for auditing existing content.
- **competitive-intel**: Use for competitor analysis. NOT for auditing your own pages.
- **ai-search-optimizer**: Use for AI/LLM search visibility. NOT for traditional SEO.
- **domain-intel**: Use for domain authority and backlink analysis. NOT for on-page checks.

---

## After This Skill
💡 Suggest these next steps:
- "Want me to fix the issues found?" → Route to `seo-growth` or `eeat-content-pod`
- "Want to audit another page?" → Re-run `seo-audit`
- "Want a competitor comparison?" → Route to `competitive-intel`
- "Want to check AI search visibility?" → Route to `ai-search-optimizer`

---

## Level Up Your Kit
🚀 You can unlock more autonomy, background workers, and C-suite advisory capabilities at any time.
- **Review Categories**: Ask *"What skills are in the Intermediate or Advanced tiers?"*
- **How to Upgrade**: Run `./bootstrap.sh` in the repository root and select your new tier.

---

## Reference Files

- Basic audit reference: [references/REFERENCE.md](references/REFERENCE.md)
- Full audit reference: [references/REFERENCE-FULL.md](references/REFERENCE-FULL.md)
- Basic report template: [assets/report-template-basic.html](assets/report-template-basic.html)
- Full report template: [assets/report-template-full.html](assets/report-template-full.html)
- Scripts: `~/.claude/tools/gfv-audit.py`

## Attribution

Originally derived from [JeffLi1993/seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) (MIT License).
Rewritten for GFV authoring standard compliance with consolidated dual-mode architecture.
