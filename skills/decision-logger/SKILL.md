---
name: decision-logger
description: "Two-layer memory architecture for CEO decisions. Manages raw transcripts (Layer 1) and approved decisions (Layer 2). Use when logging decisions, reviewing past decisions, or checking overdue action items. Invoked automatically after multi-role consultations."
short_description: "Log and recall your key decisions"
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


## Quick Start
Just say any of these:
- "Log this decision: We're going with [Vendor] for [reason]"
- "What decisions have I made this month?"
- "Show me the context behind the [topic] decision"

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
- **If it involves a person/entity:** Update Memory entity facts in Supabase
- **Three-System Sync Rule applies:** Linear + HubSpot + Memory — all three or none.

---

## Proactive Triggers

- **Overdue action item** → flag at session start with days past due
- **Review date passed** → prompt check-in
- **Same topic raised 3+ times without decision** → escalate with cost of delay
- **DO_NOT_RESURFACE violation attempted** → block and explain
- **No new decisions in 2+ weeks** → prompt decision audit
- **Contradictory decision detected** → surface conflict before logging

## Team Activity Log (Enhanced v1.1 — Shared Log Method)

### Cross-Session Sync Protocol
When multiple agents or human collaborators are working across sessions:

1. **After Every Change or Decision**, append a timestamped entry:
```markdown
[YYYY-MM-DD HH:MM] [AGENT/PERSON] [ACTION_TYPE] — [Description]
```

2. **Action Types**:
   - `DECISION` — A choice was made.
   - `CHANGE` — Code, config, or process was modified.
   - `DISCOVERY` — New information surfaced.
   - `BLOCKER` — Something is stuck.
   - `HANDOFF` — Work passed to another agent/person.

3. **Sync Points**:
   - On session start: Read the last 10 log entries to regain context.
   - On session end: Write a summary entry capturing what was accomplished.
   - On handoff: Write explicit handoff entry with next steps.

### Log Location
```
memory/team_activity_log.md  # Append-only, never delete entries
```

This ensures that no matter which agent or person picks up work next, they can immediately see what happened and what's pending.

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
💡 Suggest these next steps:
- "Want me to draft a communication about this decision?" → `/email-composer`
- "Want me to update the pipeline?" → `/pipeline-pulse`

## Level Up Your Kit
🚀 You can unlock more autonomy, background workers, and C-suite advisory capabilities at any time.
- **Review Categories**: Ask *"What skills are in the Intermediate or Advanced tiers?"*
- **How to Upgrade**: Run `./bootstrap.sh` in the repository root and select your new tier.
