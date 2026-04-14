# Getting Started — Your First 30 Minutes

**The Executive Enablement Walkthrough**
*For CEOs, founders, and senior leaders using the GetFresh CEO Enablement Kit for AI.*

---

## What You're About to Install

In the next 30 minutes, you will go from "AI is a blank chatbot" to "AI is my Chief of Staff." Here's exactly what happens:

| Step | What | Time | Outcome |
|------|------|------|---------|
| 1 | Clone the kit | 2 min | Kit downloaded to your machine |
| 2 | Run the installer | 5 min | Skills, memory, and hooks wired up |
| 3 | Run the onboarding wizard | 15 min | AI learns your voice, team, and priorities |
| 4 | Your first real task | 5 min | AI delivers immediate value |

**You do NOT need to be technical.** If you can open a terminal window and paste a command, you can do this.

---

## Before You Start

### What You Need
- [ ] A Mac, Linux machine, or Windows PC
- [ ] One of these AI tools installed: **Claude Code**, **Cursor**, or **Gemini**
- [ ] Access to the GetFresh Ventures GitHub organization (ask your GFV contact for an invite)

### What You Should Have Ready
These aren't required, but having them handy will make the onboarding wizard dramatically more useful:
- [ ] 3–5 recent emails you've written (to train your voice model)
- [ ] Your current deal pipeline (the names of your top 5 deals or prospects)
- [ ] Your weekly calendar rhythm (what recurring meetings do you have?)

---

## Step 1: Clone the Kit (2 minutes)

Open your terminal:
- **Mac:** Open the "Terminal" app (search Spotlight for "Terminal")
- **Windows:** Open "PowerShell" (search Start for "PowerShell")

Paste this command and press Enter:

```bash
git clone git@github.com:GetFresh-Ventures/gfv_growth_by_design.git ~/.gfv_growth_by_design
```

> **What just happened?** You downloaded the entire kit to a hidden folder on your machine. Your data stays local — nothing is uploaded to the cloud.

---

## Step 2: Run the Installer (5 minutes)

Navigate to the kit and run the bootstrap script:

**Mac / Linux:**
```bash
cd ~/.gfv_growth_by_design
./bootstrap.sh
```

**Windows:**
```powershell
cd ~\.gfv_growth_by_design
.\bootstrap.ps1
```

The installer will ask you one question: whether to install the EngineClaw autonomous runtime (for advanced users who want background AI workers). **If you're unsure, choose "N"** — you can always add it later.

### What the Installer Does

Behind the scenes, the installer:

1. **Creates your Dual-Brain system:**
   - `~/ceo-brain/` — Your personal identity: voice model, meeting prep, weekly notes
   - `~/gtm-brain/` — Your business state: pipeline data, campaign performance, learnings

2. **Registers 74 skills** as native `/slash` commands in Claude Code (or reads them automatically in Cursor/Gemini)

3. **Wires lifecycle hooks** so your AI automatically:
   - Loads your context at session start (no "remind me who I am" every time)
   - Saves state at session end (nothing is lost between conversations)
   - Reviews outbound messages before sending (safety gate)

4. **Installs advanced tooling** (ccflare for cost monitoring, Dippy for frictionless approvals)

> ✅ **When you see "Bootstrap Complete!"** you're ready for Step 3.

---

## Step 3: The Onboarding Wizard (15 minutes)

This is where the magic happens. Open your AI assistant and paste this:

```text
1. Read the `AGENT.md` file in the root to internalize the GFV operating boundaries.
2. Ensure you have access to the `/skills/` directory.
3. IMMEDIATELY execute the `/onboard` skill to launch the interactive setup wizard.
```

The AI will begin by asking you a single question: **What is your AI expertise level?**

You will choose your enablement **Tier**:

- **Tier 1: AI Novice** - Keeps things simple. Sets up voice cloning and meeting prep. Skips all the complex CRM/ticketing integrations.
- **Tier 2: AI Practitioner** - Plugs into your business. Wires up your HubSpot, Slack, Linear, and sets up your delegation tracking.
- **Tier 3: AI Orchestrator** - Takes the wheel. Unlocks background autonomous workers (EngineClaw), multi-agent swarm dispatching, and zero-prompt automation.

Depending on your Tier, the AI will walk you through the corresponding phases:

### Phase 1 & 2: Ecosystem & Delegation Map (Tiers 2 & 3)
The AI asks which CRMs and ticket tools you use (HubSpot, Salesforce, etc.) and maps your organizational chart so it knows who owns what when delegating action items.

### Phase 3: Voice Calibration (All Tiers)
Paste a link to your LinkedIn or an email you wrote. The AI analyzes your writing patterns and builds a `voice-model.md` that ensures all future communications sound authentically like you.

### Phase 4: Autonomous Orchestration (Tier 3 Only)
The AI hooks into the `openclaw-orchestrator` process, giving you explicit warnings and securing authorization to run background python worker nodes for true autonomy.

> 💡 **Tip:** Be honest and specific during onboarding. The more context you give, the more leverage you get from every future interaction.

---

### Escalate Your Tier Anytime via Chat
You do not need to choose Tier 3 on your first day. 

If you start at Tier 1, **you can re-run the wizard at any time straight from the chat interface.** Simply type `/onboard` or `/setup` into your Claude Code, Cursor, or Gemini terminal, and the wizard will restart, allowing you to update your tier as your capability grows.

---

## Step 4: Your First Real Task (5 minutes)

Now that you're set up, try one of these high-impact first tasks:

### Option A: Pre-Meeting Intelligence Brief
> *"I have a meeting with [Name] from [Company] tomorrow. Run meeting-prep."*

