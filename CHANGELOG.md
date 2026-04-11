# Changelog

All notable changes to this project will be documented in this file.

## 2026-04-10 6:53 PM CT — v1.3.0 — Autonomous Execution Hardening

### Why it matters
This release hardens the GFV Enablement Kit from a static prompt library into a self-monitoring autonomous agent framework. CEOs now have native tooling for token cost visibility, secure deployment reviews, and persistent memory consolidation — closing the gap between ad-hoc AI usage and governed, repeatable execution.

### Added
- **`tools/ccflare.py`** — Local executive dashboard for real-time Claude token burn tracking, including cache creation/read costs
- **`tools/gfv-dream.sh`** — Autonomous memory consolidation script that parses Claude `.jsonl` session logs and compresses insights into durable knowledge
- **`skills/review-pr`** — 3-pass deployment review skill (Security, Logic, GTM Strategy) modeled on Anthropic's internal security protocols
- **`tools/lint-agent.sh`** — AST integrity validator for `AGENT.md` to prevent silent IDE tooling failures
- **`skills/project-release`** — Governed release workflow for version management
- **`skills/verify-execution`** — Post-task verification skill
- **`skills/onboard`** — Zero-friction CEO onboarding skill

### Changed
- **`AGENT.md`** — Formally adopted multi-model agent routing, multi-agent pipelining, and parallel planning frameworks
- **`skills/autoresearch`** — Now requires explicit "Interview Phase" before applying environment mutations
- **`ONBOARDING_PROMPT.md`** — Updated for v1.3.0 capabilities
- **`bootstrap.sh`** — Refined for new tool registrations
- Promoted `README.md` to version 1.3.0

### Files Modified
- AGENT.md, CHANGELOG.md, ONBOARDING_PROMPT.md, README.md, bootstrap.sh
- skills/autoresearch/SKILL.md, skills/onboard/SKILL.md, skills/project-release/SKILL.md
- skills/review-pr/SKILL.md, skills/verify-execution/SKILL.md
- tools/ccflare.py, tools/gfv-audit.sh, tools/gfv-dream.sh, tools/gfv-ralph.sh, tools/lint-agent.sh


## 2026-04-10 10:10 AM CT — v1.2.0 — Awesome Claude Edition

### Added
- Integrated `claude-mem` for persistent background vector-database memory across sessions natively via `bootstrap.sh`.
- Added the `/autoresearch` meta-skill for autonomous multi-loop skill evaluation and mutation testing.
- Integrated `ccflare` dashboard for cost and latency token visualization.
- Implemented `Dippy` friction removal to auto-approve non-destructive system tools.
- Included the "Ralph" (`tools/gfv-ralph.sh`) background execution loop.
- Wrote `guides/prompt-eval-guide.md` to standardize custom binary evaluations.

### Changed
- Promoted `README.md` to version 1.2.0, documenting all new awesome-claude capabilities.
- Redefined `AGENT.md` to mandate proactive consumption of `# search`, `# timeline`, and `# get_observations` memory events prior to polling the user.

## 2026-04-09 9:44 PM CT — v1.1.0 — Agent Agnostic Universal Architecture

### Added
- `ONBOARDING_PROMPT.md` template for zero-friction agent spinning and quickstarts.
- `tools/gfv-cost-estimator.sh` to estimate LLM costs on large payloads (CRM files/exports).
- `claude_settings.template.json` logic for automated guardrails mapping.

### Changed
- Converted `CLAUDE.md` to `AGENT.md` (universal context rules).
- Refactored `bootstrap.sh` to dynamically link the `AGENT.md` to `.cursorrules` and `CLAUDE.md` contexts simultaneously.
- Refactored `bootstrap.sh` to conditionally symlink skills into `.claude/skills` only if Claude is detected.
- Updated README to reflect universal availability across Claude Code, Cursor, and Gemini architectures.

## 2026-04-09 8:50 PM CT — v1.0.0 — Initial Release: Enablement Kit Foundation

### Added
- Core enablement `README.md` containing full architecture reference.
- `bootstrap.sh` script for rapid setup and symlinking of the environment.
- Foundational `skills/` directory (email-composer, meeting-prep, pipeline-pulse).
- Foundational `workflows/` directory (weekly-pipeline-review, outreach-cadence, meeting-day).
- Pre-send review hook implementation for communication safety.
