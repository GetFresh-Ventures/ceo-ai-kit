---
name: experiment-loop
description: "Apply the scientific method to any CEO initiative — define a metric, make ONE change per cycle, measure impact, keep or discard, repeat. Inspired by autoagent's autonomous hill-climbing methodology. Use when the CEO mentions 'test this,' 'experiment,' 'try and see,' 'A/B test,' 'iterate on,' 'what if we,' 'optimize,' 'is this working,' or any situation where systematic, measurable improvement beats guessing."
short_description: "Apply the scientific method to initiatives"
metadata:
  version: 1.0.0
  category: execution-infrastructure
  origin: autoagent (kevinrgu/autoagent)
  triggers:
    - test this
    - experiment
    - try and see
    - iterate on
    - optimize
    - is this working
    - what if we
    - A/B test
---

# Experiment Loop

Stop guessing. Use the scientific method to improve anything — ads, messaging, pricing, process, content, ops.


## Quick Start
Just say any of these:
- "Design an experiment to test [hypothesis]"
- "Track and measure the impact of [change]"
- "What did we learn from the [experiment]?"


## When to Activate

- Testing a new approach vs. the current baseline
- Optimizing a metric (leads, revenue, conversion, NPS, response rate)
- Evaluating whether a change helped, hurt, or was neutral
- Running structured A/B tests on any business initiative
- Any time the CEO says "let's try" — convert that impulse into a disciplined loop

## The Core Loop

```
1. BASELINE  → Measure the current state (the number to beat)
2. HYPOTHESIZE → One specific change + predicted impact
3. EXECUTE   → Make ONE change (not three)
4. MEASURE   → Same metric, same timeframe
5. DECIDE    → Keep, discard, or refine
6. LOG       → Record everything in the experiment ledger
7. REPEAT    → Next hypothesis
```

**The meta-agent pattern:** You are not solving the problem directly. You are *improving the system that solves the problem.* This means every cycle makes the overall operation better, even when individual experiments fail.

## Non-Negotiables

1. **One variable per experiment** — If you change three things, you learn nothing
2. **Baseline first** — Never skip establishing the "before" number
3. **Log everything** — Failed experiments teach as much as successes
4. **Simplicity criterion** — If same result with simpler approach, keep simpler
5. **No overfitting** — "If this exact situation disappeared, would this still be a worthwhile improvement?"

## Experiment Ledger Format

Maintain a running log (markdown table or TSV):

| # | Date | Hypothesis | Change Made | Metric Before | Metric After | Verdict | Notes |
|---|------|-----------|-------------|---------------|--------------|---------|-------|
| 1 | 2026-04-11 | Higher-intent keywords will reduce CPC | Replaced broad match with exact match | $45 CPC | $28 CPC | ✅ KEEP | 38% CPC reduction |
| 2 | 2026-04-12 | Night bidding wedge will capture emergency jobs | +40% bid adj 8pm-6am | 2 night leads/wk | 7 night leads/wk | ✅ KEEP | 3.5x increase |
| 3 | 2026-04-13 | Removing phone field will increase form conversion | 5-field → 4-field form | 12% conv rate | 11% conv rate | ❌ DISCARD | Phone field removal hurt trust signals |

## Keep / Discard Rules

Apply these strictly:

- **If the target metric improved → KEEP**
- **If the metric stayed the same but the approach is simpler → KEEP**
- **If the metric stayed the same and complexity increased → DISCARD**
- **If the metric got worse → DISCARD** (but extract the learning)
- **If the data is inconclusive → EXTEND** (run longer, don't decide on noise)

## Failure Analysis

When an experiment fails, diagnose the root cause:

| Failure Pattern | Example | What to Try Next |
|----------------|---------|-----------------|
| Wrong hypothesis | "Price is the objection" but it's actually trust | Test trust signals instead |
| Right hypothesis, wrong execution | Good keyword strategy but bad ad copy | Fix the execution, retest |
| Measurement error | Tracking was broken during the test period | Fix tracking, rerun |
| Insufficient sample | Only 50 visitors during test period | Extend test duration |
| External interference | Competitor launched same week | Wait for clean window |
| Overfitting | Optimized for one segment, hurt others | Broaden the change |

## CEO Application Examples

### Google Ads Optimization
```
Baseline: $45 CPC, 3% conversion rate
Experiment 1: Switch to exact match keywords → $28 CPC ✅ KEEP
Experiment 2: Add call extensions → 4.2% conversion rate ✅ KEEP
Experiment 3: Reduce landing page fields → No change ❌ DISCARD
```

### Sales Process
```
Baseline: 12% close rate, 45-day cycle
Experiment 1: Add ROI calculator to proposals → 15% close rate ✅ KEEP
Experiment 2: Shorten proposal from 10 → 5 pages → Same close rate, faster ✅ KEEP
Experiment 3: Send video proposal instead of PDF → 9% close rate ❌ DISCARD
```

### Content Strategy
```
Baseline: 500 monthly organic visitors
Experiment 1: Publish 2x/week instead of 1x → 750 visitors ✅ KEEP
Experiment 2: Add FAQ schema markup → 820 visitors (rich snippets) ✅ KEEP
Experiment 3: Switch to all video content → 600 visitors ❌ DISCARD
```

### Hiring / Outreach
```
Baseline: 8% email response rate
Experiment 1: Personalized first line → 14% response rate ✅ KEEP
Experiment 2: Shorter subject lines → 15% response rate ✅ KEEP
Experiment 3: Add mutual connection reference → Same ❌ DISCARD (added complexity)
```

## Integration with Other Skills

| When combined with... | The experiment loop covers... |
|----------------------|------------------------------|
| `conversion-optimizer` | A/B tests on forms, CTAs, landing pages |
| `seo-growth` | Content and technical SEO experiments |
| `sales-enablement` | Sales process and collateral experiments |
| `outreach-sequence` | Email cadence and messaging experiments |
| `content-strategy` | Content format and topic experiments |
| `pipeline-pulse` | Pipeline velocity and stage conversion experiments |

## The "Never Stop" Rule

Once the experiment loop begins on a metric:
- Do NOT stop after one experiment
- Do NOT declare victory on a single positive result
- Keep running until the CEO explicitly says "good enough" or the metric plateaus
- **Compound gains:** 5 small wins (each +10%) = 1.61x total improvement

## Quality Gate

Before logging any experiment result:
- [ ] Baseline was established before the change
- [ ] Only ONE variable was changed
- [ ] Sufficient sample size / time period
- [ ] Metric measured consistently (same source, same method)
- [ ] Learning extracted even from failed experiments
- [ ] Next hypothesis identified (the loop never stops)

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

- `strategic-decision` — For GO/NO-GO decisions informed by experiment data
- `decision-logger` — For recording strategic decisions with Memory integration
- `verify-execution` — For confirming experiments were implemented correctly


## After This Skill
💡 Suggest these next:
- "Try `decision-logger` — Log and recall your key decisions"
- "Try `conversion-optimizer` — Optimize conversion rates across funnels"
- "Try `scenario-war-room` — What-if modeling for strategic decisions"

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
