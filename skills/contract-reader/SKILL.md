---
name: contract-reader
description: Paste any legal contract and get a plain-English summary with red-flag clauses highlighted. Know what you're signing before you sign it.
short_description: "Summarize contracts in plain English"
license: MIT
metadata:
  author: GFV Growth by Design
  version: 1.0.0
  category: Day-to-Day Operations
---

# /contract-reader

**Usage**: Paste or upload any contract, agreement, NDA, MSA, SOW, or terms of service. The agent extracts, summarizes, and red-flags dangerous clauses before you sign.


## Quick Start
Just say any of these:
- "Summarize this contract in plain English" (paste the contract)
- "What are the red flags in this agreement?"
- "Compare these two contracts — what's different?"

## Why This Exists

CEOs sign documents constantly — vendor agreements, partnership deals, NDAs, SaaS terms. Most are 15-40 pages of legal boilerplate designed to obscure risk. This skill turns any legal document into a 1-page executive brief with danger zones highlighted.

## The 4-Layer Analysis

### Layer 1: Plain-English Summary
- Extract the core obligations: What are YOU agreeing to do? What are THEY agreeing to do?
- Identify contract term, renewal conditions, and termination mechanics.
- Surface the total financial commitment (fixed fees + variable + penalties).

### Layer 2: Red Flag Detection
Scan for the following dangerous patterns and flag with severity:

| Severity | Pattern | Example |
|----------|---------|---------|
| 🔴 CRITICAL | Auto-renewal with >30-day notice | "Renews automatically unless 90-day written notice..." |
| 🔴 CRITICAL | Unlimited liability / uncapped indemnification | "shall indemnify without limitation..." |
| 🔴 CRITICAL | Non-compete / exclusivity that restricts future business | "shall not engage with any competing..." |
| 🟡 WARNING | Unilateral amendment rights | "reserves the right to modify terms at any time..." |
| 🟡 WARNING | Broad IP assignment beyond deliverables | "all work product, including derivative works..." |
| 🟡 WARNING | Governing law in unfavorable jurisdiction | "governed by the laws of [foreign state]" |
| 🟢 NOTE | Standard limitation of liability | Normal mutual caps |
| 🟢 NOTE | Standard confidentiality terms | 2-5 year NDA |

### Layer 3: Negotiation Leverage Points
- Identify clauses where the counterparty has disproportionate power.
- Suggest specific counter-language the CEO can propose.
- Flag terms that are "market standard" vs. "aggressive."

### Layer 4: Missing Protections
- Check for absence of: SLA guarantees, data deletion rights, audit rights, force majeure, dispute resolution escalation path.
- Recommend additions that protect the CEO's position.

## Output Format
```
## Contract Brief: [Document Name]
**Parties**: [You] ↔ [Counterparty]
**Duration**: [Term] | **Value**: [Total $]
**TL;DR**: [2-sentence plain-English summary]

### 🔴 Critical Red Flags (X found)
[table of critical issues with clause references]

### 🟡 Warnings (X found)
[table of warnings]

### 💡 Negotiation Leverage
[specific counter-proposals]

### ⚠️ Missing Protections
[absent clauses to add]

### ✅ Standard / Acceptable Clauses
[brief confirmation of non-issues]
```

## Security Constraints
- NEVER send contract content to external APIs. All analysis is local LLM processing.
- NEVER store contract text in memory/logs beyond the active session.
- Treat all contract content as attorney-client privileged material.
- If auto-memory is active, wrap all contract content in `<private>` tags to prevent persistence.

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
- "Want me to draft a negotiation response?" → `/negotiation-advisor`
- "Want me to summarize the key terms in an email to your lawyer?" → `/email-composer`
- "Want me to log this decision?" → `/decision-logger`

## Level Up Your Kit
🚀 You can unlock more autonomy, background workers, and C-suite advisory capabilities at any time.
- **Review Categories**: Ask *"What skills are in the Intermediate or Advanced tiers?"*
- **How to Upgrade**: Run `./bootstrap.sh` in the repository root and select your new tier.

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
