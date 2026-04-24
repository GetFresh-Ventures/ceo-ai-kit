---
name: conversion-optimizer
description: "Optimize conversion rates across forms, signup flows, landing pages, and onboarding experiences. Use when the CEO mentions 'conversion rate,' 'not converting,' 'form optimization,' 'signup flow,' 'landing page optimization,' 'onboarding,' 'CRO,' 'A/B test,' 'drop-off,' or 'abandoned forms.'"
short_description: "Optimize conversion rates across funnels"
metadata:
  version: 1.0.0
  category: growth-engine
  triggers:
    - conversion rate
    - not converting
    - form optimization
    - signup flow
    - landing page
    - onboarding
    - CRO
    - A/B test
    - drop-off
    - abandoned forms
---

# Conversion Optimizer

Find and fix the leaks in your conversion funnel — forms, signups, landing pages, and onboarding.


## Quick Start
Just say any of these:
- "Audit my signup flow for conversion leaks"
- "How do I improve my landing page conversion rate?"
- "A/B test ideas for my checkout page"


## When to Activate

- Form conversion optimization (lead gen, contact forms)
- Signup/registration flow optimization
- Landing page CRO
- Post-signup onboarding optimization
- A/B test planning and analysis
- Funnel drop-off diagnosis

## Form CRO

### Reduce Fields

**Default rule: Every field you remove increases conversion.**

| Field Count | Typical Impact |
|-------------|----------------|
| 10+ fields | High abandonment, only for qualified leads |
| 5-7 fields | Standard for B2B, reasonable friction |
| 3-4 fields | Good for top-of-funnel |
| 1-2 fields | Best for newsletter, free tools |

### Field Optimization

- **Remove** fields you can get later (company size, industry — enrich with Clearbit)
- **Default** fields when possible (country from IP, timezone)
- **Conditional** fields (only show if relevant)
- **Inline validation** — Don't wait until submit to show errors
- **Smart placeholders** — Show format examples ("123-456-7890")

### Trust Signals Near Forms

- "No credit card required"
- Security badges (if collecting payment)
- Privacy statement (GDPR/CCPA)
- Social proof (customer count, logos)

### Abandoned Form Recovery

- **Exit-intent popup** — Offer something (discount, free resource)
- **Email capture first** — If multi-step, get email on step 1
- **Retargeting** — Pixel the form page for remarketing

## Signup Flow CRO

### Reduce Steps

Map the current flow and cut:
```
Landing Page → Signup Form → Email Verification → 
Profile Setup → Onboarding → First Value

Ask: Which steps can be deferred or removed?
```

### Key Principles

1. **Value before friction** — Show the product before asking for details
2. **Progressive profiling** — Collect info over time, not all at once
3. **Social login** — Google/GitHub SSO reduces friction significantly
4. **Clear progress** — Show step X of Y if multi-step is necessary
5. **Skip everything possible** — Pre-fill, default, or defer

## Landing Page CRO

### Above the Fold Checklist

- [ ] Clear headline (what you do + for whom)
- [ ] Subheadline (the benefit or proof point)
- [ ] One primary CTA (visible without scrolling)
- [ ] Social proof (customer logos, review count, testimonials)
- [ ] No navigation menu (or minimal — reduce exit paths)

### Page Structure

```
1. Hero (headline + CTA)
2. Social proof (logos or testimonial)
3. Problem agitation
4. Solution overview
5. How it works (3 steps)
6. Benefits (not features)
7. Case study / proof
8. Pricing (if applicable)
9. FAQ
10. Final CTA
```

### CTA Optimization

| Bad CTA | Better CTA |
|---------|-----------|
| "Submit" | "Get My Free Quote" |
| "Sign Up" | "Start Free Trial" |
| "Contact Us" | "Get a Response in 2 Hours" |
| "Learn More" | "See How It Works" |

## Onboarding CRO

### Time to First Value

**Goal: Get the user to their "aha moment" as fast as possible.**

1. Identify the activation event (what makes users stick)
2. Remove every step between signup and that event
3. Use checklists, not tutorials (people skip tutorials)
4. Celebrate completion (micro-animations, congratulations)

### Onboarding Patterns

| Pattern | When to Use |
|---------|------------|
| **Product tour** | Complex UI, first-time user |
| **Checklist** | Multiple setup steps required |
| **Empty state** | Guide through first action |
| **Template gallery** | Value comes from pre-built content |
| **Wizard flow** | Configuration-heavy products |

## A/B Testing Framework

### What to Test (Priority Order)

1. **Headlines** — Highest impact, easiest to test
2. **CTA text and color** — Direct conversion impact
3. **Form length** — Field count affects completion
4. **Social proof** — Type and placement
5. **Page layout** — Hero vs. no hero, long vs. short

### Test Design

- **One variable per test** — Isolate what matters
- **Minimum sample size** — 1,000+ visitors per variant for statistical significance
- **Run for full weeks** — Account for day-of-week variation
- **Measure primary metric only** — Don't declare victory on secondary metrics

## Diagnosis Workflow

When conversion is "bad," diagnose systematically:

1. **Where do people drop off?** — Funnel analytics (GA4, Hotjar)
2. **What do they see?** — Check mobile AND desktop experience
3. **What do they expect?** — Does the page match the ad/source?
4. **What stops them?** — Forms too long? Trust missing? Value unclear?
5. **What would help?** — Hypothesis → test → learn

## Quality Gate

Before delivering CRO recommendations:
- [ ] Based on data, not opinion (where possible)
- [ ] Prioritized by expected impact
- [ ] Each recommendation includes what to do and how to measure success
- [ ] Quick wins separated from bigger projects
- [ ] Mobile experience addressed (not just desktop)

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

- `content-strategy` — Content planning for conversion paths
- `seo-growth` — Traffic acquisition
- `sales-enablement` — Post-lead conversion
- `launch-strategy` — Go-to-market planning

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Can't identify the leak | Start with funnel analytics — where's the biggest drop-off? |
| A/B tests inconclusive | You likely need more traffic volume. Run tests for at least 2 weeks |



## After This Skill
💡 Suggest these next:
- "Try `seo-growth` — Audit and optimize SEO — technical and content"
- "Try `sales-enablement` — Create sales collateral reps actually use"
- "Try `hubspot-architect` — Build HubSpot CRM integrations and pipelines"

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
