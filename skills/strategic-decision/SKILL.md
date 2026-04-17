---
name: strategic-decision
short_description: "Framework for high-stakes strategic choices"
description: >
  Multi-phase strategic decision framework for CEO founders. Orchestrates research, feasibility,
  planning, and implementation for any business initiative — product launches, market entry,
  hiring, fundraising, partnerships, or pivots. Triggers on "should we", "evaluate", "feasibility",
  "go/no-go", "strategic decision", "initiative review", or any request requiring structured
  decision-making before committing resources.
---

# Strategic Decision Framework

**Pattern:** Research → Plan → Implement (RPI)
**Adapted from:** claude-code-best-practice RPI workflow
**Purpose:** Prevent wasted effort on non-viable initiatives. Ensure every major decision has a structured audit trail.

---


## Quick Start
Just say any of these:
- "Walk me through this strategic decision"
- "What's the best framework for deciding [X]?"
- "Help me evaluate these 3 options rigorously"


## When to Use

- CEO is considering a new product, feature, market, hire, or partnership
- Any initiative requiring >$10K in resources or >2 weeks of effort
- Board-level decisions that need structured justification
- "Should we do X?" questions that deserve more than a gut check

## Decision Taxonomy

Every initiative receives one of four verdicts:

| Verdict | Meaning | Next Action |
|---------|---------|-------------|
| **GO** | Proceed with confidence | Move to Plan phase |
| **CONDITIONAL GO** | Proceed only if conditions are met | Address conditions, then re-evaluate |
| **DEFER** | Not now, but revisit later | Set a reminder date, archive research |
| **NO-GO** | Do not proceed | Document rationale, archive for reference |

---

## Phase 1: Capture & Parse the Initiative

**Goal:** Turn raw CEO thinking into structured requirements.

### Process

1. **Collect the brief** — Accept the initiative description in any form:
   - Stream-of-consciousness verbal dump
   - Slack thread or email chain
   - Meeting notes or transcript excerpt
   - Single sentence ("should we expand to Austin?")

2. **Parse into structured format:**

```markdown
## Initiative Brief

**Name:** [concise initiative name]
**Type:** [product | market | hire | partnership | fundraise | pivot | process | technology]
**Sponsor:** [who is championing this]
**Stage:** [pre-seed | seed | series-a | series-b | growth | enterprise]

### Problem Statement
[What problem does this solve? For whom?]

### Proposed Solution
[What is the CEO proposing?]

### Success Criteria
[How do we know this worked? 3-5 measurable outcomes]

### Constraints
[Budget, timeline, team, technology, regulatory]

### Open Questions
[What we don't know yet — these drive the research phase]
```

3. **Save to:** `decisions/{initiative-slug}/BRIEF.md`

---

## Phase 2: Multi-Angle Research

**Goal:** Evaluate the initiative from 5 independent perspectives before making a GO/NO-GO call.

### Perspective 1: Market & Product Viability

**Invoke:** `[INVOKE:cmo-advisor|Evaluate market viability of this initiative]`

Analyze:
- Market size and growth trajectory
- Customer demand signals (existing data, search volume, competitor traction)
- Competitive landscape — who else is doing this?
- Differentiation — why us, why now?
- Go-to-market complexity

**Output:** Market viability score (High/Medium/Low) with rationale.

### Perspective 2: Financial Feasibility

**Invoke:** `[INVOKE:cfo-advisor|Evaluate financial feasibility of this initiative]`

Analyze:
- Total cost to execute (people, tools, marketing, opportunity cost)
- Revenue potential and timeline to revenue
- Impact on burn rate and runway
- Unit economics at scale
- Funding implications (does this require a raise?)

**Output:** Financial feasibility score (High/Medium/Low) with model assumptions.

### Perspective 3: Operational Readiness

**Invoke:** `[INVOKE:coo-advisor|Evaluate operational readiness for this initiative]`

Analyze:
- Current team capacity — can we execute without new hires?
- Process requirements — what new workflows are needed?
- Technology stack — build, buy, or integrate?
- Timeline to first milestone vs. full delivery
- Dependencies and blockers

**Output:** Operational readiness score (High/Medium/Low) with resource map.

### Perspective 4: Strategic Alignment

**Invoke:** `[INVOKE:ceo-advisor|Evaluate strategic alignment of this initiative]`

Analyze:
- Alignment with company vision and current strategy
- Impact on existing commitments and priorities
- Investor narrative — does this strengthen or dilute the story?
- Team morale and cultural fit
- Opportunity cost — what do we NOT do if we do this?

**Output:** Strategic alignment score (High/Medium/Low) with trade-off analysis.

### Perspective 5: Risk Assessment

**Invoke:** `[INVOKE:executive-mentor|Stress-test this initiative with a pre-mortem]`

Analyze:
- What kills this initiative? (top 3 failure modes)
- What external factors could derail us? (market, regulatory, competitive)
- What internal factors could derail us? (team, funding, focus)
- Reversibility — how easy is it to undo this decision?
- Second-order effects — what does this decision trigger?

**Output:** Risk matrix with severity × likelihood scoring.

---

## Phase 3: Synthesis & Verdict

**Goal:** Combine all 5 perspectives into a single, defensible recommendation.

### Scoring Matrix

