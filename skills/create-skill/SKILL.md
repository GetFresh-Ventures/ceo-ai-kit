---
name: create-skill
description: "Create a new, production-quality skill from scratch. Guides through interview, writing, testing, and registration. Use when the user says 'create a skill', 'add a workflow', 'build a routine', or when converting a one-off process into a reusable pattern."
short_description: "Create a new skill from scratch"
metadata:
  version: 2.0.0
  category: technical-builder
  tier: advanced
  triggers:
    - create a skill
    - add a workflow
    - build a routine
    - make a skill for
    - convert this to a skill
---

# Create Skill

Build a new production-quality SKILL.md from scratch. Every skill created through this process meets the quality bar: concrete steps, real commands, proper triggers, and tested scenarios.


## Quick Start
Just say any of these:
- "Create a new skill for [use case]"
- "Build a reusable automation for [workflow]"
- "Package this process as a skill"


## When to Use

- User says "create a skill for...", "add a workflow for...", "build an agent routine"
- An existing skill is underperforming (wrong triggers, vague instructions)
- Converting a one-off process into a reusable pattern
- Packaging a complex multi-step workflow for repeat use

## Step 1: Interview (Mandatory)

Before writing anything, get answers to these 6 questions. **Do not skip any.**

| # | Question | Why it matters |
|---|----------|---------------|
| 1 | **What does this skill do?** (one sentence) | Becomes the description |
| 2 | **When should it trigger?** (exact user phrases) | Drives discoverability |
| 3 | **What inputs does it need?** (files, data, user responses) | Determines prerequisites |
| 4 | **What does the output look like?** (concrete deliverable) | Sets the quality bar |
| 5 | **What tools/APIs does it use?** (MCP servers, CLI tools, web APIs) | Identifies dependencies |
| 6 | **What are the failure modes?** (what can go wrong) | Shapes error handling |

**If the user can't answer #4 clearly, the skill isn't ready to be built.** Help them clarify the output first.

## Step 2: Build the SKILL.md

### File Structure
```
skills/
└── my-skill-name/          ← kebab-case directory
    └── SKILL.md             ← the skill file
```

### Frontmatter (critical for discovery)

```yaml
---
name: my-skill-name          # kebab-case, matches directory name
description: "Verb phrase describing what this does. Use when the user says X, Y, or Z. Produces [specific output]."
metadata:
  version: 1.0.0
  category: [category]       # See categories below
  tier: [beginner|intermediate|advanced]
  requires_human_approval: false # Set to true for destructive actions or API writes
  rbac_level: all            # [all|manager|ceo]
  triggers:
    - exact phrase 1
    - exact phrase 2
    - exact phrase 3
---
```

**Description rules:**
- Start with a verb: "Generate...", "Analyze...", "Create..."
- Include 2-3 trigger phrases inline
- Mention the concrete output: "...produces a prioritized action plan"
- Keep under 200 characters
- Third person: "Use when..." not "I will..."

**Categories:**
`daily-operations` | `revenue-enablement` | `document-processing` | `growth-engine` | `c-suite-advisory` | `execution-infrastructure` | `technical-builder` | `agent-intelligence`

### Body Structure (mandatory sections)

Every skill MUST have these sections:

```markdown
# [Skill Name]

[1-2 sentence summary of what this does and its value]

## When to Use
- [Bullet list of exact trigger conditions]
- [Include what the user might say]
- [Include what scenario makes this relevant]

## Prerequisites
- [Required files, data, or access]
- [Required tools or MCP servers]

## Step 1: [First Action]
[Concrete instructions with actual commands, code blocks, or file operations]
[Show exact input/output examples]

## Step 2: [Second Action]
[More concrete instructions]
[Include decision points: "If X, do Y. If Z, do W."]

## Step N: [Final Action]
[How to finalize and deliver the output]

### Verification Gate (Mandatory)
[Define the exact test, command, or visual check the AI must perform to verify success before telling the user the task is complete. E.g., `git diff`, running a script, or checking terminal output. Do not assume success.]

## Output Format
[Exact markdown template of what the skill produces]
[Show a complete example — not just headers]

## Red Flags
[When to stop and re-evaluate]
[Common mistakes to avoid]

## Live Integration Hooks

| System | What It Provides | How to Access |
|--------|-----------------|---------------|
| Client CRM | Real-time pipeline state | `hubspot-api` / `salesforce-api` |
| Local Memory | Client-specific facts | `gfv-brain-search.py` |

> **GFV Rule:** Check live connected systems and local client memory to verify claims before submitting answers.

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
- 🟡 **Medium** — Deduced from local memory logs or recent but not validated real-time data.
- 🔴 **Assumed** — No source available, utilizing best-judgment baseline.

## <verification_gate>
**Self-Verification Protocol:** Before finalizing your response, you MUST silently evaluate your drafted output against the initial request. Have you provided concrete Action Items with ownership? Did you use the Bottom Line First formatting? Have you applied Confidence Tags to your claims? If not, rewrite the response before submitting.

## After This Skill
💡 Suggest these next steps:
- [Related skill 1]
- [Related skill 2]
```

