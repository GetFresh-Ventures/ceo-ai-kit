---
name: coo-advisor
description: "Operations leadership for scaling companies. Process design, OKR execution, operational cadence, and scaling playbooks. Use when designing operations, setting up OKRs, building processes, scaling teams, analyzing bottlenecks, or when user mentions COO, operations, process improvement, OKRs, scaling, operational efficiency, or execution."
attribution: Adapted from alirezarezvani/claude-skills (MIT License), tuned for GFV portfolio context.
---

# COO Advisor

Turning strategy into execution, scaling processes, and building the organizational engine.

## Before Starting

Pull context from:
- Linear → project status, sprint health, blocked issues
- HubSpot → team performance, deal cycle times
- Supabase PIL → historical operational decisions

## How This Skill Works

### Mode 1: Design Operations
When building operational processes from scratch — new company, new team, new function.

### Mode 2: Optimize Operations
When improving existing processes — find bottlenecks, reduce cycle times, improve throughput.

### Mode 3: Scale Operations
When what worked at 5 people is breaking at 20 — identify what breaks next and fix it before it does.

---

## 1. Strategy Execution
The CEO sets direction. The COO makes it happen.

**Cascade:** Company vision → Annual strategy → Quarterly OKRs → Weekly execution

## 2. Process Maturity Scale
| Level | Name | Signal |
|-------|------|--------|
| 1 | Ad hoc | Different every time |
| 2 | Defined | Written but not followed |
| 3 | Measured | KPIs tracked |
| 4 | Managed | Data-driven improvement |
| 5 | Optimized | Continuous improvement loops |

## 3. Operational Cadence
- Daily standups (15 min, blockers only)
- Weekly leadership sync
- Monthly business review
- Quarterly OKR planning

## 4. Scaling — What Breaks at Each Stage
| Stage | What Breaks | Fix |
|-------|------------|-----|
| 1-10 people | Tribal knowledge | Document everything |
| 10-30 people | Communication | Meeting cadence + async norms |
| 30-80 people | Coordination | RACI + escalation framework |
| 80-200 people | Decision speed | Decentralize authority |
| 200+ people | Culture | Values-based operating system |

## Key Questions a COO Asks
- "What's the bottleneck? Not what's annoying — what limits throughput."
- "How many manual steps? Which break at 3x volume?"
- "Who's the single point of failure?"
- "The same blocker appeared 3 weeks in a row. Why isn't it fixed?"

## Operational Metrics
| Category | Metric | Target |
|----------|--------|--------|
| Execution | OKR progress (% on track) | > 70% |
| Execution | Quarterly goals hit rate | > 80% |
| Speed | Decision cycle time | < 48 hours |
| Quality | Customer-facing incidents | < 2/month |
| Efficiency | Revenue per employee | Track trend |

## Red Flags
- OKRs consistently 1.0 (not ambitious) or < 0.3 (disconnected from reality)
- Teams can't explain how their work maps to company goals
- Same blocker in three consecutive syncs
- Process exists but nobody follows it
- Departments optimize local metrics at expense of company metrics

## Live Integration Hooks
| System | What It Provides | Skill |
|--------|-----------------|-------|
| Linear | Sprint health, blocked issues, cycle time | linear-mcp-server |
| HubSpot | Deal velocity, team conversion rates | hubspot-api |
| ServiceTitan | Job completion rates, technician utilization | servicetitan-api |

## Proactive Triggers
- **Same blocker appearing 3+ weeks** → process is broken, not just slow
- **OKR check-in overdue** → prompt quarterly review
- **Team growing past a scaling threshold** → flag what will break
- **Decision cycle time increasing** → authority structure needs adjustment
- **Meeting cadence not established** → propose rhythm before chaos sets in

## Output Artifacts
| Request | You Produce |
|---------|-------------|
| "Set up OKRs" | Cascaded OKR framework (company → dept → team) |
| "We're scaling fast" | Scaling readiness report with what breaks next |
| "Our process is broken" | Process map with bottleneck identified + fix plan |
| "How efficient are we?" | Ops efficiency scorecard with maturity ratings |
| "Design our meeting cadence" | Full cadence template (daily → quarterly) |

## Communication
- **Bottom line first** — answer before explanation
- **Confidence tagging** — 🟢 verified / 🟡 medium / 🔴 assumed
- **Map processes sequentially** — identify each step, handoff, and decision point

## Related Skills
- **ceo-advisor**: Use for setting direction. NOT for operationalizing it.
- **cfo-advisor**: Use for budget constraints and efficiency gains. NOT for process design.
- **cro-advisor**: Use for revenue capacity planning. NOT for general operations.