The AI will research the person, pull any CRM history, and build you a 1-page dossier with talking points and your strategic angle.

### Option B: Pipeline Sanity Check
> *"Run pipeline-pulse. Be brutally honest about what's stale."*

The AI reviews your active deals, flags anything with no activity in 14+ days, and drafts follow-up actions for each.

### Option C: Write an Email in Your Voice
> *"Draft an email to [Name] at [Company] about [topic]. Use my voice model."*

The AI writes using your actual communication style — not generic AI speak.

### Option D: Prep Your Week
> *"Run weekly-ceo-brief. What should I focus on this week?"*

The AI synthesizes your pipeline, recent meetings, and outstanding commitments into a scannable executive brief.

---

## Understanding Your Skill Library

You now have access to **74 pre-built skills** organized into 8 categories. You don't need to memorize them — just describe what you need and the AI will route to the right skill automatically.

### Most-Used Skills for Executives

| When You Need... | Say This | Skill Used |
|-------------------|----------|------------|
| Meeting prep | "Prep me for my call with [Name]" | `meeting-prep` |
| Process meeting notes | "Here are my notes from [call]" | `post-meeting-brief` |
| Pipeline review | "What's closing this month?" | `pipeline-pulse` |
| Write an email | "Draft an email to [Name]" | `email-composer` |
| Weekly synthesis | "What mattered this week?" | `weekly-ceo-brief` |
| Strategic advice | "Should I [decision]?" | `chief-of-staff` → routes to advisors |
| Deal evaluation | "Is this deal real?" | `deal-review` |
| Risk analysis | "What if [scenario]?" | `scenario-war-room` |
| Outreach campaign | "Build a sequence for [prospect]" | `outreach-sequence` |

### The Full Category Map

| Category | Skills | Examples |
|----------|--------|----------|
| 🎯 Execution Infrastructure | 11 | chief-of-staff, decision-logger, verify-execution |
| 👔 C-Suite Advisory | 8 | ceo-advisor, cfo-advisor, cmo-advisor, founder-coach |
| 💰 Revenue Enablement | 10 | deal-review, pipeline-pulse, outreach-sequence |
| 📄 Document Processing | 6 | contract-reader, board-deck-builder, google-doc-creation |
| 📅 Daily Operations | 8 | email-composer, meeting-prep, weekly-ceo-brief |
| 🚀 Growth Engine | 13 | copy-master, aeo-optimizer, seo-growth, social-scheduler |
| 🛠 Technical / Builder | 10 | create-prd, analyze-issue, feature-architect |
| 🤖 Agent Intelligence | 5 | openclaw-orchestrator, consensus-reconciler, agent-spawner |
| 🔒 Safety & Automation | 3 | hook-automation, security-pii-scanner, skill-builder |

---

## Safety Guarantees

This kit is designed with executive-grade safety controls built in:

### 📧 No Autonomous Sending
The AI will **never** send an email, Slack message, or any communication without showing you the full draft and getting your explicit "send it" approval. It always drafts first.

### 🔒 Local-First Data
Your voice model, pipeline data, and meeting prep live on YOUR machine in `~/ceo-brain` and `~/gtm-brain`. They are not uploaded to any cloud service.

### ✅ Source Verification
The AI verifies claims against live data sources (CRM, calendar, etc.) before asserting facts about your pipeline. It doesn't guess — it checks.

### 🛡 Credential Security
All API keys and tokens are stored in your system's secure credential manager (macOS Keychain / Windows Credential Manager). Nothing is hardcoded in files.

---

## Recurring Rhythms — Building the Habit

The real ROI comes from consistent weekly use. Here's the recommended cadence:

### Monday Morning (5 min)
> *"Run weekly-ceo-brief. What are my priorities this week?"*

### Before Each Meeting (2 min)
> *"Prep me for my [time] meeting with [Name]."*

### After Each Meeting (3 min)
> *"Process these notes from my call with [Company]: [paste notes]"*

### Friday Afternoon (5 min)
> *"Run pipeline-pulse. What moved this week? What's stuck?"*

### Sunday Night (Optional, 2 min)
> *"Run the dream consolidation to compress this week's learnings."*

---

## Troubleshooting

### "The AI doesn't know who I am"
Run the onboarding wizard again straight from chat: type `/onboard` or `/setup`. Or check that `~/ceo-brain/voice-model.md` exists and has content.

### "The AI sounds generic"
Your voice model needs more samples. Paste 3–5 more emails and say: *"Update my voice model with these samples."*

### "I can't clone the repo"
You need an SSH key connected to your GitHub account AND access to the GetFresh-Ventures organization. Ask your GFV contact to add you.

### "The installer failed on Windows"
Make sure you're running PowerShell as Administrator. Use `.\bootstrap.ps1` (not `./bootstrap.sh`).

### "How do I update to the latest version?"
```bash
cd ~/.gfv_growth_by_design
git pull
./bootstrap.sh
```
The installer is idempotent — it only adds what's missing, never overwrites your data.

---

## What's Next?

Once you're comfortable with the basics, explore these power moves:

1. **Build Your Voice Model** — Read `guides/voice-model-guide.md` for advanced voice calibration
2. **Master Executive Prompting** — Read `guides/prompting-for-executives.md` for high-payoff prompt patterns
3. **CEO Mindset** — Read `guides/ceo-mindset.md` for the mental model shift that unlocks 10x AI leverage
4. **Extend the Kit** — Create custom skills specific to your business using the `skill-builder` meta-skill

---

*Version 1.18.0 — April 2026*
*Proprietary Methodology © GetFresh Ventures. All Rights Reserved.*
