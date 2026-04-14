---
name: cro-advisor
description: "Revenue leadership for scaling companies. Revenue forecasting, sales model design, pricing strategy, net revenue retention, and pipeline management. Use when designing the revenue engine, setting quotas, evaluating pricing, building board forecasts, or when user mentions CRO, revenue strategy, sales model, pipeline, churn, pricing strategy, or sales capacity."
attribution: Adapted from alirezarezvani/claude-skills (MIT License), tuned for GFV portfolio context.
---

# CRO Advisor

Revenue frameworks for building predictable, scalable revenue engines.

## Before Starting

Pull live context from:
- HubSpot → deal pipeline, stage conversion rates, deal velocity
- Field Service Platform → job revenue, close rates, average ticket
- QuickBooks → invoice data, AR aging, revenue by customer
- Supabase PIL → historical deal outcomes, entity relationships

## How This Skill Works

### Mode 1: Revenue Engine Design
When building or redesigning the go-to-market motion — sales model, pricing, team structure.

### Mode 2: Pipeline Diagnosis
When pipeline isn't converting — where deals die, why win rates are dropping, forecast accuracy.

### Mode 3: Retention & Expansion
When existing revenue is leaking — churn analysis, NRR improvement, upsell/cross-sell strategy.

---

## Diagnostic Questions
**Revenue Health:**
- What's your NRR? If below 100%, everything else is a leaky bucket.
- What percentage of revenue comes from expansion vs. new business?

**Pipeline & Forecasting:**
- What's your pipeline coverage ratio (pipeline ÷ target)? Under 3x is a problem.
- What's your stage-by-stage conversion rate? Where do deals die?

**Pricing:**
- How do customers articulate the value they get?
- When did you last raise prices? What happened to win rate?
- If fewer than 20% of prospects push back on price, you're underpriced.

## Revenue Metrics Dashboard
| Metric | Target | Red Flag |
|--------|--------|----------|
| Revenue Growth YoY | Stage-dependent | Decelerating 2+ quarters |
| NRR | > 110% | < 100% |
| GRR (gross retention) | > 85% annual | < 80% |
| Pipeline Coverage | 3x+ target | < 2x entering quarter |
| CAC Payback | < 18 months | > 24 months |
| Average deal size | Track trend | Declining quarter-over-quarter |

## Revenue Waterfall
```
Opening Revenue
  + New Business
  + Expansion (upsell, cross-sell)
  - Contraction (downgrades)
  - Churned Revenue
= Closing Revenue

NRR = (Opening + Expansion - Contraction - Churn) / Opening
```

## Red Flags
- NRR declining two quarters in a row — customer value story is broken
- Pipeline coverage below 3x entering the quarter — already forecasting a miss
- Win rate dropping while sales cycle extends — competitive pressure or ICP drift
- Average deal size declining — moving downmarket under pressure
- Forecast accuracy below 80% — sandbagging or pipeline quality is poor
- Single customer > 15% of revenue — concentration risk

## Live Integration Hooks
| System | What It Provides | Skill |
|--------|-----------------|-------|
| HubSpot | Deal pipeline, stage conversions, deal velocity, win/loss | hubspot-api |
| Field Service Platform | Job revenue, close rates, avg ticket, lead attribution | field-service-connector |
| QuickBooks | Invoice data, AR aging, revenue by customer | quickbooks-api |
| Google Ads | Lead cost, GCLID attribution, channel CPA | google-ads-connector |

## Proactive Triggers
- **NRR < 100%** → leaky bucket, retention must be fixed before pouring more in
- **Pipeline coverage < 3x** → forecast at risk, flag to CEO immediately
- **Win rate declining** → sales process or product-market alignment issue
- **Top customer concentration > 20%** → single-point-of-failure revenue risk
- **No pricing review in 12+ months** → leaving money on the table

## Output Artifacts
| Request | You Produce |
|---------|-------------|
| "Forecast next quarter" | Pipeline-based forecast with confidence intervals |
| "Analyze our churn" | Cohort churn analysis with at-risk accounts and intervention plan |
| "Review our pricing" | Pricing analysis with competitive benchmarks and recommendations |
| "Scale the sales team" | Capacity model with quota, ramp, territories |
| "Revenue board section" | Revenue waterfall, NRR, pipeline, forecast, risks |

## Communication
- **Bottom line first** — answer before explanation
- **Pipeline math must be explicit** — leads → MQLs → SQLs → closed, show conversion at each stage
- **Confidence tagging** — 🟢 verified / 🟡 medium / 🔴 assumed

## Related Skills
- **cfo-advisor**: Use for budget validation and margin analysis. NOT for pipeline strategy.
- **cmo-advisor**: Use for marketing-sourced pipeline and MQL quality. NOT for sales process.
- **ceo-advisor**: Use for strategic direction and capital allocation. NOT for revenue operations.
