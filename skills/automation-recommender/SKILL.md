---
name: automation-recommender
description: Analyze a codebase and recommend automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their setup, mentions improving workflows, or wants to know what features they should use in their repository.
---

# Automation Recommender

Analyze codebase patterns to recommend tailored AI automations across all extensibility options.

**This skill is read-only.** It analyzes the codebase and outputs recommendations. It does NOT create or modify any files. 

## Workflow

### Phase 1: Codebase Analysis
Gather project context:
1. Detect project type and tools (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`).
2. Check dependencies for MCP server recommendations (e.g., React, Supabase, Stripe).
3. Analyze project structure (e.g., `src/`, `tests/`, `components/`).

### Phase 2: Generate Recommendations
Based on analysis, generate recommendations across categories:
- **MCP Servers**: Live documentation lookup (context7), Browser testing (Playwright), Databases.
- **Skills**: Document workflows, API documenter, component scaffolding.
- **Hooks**: Format on save, lint checks, blocking `.env` edits.
- **Subagents**: Specialized reviewers (accessibility, security).

### Phase 3: Output Recommendations Report
Format recommendations clearly. **Only include 1-2 recommendations per category** - the most valuable ones for this specific codebase. Skip categories that aren't relevant.

```markdown
## Automation Recommendations
I've analyzed your codebase and identified the top automations for each category.

### 🔌 MCP Servers
#### [MCP Server Name]
**Why**: [Reason based on detected libraries]
**Install**: [Installation command]

### 🎯 Skills
#### [Skill Name]
**Why**: [Specific reason]

### ⚡ Hooks
#### [Hook Name]
**Why**: [Specific reason based on detected config]

### 🤖 Subagents
#### [Agent Name]
**Why**: [Specific reason]
```
