---
name: review-pr
description: "Perform a structured code review on a pull request or git diff. Use when asked to review code, check a PR, audit changes, or before merging any branch."
---

# Code Review

Perform a rigorous, structured review of code changes. Never rubber-stamp. Every review must produce actionable findings or an explicit clean bill.

## When to Use

- User says "review this PR", "check my changes", "look at this diff"
- Before any merge to main/master
- After completing a major feature branch
- When another agent's output needs validation

## Step 1: Gather the Diff

```bash
# For a branch vs main
git diff main...HEAD --stat
git diff main...HEAD

# For staged changes
git diff --cached

# For a specific PR (GitHub CLI)
gh pr diff <PR_NUMBER>

# For last N commits
git log --oneline -5
git diff HEAD~3..HEAD
```

Summarize: how many files changed, lines added/removed, which subsystems are touched.

## Step 2: Structural Scan

Before reading code line-by-line, answer these architectural questions:

| Question | What to check |
|----------|--------------|
| **Scope creep?** | Does the diff touch files unrelated to the stated goal? |
| **Missing tests?** | Are there new functions/endpoints without corresponding test files? |
| **Config drift?** | Are there changes to `.env`, `config`, or infra files mixed with feature code? |
| **Migration safety?** | Database schema changes — are they reversible? |
| **Dependency changes?** | New packages added to `package.json`, `requirements.txt`, `Cargo.toml`? |

## Step 3: Line-by-Line Review

For each changed file, evaluate against this checklist:

### Correctness
- [ ] Logic handles edge cases (null, empty, negative, overflow)
- [ ] Error paths return meaningful messages, not silent failures
- [ ] Async operations have proper error handling and timeouts
- [ ] Types are correct (no implicit `any`, no wrong casts)

### Security
- [ ] No hardcoded secrets, API keys, or credentials
- [ ] User input is validated/sanitized before use
- [ ] SQL queries use parameterized statements
- [ ] File paths are validated (no path traversal)
- [ ] Auth checks exist on protected endpoints

### Performance
- [ ] No N+1 query patterns
- [ ] No unbounded loops or recursive calls without limits
- [ ] Large data sets use pagination or streaming
- [ ] Expensive operations aren't inside hot loops

### Maintainability
- [ ] Functions are under 50 lines (split if larger)
- [ ] Variable names describe intent, not implementation
- [ ] No duplicated logic that should be extracted
- [ ] Comments explain *why*, not *what*

## Step 4: Classify Findings

Every finding gets a severity:

| Severity | Definition | Action |
|----------|-----------|--------|
| 🔴 **Critical** | Will cause crashes, data loss, or security vulnerabilities | Must fix before merge |
| 🟠 **Important** | Incorrect behavior, missing error handling, test gaps | Should fix before merge |
| 🟡 **Minor** | Style issues, naming, minor optimization opportunities | Fix at author's discretion |
| 💡 **Suggestion** | Alternative approaches, future improvements | No action required |

## Step 5: Produce the Review

Output format — always use this structure:

```markdown
## Code Review: [Branch/PR Name]

**Scope:** [N files, +X/-Y lines, subsystems touched]
**Verdict:** 🟢 Approve / 🟡 Approve with comments / 🔴 Request changes

### Findings

#### 🔴 Critical
- **[filename:line]** — [description of issue]
  - **Why:** [impact if not fixed]
  - **Fix:** [concrete suggestion]

#### 🟠 Important
- ...

#### 🟡 Minor
- ...

#### 💡 Suggestions
- ...

### What's Good
- [Specific praise for well-written code, good patterns, thorough tests]
```

## Red Flags — Stop and Escalate

- Diff includes `.env` files with real values → **Block immediately**
- Diff deletes tests without replacing them → **Request justification**
- Single commit touches 20+ files across unrelated systems → **Request split**
- No tests for new public API surface → **Block until covered**

## Integration

- Chain with `/commit-fast` after review passes
- Chain with `/analyze-issue` if review uncovers a bug
- Use `project-release` skill when review is the final gate before release
