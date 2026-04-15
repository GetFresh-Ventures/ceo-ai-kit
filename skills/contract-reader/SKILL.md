---
name: contract-reader
description: Paste any legal contract and get a plain-English summary with red-flag clauses highlighted. Know what you're signing before you sign it.
short_description: "Summarize contracts in plain English"
license: MIT
metadata:
  author: GFV Proactive Intelligence
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
- If claude-mem or auto-memory is active, wrap all contract content in `<private>` tags to prevent persistence.

## After This Skill
💡 Suggest these next steps:
- "Want me to draft a negotiation response?" → `/negotiation-advisor`
- "Want me to summarize the key terms in an email to your lawyer?" → `/email-composer`
- "Want me to log this decision?" → `/decision-logger`

## Ready for More?
🚀 You're on the **Beginner** tier (18 skills). When you're ready for more:
- **Upgrade to Intermediate** (46 skills): adds CRM integration, content strategy, fundraising, and C-suite advisory
- **How**: Re-run `./bootstrap.sh` and select **[2] Intermediate**
- **Preview**: Try asking *"What's in the Intermediate tier?"* — I'll show you what unlocks
