---
name: spreadsheet-builder
description: "Build, edit, and analyze spreadsheets (.xlsx, .csv) with investment-grade standards. Use when the CEO needs financial models, P&L templates, forecasting, pipeline tracking, board-ready data exports, scenario analysis, or any structured tabular deliverable. Triggers on 'spreadsheet,' 'Excel,' 'financial model,' 'P&L,' 'budget,' 'forecast,' 'xlsx,' or 'csv.'"
metadata:
  version: 1.0.0
  category: document-processing
  triggers:
    - spreadsheet
    - excel
    - financial model
    - P&L
    - budget
    - forecast
    - xlsx
    - csv
---

# Spreadsheet Builder

Build spreadsheets that are investor-defensible, not just functional.

## When to Activate

- Creating financial models, P&L projections, or budget forecasts
- Building board-ready data exports or KPI dashboards
- Cleaning and restructuring messy tabular data
- Creating scenario analysis (bear/base/bull)
- Pipeline tracking exports from HubSpot or CRM data
- Unit economics models, cohort analysis, or LTV calculations
- Any task where the deliverable must be an `.xlsx` or `.csv` file

## Portfolio Co A

**Use Excel formulas, never hardcoded calculations.** The spreadsheet must remain dynamic — if source data changes, everything recalculates.

## Financial Model Standards

### Color Coding (Investment Banking Standard)

| Color | Usage |
|-------|-------|
| **Blue text** (RGB: 0,0,255) | Hardcoded inputs, assumptions the user will change |
| **Black text** (RGB: 0,0,0) | ALL formulas and calculations |
| **Green text** (RGB: 0,128,0) | Cross-sheet references within same workbook |
| **Red text** (RGB: 255,0,0) | External file links |
| **Yellow background** (RGB: 255,255,0) | Key assumptions needing attention |

### Number Formatting

- **Years**: Text strings ("2026" not "2,026")
- **Currency**: `$#,##0` format; ALWAYS specify units in headers ("Revenue ($mm)")
- **Zeros**: Format all zeros as "-" (e.g., `$#,##0;($#,##0);-`)
- **Percentages**: Default to 0.0% format (one decimal)
- **Multiples**: Format as 0.0x for valuation multiples (EV/EBITDA, P/E)
- **Negative numbers**: Use parentheses `(123)` not minus `-123`

## Formula Rules

### Assumptions Placement
- Place ALL assumptions in separate, clearly labeled assumption cells
- Use cell references, never hardcoded values in formulas
- Example: Use `=B5*(1+$B$6)` instead of `=B5*1.05`

### Error Prevention
- Zero formula errors — no `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NAME?`
- Test with edge cases (zero values, negative numbers)
- Verify no unintended circular references
- Cross-check all cross-sheet references

### Documentation
- Comment every hardcoded value with source: "Source: [System], [Date], [Reference]"
- Add notes for key calculations and model sections

## CEO Template Library

### 1. Startup Financial Model
```
Assumptions (Sheet 1)
├── Revenue Assumptions (pricing, growth rates, churn)
├── Cost Assumptions (COGS, headcount, marketing spend)
├── Funding Assumptions (raise size, runway target)

P&L (Sheet 2)
├── Revenue (MRR → ARR, by product/tier)
├── COGS
├── Gross Margin
├── Operating Expenses (by department)
├── EBITDA
├── Net Income

Cash Flow (Sheet 3)
├── Operating Cash Flow
├── Capex
├── Financing (funding rounds)
├── Net Cash / Runway

Scenarios (Sheet 4)
├── Bear Case (0.7x revenue, 1.2x costs)
├── Base Case
├── Bull Case (1.3x revenue, 0.9x costs)
```

### 2. Board KPI Dashboard
```
Monthly KPIs
├── Revenue (MRR, ARR, growth %)
├── Customers (new, churned, net)
├── Unit Economics (CAC, LTV, LTV:CAC)
├── Cash (balance, burn rate, runway months)
├── Team (headcount, open roles)
```

### 3. Pipeline Tracker
```
Deal Pipeline
├── Deal name, company, owner
├── Stage, probability, weighted value
├── Expected close date
├── Summary: Total pipeline, weighted pipeline, by stage
```

## Implementation

### Creating Excel Files (Python + openpyxl)
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
sheet = wb.active
sheet.title = "Assumptions"

# Headers with formatting
sheet['A1'] = 'Assumption'
sheet['B1'] = 'Value'
sheet['A1'].font = Font(bold=True)
sheet['B1'].font = Font(bold=True)

# Blue text for inputs
sheet['B2'] = 15000
sheet['B2'].font = Font(color='0000FF')  # Blue = input

# Formulas in black
sheet['B10'] = '=SUM(B2:B9)'
sheet['B10'].font = Font(color='000000')  # Black = formula

wb.save('model.xlsx')
```

### Reading Data (Python + pandas)
```python
import pandas as pd
df = pd.read_excel('file.xlsx', sheet_name=None)  # All sheets
```

## Quality Gate

Before delivering any spreadsheet:
- [ ] Zero formula errors
- [ ] All assumptions in blue, all formulas in black
- [ ] Units specified in every header
- [ ] Scenarios included if model involves projections
- [ ] Cross-sheet references verified
- [ ] The model tells a clear story (an investor can follow the logic)

## Related Skills

- `financial-analyst` — deep financial analysis and commentary
- `board-deck-builder` — visual board presentations
- `investor-materials` — pitch deck and fundraising docs (coming soon)
