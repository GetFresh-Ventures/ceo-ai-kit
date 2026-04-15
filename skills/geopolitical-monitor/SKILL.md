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


## After This Skill
💡 Suggest these next:
- "Try `news-digest` — Extract intelligence from news and feeds"
- "Try `scenario-war-room` — What-if modeling for strategic decisions"
- "Try `ceo-advisor` — Strategic leadership and portfolio guidance"
