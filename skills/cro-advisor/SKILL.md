---
name: cro-advisor
description: "Revenue leadership for scaling companies. Revenue forecasting, sales model design, pricing strategy, net revenue retention, and pipeline management. Use when designing the revenue engine, setting quotas, evaluating pricing, building board forecasts, or when user mentions CRO, revenue strategy, sales model, pipeline, churn, pricing strategy, or sales capacity."
short_description: "Revenue operations and growth strategy"
attribution: Adapted from alirezarezvani/claude-skills (MIT License), tuned for GFV portfolio context.
---

# CRO Advisor

Revenue frameworks for building predictable, scalable revenue engines.


## Quick Start
Just say any of these:
- "Build my revenue forecast model"
- "What's leaking from my sales funnel?"
- "Design my sales compensation plan"


## Before Starting

Pull live context from:
- HubSpot → deal pipeline, stage conversion rates, deal velocity
- Business Systems → job revenue, close rates, average ticket
- QuickBooks → invoice data, AR aging, revenue by customer
- Local Memory → historical deal outcomes, entity relationships

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
| Business Systems | Job revenue, close rates, avg ticket, lead attribution | API connectors |
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
- **cfo-advisor**: Use for budget validation and margin analysis. NOT for pipeline strategy.
- **cmo-advisor**: Use for marketing-sourced pipeline and MQL quality. NOT for sales process.
- **ceo-advisor**: Use for strategic direction and capital allocation. NOT for revenue operations.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Revenue forecast inaccurate | Weight by pipeline stage probability, not rep confidence |
| Sales and marketing misaligned | Define MQL→SQL hand-off criteria. Review weekly with both teams |



## After This Skill
💡 Suggest these next:
- "Try `pipeline-pulse` — Active pipeline management and deal tracking"
- "Try `deal-review` — Pipeline review — flag stale deals, find gaps"
- "Try `conversion-optimizer` — Optimize conversion rates across funnels"

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
