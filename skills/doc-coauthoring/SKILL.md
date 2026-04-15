---
name: doc-coauthoring
description: "Structured document writing workflow with three stages: Context Gathering, Section-by-Section Refinement, and Reader Testing (sends to fresh AI with no context to catch blind spots). Use when the CEO needs to write strategy docs, board memos, proposals, decision docs, or any high-stakes document that must be clear to readers who weren't in the room."
short_description: "Structured document co-writing workflow"
metadata:
  version: 1.0.0
  category: document-processing
  triggers:
    - write a doc
    - strategy document
    - board memo
    - coauthor
    - write together
    - help me write
    - decision doc
    - thinking doc
---

# Doc Coauthoring

Write documents that work for readers who weren't in the room.


## Quick Start
Just say any of these:
- "Co-write a strategy document with me"
- "I have a rough draft — help me structure it"
- "Build an outline, then we'll write together"


## When to Activate

- Writing strategy documents, board memos, decision docs
- Creating proposals or engagement letters
- Any high-stakes document that needs to survive without the author present
- When the CEO says "help me write" or "let's put this together"

## The Three-Stage Workflow

### Stage 1: Context Gathering

**Goal:** Close the gap between what the CEO knows and what the agent knows.

Ask these meta-questions:
1. What type of document is this? (strategy doc, decision doc, proposal, memo)
2. Who's the primary audience?
3. What's the desired impact when someone reads this?
4. Is there a template or specific format to follow?
5. Any constraints or context to know?

Then encourage the CEO to **dump all context** they have:
- Background on the project/problem
- Related discussions or prior documents
- Why alternative solutions aren't being used
- Organizational context (team dynamics, politics, past failures)

**Accept messy input.** The CEO can answer in shorthand, bullet points, or stream of consciousness. Structure comes later.

### Stage 2: Section-by-Section Refinement

Build each section iteratively:

1. **Propose structure** — Suggest document outline based on context gathered
2. **Draft section by section** — Don't try to write everything at once
3. **Brainstorm at each section** — Offer alternatives, highlight gaps, suggest stronger framing
4. **Edit iteratively** — Refine based on CEO feedback

**Key principles:**
- One idea per paragraph
- Lead with the conclusion, then support it
- Cut everything that doesn't serve the reader
- Active voice, concrete language, no weasel words
- If a section needs data you don't have, flag it explicitly

### Stage 3: Reader Testing (The Secret Weapon)

**Before delivering the final document, test it with a fresh perspective:**

1. Take the finished document
2. Read it as if you had ZERO context about the project
3. Identify:
   - Sentences that only make sense if you were in the room
   - Acronyms or references that aren't explained
   - Logic jumps that skip important reasoning
   - Claims without evidence
   - Sections where a reader would think "so what?"

4. Report findings and fix them before the CEO sends it out

**This catches the #1 failure mode of executive documents:** the author assumes the reader has context they don't.

## Document Types and Templates

### Strategy Document
```
1. Executive Summary (the answer first)
2. Context / Background
3. The Problem (why now)
4. Options Considered
5. Recommended Approach
6. Implementation Plan
7. Risks and Mitigations
8. Decision Needed
```

### Decision Document
```
1. Decision Needed (one sentence)
2. Background (brief context)
3. Options (2-4 realistic options)
4. Recommendation (with reasoning)
5. Risks of recommended option
6. Risks of NOT acting
7. Next steps if approved
```

### Board Memo
```
1. Date, To, From, Re
2. Summary (3 sentences max)
3. Background
4. Key Issues
5. Recommendation
6. Required Board Action
7. Appendix
```

## Hard Bans on Bad Writing

Delete and rewrite:
- "It goes without saying" (then don't say it)
- "At the end of the day"
- "Synergy," "leverage," "paradigm shift"
- Passive voice hiding accountability ("mistakes were made")
- Paragraphs longer than 5 sentences
- Bullet lists with more than 7 items without grouping

## Quality Gate

Before delivering:
- [ ] Reader Test passed (no context-dependent blind spots)
- [ ] Every section has a clear purpose
- [ ] The document answers "so what?" in the first paragraph
- [ ] Claims are backed by evidence or flagged as assumptions
- [ ] A reader with no context can understand and act on it

## Related Skills

- `doc-builder` — .docx file generation
- `weekly-ceo-brief` — Weekly summary documents
- `chief-of-staff` — Multi-role coordination

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Voice doesn't match mine | Load your voice model first — run `/voice-model` before co-authoring |
| Structure feels wrong | Start with the outline stage — get agreement on structure before writing |



## After This Skill
💡 Suggest these next:
- "Try `doc-builder` — Create Word docs — proposals, memos, reports"
- "Try `google-doc-creation` — Create professional Google Docs in Drive"
- "Try `voice-model` — Build your personal writing voice model"
