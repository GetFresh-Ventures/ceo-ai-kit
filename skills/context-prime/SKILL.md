---
name: context-prime
description: "Load full project context before starting work. Use at the beginning of any session, when switching projects, or when the agent seems to have lost context about the codebase."
---

# Context Prime

Rapidly build a complete mental model of a project before writing any code. Never start work without context — uninformed changes break things.

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
