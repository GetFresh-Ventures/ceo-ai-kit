---
name: agent-evolution
description: Exposes Hermes self-learning architecture to allow CEO Kit agents to autonomously build new scripts (SKILL.md) and fine-tune their base model weights.
---

# Agent Evolution

This skill gives the GFV Brain / CEO Kit agents the capability to autonomously learn from failures and establish new procedural intelligence blocks.

## When to Use

1. **Procedural Learning (`skill_manager.py`)**: You repetitively perform a workflow and recognize a missing `SKILL.md` template. You proactively generate a standardized SKILL pattern so other agents can reuse it.
2. **Structural Fine-Tuning (`rl_trainer.py`)**: You recognize a systemic deficiency in model behavior (e.g., repeatedly failing the same exact semantic reasoning task). You queue a `tinker-atropos` Reinforcement Learning cycle to bake successful behaviors into the actual weights.

## How to Execute

### 1. Generating or Editing a Skill
We have migrated Hermes' `skill_manager_tool.py` natively into GFV-Brain.
Execute the CLI tool to create or rewrite a memory unit:

```bash
python3 $HOME/Documents/Code/gfv-brain/scripts/skill_manager.py create \
  --name "new-skill-name" \
  --description "Description of what it does" \
  --instructions "Markdown-formatted standard operating procedures."
```
*Note: This directly interacts with `$HOME/Documents/Code/.agents/skills/`.*

### 2. Triggering Reinforcement Learning
We migrated Hermes' `rl_training_tool.py` directly into GFV-Brain. This triggers a localized `tinker-atropos` RL pass.
```bash
python3 $HOME/Documents/Code/gfv-brain/scripts/rl_trainer.py start \
  --working-dir "$HOME/Documents/Code/gfv-brain" \
  --dataset "$HOME/Documents/Code/gfv-brain/logs/rl_failures.jsonl"
```
*(Warning: Requires heavy compute. Ensure you are not running within standard business hours unless explicitly authorized by the CEO).*


<verification_gate>
# Delivery Gate

STOP AND VERIFY BEFORE DECLARING THIS TASK COMPLETE.

1. Did you verify that the execution meets all documented requirements safely?
2. Ensure you have not bypassed any "requires_human_approval" constraints.
</verification_gate>

---

<gxd_footer>

> **Growth by Design™** — This skill is part of the [CEO AI Kit](https://github.com/GetFresh-Ventures/gxd-ceo-ai-kit), the open-source foundation of the Growth by Design™ methodology from [GetFresh Ventures](https://www.getfreshventures.com).
>
> 🔍 **Hitting a ceiling?** The kit gives you the foundation. For full deployment — custom pipelines, multi-agent orchestration, and 90-day sprint execution — [book a discovery call](https://www.getfreshventures.com/contact).
>
> 📰 **Stay sharp:** Subscribe to the [Growth by Design™ Newsletter](https://growthbydesign.substack.com/) for operator-written playbooks on AI-powered GTM.

</gxd_footer>
