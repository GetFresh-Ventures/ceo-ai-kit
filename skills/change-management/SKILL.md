---
name: change-management
description: "Framework for rolling out organizational changes without chaos. Covers ADKAR model, communication templates, resistance patterns, and change fatigue management. Use when announcing a reorg, switching tools, pivoting strategy, killing a product, changing leadership, or when user mentions change management, managing resistance, org change, or pivot communication."
short_description: "Roll out organizational changes smoothly"
attribution: Adapted from alirezarezvani/claude-skills (MIT License), tuned for GFV portfolio context.
---

# Change Management

Most changes fail at implementation, not design. The ADKAR model tells you why and how to fix it.


## Quick Start
Just say any of these:
- "We're switching CRMs — plan the rollout"
- "How do I get buy-in for [change]?"
- "Build a communication plan for this reorg"


## How This Skill Works

### Mode 1: Process Change (new tools, new workflows)
Timeline: 4–8 weeks. Hardest phase: Ability (habit building).

### Mode 2: Org Change (reorg, new leader, team splits)
Timeline: 3–6 months. Hardest phase: Desire (people fear for their roles).

### Mode 3: Strategy Pivot
Timeline: 3–12 months. Hardest phase: Awareness (people don't believe it's real).

### Mode 4: Culture Change
Timeline: 12–24 months. Hardest phase: Reinforcement (behavior doesn't change from announcements).

---

## Core Model: ADKAR

### A — Awareness
People understand WHY, not just WHAT.

**The mistake:** Communicating the WHAT before the WHY.

**Startup shortcut:** A 5-minute video from the decision-maker explaining the "why" beats a formal announcement.

### D — Desire
People want to participate — or at least don't actively resist.

**What creates desire:** "What's in it for me?" answered honestly per stakeholder group.
**What destroys desire:** Pretending the change is better for everyone than it is.

### K — Knowledge
People know HOW to operate in the new world.

| Method | Best for |
|--------|---------|
| Live training | Skill-based changes, complex tools |
| Documentation | Process changes, reference material |
| Video walkthroughs | Tool migrations |
| Peer learning | Behavior changes |
| Office hours | Changes with many edge cases |

### A — Ability
People have the time, tools, and support to actually do it differently.

**Signs of ability gap:** People revert under pressure. Workarounds emerge. Training scores high but behavior unchanged.

### R — Reinforcement
The change sticks. **This is where most changes die.**

**What creates reinforcement:** Visible measurement, early adopter recognition, leader modeling, removing the old option.

---

## Resistance Patterns
| Pattern | Signal | Response |
|---------|--------|----------|
| "This won't work" | Awareness or credibility gap | Explain the evidence base |
| "Why now?" | Awareness gap | Explain urgency |
| "I wasn't consulted" | Desire gap | Involve them in the "how" |
| "I don't have time" | Ability gap | Reduce their load or push timeline |
| "We tried this before" | Trust gap | Explain what's different this time |
| Silent non-compliance | Unknown gap | 1:1 conversation to diagnose |

## Change Fatigue
**Signals:** Eye-rolls during announcements. Low attendance. Fast compliance, slow adoption.

**Prevention:**
- Finish what you start before launching the next change
- Space changes — 2-3 months of stability between major ones
- Announce what's NOT changing
- Show results from the previous change before launching the next

## Red Flags
- Change announced on Friday afternoon
- "This is final, questions are not welcome" framing
- No FAQ or way to ask questions safely
- Old system still running 6 weeks after "go-live"
- Leaders exempted from the change they're pushing
- No measurement of adoption

## Proactive Triggers
- **Multiple changes running simultaneously** → change fatigue risk, prioritize ruthlessly
- **Reorg announced without 1:1s scheduled** → desire gap forming, schedule immediately
- **New tool deployed without training** → ability gap guaranteed
- **Old process still available 4+ weeks post-change** → reinforcement failure
- **Leaders not using the new process themselves** → adoption will fail

## Output Artifacts
| Request | You Produce |
|---------|-------------|
| "We're doing a reorg" | Full communication plan with ADKAR timeline |
| "People are resisting" | Resistance diagnosis with targeted interventions |
| "We're switching tools" | Process change rollout plan (8-week timeline) |
| "We're pivoting strategy" | Pivot communication sequence with milestone proof points |
| "Too many changes at once" | Change inventory with prioritization and stability plan |

## Communication
- **Bottom line first**
- **Confidence tagging** — 🟢 verified / 🟡 medium / 🔴 assumed
- **Resistance is information, not defiance. Diagnose before responding.**

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
- **coo-advisor**: Use for operational process design. NOT for change communication.
- **ceo-advisor**: Use for strategic direction. NOT for managing the human side of change.
- **founder-coach**: Use for personal leadership through change. NOT for organizational change management.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Team resists the change | Address WIIFM (What's In It For Me) for each stakeholder group |
| Change stalls after announcement | Assign change champions in each team. They drive adoption peer-to-peer |



## After This Skill
💡 Suggest these next:
- "Try `coo-advisor` — Operations, process, and team scaling"
- "Try `chief-of-staff` — Your always-on executive AI assistant"
- "Try `decision-logger` — Log and recall your key decisions"

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
