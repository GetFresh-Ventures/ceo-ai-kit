---
name: seo-growth
description: "Audit and optimize SEO — technical SEO, on-page optimization, schema markup, site architecture, and AI search optimization. Use when the CEO mentions 'SEO,' 'not ranking,' 'traffic dropped,' 'Google rankings,' 'structured data,' 'schema,' 'site structure,' 'why aren't we showing up,' or 'AI search optimization.'"
short_description: "Audit and optimize SEO — technical and content"
metadata:
  version: 1.0.0
  category: growth-engine
  triggers:
    - SEO
    - not ranking
    - traffic dropped
    - Google rankings
    - structured data
    - schema
    - site structure
    - why aren't we showing up
    - rich snippets
    - AI search
---

# SEO Growth

Diagnose SEO issues and implement fixes that move rankings, not just check boxes.


## Quick Start
Just say any of these:
- "Audit my website's SEO"
- "What keywords should I target?"
- "Fix my site's technical SEO issues"


## When to Activate

- Auditing SEO technical health
- Diagnosing traffic drops or ranking losses
- Implementing structured data / schema markup
- Planning site architecture and URL structure
- Optimizing for AI search engines (Perplexity, ChatGPT Search, Gemini)
- Building internal linking strategy
- Identifying keyword cannibalization

## SEO Audit Framework

### 1. Technical SEO

Diagnose infrastructure issues that prevent indexing:

| Check | How | Fix |
|-------|-----|-----|
| **Crawlability** | Check robots.txt, XML sitemap | Ensure all important pages are crawlable |
| **Indexation** | `site:domain.com` in Google | Submit missing pages via GSC |
| **Page Speed** | Core Web Vitals (LCP, CLS, INP) | Optimize images, defer JS, fix layout shifts |
| **Mobile** | Mobile-friendly test | Responsive design, tap targets, font sizes |
| **HTTPS** | Check SSL cert | Force HTTPS redirect |
| **Canonical tags** | Check for duplicates | Add canonical to preferred version |
| **404 errors** | GSC Coverage report | 301 redirect or restore content |

### 2. On-Page SEO

Optimize individual page elements:

| Element | Best Practice |
|---------|--------------|
| **Title tag** | Primary keyword + brand, 50-60 chars |
| **Meta description** | Action-oriented, 150-160 chars |
| **H1** | One per page, includes primary keyword |
| **Heading hierarchy** | H1 → H2 → H3, logical structure |
| **Internal links** | 3-5 per page to related content |
| **Image alt text** | Descriptive, includes keyword when natural |
| **URL structure** | Short, descriptive, includes keyword |

### 3. Content Quality (E-E-A-T)

Google evaluates Experience, Expertise, Authoritativeness, Trust:

- **Experience**: Show first-hand experience with the topic
- **Expertise**: Author credentials visible, bio pages
- **Authoritativeness**: Backlinks, citations, brand mentions
- **Trust**: Accurate info, secure site, transparent business info

## Schema Markup Implementation

### Common Schema Types

```json
// LocalBusiness (for service companies)
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Company Name",
  "address": { ... },
  "telephone": "...",
  "openingHours": "Mo-Fr 08:00-17:00",
  "priceRange": "$$"
}

// FAQ (for rich snippets)
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How much does X cost?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "..."
    }
  }]
}

// Service (for service pages)
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "HVAC Installation",
  "provider": { ... },
  "areaServed": { ... }
}
```

