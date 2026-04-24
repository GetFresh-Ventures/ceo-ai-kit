---
name: social-engine
description: "Create platform-native content for LinkedIn, X/Twitter, Instagram, and newsletters — adapted to each platform's format, character limits, and engagement patterns. Also handles content repurposing from articles, meetings, or internal notes into social-ready formats. Use when the CEO mentions 'LinkedIn post,' 'Twitter thread,' 'social media,' 'content calendar,' 'what should I post,' 'repurpose this,' or 'personal brand.'"
short_description: "Create platform-native social media content"
metadata:
  version: 1.0.0
  category: growth-engine
  triggers:
    - LinkedIn post
    - Twitter thread
    - social media
    - content calendar
    - what should I post
    - repurpose
    - personal brand
    - social content
---

# Social Engine

Build platform-native content without flattening the CEO's real voice into generic AI slop.


## Quick Start
Just say any of these:
- "Write a LinkedIn post about [topic]"
- "Create a tweet thread about [announcement]"
- "Repurpose this blog post for social media"


## When to Activate

- Writing LinkedIn posts or articles
- Drafting X threads or standalone posts
- Repurposing articles, meeting notes, or internal docs into social content
- Building a content cadence or posting calendar
- Creating launch sequences across platforms
- Building the CEO's personal brand

## Non-Negotiables

1. **Start from source material** — never from generic post formulas
2. **Adapt format for platform** — not persona
3. **One post = one actual claim** — no kitchen-sink posts
4. **Specificity beats adjectives** — "grew from 5 to 47 customers" not "experienced massive growth"
5. **No engagement bait** unless explicitly requested

## Hard Bans

Delete and rewrite:
- "I'm thrilled to announce"
- "Agree? 👇"
- "Here's what nobody tells you about..."
- Humblebrags disguised as "lessons learned"
- 🚀 emoji as a substitute for substance
- "Drop a comment below if you..."

## Source-First Workflow

Before drafting, identify the source material:
- Published articles, blogs, or case studies
- Internal memos, strategy docs, or meeting notes
- Real conversations, customer feedback, or data insights
- Personal experiences, decisions made, or lessons learned

**If the CEO says "write something about X," ask for the source.** The post should contain real insight, not synthesized platitudes.

## Platform-Specific Rules

### LinkedIn

**Format:** 1,300 character sweet spot (max 3,000)
**Structure:**
- Hook in first 2 lines (visible before "see more")
- Short paragraphs (1-3 sentences)
- White space between paragraphs
- Optional: end with a question or clear CTA

**What works:**
- Contrarian takes backed by personal experience
- Behind-the-scenes decisions ("Why we turned down a $500K deal")
- Data + narrative ("We tracked X for 6 months. Here's what we found.")
- Framework posts (3-5 numbered insights)

**What doesn't:**
- Motivational quotes without context
- "Day 1 of 365" posts
- Posts that read like a press release

### X / Twitter

**Format:** 280 characters per post, threads for depth
**Thread structure:**
1. Hook tweet (the claim — must stand alone)
2. Context (why this matters)
3. 3-5 supporting points (one per tweet)
4. Conclusion or takeaway
5. Optional: CTA or link

**What works:**
- Hot takes with receipts
- Number-driven insights ("We spent $X on Y. Here's the real ROI.")
- Threads that teach one specific thing

### Newsletter / Email

**Format:** 500-800 words, conversational
**Structure:**
- Subject line: specific, curiosity-driven (not clickbait)
- Opening: one personal/concrete observation
- Body: one main idea, well-supported
- Close: one clear takeaway or CTA

## Content Calendar Framework

### Weekly Cadence (for CEOs with limited time)

| Day | Platform | Type |
|-----|----------|------|
| Mon | LinkedIn | Industry insight or framework post |
| Wed | X | Thread or hot take based on Mon's topic |
| Fri | LinkedIn | Personal story, behind-the-scenes, or lesson learned |

### Monthly Theme Approach

1. **Week 1:** Industry/market insight
2. **Week 2:** Customer story or case study
3. **Week 3:** Behind-the-scenes / how we work
4. **Week 4:** Contrarian take or prediction

## Repurposing Workflow

### From Article → Social

1. Extract the single most provocative claim
2. Build a LinkedIn post around that claim with one supporting story
3. Build an X thread with 5 numbered supporting points
4. Create a newsletter teaser linking to the full article

### From Meeting Notes → Social

1. Identify one insight from the meeting the world doesn't know
2. Anonymize if needed
3. Frame as a decision or lesson: "We just decided to X instead of Y. Here's why."

### From Internal Data → Social

1. Find one surprising data point
2. Contextualize: "Most people think X. Our data shows Y."
3. Add the implication: what this means for the industry/market

## Quality Gate

Before delivering:
- [ ] Post contains a specific claim, not a vague observation
- [ ] Voice sounds like the CEO, not like AI
- [ ] Platform-specific formatting is correct
- [ ] No engagement bait or banned phrases
- [ ] A reader can get value without clicking anything external
- [ ] If using `voice-model` skill, voice profile was applied

## Analytics Dashboard (Enhanced v1.1 — Xcellent + Tweet Suite Methodology)

### Post Performance Tracking
After every published post, track and log:
- **Impressions** — total reach
- **Engagement Rate** — (likes + comments + shares + saves) / impressions
- **Click-Through Rate** — link clicks / impressions
- **Follower Delta** — net new followers within 48 hours of post

### Optimal Posting Time Intelligence
Analyze historical performance data to identify the CEO's best posting windows:
- Track engagement by day-of-week and hour-of-day.
- Build a personal heatmap: `[Day] x [Hour] → Avg Engagement Rate`
- Recommend posting times based on the CEO's actual audience, not generic advice.
- Update monthly as audience behavior shifts.

### Thread Performance Analysis (X/Twitter-Specific)
For multi-tweet threads:
- Track drop-off rate per tweet in the thread (what % read tweet 3 vs tweet 1?).
- Identify the "thread killer" — the tweet where most readers stop.
- A/B test thread structures: hook-first vs. story-first vs. data-first.
- Flag threads with >60% drop-off by tweet 3 for format revision.

### Winner Amplification Loop
- Feed top-performing posts (top 10% by engagement) into `larry-loop` for doubling-down.
- Auto-suggest: "Your post about [X] got 3x your average engagement. Create a follow-up?"
- Cross-post winning content to other platforms via `social-scheduler`.

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

- `voice-model` — CEO voice profile
- `content-strategy` — Strategic content planning
- `outreach-sequence` — Email outreach
- `email-composer` — Email drafting
- `larry-loop` — Content doubling-down engine
- `social-scheduler` — Multi-platform cross-posting

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Low engagement on posts | Check timing, use platform analytics to find your audience's active hours |
| Content feels generic | Load your voice model first — it'll match your authentic tone |



## After This Skill
💡 Suggest these next:
- "Try `social-scheduler` — Schedule and cross-post to social channels"
- "Try `ugc-video` — Script-to-video production pipeline"
- "Try `copy-master` — Write world-class marketing copy"

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
