---
name: geopolitical-monitor
description: Global intelligence pipeline with country instability scoring, geopolitical risk tracking, and supply chain impact analysis for international business.
short_description: "Global intelligence and risk monitoring"
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: Infrastructure
---

# /geopolitical-monitor

**Usage**: For CEOs with international exposure — track geopolitical events that could impact supply chains, market expansion plans, or client operations.


## Quick Start
Just say any of these:
- "What's the risk level in [country]?"
- "Monitor supply chain risks in [region]"
- "Brief me on geopolitical events affecting [industry]"


## Intelligence Pipeline

### 1. Source Ingestion
- Pull from verified news sources (Reuters, AP, BBC World, Financial Times).
- Filter exclusively for: regulatory changes, sanctions, tariffs, political instability, currency events, natural disasters.
- Ignore: opinion pieces, entertainment, sports.

### 2. Country Instability Index
Score each country on a 1-10 instability scale based on:
- Political stability (elections, coups, protests)
- Economic indicators (currency volatility, inflation)
- Regulatory changes (sanctions, trade restrictions)
- Security events (conflict, terrorism)

### 3. Pipeline Impact Mapping
Cross-reference geopolitical events against:
- Active deals in the CRM (which clients operate in affected regions?)
- Supply chain dependencies
- Expansion plans under evaluation

### 4. Executive Alert System
- 🔴 **CRITICAL**: Sanctions affecting active client, tariff impacting pricing
- 🟡 **MONITOR**: Political instability in expansion target market
- 🟢 **AWARE**: Background regulatory changes in secondary markets

## Output
Weekly 1-page global risk brief:
```
[REGION] | [EVENT] | [INSTABILITY: X/10] | [PIPELINE IMPACT: Deal Name / None]
```

## Constraints
- Source verification: minimum 2 independent sources before elevating any alert.
- Never speculate on geopolitical outcomes. Report facts, flag implications.

## Live Integration Hooks

| System | What It Provides | How to Access |
|--------|-----------------|---------------|
| PIL | Cross-session intelligence | `pil-memory-bus` / `gfv-brain-search.py` |
| HubSpot / CRM | Real-time pipeline state | `hubspot-api` |

> **GFV Rule:** Check PIL and live systems to verify claims before submitting answers.

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
- 🟡 **Medium** — Deduced from PIL/memory or recent but not validated real-time data.
- 🔴 **Assumed** — No source available, utilizing best-judgment baseline.

## <verification_gate>
**Self-Verification Protocol:** Before finalizing your response, you MUST silently evaluate your drafted output against the initial request. Have you provided concrete Action Items with ownership? Did you use the Bottom Line First formatting? Have you applied Confidence Tags to your claims? If not, rewrite the response before submitting.

## After This Skill
💡 Suggest these next:
- "Try `news-digest` — Extract intelligence from news and feeds"
- "Try `scenario-war-room` — What-if modeling for strategic decisions"
- "Try `ceo-advisor` — Strategic leadership and portfolio guidance"
