---
name: verify-execution
description: "Verify changes using runtime observation instead of diff-reading or unit tests. Includes autoagent's failure taxonomy for diagnosing what went wrong when verification fails."
metadata:
  version: 2.0.0
  category: execution-infrastructure
  origin: GFV v1 + autoagent failure taxonomy + overfitting rule
---

# Verify Execution (Runtime Observation)

**Verification is runtime observation.** You build the app, run it, drive it to where the changed code executes, and capture what you see. That capture is your evidence. Nothing else is.

**Do not run just unit tests.** CI runs tests. Running them again proves you can run CI. The time goes to running the actual application and interacting with the surface.

## Core Rules

1. **Find the Surface**: The surface is where a user meets the change. Check the surface directly.
   - *CLI / TUI* -> terminal (type the command, capture the pane).
   - *Server / API* -> socket (send the request with curl, capture the response).
   - *GUI / Web* -> pixels (drive it in a browser, capture a screenshot).
   
2. **Drive It**: Navigate to the smallest path that makes the changed code execute.
   - Changed a flag? Run the command with that flag.
   - Changed a handler? Hit that route via HTTP.
   - Changed an internal function? Find the CLI command / request / render that reaches it. Run that.
   
3. **Capture & Prove**: Captured output is evidence; your memory isn't. Take screenshots, run commands, and dump the panes.

## Failure Taxonomy (from autoagent)

When verification **fails**, diagnose the root cause before attempting a fix:

| Failure Pattern | Symptoms | What to Do |
|----------------|----------|------------|
| **Misunderstanding** | The change doesn't match what was asked for | Re-read the requirement. Clarify with the user. Don't guess. |
| **Missing capability** | The approach can't achieve the goal | Change the approach. Research alternatives. Don't force it. |
| **Weak info gathering** | Made assumptions instead of checking | Read the actual code, configs, docs. Check env vars. Don't assume. |
| **Bad execution** | Right idea, wrong implementation | Debug the specific failure. Fix that, not something else. |
| **Missing verification** | Didn't actually test the change | Go back to step 1. Find the surface. Drive it. Capture. |
| **Silent failure** | "It works" but it actually doesn't | Check edge cases. Check error logs. Check the thing downstream. |
| **Overfitting** | Fixed the symptom, not the cause | Ask: "If this exact scenario disappeared, would the fix still be worthwhile?" |

## The Overfitting Test

Before declaring a fix complete, ask:
> "If this exact test case disappeared tomorrow, would this change still be a worthwhile improvement?"

- **YES** → The fix is generalizable. Good.
- **NO** → You overfitted to one scenario. Rethink.

## The Simplicity Criterion

When two fixes produce the same result:
> "Keep the simpler one."

More code = more bugs = more maintenance. If a 3-line fix does what a 30-line fix does, choose the 3-line fix.

## Report Format

When verifying an execution, strictly use the following output format:

```markdown
## Verification: <one-line what changed>

**Verdict:** PASS | FAIL | BLOCKED | SKIP

**Claim:** <what it's supposed to do>

**Method:** <how you launched the test, which URLs/commands you ran>

### Steps
1. ✅/❌/⚠️/🔍 <what you did to the running app> -> <what you observed>

**Root Cause (if FAIL):** <diagnosis from failure taxonomy>
**Fix Applied:** <what you changed>
**Retest:** PASS / FAIL

**Screenshot / Sample Evidence:** <screenshot file path or terminal output block>
```

## The "Not Verified Until Captured" Rule

From clawchief's "not handled until in the system" principle:
- Saying "it works" ≠ verified
- Reading the diff ≠ verified
- Running unit tests ≠ verified
- **Only captured runtime output = verified**

## Quality Gate

Before marking any change as verified:
- [ ] Found the surface where the change is visible
- [ ] Drove the app to execute the changed code
- [ ] Captured evidence (screenshot, terminal output, HTTP response)
- [ ] If FAIL: diagnosed root cause from failure taxonomy
- [ ] If fix applied: retested and captured new evidence
- [ ] Overfitting test passed
- [ ] Simplicity criterion considered

## Related Skills

- `experiment-loop` — For A/B testing changes systematically
- `chief-of-staff` — For surfacing verification failures in heartbeat
- `commit-fast` — Only commit after verification passes
