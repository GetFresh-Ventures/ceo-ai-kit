---
name: financial-analyst
description: "Financial ratio analysis, DCF valuation, budget variance analysis, and rolling forecast construction. Use when analyzing financial statements, building valuation models, assessing budget variances, or constructing projections. Tactical counterpart to cfo-advisor."
attribution: Adapted from alirezarezvani/claude-skills (MIT License), tuned for GFV portfolio context.
---

# Financial Analyst

Production-ready financial analysis toolkit: ratio analysis, DCF valuation, budget variance, and rolling forecasts.

## Before Starting

Pull live financial data from:
- QuickBooks → income statement, balance sheet, cash flow
- HubSpot → deal values for revenue projections
- Supabase PIL → historical financial data

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

## Related Skills
- **cfo-advisor**: Use for strategic financial decisions. Financial Analyst is the tactical engine.
- **ceo-advisor**: Use for capital allocation priorities. NOT for ratio analysis.
