---
name: analyze-issue
description: "Systematically debug any bug, error, or unexpected behavior. Use before proposing fixes — find root cause first, never guess."
short_description: "Debug any bug or unexpected behavior"
---

# Systematic Issue Analysis

Find root cause before attempting fixes. Guessing wastes time and creates new bugs.

**The Iron Law:** No fixes without root cause investigation first.


## Quick Start
Just say any of these:
- "Debug this error: [paste error]"
- "Why is [feature] broken?"
- "Systematically find the root cause of [bug]"


## When to Use

- Test failures or build errors
- Unexpected runtime behavior
- Performance degradation
- "It worked yesterday" scenarios
- User-reported bugs
- After a failed fix attempt — especially then

## Phase 1: Reproduce and Observe

**Before touching any code:**

1. **Read the error completely**
   - Full stack trace, not just the last line
   - Note file paths, line numbers, error codes
   - Check if the error message contains the solution (it often does)

2. **Reproduce consistently**
   ```bash
   # Capture exact reproduction steps
   # Step 1: [exact command or action]
   # Step 2: [exact command or action]
   # Expected: [what should happen]
   # Actual: [what actually happens]
   ```
   - If not reproducible → add logging/instrumentation, don't guess

3. **Check what changed recently**
   ```bash
   # Recent commits
   git log --oneline -10

   # What changed in relevant files
   git diff HEAD~5 -- path/to/suspected/files

   # Recent dependency changes
   git diff HEAD~5 -- package.json requirements.txt Cargo.toml
   ```

## Phase 2: Trace the Data Flow

**Find WHERE it breaks, not just THAT it breaks:**

For multi-component systems (API → service → database, CI → build → deploy):

```
For EACH component boundary:
  1. Log/inspect what data ENTERS the component
  2. Log/inspect what data EXITS the component
  3. Find the layer where input is correct but output is wrong
  → THAT layer contains the bug
```

Example diagnostic instrumentation:
```bash
# Layer 1: API receives request
echo "=== Request payload: ==="
echo "$REQUEST_BODY" | jq .

# Layer 2: Service processes
echo "=== After transform: ==="
echo "$TRANSFORMED" | jq .

# Layer 3: Database query
echo "=== Query: ==="
echo "$SQL_QUERY"
echo "=== Result rows: $(echo "$RESULT" | wc -l) ==="
```

## Phase 3: Form and Test Hypothesis

**Scientific method — one variable at a time:**

1. **State the hypothesis clearly:**
   > "The bug is in [component] because [evidence]. Specifically, [X] happens when it should [Y] because [Z]."

2. **Test with the SMALLEST possible change**
   - One variable at a time
   - Never fix multiple things simultaneously
   - If hypothesis is wrong → form a NEW one, don't stack fixes

3. **Create a failing test first**
   ```
   Write a test that:
   - Passes with the bug present (reproduces the issue)
   - Will pass when the root cause is fixed
   ```

## Phase 4: Fix and Verify

1. **Fix the root cause, not the symptom**
   - If the fix is a null check → ask "why is it null in the first place?"
   - Trace upstream until you find the actual source of bad data

2. **Verify comprehensively**
   - Your failing test now passes?
   - No OTHER tests broke?
   - The original user-reported scenario works?
   - Edge cases covered?

3. **If fix doesn't work after 3 attempts → STOP**
   - 3+ failed fixes = architectural problem, not a bug
   - Question whether the pattern itself is sound
   - Escalate to the CEO/user before attempting fix #4

## Red Flags — Return to Phase 1

If you catch yourself thinking any of these, STOP:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "I don't fully understand but this might work"
- "One more fix attempt" (when already tried 2+)

## Output Format

```markdown
## Issue Analysis: [Brief Description]

**Symptom:** [What the user sees]
**Root Cause:** [What actually causes it]
**Evidence:** [How you confirmed this]

### Fix
- **File:** `path/to/file.py:42`
- **Change:** [Description of the fix]
- **Why:** [Why this fixes the root cause, not just the symptom]

### Verification
- [ ] Failing test created and passes after fix
- [ ] Existing test suite passes
- [ ] Original scenario works end-to-end
```

## Integration

- If analysis reveals a code quality issue → chain with `/review-pr`
- If fix requires planning → chain with `/create-prd`
- If issue is in production → document in `~/gtm-brain/learnings.md`

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

## After This Skill
💡 Suggest these next:
- "Try `verify-execution` — Verify changes with runtime observation"
- "Try `review-pr` — Structured code review for pull requests"
- "Try `feature-architect` — Guide features from spec to deployed code"
