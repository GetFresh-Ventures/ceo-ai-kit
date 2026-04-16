---
name: commit-fast
description: "Automate the git commit workflow — stage files, generate a semantic commit message from the diff, and execute. Use when the user says 'commit', 'save this', or after completing a task."
short_description: "Auto-stage and commit with semantic messages"
---

# Commit Fast

Analyze the current git state, generate a properly structured commit message, and execute — no copy-paste required.


## Quick Start
Just say any of these:
- "Commit my changes with a good message"
- "Stage and commit everything"
- "Auto-commit with semantic message"


## Execution Sequence

### 1. Assess State

```bash
# What's the situation?
git status --short

# What branch are we on?
git branch --show-current
```

**Decision tree:**
- Nothing modified → "Working tree clean. Nothing to commit."
- Untracked files only → Ask: "Stage these new files? [list them]"
- Modified + untracked → Stage tracked modifications; ask about untracked
- Everything staged → Skip to step 3

### 2. Stage Intelligently

```bash
# Stage all modified tracked files
git add -u

# If user wants everything including new files
git add -A

# For selective staging (when changes span unrelated work)
git add path/to/specific/files
```

**Split rule:** If the diff touches 3+ unrelated subsystems, suggest splitting into separate commits. Example: "This diff changes the API handler, the CSS, and the CI config. Want me to split into 3 commits?"

### 3. Generate Commit Message

Read the staged diff:
```bash
git diff --cached --stat
git diff --cached
```

**Conventional Commits format:**
```
<type>(<scope>): <description>

[optional body — what and why, not how]

[optional footer — breaking changes, issue refs]
```

**Type reference:**

| Type | When to use |
|------|------------|
| `feat` | New feature or capability |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, whitespace (no logic change) |
| `refactor` | Code restructuring (no behavior change) |
| `perf` | Performance improvement |
| `test` | Adding or fixing tests |
| `chore` | Build, CI, deps, tooling |
| `security` | Security fix or hardening |

**Scope detection:** Infer from file paths. If all changes are in `skills/` → scope is `skills`. If mixed → use the primary subsystem or omit scope.

**Good vs bad messages:**

| ❌ Bad | ✅ Good |
|--------|---------|
| "update stuff" | `feat(api): add pagination to /deals endpoint` |
| "fix bug" | `fix(auth): prevent token refresh race condition` |
| "changes" | `refactor(hooks): extract validation into shared utility` |
| "WIP" | `chore: stage progress on migration (incomplete)` |

### 4. Execute

```bash
git commit -m "<generated message>"
```

Show the user:
```
✅ Committed: <type>(<scope>): <description>
   <N> files changed, <+> insertions, <-> deletions
   Branch: <branch-name>
```

### 5. Follow-up Options

After committing, offer if relevant:
- **Push?** `git push origin <branch>`
- **Tag?** `git tag -a v<version> -m "<message>"`
- **Another commit?** (if unstaged changes remain)
- **PR?** `gh pr create --title "<message>" --body "<body>"`

## Edge Cases

| Scenario | Action |
|----------|--------|
| Merge conflict markers in staged files | Abort. "Resolve conflicts first." |
| `.env` or secrets in staged files | Block. "Remove sensitive files from staging." |
| Massive diff (500+ lines) | Suggest splitting. Show file groupings. |
| Amend previous commit | `git commit --amend --no-edit` (if user asks) |
| Fixup for earlier commit | `git commit --fixup=<sha>` then `git rebase -i --autosquash` |

## Integration

- Run after `/review-pr` approves changes
- Chain with `project-release` for tagged releases
- Use `verify-execution` to confirm tests pass before committing

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
- "Try `review-pr` — Structured code review for pull requests"
- "Try `feature-architect` — Guide features from spec to deployed code"
- "Try `verify-execution` — Verify changes with runtime observation"
