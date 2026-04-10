# Changelog

All notable changes to this project will be documented in this file.

## 2026-04-10 6:53 PM CT — v1.3.0 — Autonomous Execution Hardening

### Added
- Created `tools/ccflare.py` local executive dashboard to accurately calculate and display total agent token burn factoring in cache tokens natively.
- Integrated `tools/gfv-dream.sh` and `/gfv-dream-mode` to synthesize and compress fragmented session transcripts into durable knowledge natively via JSONL parsing.
- Added `skills/review-pr` skill to perform secure 3-pass reviews (Security, Logic, GTM Strategy) on deployment candidates.
- Added `tools/lint-agent.sh` to enforce AST integrity and formatting validations on `AGENT.md`.
- Added new workflows `project-release` to structure repo deployments.

### Changed
- Promoted `README.md` to version 1.3.0.
- Enhanced `AGENT.md` to formally adopt multi-model agent routing, multi-agent pipelining, and parallel planning frameworks.
- Updated `skills/autoresearch` to require an explicit context 'Interview Phase' prior to arbitrary code mutations.


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
