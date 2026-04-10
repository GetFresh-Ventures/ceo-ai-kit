---
name: verify-execution
description: "Verify changes using runtime observation instead of diff-reading or unit tests"
version: 1.0.0
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

## Report Format
When verifying an execution, strictly use the following output format in your message or documentation update:

```markdown
## Verification: <one-line what changed>

**Verdict:** PASS | FAIL | BLOCKED | SKIP

**Claim:** <what it's supposed to do>

**Method:** <how you launched the test, which URLs/commands you ran>

### Steps
1. ✅/❌/⚠️/🔍 <what you did to the running app> -> <what you observed>

**Screenshot / Sample Evidence:** <screenshot file path or terminal output block>
```
