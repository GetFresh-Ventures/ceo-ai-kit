# Growth by Design
**Version**: v1.0.0
**A GTM Enablement Kit for the AI-Powered Executive**

*An exclusive framework for GFV Portfolio CEOs.*

Growth by Design is a plug-and-play enablement kit that integrates directly into your Claude Code environment. It packages battle-tested Go-To-Market (GTM) methodologies, workflows, and prompts into a system that acts as your autonomous Chief of Staff.

## What's New in v1.0.0
- **Initial Release:** Complete architecture mapping for GFV Growth By Design.
- **Bootstrapping Script:** Fully functional `bootstrap.sh` added for fast installation.
- **Core Framework:** Foundational skills, workflows, and hooks configured for executives.

## Why This Exists
As a CEO, your time is your most constrained asset. You don't have time to write 5-touch email sequences from scratch, manually synthesize pipeline reports, or dig through CRM notes before a critical meeting. 

This repository installs the **"Brain Architecture"** directly onto your machine, turning Claude from a generic chatbot into a personalized growth engine tailored exactly to your company and your voice.

## Installation & Setup

1. **Clone the Repo:**
   ```bash
   git clone git@github.com:GetFresh-Ventures/gfv_growth_by_design.git ~/.gfv_growth_by_design
   ```

2. **Run the Bootstrap Script:**
   ```bash
   cd ~/.gfv_growth_by_design
   chmod +x bootstrap.sh
   ./bootstrap.sh
   ```
   *This creates your `~/brain` directory, symlinks necessary hooks, and sets up your default context.*

3. **Configure Your Voice Model:**
   Open `~/brain/voice-model.md` and fill it out. This step is critical to ensure Claude writes in your authentic voice rather than generic B2B jargon.

## The Architecture

### 1. Your `~/brain` Directory
Think of this as Claude's persistent, local memory of your company. It contains:
- `voice-model.md`: How you write and speak.
- `pipeline.md`: The current state of your deals.
- `learnings.md`: An iterative log of market feedback.
- `meetings/`: Your intelligent meeting briefs.

### 2. Skills (`/skills`)
Specific, parameter-driven functions Claude knows how to execute flawlessly.
- `email-composer`: Writes outbound in your authentic voice.
- `meeting-prep`: Builds actionable 1-page intelligence dossiers.
- `pipeline-pulse`: Generates executive pipeline dashboards.
- ...and 5 more.

### 3. Workflows (`/workflows`)
Step-by-step methodologies combining multiple skills for larger tasks.
- `weekly-pipeline-review.md`: The 30-minute Friday sanity check.
- `outreach-cadence.md`: Designing strategic, multi-touch engagement.
- `meeting-day.md`: The pre/during/post playbook.

### 4. Safety Hooks (`/hooks`)
Scripts that intercept system actions to keep you safe.
- `pre-send-review.py`: Explicitly blocks Claude from autonomously sending outward emails without your final approval.

## Getting Started: Your First Run
Once bootstrapped, open Claude Code and try this prompt to see the system in action:

> "Review my `~/brain/voice-model.md`. Tell me what you understand about my communication style. Then, use the `meeting-prep` skill to build a placeholder brief for a meeting with Acme Corp."

---
*Proprietary Methodology © GetFresh Ventures. All Rights Reserved.*
