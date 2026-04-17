---
name: negotiation-advisor
description: Battle-tested negotiation frameworks for deal closers. Preparation, BATNA analysis, concession strategy, and real-time tactical guidance.
short_description: "Battle-tested negotiation frameworks"
license: MIT
metadata:
  author: GFV Proactive Intelligence
  version: 1.0.0
  category: C-Suite Advisory
---

# /negotiation-advisor

**Usage**: Invoke before or during any high-stakes negotiation — vendor contracts, partnership terms, salary discussions, M&A terms, investor negotiations.


## Quick Start
Just say any of these:
- "Prep me for a salary negotiation with [name]"
- "What's my BATNA for this deal?"
- "Help me negotiate this vendor contract"


## The Negotiation Operating System

### Phase 1: Preparation Brief (Pre-Meeting)
Before any negotiation, the agent builds an intelligence dossier:
- **Your BATNA** (Best Alternative to Negotiated Agreement): What happens if you walk away?
- **Their BATNA**: What's their alternative? Research via CRM, LinkedIn, and public data.
- **ZOPA** (Zone of Possible Agreement): The overlap between your floor and their ceiling.
- **Anchoring Strategy**: Who should make the first offer? At what number? Data-backed.

### Phase 2: Concession Architecture
Design a structured give-and-take plan BEFORE the meeting:
- **Must-Haves**: Non-negotiable items (rank-ordered).
- **Nice-to-Haves**: Items you can trade as concessions.
- **Throwaway Items**: Items you include specifically to concede (creates reciprocity).
- **Concession Ladder**: Pre-planned sequence of concessions, each smaller than the last (signals firmness).

### Phase 3: Tactical Playbook
Real-time tactics matched to common scenarios:

| Scenario | Tactic | Script |
|----------|--------|--------|
| They anchor aggressively low | **Flinch + Reframe** | "That's quite far from market. Here's what comparable deals look like..." |
| They say "take it or leave it" | **Bracket + Deadline Test** | "I understand your position. Let's explore what flexibility exists on [secondary term]..." |
| Negotiation stalls | **Expand the Pie** | "What if we restructured the payment terms? That might unlock value for both sides..." |
| They use good cop / bad cop | **Call It Out** | "I appreciate both perspectives. Let's focus on what works for both organizations..." |
| You have weak leverage | **Defer to Authority** | "I'd love to agree today, but my board requires [X]. Let me take this back..." |

### Phase 4: Post-Negotiation Capture
- Extract agreed terms into a structured summary.
- Flag any verbal commitments that need written confirmation.
- Generate follow-up email confirming key terms (route through `email-composer` with voice model).
- Log outcome in `decision-logger` for pattern analysis over time.

## Output Format
The advisor produces a 1-page **Negotiation Battle Card** with:
1. BATNA comparison table
2. Concession ladder (pre-planned)
3. Opening position + fallback positions
4. Tactical scripts for likely objections
5. Walk-away threshold clearly stated

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Other party won't budge | Find their hidden interests — they may value something you can easily give |
| Prep feels insufficient | Research their recent wins, losses, and public statements before the call |

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
- "Try `deal-review` — Pipeline review — flag stale deals, find gaps"
- "Try `contract-reader` — Summarize contracts in plain English"
- "Try `executive-mentor` — Adversarial thinking partner for founders"
