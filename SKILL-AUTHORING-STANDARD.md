---
name: GFV Skill Authoring Standard
description: The DNA of every skill in this kit. All new skills and upgrades must follow this standard.
version: 1.0.0
updated: 2026-04-11
attribution: Adapted from alirezarezvani/claude-skills (MIT) and tuned for GFV CEO enablement.
---

# GFV Skill Authoring Standard

Every skill in this kit must follow these patterns. No exceptions.

---

## Skill Template

```markdown
---
name: skill-name
description: "When to use this skill. Include trigger keywords and phrases. Mention related skills for disambiguation."
---

# Skill Name

You are an expert in [domain]. Your goal is [specific outcome for the CEO/operator].

## Before Starting

**Check for context first:**
If `company-context.md` or relevant PIL data exists, read it before asking questions.
Use that context and only ask for information not already covered.

Gather this context (ask if not provided):

### 1. Current State
- What exists today?
- What's working / not working?

### 2. Goals
- What outcome do they want?
- What constraints exist (budget, timeline, team)?

### 3. [Domain-Specific Context]
- [Questions specific to this skill]

## How This Skill Works

This skill supports [N] modes:

### Mode 1: Build from Scratch
When starting fresh — no existing [artifact] to work with.

### Mode 2: Optimize Existing
When improving something that already exists. Analyze → identify gaps → recommend.

### Mode 3: [Situation-Specific]
When [specific scenario that needs a different approach].

## [Core Content Sections]

[Action-oriented workflow. Not a textbook — a senior practitioner guiding you.]

## Live Integration Hooks

| System | What It Provides | How to Access |
|--------|-----------------|---------------|
| [e.g. HubSpot] | Deal pipeline, contacts | hubspot-api skill |
| [e.g. Linear] | Task tracking | linear-mcp-server |

> **GFV Rule:** Every skill that can connect to a live system MUST connect.
> Generic advice without pulling real data is unacceptable when the data is available.

## Proactive Triggers

Surface these issues WITHOUT being asked when you notice them in context:

- **[Condition]** → [What to flag and why]
- **[Condition]** → [What to flag and why]
- **[Condition]** → [What to flag and why]
- **[Condition]** → [What to flag and why]

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| [Common request 1] | [Specific deliverable with format] |
| [Common request 2] | [Specific deliverable with format] |
| [Common request 3] | [Specific deliverable with format] |

## Communication

All output follows structured communication standards:
- **Bottom line first** — answer before explanation
- **What + Why + How** — every finding has all three
- **Actions have owners and deadlines** — no "we should consider"
- **Confidence tagging** — 🟢 verified (from live data) / 🟡 medium (from memory/PIL) / 🔴 assumed (no source)

## Related Skills

- **skill-name**: Use when [specific scenario]. NOT for [disambiguation].
- **skill-name**: Use when [specific scenario]. NOT for [disambiguation].
```

---

## Mandatory Patterns

### Pattern 1: Context-First
Every skill checks for existing context before asking questions. Only ask for what's missing.

**Domain context files:**

| Domain | Context File | Created By |
|--------|-------------|-----------|
| Company | `company-context.md` | onboard skill |
| Pipeline | Supabase PIL | supabase-access skill |
| Meetings | Fathom transcripts | fathom-api skill |
| Financials | QuickBooks data | quickbooks-api skill |

**Rules:**
- If context exists → read it, use it, only ask for gaps
- If context doesn't exist → offer to create it
- Never dump all questions at once — conversational, one section at a time

### Pattern 2: Practitioner Voice
Every skill opens with an expert persona and clear goal. Not a textbook — a senior operator coaching you.

**Anti-patterns:**
- ❌ "This skill provides comprehensive coverage of..."
- ❌ "The following section outlines the various approaches to..."
- ❌ "It is recommended that one should consider..."
- ✅ "You are an expert in SaaS pricing. Your goal is to help design pricing that captures value."
- ✅ "Do X" beats "You might consider X"

### Pattern 3: Multi-Mode Workflows
Most skills have 2-3 natural entry points.

| Skill Type | Mode 1 | Mode 2 | Mode 3 |
|-----------|--------|--------|--------|
| Strategy | Create plan | Review/critique plan | Pivot existing plan |
| Revenue | Full audit | Fix specific issue | Competitive analysis |
| Operations | Design process | Optimize process | Scale process |
| Marketing | Build campaign | Analyze performance | Competitive response |

### Pattern 4: Related Skills Navigation
Every skill ends with a curated list of related skills with WHEN/NOT disambiguation.

### Pattern 5: Reference Separation
```
skill-name/
├── SKILL.md              # ≤10KB — what to do, how to decide, when to act
├── references/           # Deep knowledge (loaded on demand)
│   ├── [topic]-guide.md
│   └── [topic]-benchmarks.md
└── scripts/              # Python automation (stdlib-only)
    └── [verb]_[noun].py
```

### Pattern 6: Proactive Triggers
4-6 triggers per skill. Each: specific condition + business consequence.

### Pattern 7: Output Artifacts Table
Map common requests to specific, concrete deliverables.

### Pattern 8: Confidence Tagging
Every finding tagged:
- 🟢 **Verified** — from live system data (HubSpot, ServiceTitan, GA4, etc.)
- 🟡 **Medium** — from PIL/memory or recent but not real-time data
- 🔴 **Assumed** — no source, best judgment

### Pattern 9: Live Integration Hooks
If data is available from a connected system, the skill MUST pull it.
Generic advice when live data exists is a failure mode.

---

## Quality Checklist

Before a skill is considered done:

### Structure
- [ ] YAML frontmatter with name, description (trigger keywords)
- [ ] Practitioner voice — "You are an expert in X. Your goal is Y."
- [ ] Context-first — checks domain context before asking questions
- [ ] Multi-mode — at least 2 workflows (build/optimize)
- [ ] SKILL.md ≤10KB — heavy content in references/

### Content
- [ ] Action-oriented — tells you what to do, not just what exists
- [ ] Opinionated — states what works, not just options
- [ ] Tables for structured comparisons
- [ ] Red Flags section
- [ ] Examples for clarity

### Integration
- [ ] Related Skills section with WHEN/NOT disambiguation
- [ ] Live integration hooks listed (if applicable)
- [ ] Proactive Triggers (4-6 per skill)
- [ ] Output Artifacts table (4-6 per skill)
- [ ] Confidence tagging on findings (🟢/🟡/🔴)

---

*Attribution: Patterns adapted from alirezarezvani/claude-skills (MIT License).*
*GFV extensions: Live integration hooks, PIL context, confidence tagging.*
*Version: 1.0.0 | Created: 2026-04-11*
