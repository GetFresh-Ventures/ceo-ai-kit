# Growth by Design
**Version**: v1.3.0
**A GTM Enablement Kit for the AI-Powered Executive**

*An exclusive framework for GFV Portfolio CEOs.*

Growth by Design is a plug-and-play enablement kit that integrates directly into your Claude Code environment. It packages battle-tested Go-To-Market (GTM) methodologies, workflows, and prompts into a system that acts as your autonomous Chief of Staff.

## What's New in v1.3.0 (Autonomous Execution Hardening)
- **Precise Token Monitoring (`ccflare.py`):** An executive token burn dashboard executing locally ensuring CEOs actively track Claude usage costs including cache creation/reads.
- **Autonomous Memory Consolidation (`gfv-dream.sh`):** A robust script to natively search through your Claude session `jsonl` logs and compress insights directly into persistent memory.
- **Strict Code/Deployment Pipeline (`/review-pr`):** Instantiates the rigorous Anthropic security prompt architecture to safeguard your GitHub / Tracking deploy loops.
- **Multi-Level Agent Validations (`lint-agent.sh`):** Failsafe scripts ensuring that prompt/agent configuration structures never break IDE tooling silently.
- **Smarter Auto-researching (`/autoresearch`):** Updated meta-skills to require explicit interview phases prior to applying environment mutations.

## What's New in v1.2.0 (Awesome Claude Edition)
- **Persistent State Vector DB (`claude-mem`):** Integrates an autonomous background memory system that hooks into CLI tools, allowing you to ask "what did I do yesterday" and instantly pull relevant terminal context via MCP.
- **Self-Optimizing Architecture (`/autoresearch`):** The kit now includes a premier meta-learning utility that can autonomously benchmark and improve any custom skill or prompt you write using pure experimental loops.
- **Frictionless Permissions (Dippy):** Automatically bypasses permission prompts for non-destructive commands like `ls` and `git diff` so your flow state is never interrupted.
- **Cost & Usage Dashboards:** Included `ccflare` gives you live dashboards of your token usage and execution pipeline. Type `ccflare` in your terminal to view.
- **New Supercharged Slash Commands:** Native Claude commands that execute massive tasks instantly: `/create-prd`, `/analyze-issue`, `/context-prime`, and `/commit-fast`.
- **The "Ralph" Execution Loop:** Batch-process hundreds of URLs or CRM logs fully unattended using the `tools/gfv-ralph.sh` loop.
- **Onboarding Pipeline:** Contains `ONBOARDING_PROMPT.md` for seamless environment booting.
- **Agent Agnostic Tools:** Decoupled from Claude Code specifically, mapped to Cursor `/rules` natively via `AGENT.md`.

## Why This Exists
As a CEO, your time is your most constrained asset. You don't have time to write 5-touch email sequences from scratch, manually synthesize pipeline reports, or dig through CRM notes before a critical meeting. 

This repository installs the **"Brain Architecture"** directly onto your machine, turning any generic AI (whether it's **Cursor, Claude Code, Copilot, or Antigravity**) into a personalized growth engine tailored exactly to your company and your voice.

## Installation & Setup

1. **Clone the Repo:**
   ```bash
   git clone git@github.com:GetFresh-Ventures/gfv_growth_by_design.git ~/.gfv_growth_by_design
   ```

2. **Run the Bootstrap Script:**
   ```bash
   cd ~/.gfv_growth_by_design
   ./bootstrap.sh
   ```
   *This script does the magic. It creates your `~/brain` directory, identifies if you're using Claude Code or Cursor, and maps the `AGENT.md` context and skills universally.*

3. **Configure Your Voice Model:**
   Open `~/brain/voice-model.md` and fill it out. This step is critical to ensure Claude writes in your authentic voice rather than generic B2B jargon.

## The Architecture

### 1. Your `~/brain` Directory
Think of this as Claude's persistent, local memory of your company. It contains:
- `voice-model.md`: How you write and speak.
- `pipeline.md`: The current state of your deals.
- `learnings.md`: An iterative log of market feedback.
- `meetings/`: Your intelligent meeting briefs.

### 2. Multi-Agent Context (The `AGENT.md` Core)
A single truth file representing the GFV Voice Model. When you run `bootstrap.sh`, it universally links to `.cursorrules` (for Cursor users) and `CLAUDE.md` (for Claude users).

### 3. Skills (`/skills`)
Specific, parameter-driven functions your agent knows how to execute flawlessly. 
- **Claude Code Users:** Automatically mapped to `.claude/skills/` to provide blazing fast native `/slash-commands` (e.g. `/email-composer`).
- **Cursor/Other LLM Users:** Read natively from the `/skills/` directory via the universal `AGENT.md` context instructions. You can simply state: "Run the email-composer skill."
    - `email-composer`: Writes outbound in your authentic voice.
    - `meeting-prep`: Builds actionable 1-page intelligence dossiers.
    - `pipeline-pulse`: Generates executive pipeline dashboards.
    - `autoresearch`: (NEW) Autonomously optimizes your custom prompts and skills via rigorous experimental loops.

### 4. Workflows (`/workflows`)
Step-by-step methodologies combining multiple skills for larger tasks.
- `weekly-pipeline-review.md`: The 30-minute Friday sanity check.
- `outreach-cadence.md`: Designing strategic, multi-touch engagement.
- **NEW** `gfv-ralph.sh` (The Ralph Loop): An orchestration loop to batch run hundreds of generative queries fully unattended.

### 5. Configs, Hooks & Tools (`/hooks` & `/tools`)
Scripts that intercept system actions or augment capabilities.
- **Dippy (Auto-Approval):** Automatically installed via `bootstrap.sh`. Intercepts safe shell commands (ls, cat, git status) and approves them instantly, saving you from constant "Y/n" prompts.
- **ccflare (Dashboards):** Installed globally. Run `ccflare` in your terminal to see real-time streaming dashboards of your active agents and token spend.
- **Linting:** Use `tools/lint-claude-md.sh` to ensure your Agent rules are perfectly formatted.
- **Tools:** Use `tools/gfv-cost-estimator.sh` to estimate LLM token pricing before you ask your agent to analyze huge CRM data exports.
- **Claude Users:** A template `claude_settings.template.json` is provided to auto-bind the `pre-send-review.py` script to prevent accidental email sending.
- **Cursor/Other Users:** Call explicitly in workflows (e.g. `python pre-send-review.py`).

### 6. Guides (`/guides`)
Best practices documents to ensure you extract maximum value from your AI.
- `prompt-eval-guide.md`: Detailed framework on how to construct rigorous standard operating procedures and pass criteria so `/autoresearch` can reliably score your prompts.

## Getting Started: The Zero-Friction Quickstart
Once bootstrapped, simply copy the contents of `ONBOARDING_PROMPT.md` and paste it into any new Cursor, Claude Code, or Gemini chat to instantly align your assistant with the GFV methodologies.

---
*Proprietary Methodology © GetFresh Ventures. All Rights Reserved.*
