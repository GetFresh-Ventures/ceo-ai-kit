---
name: context-prime
description: "Load full project context before starting work. Use at the beginning of any session, when switching projects, or when the agent seems to have lost context about the codebase."
short_description: "Load project context before starting work"
---

# Context Prime

Rapidly build a complete mental model of a project before writing any code. Never start work without context — uninformed changes break things.


## Quick Start
Just say any of these:
- "Load context for [project name]"
- "Prime yourself on everything about [client]"
- "Read all my project files before we start"


## When to Use

- Start of a new session
- Switching to a different project or repo
- Agent is making assumptions that don't match the codebase
- Before any architectural change
- User says "look at this project", "get up to speed", "context"

## Step 1: Project Identity

```bash
# What is this?
cat README.md | head -30

# What language/framework?
ls package.json Cargo.toml pyproject.toml setup.py go.mod Gemfile pom.xml 2>/dev/null

# How big is it?
find . -type f -name "*.py" -o -name "*.ts" -o -name "*.js" -o -name "*.go" -o -name "*.rs" | wc -l
```

Note and report:
- **Language:** Python / TypeScript / Go / Rust / etc.
- **Framework:** Next.js / FastAPI / Rails / etc.
- **Package manager:** npm / pip / cargo / etc.

## Step 2: Architecture Scan

```bash
# Directory structure (2 levels deep)
find . -maxdepth 2 -type d | grep -v node_modules | grep -v .git | grep -v __pycache__ | sort

# Entry points
ls src/index.* src/main.* app.* manage.py main.* cmd/ 2>/dev/null

# Configuration files
ls .env .env.example .env.local docker-compose.yml Dockerfile Makefile 2>/dev/null
```

Build a mental map:
- Where does code live? (`src/`, `lib/`, `app/`)
- Where are tests? (`tests/`, `__tests__/`, `spec/`)
- Where is config? (`.env`, `config/`)
- Where are docs? (`docs/`, `README.md`)

## Step 3: Dependency Map

```bash
# Node.js
cat package.json | jq '.dependencies, .devDependencies' 2>/dev/null

# Python
cat requirements.txt 2>/dev/null || cat pyproject.toml 2>/dev/null | head -40

# Go
cat go.mod 2>/dev/null | head -20
```

Flag notable dependencies:
- Database ORMs (SQLAlchemy, Prisma, Sequelize)
- Auth libraries (passport, authlib, jwt)
- API frameworks
- Testing frameworks

## Step 4: Test Infrastructure

```bash
# Find test runner
grep -r "test\|jest\|pytest\|mocha\|vitest" package.json pyproject.toml 2>/dev/null | head -5

# Count tests
find . -name "test_*" -o -name "*.test.*" -o -name "*_test.*" -o -name "*.spec.*" 2>/dev/null | wc -l

# Run tests (dry run to see what exists)
# npm test -- --listTests 2>/dev/null
# pytest --collect-only 2>/dev/null | tail -5
```

## Step 5: Git State

```bash
# Recent history
git log --oneline -10

# Current branch and status
git branch --show-current
git status --short

# Active branches
git branch -a --sort=-committerdate | head -10
```

## Step 6: Environment and Secrets

```bash
# Check for env template
cat .env.example 2>/dev/null || cat .env.template 2>/dev/null

# Check for required environment variables in code
grep -rn "os.environ\|process.env\|os.Getenv" --include="*.py" --include="*.ts" --include="*.js" --include="*.go" . 2>/dev/null | head -15
```

**Never read `.env` files aloud.** Note which env vars are required, not their values.

## Step 7: Special Files

Check for agent/AI configuration:
```bash
ls CLAUDE.md .cursorrules AGENT.md .github/copilot-instructions.md 2>/dev/null
```

If any exist, read them — they contain project-specific rules the agent must follow.

## Output: Context Brief

After completing the scan, produce this summary:

```markdown
## Context Brief: [Project Name]

**Stack:** [Language] + [Framework] + [Database]
**Size:** [N] source files, [M] test files
**Branch:** [current branch] — [clean/dirty]

### Architecture
- [Key architectural patterns observed]
- [Entry point: path/to/main]
- [Database: type + ORM]

### Dependencies (notable)
- [Key deps and what they do in this project]

### Test Coverage
- [Test framework, approximate coverage level]
- [How to run tests: command]

### Environment
- [Required env vars (names only)]
- [Local setup needed?]

### Agent Rules
- [Any rules from CLAUDE.md/AGENT.md/.cursorrules]

### Recent Activity
- [Last 3-5 commits summarized]
```

## Integration

- Always run before `/create-prd` or `/analyze-issue` on unfamiliar code
- Feeds into `/chief-of-staff` situational awareness
- Re-run after major refactors to update mental model

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
- "Try `meeting-prep` — Build pre-meeting intelligence dossiers"
- "Try `deal-review` — Pipeline review — flag stale deals, find gaps"
- "Try `chief-of-staff` — Your always-on executive AI assistant"
