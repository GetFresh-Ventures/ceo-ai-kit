---
name: scenario-war-room
description: "Cross-functional what-if modeling for cascading multi-variable scenarios. Models compound adversity across all business functions simultaneously. Use when facing complex risk scenarios, strategic decisions with major downside, or when the CEO asks 'what if X AND Y both happen?'"
short_description: "What-if modeling for strategic decisions"
attribution: Adapted from alirezarezvani/claude-skills (MIT License), hardened for GFV portfolio context.
metadata:
  version: 1.0.0
  category: c-level
  domain: strategic-planning
  updated: 2026-04-11
---

# Scenario War Room

Model cascading what-if scenarios across all business functions. Not single-assumption stress tests — compound adversity that shows how one problem creates the next.

**Trigger phrases:** "what if", "worst case", "what happens if we lose", "pre-mortem", "stress test", "scenario plan", "risk model"

---


## Quick Start
Just say any of these:
- "What happens if we lose our biggest client?"
- "Model the impact of a 20% price increase"
- "Run a worst-case scenario for our Q3 forecast"


## What This Is NOT
- **Not** a single-assumption stress test (that's executive-mentor stress-test)
- **Not** financial modeling only — every function gets modeled
- **Not** worst-case-only — models 3 severity levels
- **Not** paralysis by analysis — outputs concrete hedges and triggers

---

## Step 1: Define Scenario Variables (max 3)

State each variable with:
- **What changes** — specific, quantified if possible
- **Probability** — your best estimate
- **Timeline** — when it hits

```
Variable A: Top customer (28% of revenue) gives 60-day termination notice
  Probability: 15% | Timeline: Within 90 days

Variable B: Key hire (lead tech or sales lead) resigns
  Probability: 20% | Timeline: Unknown

Variable C: Market downturn reduces inbound leads by 30%
  Probability: 25% | Timeline: Q3-Q4
```

**Max 3 variables per scenario.** More than 3 is noise — you can't meaningfully prepare for 5-variable collapse.

---

## Step 2: Domain Impact Mapping

For each variable, each relevant role models impact:

| Domain | Owner | Models |
|--------|-------|--------|
| Cash & runway | CFO Advisor | Burn impact, runway change, bridge options |
| Revenue | CRO Advisor | Revenue gap, churn cascade risk, pipeline |
| Operations | COO Advisor | Capacity, process risk, OKR impact |
| Marketing | CMO Advisor | CAC impact, competitive exposure |
| People | Founder Coach | Attrition cascade, hiring implications |
| Strategy | CEO Advisor | Direction impact, investor narrative |

---

## Step 3: Cascade Effect Mapping

**This is the core.** Show how Variable A triggers consequences that trigger Variable B's effects:

```
TRIGGER: Customer churn ($280K annual revenue)
  ↓
CFO: Revenue drops, cash runway shrinks from 14 → 9 months
  ↓
COO: Hiring freeze; 2 planned hires deferred
  ↓
CRO: Pipeline coverage drops; existing team stretched → close rates decline
  ↓
CMO: CAC increases as we fight harder for same leads
  ↓
CFO: [DEATH SPIRAL WARNING — if not interrupted here]
  ↓
INTERRUPT: Cut 2 low-ROI channels, redirect $50K/mo to highest-converting source
```

Name the cascade explicitly. **Show where it can be interrupted.**

---

## Step 4: Severity Matrix

Model three scenarios:

| Scenario | Definition | Recovery |
|----------|------------|---------|
| **Base** | One variable hits; others don't | Manageable with plan |
| **Stress** | Two variables hit simultaneously | Requires significant response |
| **Severe** | All variables hit; full cascade | Existential; requires board/investor intervention |

For each severity level:
- Runway impact (months)
- Revenue impact ($)
- Headcount impact
- Timeline to unacceptable state (trigger point)

---

## Step 5: Early Warning Signals

Define the measurable signal that tells you a scenario is unfolding **before** it's confirmed:

```
Trigger for Customer Churn Risk:
  - Sponsor goes dark for >3 weeks
  - Usage/engagement drops >25% MoM
  - No renewal conversation initiated 60 days before contract end
  - Customer mentions evaluating alternatives

Trigger for Key Person Departure:
  - Multiple referral interview requests from team members
  - Above-market counter-offer required in last 3 months
  - Glassdoor activity or LinkedIn "open to work" signals
  - Team member misses 2+ deadlines unusually

Trigger for Market Downturn:
  - Inbound lead volume drops >15% MoM for 2 consecutive months
  - Win rates decline >10% from trailing 6-month average
  - Competitor raises at lower valuation (market signal)
  - CAC increases >20% with no channel changes
```

---

## Step 6: Hedging Strategies

Actions to take **now** (before the scenario materializes) that reduce impact if it does.

| Hedge | Cost | Impact | Owner | Deadline |
|-------|------|--------|-------|----------|
| Diversify revenue concentration to <20% per customer | Sales effort | Reduces single-customer risk | CRO | 2 quarters |
| Retention bonus for 2-3 key people | $30-90K | Locks team through critical period | CEO | 30 days |
| Establish credit line or bridge option | $5K/year | Buys 3 months if revenue drops | CFO | 60 days |
| Document all key-person knowledge | Time | Reduces bus-factor risk | COO | 30 days |
| Pre-negotiate contract extensions with top 3 customers | Relationship | Reduces churn surprise risk | CRO | 45 days |

---

## Output Format

Every war room session produces:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 SCENARIO: [Name]
Variables: [A, B, C]
Most likely path: [which combination plays out, with probability]

SEVERITY LEVELS
Base (A only): [runway/revenue impact] — recovery: [X actions]
Stress (A+B): [runway/revenue impact] — recovery: [X actions]
Severe (A+B+C): [runway/revenue impact] — existential risk: [yes/no]

CASCADE MAP
[A → domain impact → B trigger → domain impact → interrupt point → end state]

EARLY WARNING SIGNALS
- [Signal 1 → which scenario it indicates]
- [Signal 2 → which scenario it indicates]
- [Signal 3 → which scenario it indicates]

HEDGES (take these actions now)
1. [Action] — cost: $X — impact: [what it buys] — owner: [role] — deadline: [date]
2. [Action] — cost: $X — impact: [what it buys] — owner: [role] — deadline: [date]
3. [Action] — cost: $X — impact: [what it buys] — owner: [role] — deadline: [date]

RECOMMENDED DECISION
[One paragraph. What to do, in what order, and why.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Common Scenarios by Stage

**Pre-seed / Seed:**
- Co-founder leaves + product misses market
- Cash runs out + bridge terms unfavorable
- Key customer churns + can't replace revenue fast enough

**Series A:**
- Miss revenue target + fundraise delayed
- Key customer churns + competitor raises
- Lead engineer quits + roadmap slips

**Series B+:**
- Market contraction + burn multiple spikes
- Lead investor wants pivot + team resists
- Regulatory change + compliance costs spike

**Home Services (Portfolio Co A, Portfolio Co C):**
- Top tech quits + peak season starts
- Google Ads cost spikes + lead volume drops
- Major equipment failure + customer complaints surge
- Field Service Platform data loss + billing disruption

---

## Rules for Good War Room Sessions

1. **Max 3 variables.** More is noise.
2. **Quantify or estimate.** "Revenue drops" is useless. "$280K at risk over 60 days" is useful.
3. **Don't stop at first-order effects.** The damage is in the cascade, not the initial hit.
4. **Model recovery, not just impact.** Every scenario needs a "what we do" path.
5. **Separate base from sensitivity.** Don't conflate "what probably happens" with "what could happen."
6. **3-4 scenarios per planning cycle.** More creates analysis paralysis.

---

## Integration with C-Suite Roles

| Scenario Type | Primary Roles | Cascade To |
|--------------|---------------|------------|
| Revenue miss | CRO, CFO | CMO (pipeline), COO (cuts) |
| Key person departure | Founder Coach, COO | CRO (if sales), CFO (if finance) |
| Cash crisis | CFO, CEO | COO (runway extension), CRO (accelerate revenue) |
| Market shift | CEO, CMO | CRO (repositioning), COO (new segments) |
| Competitor move | CMO, CRO | CEO (strategy response) |
| Operational failure | COO, CFO | CEO (comms), CRO (customer impact) |

---

## Proactive Triggers

- **CEO mentions "worried about" or "what if"** → offer war room session
- **Runway < 9 months detected** → auto-trigger cash crisis scenario
- **Customer concentration > 30%** → flag and offer churn cascade modeling
- **Key person risk detected** (from context or conversation) → offer departure scenario
- **Market signal detected** (competitor raise, pricing change) → offer competitive scenario

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Too many variables to model | Fix 80% of variables, vary only the 2-3 that matter most |
| Scenarios feel unrealistic | Ground them in historical data — 'what happened last time X occurred?' |



## After This Skill
💡 Suggest these next:
- "Try `decision-logger` — Log and recall your key decisions"
- "Try `ceo-advisor` — Strategic leadership and portfolio guidance"
- "Try `financial-analyst` — Financial ratios, DCF, and budget analysis"