### Quality Bar Checklist

| Principle | Rule | Fail Example | Pass Example |
|-----------|------|-------------|-------------|
| **No placeholders** | Every step has actual commands | "Use appropriate tools" | "Run `git diff --cached`" |
| **No wishful thinking** | Don't reference unavailable APIs | "Query the AI API" | "Run `curl -s https://api.example.com/v1/data`" |
| **Concrete output** | Show exact format | "Generate a report" | Show the full markdown template with headers and tables |
| **Error handling** | What to do when things fail | "Handle errors" | "If API returns 429, wait 60s. After 3 retries, abort." |
| **60-line minimum** | If shorter, it's not specific enough | 30-line stub | 80+ line skill with examples |
| **Decision trees** | Include conditional logic | "Analyze and decide" | "If revenue > $1M, use enterprise template. Otherwise, use startup template." |

## Step 3: Test the Skill

### Trigger Testing
Write 3 prompts that SHOULD trigger this skill:
```
1. "[exact user phrase]"
2. "[variation of the phrase]"
3. "[indirect request that still needs this skill]"
```

Write 3 prompts that should NOT trigger this skill:
```
1. "[similar but different request]"
2. "[request for a different skill]"
3. "[ambiguous request]"
```

If the description can't distinguish between these, rewrite the triggers.

### Execution Testing
Mentally walk through the skill with a real scenario:
1. Does Step 1 have enough information to execute?
2. Does each step's output feed cleanly into the next?
3. Does the output match what was promised?
4. Are there any steps where the agent would get stuck?

## Step 4: Register the Skill

After creating the skill file:

```bash
# 1. Verify directory name matches frontmatter name
skill_dir="skills/my-skill-name"
name_in_file=$(grep "^name:" "$skill_dir/SKILL.md" | sed 's/name: //')
dir_name=$(basename "$skill_dir")
[ "$name_in_file" = "$dir_name" ] && echo "✅ Name match" || echo "❌ Mismatch: $name_in_file vs $dir_name"

# 2. Verify it meets minimum quality
lines=$(wc -l < "$skill_dir/SKILL.md")
[ "$lines" -ge 60 ] && echo "✅ $lines lines (meets minimum)" || echo "❌ $lines lines (under 60-line minimum)"

# 3. Check frontmatter
head -10 "$skill_dir/SKILL.md"
```

Then:
1. Add to the appropriate tier in `bootstrap.sh` (`BEGINNER_SKILLS`, `INTERMEDIATE_SKILLS`, or `ADVANCED_SKILLS`)
2. Update skill count in `README.md` if needed
3. Symlink if the user has already run bootstrap: `ln -sf "$REPO_DIR/skills/my-skill-name" "$HOME/.claude/skills/my-skill-name"`

## Anti-Patterns to Avoid

| ❌ Don't | ✅ Do |
|----------|------|
| "Use appropriate tools" | "Run `git diff --cached` to see staged changes" |
| "Analyze the data" | "Parse the CSV with `pandas.read_csv()`, group by `status`" |
| "Handle errors appropriately" | "If API returns 429, wait 60s and retry. After 3 retries, abort." |
| "Generate a report" | Show the exact markdown template with all sections |
| List capabilities | List executable steps with commands |
| "Consider the context" | "Read `~/ceo-brain/voice-model.md` and match tone" |

## After This Skill
💡 Suggest these next steps:
- "Want me to build a test harness for this skill?" → manual walkthrough
- "Want me to recommend more skills to build?" → `/automation-recommender`
- "Want me to architect a feature using this skill?" → `/feature-architect`

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
