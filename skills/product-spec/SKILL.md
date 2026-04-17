---
name: product-spec
description: "Convert a rough idea, meeting notes, or shorthand into a structured Product Requirements Document. Use when the user mentions PRD, requirements, spec, or wants to formalize an idea before building."
short_description: "Turn rough ideas into product requirement docs"
---

# Create PRD

Transform unstructured input into a rigorous, actionable Product Requirements Document. CEOs hate fluff — every sentence must earn its place.


## Quick Start
Just say any of these:
- "Turn this idea into a product spec"
- "Write a PRD for [feature]"
- "Convert these meeting notes into requirements"


## When to Use

- User has a rough idea they want formalized
- Meeting transcript needs to become actionable requirements
- Before starting any multi-day engineering effort
- User says "write a PRD", "spec this out", "requirements for..."

## Step 1: Intake

If the user hasn't provided input, ask exactly these questions:

1. **What problem does this solve?** (1-2 sentences)
2. **Who is the user?** (role, not demographics)
3. **What does success look like?** (measurable outcome)
4. **What's the deadline or urgency?** (timeline)
5. **What already exists?** (starting point — greenfield or iteration)

If the user provides a brain dump, meeting notes, or voice transcript — extract answers to these 5 questions from the text. Don't ask questions the input already answers.

## Step 2: Generate the PRD

**Every PRD follows this exact 6-section structure:**

```markdown
# [Feature/Product Name] — PRD

**Author:** [CEO's name or "Generated"]
**Date:** [today]
**Status:** Draft
**Priority:** [P0/P1/P2]

---

## 1. Problem Statement

[1-2 sentences. What is broken or missing, and what is the business cost
of not fixing it. Be specific — "$X/month in lost revenue" beats
"suboptimal experience".]

## 2. Proposed Solution

[2-3 paragraphs max. What we will build, at a high level.
Include what is IN scope and what is explicitly OUT of scope.
Use bullet points for clarity.]

### In Scope
- [Concrete deliverable 1]
- [Concrete deliverable 2]

### Out of Scope
- [Thing we are NOT building and why]

## 3. User Stories

| # | As a... | I want to... | So that... | Priority |
|---|---------|-------------|-----------|----------|
| 1 | [role] | [action] | [outcome] | P0 |
| 2 | [role] | [action] | [outcome] | P1 |

## 4. Technical Requirements

### Architecture
- [Key technical decisions: framework, database, API patterns]
- [Integration points with existing systems]

### Constraints
- [Performance requirements: "< 200ms response time"]
- [Scale requirements: "handle 10K concurrent users"]
- [Security requirements: "SOC2 compliant data handling"]
- [Platform requirements: "must work on mobile Safari"]

### Dependencies
- [External services or APIs needed]
- [Internal systems that must change]
- [Team members or approvals required]

## 5. Success Metrics

| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| [metric name] | [baseline] | [goal] | [how to measure] |

## 6. Milestones

| Phase | Deliverable | Date | Owner |
|-------|------------|------|-------|
| Alpha | [what ships] | [date] | [who] |
| Beta | [what ships] | [date] | [who] |
| GA | [what ships] | [date] | [who] |
```

## Step 3: Quality Gate

Before presenting the PRD, self-check:

| Check | Pass? |
|-------|-------|
| Problem statement mentions a measurable business cost? | |
| Every user story has a clear "so that" outcome? | |
| Out-of-scope section exists and has at least 1 item? | |
| Technical constraints include actual numbers? | |
| Success metrics have a measurable baseline AND target? | |
| No buzzwords? (no "leverage", "synergy", "holistic") | |

If any check fails, fix it before presenting.

## Step 4: Export Options

After the CEO approves, offer:

1. **Linear** — Create issues from each user story:
   ```
   /linear-sync to create issues from this PRD
   ```
2. **Google Doc** — Push to Drive:
   ```
   /google-doc-creation to create a formatted version
   ```
3. **Markdown file** — Save locally:
   ```bash
   mkdir -p ~/ceo-brain/prds
   # Save as ~/ceo-brain/prds/YYYY-MM-DD-feature-name.md
   ```

## Red Flags

- If the user can't articulate the problem statement → the idea isn't ready for a PRD. Say so.
- If technical requirements are "TBD" → flag as a risk in the milestones section.
- If there are no success metrics → the PRD is incomplete. Add at least one.

## Integration

- Chain with `/context-prime` to understand the existing codebase first
- Chain with `/meeting-prep` if the PRD is for a stakeholder review
- Chain with `/analyze-issue` if the PRD stems from a bug or incident

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
- "Try `feature-architect` — Guide features from spec to deployed code"
- "Try `launch-strategy` — Plan product launches and release strategies"
- "Try `doc-builder` — Create Word docs — proposals, memos, reports"