### Schema Validation
- Test with [Rich Results Test](https://search.google.com/test/rich-results)
- Validate with [Schema.org Validator](https://validator.schema.org/)

## Site Architecture Planning

### URL Structure
```
domain.com/
├── /services/
│   ├── /services/plumbing/
│   ├── /services/heating/
│   └── /services/cooling/
├── /locations/
│   ├── /locations/salt-lake-city/
│   └── /locations/des-moines/
├── /blog/
│   ├── /blog/category-1/
│   └── /blog/category-2/
└── /about/
```

### Internal Linking Strategy
- Hub pages link to all cluster pages
- Cluster pages link back to hub
- Related cluster pages cross-link
- Use descriptive anchor text (not "click here")

## AI Search Optimization

Optimize for AI search engines (Perplexity, ChatGPT Search, Google AI Overviews):

1. **Answer questions directly** — AI search pulls concise, authoritative answers
2. **Structure content with clear headers** — AI extracts by section
3. **Use statistics and data** — AI prefers citable facts
4. **Build topical authority** — Deep coverage of a topic increases citation likelihood
5. **Get cited in Wikipedia, Reddit, forums** — AI trains on these sources
6. **Maintain E-E-A-T signals** — Author bios, credentials, first-hand experience

## Traffic Drop Diagnosis

When traffic drops, check in order:
1. **Google algorithm update?** — Check industry news, MozCast
2. **Indexing issue?** — GSC Coverage report
3. **Technical problem?** — Server errors, redirect loops, robots.txt changes
4. **Content decay?** — Pages losing freshness signals
5. **Competitor surge?** — New competitor ranking for your keywords
6. **Seasonality?** — Compare to same period last year

## GSC Intelligence Analysis

### Cannibalization Detection
When two or more of your pages compete for the same query and split traffic:
1. Pull GSC data for last 90 days — look for queries with 2+ URLs getting clicks
2. For each cannibalized query, identify the **stronger page** (higher CTR + more backlinks)
3. **Action**: Merge/redirect the weaker page, or differentiate intent (informational vs. transactional)
4. Add canonical tag on weaker page pointing to stronger page

### Striking Distance Keywords
Keywords ranking in positions 8-15 with 1,000+ impressions — easiest traffic wins:
1. Filter GSC: `position >= 8 AND position <= 15 AND impressions >= 1000`
2. Sort by impressions descending — these have the most traffic potential
3. For each: optimize title tag, add FAQ schema, improve internal linking
4. Expected result: moving from page 2 to page 1 ~4-10x click increase

### Z-Score Anomaly Detection
Detect sudden traffic drops/spikes statistically:
1. Pull daily clicks for 90 days, compute mean and standard deviation
2. Any day > 2 standard deviations from mean = anomaly
3. Cross-reference anomaly dates with: algorithm updates, site deployments, server issues
4. Flag pages responsible for >50% of the drop

### Opportunity Score Matrix
Rank keywords by `Impressions ÷ Position` to find highest-leverage optimizations:
- **High impressions + poor position** = massive opportunity (content needs work)
- **Low impressions + good position** = niche maintained (low priority)
- **High impressions + good position** = protect and maintain

### Brand vs. Non-Brand Segmentation
Split all GSC data into brand and non-brand:
- Brand: queries containing your company/product name
- Non-brand: everything else
- **Health check**: If >60% of organic traffic is brand-only, you're not capturing demand → focus on informational/transactional content

## Quality Gate

Before delivering SEO recommendations:
- [ ] Prioritized by impact (not just easy wins)
- [ ] Technical issues ranked before content issues
- [ ] Specific URLs identified (not generic advice)
- [ ] Schema validated with testing tools
- [ ] Recommendations are actionable (who does what, by when)

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

- `content-strategy` — Content planning and prioritization
- `competitive-intel` — Competitor analysis
- `launch-strategy` — Go-to-market planning

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Rankings dropped suddenly | Check Google Search Console for manual actions or crawl errors first |
| No organic traffic growth | Verify pages are indexed — use `site:yourdomain.com` in Google |



## After This Skill
💡 Suggest these next:
- "Try `content-strategy` — Plan and execute your content calendar"
- "Try `eeat-content-pod` — Build E-E-A-T verified content for decaying pages"
- "Try `ai-search-optimizer` — Optimize your content for AI search engines"
- "Try `competitive-intel` — Track competitors and market positioning"
