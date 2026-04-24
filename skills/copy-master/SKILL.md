---
name: copy-master
description: World-class copywriting intelligence engine overriding generic LLM communication tendencies with high-converting, proven direct-response architectures. 
short_description: "Write world-class marketing copy"
license: MIT
metadata:
  author: GFV Growth by Design
  version: 1.0.0
  category: Growth Engine
---

# /copy-master

**Usage**: Utilize this skill when writing landing pages, sales sequences, ad copy, or high-stakes announcements. It acts as an orchestrator sitting *above* the `/email-composer` and `/social-engine` to inject direct-response mastery.


## Quick Start
Just say any of these:
- "Write landing page copy for [product]"
- "Rewrite this headline to be more compelling"
- "Create ad copy for [campaign]"


## The Problem With AI Copy
Out-of-the-box LLMs write with a recognizable "AI smell": overly verbose, heavy on adverbs, generic structure, and weak hooks. The `copy-master` skill prevents this by mathematically scoring and restricting output based on 7 core pillars.

## The 7 Core Pillars of Copy-Master Execution

When invoked, the resulting copy MUST adhere to:

1. **The Rule of One**: One Big Idea. One Core Emotion. One Desirable Benefit. One Single Call to Action. (Reject any generation that tries to do three things at once).
2. **The "So What?" Filter**: Every technical feature mentioned must be immediately followed by its direct functional benefit to the user.
3. **Flesch-Kincaid Rigidity**: Keep reading level between Grade 5 to Grade 8. Short sentences. High variance in sentence length. (e.g., Use a 1-word sentence to break cadence).
4. **Adverb Annihilation**: Strip all lazy adverbs (very, truly, deeply, highly). Replace with stronger base verbs.
5. **The PAS / AIDA Arch**: Structure must clearly reflect Problem-Agitation-Solution or Attention-Interest-Desire-Action.
6. **Visceral Hooks**: The first 3 seconds/words must stop the scroll or the open. Avoid pleasantries. Start in the action.
7. **The Voice Model Check**: The output MUST be cross-referenced against `~/ceo-brain/voice-model.md`. The copy must sound like the CEO, not a 1990s infomercial.

## Narrative Submode (Enhanced v1.1 — StoryMaster Method)

When the content calls for storytelling (case studies, origin stories, testimonials):

### The 5-Beat Story Arc
1. **The Before** — Paint the painful status quo the reader recognizes.
2. **The Catalyst** — The moment everything changed (specific, concrete).
3. **The Struggle** — What made it hard (builds credibility via vulnerability).
4. **The Breakthrough** — The insight, decision, or action that unlocked progress.
5. **The After** — The measurable, specific result. Never vague.

### Story Selection Criteria
- Does this story prove a specific claim? (If not, it's entertainment, not persuasion.)
- Is the protagonist relatable to the target audience?
- Can you include at least one specific number, date, or name?

## Persuasion Tactics (Enhanced v1.1 — Charm-Claw Method)

Advanced persuasion techniques layered on top of the 7 pillars:

| Tactic | When to Use | Example |
|--------|------------|---------|
| **Social Proof Stack** | Landing pages, case studies | "Join 1,200+ CEOs who..." |
| **Future Pacing** | Sales pages, proposals | "Imagine logging in Monday to see..." |
| **Loss Aversion Frame** | Urgency scenarios | "Every week without X costs you Y" |
| **Authority Transfer** | Credibility building | "As featured in Forbes / Used by [Brand]" |
| **Specificity Anchor** | Anywhere numbers exist | "37.4% increase" beats "significant improvement" |
| **Contrast Frame** | Comparisons, competitive | "Before: 4 hours manual. After: 12 minutes automated." |

## Output Structure
When generating, the agent must present the CEO with:
1. **The Hook Options** (Provide 3 distinct angles: Logical, Emotional, Urgent).
2. **The Core Copy** (Drafted exactly to the pillars).
3. **The Scorecard** (A brief internal audit of how the draft meets the 7 pillars and integrates the CEO's specific voice).
4. **The Story Option** (If narrative submode applies, present one StoryMaster 5-beat arc).
5. **The Persuasion Layer** (Which tactics were applied, and why they fit this context).

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Copy sounds too 'AI' | Paste 3-5 examples of your best copy first to calibrate the voice |
| Headlines don't convert | Test benefit-driven headlines vs curiosity-driven — track which wins |

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
- "Try `email-composer` — Draft emails in your authentic voice"
- "Try `content-strategy` — Plan and execute your content calendar"
- "Try `sales-enablement` — Create sales collateral reps actually use"

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
