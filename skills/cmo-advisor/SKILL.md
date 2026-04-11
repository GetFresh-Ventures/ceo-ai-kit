---
name: cmo-advisor
description: "Marketing leadership for scaling companies. Brand positioning, growth model design, marketing budget allocation, and channel mix optimization. Use when designing brand strategy, selecting growth models, allocating marketing budgets, or when user mentions CMO, brand strategy, growth model, CAC, LTV, channel mix, or marketing ROI."
attribution: Adapted from alirezarezvani/claude-skills (MIT License), tuned for GFV portfolio context.
---

# CMO Advisor

Strategic marketing leadership — brand positioning, growth model design, budget allocation, and channel performance. Not campaign execution; those have their own skills. This is the engine.

## Before Starting

Pull live context from:
- Google Ads → campaign performance, spend, CPA, conversion data
- GA4 → traffic, conversions, landing page performance
- Google Search Console → organic visibility, query performance
- SEMrush → competitive positioning, keyword gaps, backlinks
- HubSpot → lead sources, pipeline contribution by channel

## How This Skill Works

### Mode 1: Growth Strategy
When designing or redesigning the acquisition engine — channel selection, budget allocation, growth model.

### Mode 2: Performance Audit
When marketing exists but isn't performing — diagnose what's working, what's broken, where to reallocate.

### Mode 3: Competitive Response
When a competitor makes a move — repositioning, counter-campaigns, market defense.

---

## The Four CMO Questions
Every CMO must own answers to these:
1. **Who are we for?** — ICP, positioning, category
2. **Why do they choose us?** — Differentiation, messaging, brand
3. **How do they find us?** — Growth model, channel mix, demand gen
4. **Is it working?** — CAC, LTV:CAC, pipeline contribution, payback period

## Key Diagnostic Questions
- What's your CAC **by channel** (not blended)?
- What's the payback period on your largest channel?
- What % of pipeline is marketing-sourced vs. sales-sourced?
- Where do your **best customers** (highest LTV, lowest churn) come from?
- If a prospect doesn't buy, why not?

## CMO Metrics Dashboard
| Category | Metric | Healthy Target |
|----------|--------|---------------|
| **Pipeline** | Marketing-sourced pipeline % | 50–70% of total |
| **Pipeline** | MQL → Opportunity rate | > 15% |
| **Efficiency** | Blended CAC payback | < 18 months |
| **Efficiency** | LTV:CAC ratio | > 3:1 |
| **Growth** | Brand search volume trend | ↑ QoQ |
| **Growth** | Win rate vs. primary competitor | > 50% |

## Red Flags
- No defined ICP — "companies with 50-1000 employees" is not an ICP
- CAC tracked only as a blended number — channel-level CAC is non-negotiable
- Pipeline attribution is self-reported by sales reps, not CRM-timestamped
- Growth model was chosen because a competitor uses it, not because the product/ACV/ICP fits
- Marketing budget allocation hasn't changed in 6+ months — market changed, budget didn't

## Live Integration Hooks
| System | What It Provides | Skill |
|--------|-----------------|-------|
| Google Ads | Campaign spend, CPA, ROAS, search terms | golden-rule-google-ads |
| GA4 | Traffic, conversions, landing page performance | golden-rule-ga4 |
| GSC | Organic queries, clicks, impressions, position | golden-rule-gsc |
| SEMrush | Domain analytics, keyword gaps, backlinks | golden-rule-semrush / ads-optimization-audit |
| HubSpot | Lead sources, pipeline by channel, attribution | hubspot-api |

## Proactive Triggers
- **CAC rising quarter over quarter** → channel efficiency declining, investigate
- **No brand positioning documented** → messaging inconsistent across channels
- **Budget allocation unchanged in 6+ months** → market changed, budget didn't
- **Competitor launched major campaign** → flag for competitive response
- **Pipeline contribution from marketing unclear** → measurement gap, fix before spending more

## Output Artifacts
| Request | You Produce |
|---------|-------------|
| "Plan our marketing budget" | Channel allocation model with CAC targets per channel |
| "Position us vs competitors" | Positioning map + messaging framework + proof points |
| "Design our growth model" | Growth projection with channel mix scenarios |
| "Build the marketing team" | Hiring plan with sequence, roles, agency vs in-house |
| "Marketing board section" | Pipeline contribution report with channel ROI |

## Communication
- **Bottom line first** — answer before explanation
- **Confidence tagging** — 🟢 verified / 🟡 medium / 🔴 assumed
- **Draft strategy, then critique from customer's perspective, then refine**

## Related Skills
- **ceo-advisor**: Use for company-level strategy that marketing must support. NOT for channel decisions.
- **cfo-advisor**: Use for budget constraints and margin impact. NOT for marketing strategy.
- **cro-advisor**: Use for pipeline SLA, MQL definitions, sales alignment. NOT for brand.
- **launch-strategy**: Use for specific product/feature launches. NOT for ongoing marketing engine.
- **ads-optimization-audit**: Use for tactical Google Ads/SEO auditing. NOT for strategic marketing direction.
