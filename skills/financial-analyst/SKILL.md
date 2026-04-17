---
name: financial-analyst
description: "Financial ratio analysis, DCF valuation, budget variance analysis, and rolling forecast construction. Use when analyzing financial statements, building valuation models, assessing budget variances, or constructing projections. Tactical counterpart to cfo-advisor."
short_description: "Financial ratios, DCF, and budget analysis"
attribution: Adapted from alirezarezvani/claude-skills (MIT License), tuned for GFV portfolio context.
---

# Financial Analyst

Production-ready financial analysis toolkit: ratio analysis, DCF valuation, budget variance, and rolling forecasts.


## Quick Start
Just say any of these:
- "Run a DCF valuation on this opportunity"
- "Analyze these financial ratios"
- "Compare these two investment options"


## Before Starting

Pull live financial data from:
- QuickBooks → income statement, balance sheet, cash flow
- HubSpot → deal values for revenue projections
- Local Memory → historical financial data

## How This Skill Works

### Mode 1: Financial Health Assessment
Ratio analysis across profitability, liquidity, leverage, efficiency.

### Mode 2: Valuation
DCF modeling with WACC, terminal value, and sensitivity analysis.

### Mode 3: Budget Variance
Actual vs budget vs prior year with materiality filtering.

### Mode 4: Forecasting
Driver-based revenue forecasting with scenario modeling.

---

## Ratio Categories
| Category | Ratios |
|----------|--------|
| **Profitability** | ROE, ROA, Gross Margin, Operating Margin, Net Margin |
| **Liquidity** | Current Ratio, Quick Ratio, Cash Ratio |
| **Leverage** | Debt-to-Equity, Interest Coverage, DSCR |
| **Efficiency** | Asset Turnover, Inventory Turnover, DSO |
| **Valuation** | P/E, P/B, P/S, EV/EBITDA |

## Key Accuracy Targets
| Metric | Target |
|--------|--------|
| Forecast accuracy (revenue) | +/-5% |
| Forecast accuracy (expenses) | +/-3% |
| Report delivery | 100% on time |
| Variance explanation | 100% of material variances |

## Live Integration Hooks
| System | What It Provides | Skill |
|--------|-----------------|-------|
| QuickBooks | Financial statements, invoices, AR/AP | quickbooks-api |
| HubSpot | Deal pipeline values, revenue forecasts | hubspot-api |

## Proactive Triggers
- **Gross margin declining 2+ periods** → investigate cost structure
- **AR aging > 60 days growing** → cash collection issue
- **Revenue forecast variance > 10%** → model needs recalibration
- **No scenario planning in current model** → build base/bull/bear

## Output Artifacts
| Request | You Produce |
|---------|-------------|
| "Analyze our financials" | Ratio scorecard with benchmarks and trends |
| "Value the company" | DCF model with sensitivity table |
| "Budget variance report" | Material variances with root causes |
| "Build a forecast" | Driver-based revenue forecast with scenarios |

## Communication
- **Show all math** — every calculation explicit
- **Be conservative** — model downside first, then upside
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
- **cfo-advisor**: Use for strategic financial decisions. Financial Analyst is the tactical engine.
- **ceo-advisor**: Use for capital allocation priorities. NOT for ratio analysis.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Valuation seems off | Check your discount rate and terminal growth assumptions first |
| Too many ratios, unclear story | Focus on the 3-5 ratios your audience cares about most |



## After This Skill
💡 Suggest these next:
- "Try `cfo-advisor` — Financial modeling, forecasting, and controls"
- "Try `spreadsheet-builder` — Build and analyze Excel spreadsheets"
- "Try `scenario-war-room` — What-if modeling for strategic decisions"