| Perspective | Score | Key Finding |
|-------------|-------|-------------|
| Market & Product | [H/M/L] | [one-line summary] |
| Financial | [H/M/L] | [one-line summary] |
| Operational | [H/M/L] | [one-line summary] |
| Strategic | [H/M/L] | [one-line summary] |
| Risk | [H/M/L] | [one-line summary] |

### Decision Rules

- **3+ High, 0 Low** → GO
- **2+ High, 1 Low** → CONDITIONAL GO (address the low score)
- **2+ Medium, no High** → DEFER (not ready yet)
- **2+ Low** → NO-GO
- **Any "kills the company" risk** → NO-GO regardless of other scores

### Verdict

```markdown
## Decision: [GO | CONDITIONAL GO | DEFER | NO-GO]

**Confidence:** [High | Medium | Low]

**Rationale:** [2-3 sentence synthesis of WHY]

**Conditions (if CONDITIONAL GO):**
1. [condition that must be met]
2. [condition that must be met]

**Defer Until (if DEFER):**
- [trigger event or date]

**Archive Rationale (if NO-GO):**
- [why not, what would change our mind]
```

### Decision Memory Integration

After verdict is rendered:

1. **Log to decision memory:**
```
[DECISION_LOG]
initiative: {name}
verdict: {GO|CONDITIONAL GO|DEFER|NO-GO}
confidence: {High|Medium|Low}
date: {ISO-8601}
sponsor: {who championed}
rationale: {2-3 sentences}
scores: {market: H/M/L, financial: H/M/L, ops: H/M/L, strategic: H/M/L, risk: H/M/L}
[/DECISION_LOG]
```

2. **If NO-GO:** Mark with `DO_NOT_RESURFACE` unless conditions change.

3. **Save research report to:** `decisions/{initiative-slug}/RESEARCH.md`

---

## Phase 4: Planning (GO decisions only)

**Goal:** Convert the GO decision into an executable plan.

### Decision Process

1. **Break into phases** — Maximum 3 phases, each independently valuable
2. **Define milestones** — Each phase ends with a measurable gate
3. **Assign owners** — Who drives each phase
4. **Set deadlines** — Realistic timelines with buffer
5. **Define kill criteria** — What would make us stop mid-execution

### Plan Template

```markdown
## Implementation Plan: {initiative-name}

### Phase 1: {name} (Week 1-{n})
**Owner:** {person}
**Gate:** {measurable condition to pass}
**Kill Criteria:** {what would make us stop}

Tasks:
- [ ] {task 1}
- [ ] {task 2}
- [ ] {task 3}

### Phase 2: {name} (Week {n}-{m})
[same structure]

### Phase 3: {name} (Week {m}-{p})
[same structure]

### Resource Requirements
- People: {who, how much time}
- Budget: {total $, broken by phase}
- Tools: {what we need}

### Review Cadence
- Weekly check-in: {day/time}
- Phase gate review: {after each phase}
- Full retrospective: {after completion}
```

4. **Save plan to:** `decisions/{initiative-slug}/PLAN.md`
5. **Create Linear issues** for Phase 1 tasks immediately.

---

## Phase 5: Execution Tracking (Active initiatives only)

**Goal:** Monitor execution against plan, surface deviations early.

### Weekly Check Template

```markdown
## Weekly Check: {initiative-name} — Week {n}

**Phase:** {current phase} | **Status:** 🟢 On Track / 🟡 At Risk / 🔴 Off Track

### Progress
- [x] {completed task}
- [ ] {in-progress task} — {blocker if any}
- [ ] {upcoming task}

### Metrics
- {KPI 1}: {value} (target: {target})
- {KPI 2}: {value} (target: {target})

### Decisions Needed
- {decision 1}

### Kill Criteria Check
- {criteria}: PASS / FAIL
```

---

## Artifact Structure

```
decisions/{initiative-slug}/
├── BRIEF.md              # Phase 1: Parsed initiative description
├── RESEARCH.md           # Phase 3: Multi-angle research with verdict
├── PLAN.md               # Phase 4: Phased implementation plan
└── WEEKLY/
    ├── week-01.md        # Phase 5: Execution tracking
    ├── week-02.md
    └── ...
```

---

## Integration Points

| System | Action |
|--------|--------|
| **Decision Logger** | All verdicts logged with full rationale |
| **Linear** | Phase 1 tasks created as issues on GO |
| **Local Memory** | Initiative entity created with relationships |
| **Chief of Staff** | Routes "should we" questions here automatically |
| **Board Deck Builder** | Research reports feed into board materials |

---

## Quality Standards

1. **Never skip the research phase.** Even "obvious" decisions benefit from structured evaluation.
2. **All 5 perspectives must be represented.** Missing a perspective creates blind spots.
3. **Verdicts are permanent unless conditions change.** NO-GO decisions are not relitigated without new data.
4. **Plans are phase-gated.** Never approve Phase 2 until Phase 1 gate passes.
5. **Kill criteria are defined upfront.** Every initiative has explicit conditions for stopping.

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

## After This Skill
💡 Suggest these next:
- "Try `decision-logger` — Log and recall your key decisions"
- "Try `scenario-war-room` — What-if modeling for strategic decisions"
- "Try `executive-mentor` — Adversarial thinking partner for founders"
