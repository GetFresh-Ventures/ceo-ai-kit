---
name: decision-logger
description: "Two-layer memory architecture for CEO decisions. Manages raw transcripts (Layer 1) and approved decisions (Layer 2). Use when logging decisions, reviewing past decisions, or checking overdue action items. Invoked automatically after multi-role consultations."
attribution: Adapted from alirezarezvani/claude-skills (MIT License), hardened for GFV portfolio context.
metadata:
  version: 1.0.0
  category: c-level
  domain: decision-memory
  updated: 2026-04-11
---

# Decision Logger

Two-layer memory system. Layer 1 stores everything. Layer 2 stores only what the CEO approved. Future sessions read Layer 2 only — this prevents hallucinated consensus from past debates bleeding into new deliberations.

---

## Commands

| Command | Effect |
|---------|--------|
| `/cs:decisions` | Last 10 approved decisions |
| `/cs:decisions --all` | Full history |
| `/cs:decisions --owner CMO` | Filter by owner |
| `/cs:decisions --topic pricing` | Search by keyword |
| `/cs:review` | Action items due within 7 days |
| `/cs:review --overdue` | Items past deadline |

---

## Two-Layer Architecture

### Layer 1 — Raw Transcripts
**Location:** `memory/consultations/YYYY-MM-DD-raw.md`
- Full agent contributions, critique, synthesis
- All debates, including rejected arguments
- **NEVER auto-loaded.** Only on explicit CEO request.
- Archive after 90 days → `memory/consultations/archive/YYYY/`

### Layer 2 — Approved Decisions
**Location:** `memory/consultations/decisions.md`
- ONLY CEO-approved decisions, action items, corrections
- **Loaded automatically at start of every advisory session**
- Append-only. Decisions are never deleted — only superseded.
- Managed by Chief of Staff after CEO approval. Never written by agents directly.

---

## Decision Entry Format

```markdown
## [YYYY-MM-DD] — [TOPIC TITLE]

**Decision:** [One clear statement of what was decided.]
**Owner:** [One person or role — accountable for execution.]
**Deadline:** [YYYY-MM-DD]
**Review:** [YYYY-MM-DD]
**Rationale:** [Why this over alternatives. 1-2 sentences.]

**CEO Override:** [If CEO changed agent recommendation — what and why. Blank if not applicable.]

**Rejected:**
- [Proposal] — [reason] [DO_NOT_RESURFACE]

**Action Items:**
- [ ] [Action] — Owner: [name] — Due: [YYYY-MM-DD] — Review: [YYYY-MM-DD]

**Supersedes:** [DATE of previous decision on same topic, if any]
**Superseded by:** [Filled in retroactively if overridden later]
**Raw transcript:** memory/consultations/[DATE]-raw.md
```

---

## Conflict Detection

Before logging, Chief of Staff checks for:

1. **DO_NOT_RESURFACE violations** — new decision matches a rejected proposal
2. **Topic contradictions** — two active decisions on same topic with different conclusions
3. **Owner conflicts** — same action assigned to different people in different decisions

When a conflict is found:
```
⚠️ DECISION CONFLICT
New: [text]
Conflicts with: [DATE] — [existing text]

Options: (1) Supersede old  (2) Merge  (3) Defer to CEO
```

**DO_NOT_RESURFACE enforcement:**
```
🚫 BLOCKED: "[Proposal]" was rejected on [DATE]. Reason: [reason].
To reopen: CEO must explicitly say "reopen [topic] from [DATE]".
```

---

## Logging Workflow (Post Consultation)

1. CEO approves synthesis
2. Write Layer 1 raw transcript → `YYYY-MM-DD-raw.md`
3. Check conflicts against `decisions.md`
4. Surface conflicts → wait for CEO resolution
5. Append approved entries to `decisions.md`
6. Confirm: decisions logged, actions tracked, DO_NOT_RESURFACE flags added

---

## Marking Actions Complete

```markdown
- [x] [Action] — Owner: [name] — Completed: [DATE] — Result: [one sentence]
```

Never delete completed items. The history is the record.

---

## Session Start Protocol

At the start of every advisory session:

1. Load `decisions.md` (Layer 2)
2. Check for overdue action items
3. Check for review dates that have passed
4. If overdue items exist, flag them:
   *"You decided [X] on [date] with a review date of [date]. Worth a check-in?"*

---

## File Structure

```
memory/consultations/
├── decisions.md              # Layer 2: append-only, CEO-approved
├── YYYY-MM-DD-raw.md         # Layer 1: full transcript per session
└── archive/YYYY/             # Raw files after 90 days
```

---

## GFV System Sync

When a decision is logged:
- **If it involves a task:** Create or update a Linear issue
- **If it involves a deal:** Update HubSpot deal notes
- **If it involves a person/entity:** Update PIL entity facts in Supabase
- **Three-System Sync Rule applies:** Linear + HubSpot + PIL — all three or none.

---

## Proactive Triggers

- **Overdue action item** → flag at session start with days past due
- **Review date passed** → prompt check-in
- **Same topic raised 3+ times without decision** → escalate with cost of delay
- **DO_NOT_RESURFACE violation attempted** → block and explain
- **No new decisions in 2+ weeks** → prompt decision audit
- **Contradictory decision detected** → surface conflict before logging
