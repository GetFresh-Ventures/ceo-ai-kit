# The CEO Mindset for AI

Most executives fail with AI because they treat it like a search engine or an intern. They type a quick question, get a generic answer, and conclude, "It's not there yet."

To get ROI from Claude Code and this CEO AI Kit, you need to change your mental model.

## 1. Treat It Like a Chief of Staff
You wouldn't tell a brilliant new Chief of Staff: "Write a cold email to Acme." You'd give them context: "We met Acme at the SaaS conference. They have a $500k problem with churn. Draft an email that leans on our case study, doesn't sound salesy, and asks for a 15-minute call on Thursday to share our data."

**The Rule**: High-context inputs equal high-leverage outputs. Give the AI the *why*, the *who*, and the *angle*.

### Real Example — Bad vs. Good

❌ **Low-context (intern mode)**:
> "Write a follow-up email to John."

✅ **High-context (Chief of Staff mode)**:
> "Write a follow-up email to John Park at Meridian Capital. We met at the CFO roundtable last Thursday. He mentioned they're evaluating board portals because their current one (Diligent) costs $40k/year and their audit committee hates the interface. Reference our conversation about the audit workflow. Don't pitch — ask if he'd be open to seeing a 3-minute demo video I can send over. Keep it under 100 words."

The second prompt produces an email you'd actually send. The first produces corporate filler.

## 2. Give It Your Brain
AI defaults to the average of the internet. The average of the internet is B2B corporate speak ("synergize," "leverage," "transformative innovations"). 

To make the AI sound like you, you have to give it your communication patterns. That's why the `voice-model.md` exists. Spend the 20 minutes to fill it out. The ROI on that 20 minutes is hundreds of saved hours over the next year.

### What to Include in Your Voice Model
- **3 emails you've sent** that you're proud of (paste them in)
- **Words you never use** (e.g., "synergy," "leverage," "paradigm")
- **Words you always use** (e.g., "straightforward," "here's the deal," "let's move")
- **Your sign-off style** (e.g., "Best," vs. "Talk soon," vs. just your name)
- **Your formatting preference** (bullets vs. paragraphs, short vs. detailed)

## 3. Emphasize "Cheapest First" Execution
When trying to solve a problem with Claude, look at your resources in order of cost and reliability:
1. **In-Context**: Do I already know this? (Zero cost, instant)
2. **CRM/Memory**: Is this in our systems? (Low cost, highly reliable)
3. **Web Search**: Can I find it publicly? (Medium cost, variable reliability)
4. **Reasoning/Synthesis**: Is this a brand new problem? (High cost, requires advanced models)

### Example
If you ask "What stage is the Meridian deal in?" — the AI should check your CRM first (cost: 1 API call), not reason about it from scratch (cost: thousands of tokens of hallucination risk).

## 4. Iterate, Don't Accept the First Draft
If the first draft of an email or brief is 80% there, don't throw it out or rewrite it yourself. Tell Claude what needs to change.

```
"This sounds too formal. Make it punchier. Remove the bullet points 
and make it two short paragraphs."
```

```
"Good structure but the opening line is weak. Start with the 
specific problem they mentioned on the call, not a generic greeting."
```

The magic is in **iteration**, not generation. The first draft is raw material. Your job is editorial direction.

## 5. Automate the Rote to Elevate the Human
Don't use AI to completely replace human touch in relationships (e.g., auto-sending cold emails without review). Use it to automate the *preparation* (research docs, CRM hygiene, drafting) so your actual human interaction is 10x more prepared, present, and valuable.

**Automate**: Research, drafting, data synthesis, scheduling prep, report generation.
**Keep human**: Final send approval, relationship judgment, strategic decisions, tone calibration.

You are the relationship owner. Claude is your intelligence layer.

## 6. Build Compound Intelligence
Every session with your AI should make the next session better. This is why the CEO AI Kit saves:
- **Voice model** → learns your communication style
- **Decision log** → tracks patterns in your choices
- **Meeting notes** → builds institutional memory
- **Learnings file** → captures what works and what doesn't

A CEO who uses this for 90 days has an AI that knows their business intimately. A CEO who starts fresh every session is stuck in perpetual onboarding.

## 7. Think in Workflows, Not One-Shots
The biggest ROI comes from chaining skills together, not using them in isolation:

| Scenario | Workflow |
|----------|----------|
| Before a board meeting | `/meeting-prep` → `/board-deck-builder` → `/email-composer` (to send agenda) |
| Friday pipeline review | `/deal-review` → `/pipeline-pulse` → `/weekly-ceo-brief` |
| New lead came in | `/competitive-intel` → `/outreach-sequence` → `/email-composer` |
| After a client call | `/post-meeting-brief` → `/decision-logger` → `/email-composer` (follow-up) |

the CEO AI Kit is designed so skills feed into each other. Use them as a system, not as individual tools.
