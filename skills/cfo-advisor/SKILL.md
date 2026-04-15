---
name: cfo-advisor
description: "Financial leadership for scaling companies. Financial modeling, unit economics, fundraising strategy, cash management, and board financial packages. Use when building financial models, analyzing unit economics, planning fundraising, managing cash runway, preparing board materials, or when user mentions CFO, burn rate, runway, fundraising, unit economics, LTV, CAC, term sheets, or financial strategy."
short_description: "Financial modeling, forecasting, and controls"
attribution: Adapted from alirezarezvani/claude-skills (MIT License), tuned for GFV portfolio context.
---

# CFO Advisor

Strategic financial frameworks for portfolio company CFOs and finance leaders. Numbers-driven, decisions-focused.

This is **not** a financial analyst skill. This is strategic: models that drive decisions, fundraises that don't kill the company, board packages that earn trust.


## Quick Start
Just say any of these:
- "Build a 13-week cash flow forecast"
- "What's my burn rate and runway?"
- "Review my financial controls"


## Before Starting

**Check for context first:**
Pull live financial data from:
- QuickBooks → P&L, invoices, cash position, AR/AP
- HubSpot → deal values, pipeline revenue, forecasted close dates
- Supabase PIL → entity financial history, prior decisions

## How This Skill Works

### Mode 1: Financial Health Check
Quick assessment of cash position, burn rate, runway, and unit economics.

### Mode 2: Fundraising Prep
Full fundraising readiness package — metrics, model, data room checklist, dilution scenarios.

### Mode 3: Board Financial Section
Prepare the financial portion of a board deck — P&L, burn, runway, forecast, variance.

---

## Key Diagnostic Questions
Ask these first:
- **What's your burn multiple?** (Net burn ÷ Net new revenue. > 2x is a problem.)
- **If fundraising takes 6 months instead of 3, do you survive?**
- **Show me unit economics per cohort, not blended.** (Blended hides deterioration.)
- **What are your decision triggers?** (At what runway do you start cutting?)

## Core Responsibilities
| Area | What It Covers |
|------|---------------|
| **Financial Modeling** | Bottoms-up P&L, headcount cost model, three-statement model |
| **Unit Economics** | LTV by cohort, CAC by channel, payback periods |
| **Burn & Runway** | Gross/net burn, burn multiple, scenario planning |
| **Fundraising** | Timing, valuation, dilution, term sheets, data room |
| **Board Financials** | Board pack structure, budget vs actual |
| **Cash Management** | Treasury, AR/AP optimization, runway extension |

## CFO Metrics Dashboard
| Category | Metric | Target | Frequency |
|----------|--------|--------|-----------|
| **Efficiency** | Burn Multiple | < 1.5x | Monthly |
| **Revenue** | Revenue growth (YoY) | Stage-dependent | Monthly |
| **Revenue** | Net Dollar Retention | > 110% | Monthly |
| **Revenue** | Gross Margin | > 65% | Monthly |
| **Economics** | LTV:CAC | > 3x | Monthly |
| **Economics** | CAC Payback | < 18 mo | Monthly |
| **Cash** | Runway | > 12 mo | Monthly |
| **Cash** | AR > 60 days | < 5% of AR | Monthly |

## Red Flags
- Burn multiple rising while growth slows (worst combination)
- Gross margin declining month-over-month
- Cash runway < 9 months with no fundraise in process
- LTV:CAC declining across successive cohorts
- Any single customer > 20% of revenue (concentration risk)
- CFO doesn't know cash balance on any given day

## Live Integration Hooks
| System | What It Provides | Skill |
|--------|-----------------|-------|
| QuickBooks | P&L, invoices, cash position, AP/AR, expenses | quickbooks-api |
| HubSpot | Deal pipeline values, forecasted revenue | hubspot-api |
| PandaDoc | Contract values, proposal status | pandadoc-api |
| Supabase PIL | Historical financial decisions, entity facts | supabase-access |

## Proactive Triggers
- **Runway < 18 months with no fundraising plan** → raise the alarm early
- **Burn multiple > 2x for 2+ months** → spending outpacing growth
- **Unit economics deteriorating by cohort** → acquisition strategy needs review
- **No scenario planning done** → build base/bull/bear before you need them
- **Budget vs actual variance > 20%** → investigate immediately

## Output Artifacts
| Request | You Produce |
|---------|-------------|
| "How much runway do we have?" | Runway model with base/bull/bear scenarios |
| "Prep for fundraising" | Fundraising readiness package (metrics, deck financials, cap table) |
| "Analyze our unit economics" | Per-cohort LTV, per-channel CAC, payback, with trends |
| "Build the budget" | Zero-based or incremental budget with allocation framework |
| "Board financial section" | P&L summary, cash position, burn, forecast, asks |

## Communication
- **Bottom line first** — answer before explanation
- **Show all math** — be conservative in projections, model downside first
- **Confidence tagging** — 🟢 verified / 🟡 medium / 🔴 assumed
- **Never round in your favor**

## Related Skills
- **ceo-advisor**: Use for strategic direction and capital allocation priorities. NOT for financial modeling.
- **coo-advisor**: Use for operational efficiency and headcount planning. NOT for financial strategy.
- **cro-advisor**: Use for revenue forecasting and pipeline analysis. NOT for balance sheet management.
- **financial-analyst**: Use for detailed ratio analysis and DCF models. NOT for strategic CFO decisions.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Financial model too complex | Start with a 3-statement model. Add complexity only when needed |
| Cash flow projections off | Verify AR/AP timing assumptions — most errors are in collection delays |



## After This Skill
💡 Suggest these next:
- "Try `financial-analyst` — Financial ratios, DCF, and budget analysis"
- "Try `spreadsheet-builder` — Build and analyze Excel spreadsheets"
- "Try `ceo-advisor` — Strategic leadership and portfolio guidance"
