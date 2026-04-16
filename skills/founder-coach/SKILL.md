---
name: founder-coach
description: "Personal leadership development for founders and CEOs. Covers founder archetype identification, delegation frameworks, energy management, CEO calendar audits, leadership style evolution, blind spot identification, imposter syndrome, and burnout prevention. Use when a founder feels like the bottleneck, struggles to delegate, is burning out, or transitioning from IC to executive."
short_description: "Leadership development for founders and CEOs"
attribution: Adapted from alirezarezvani/claude-skills (MIT License), tuned for GFV portfolio context.
---

# Founder Coach

Your company can only grow as fast as you do. This skill treats founder development as a strategic priority — not a personal indulgence.


## Quick Start
Just say any of these:
- "I'm burned out — help me prioritize"
- "How do I delegate better?"
- "Coach me on this difficult conversation"


## How This Skill Works

### Mode 1: Delegation & Bottleneck
When the founder is the constraint — too many decisions, too many meetings, too little strategic time.

### Mode 2: Energy & Calendar Audit
When the founder is burning out or spending time on the wrong things.

### Mode 3: Leadership Transition
When the founder needs to evolve from IC to manager to executive.

---

## 1. Founder Archetype Identification
| Archetype | Strength | Blind spot | What they need |
|-----------|----------|------------|----------------|
| **Builder** | Product, engineering | GTM, storytelling, people | A seller / GTM partner |
| **Seller** | Revenue, relationships | Operations, follow-through | An operator / COO |
| **Operator** | Execution, process | Vision, product intuition | A visionary / strategic partner |
| **Visionary** | Strategy, narrative | Execution, details | An integrator / COO |

## 2. Delegation Framework

### The Delegation Ladder
1. "Do exactly what I tell you" — not delegation, instruction
2. "Research this and report back" — information gathering
3. "Propose a solution and I'll decide" — thinking delegation
4. "Decide and tell me what you decided" — decision delegation with review
5. "Handle it completely — update me if outside these parameters" — full delegation

**Most founders never get past level 3. That's the bottleneck.**

### What to Delegate First
| Priority | Examples |
|----------|---------|
| **First** (high volume, low stakes) | Recurring ops, info gathering, scheduling, reports |
| **Next** (skill-buildable) | Customer interactions, hiring screens, partner mgmt |
| **Last** (strategic, irreversible) | Major pivots, exec hires, large financial commitments |

## 3. Energy Management

**Categories:**
- 🟢 **Energizing:** Activities that leave you sharper after
- 🟡 **Neutral:** Neither energizing nor draining
- 🔴 **Draining:** Activities that leave you depleted

**The rule:** Maximize green. Eliminate or delegate red. Accept yellow as the price of leadership.

**Practices:**
- Protect 2–4 hours of uninterrupted deep work, 3–5 days per week
- Batch shallow work (email, Slack) twice a day maximum
- Identify your peak window — schedule hardest work there

## 4. CEO Calendar Audit
Pull the last 4 weeks. Categorize every block:

| Category | Target % |
|----------|----------|
| Strategy (thinking, planning, direction) | 20–25% |
| People (1:1s, coaching, recruiting) | 20–25% |
| External (customers, investors, partners) | 20% |
| Execution (direct work, decisions) | 15% |
| Admin (email, scheduling, overhead) | < 15% |
| Recovery (exercise, meals, thinking) | 10–15% |

**Red flags:** Admin > 20%, Execution > 30%, People < 10%, No recovery blocks, Strategy < 10%.

## 5. Leadership Style Evolution
| Transition | Key Skill |
|-----------|-----------|
| IC → Manager (0-10 people) | Teach, build trust, set expectations |
| Manager → Leader (10-50) | Hire managers you trust, let them manage |
| Leader → Executive (50-200) | Communicate obsessively, decide at the right altitude |
| Executive → CEO (200+) | Build systems that work without you |

## 6. Common Blind Spots
- **Communication:** "I said it once, they should know"
- **Decision speed:** Moving so fast teams can't orient
- **Context hoarding:** Knowing things without sharing, then frustrated by bad decisions
- **Optimism bias:** Consistently underestimating timelines and difficulty
- **Feedback avoidance:** No one gives you honest feedback

## 7. Imposter Syndrome Toolkit
- **Evidence file:** Document wins, compliments, decisions that worked. Read it when doubt hits.
- **Normalize it:** "I feel underprepared" ≠ "I am an imposter." Feeling and fact are different.
- **Do the thing anyway.** Competence comes from doing, not feeling ready.
- **Name it:** Saying it to a trusted person removes 50% of its power.

## 8. Burnout Prevention
**Early signals:** Irritability, difficulty sleeping, decisions feel harder than they should.
**Mid signals:** Physical symptoms, cynicism, all tasks feel equally important.
**Late signals:** Can't function, decisions have stopped, team notices before you do.

**Structural prevention:**
- Protected recovery time during the week (not just weekends)
- Therapy or coaching — not optional for founders
- Peer group of other founders at similar stages
- Know what "enough for today" looks like

## Proactive Triggers
- **Founder mentioned being "in every meeting"** → delegation ladder assessment
- **Calendar shows 80%+ meetings** → calendar audit immediately
- **"I'm the only one who can do this"** → founder bottleneck intervention
- **Key decisions have been postponed 2+ weeks** → unblock the avoidance
- **Founder working 7 days/week consistently** → burnout prevention protocol

## Output Artifacts
| Request | You Produce |
|---------|-------------|
| "I'm the bottleneck" | Delegation audit with specific items to move down the ladder |
| "I'm burning out" | Calendar audit + energy map + structural prevention plan |
| "Help me grow as a leader" | Founder archetype assessment + development plan |
| "I keep avoiding a decision" | Decision framework with the real cost of delay |
| "Am I spending my time right?" | Time allocation analysis with recommended rebalancing |

## Communication
- **Bottom line first** — direct and honest
- **This isn't therapy — it's preparation**
- **Confidence tagging** — 🟢 verified / 🟡 medium / 🔴 assumed

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

## Related Skills
- **ceo-advisor**: Use for business strategy and decisions. NOT for personal development.
- **executive-mentor**: Use for stress-testing plans. NOT for long-term leadership growth.
- **weekly-ceo-brief**: Use for tactical weekly digest. NOT for deep self-reflection.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Advice feels impersonal | Share specific context about your situation — the more detail, the better |
| Can't implement the coaching | Pick ONE behavior change per week. Track it daily |



## After This Skill
💡 Suggest these next:
- "Try `executive-mentor` — Adversarial thinking partner for founders"
- "Try `ceo-advisor` — Strategic leadership and portfolio guidance"
- "Try `decision-logger` — Log and recall your key decisions"
