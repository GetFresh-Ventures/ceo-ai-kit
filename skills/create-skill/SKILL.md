---
name: create-skill
description: "Create new skills, improve existing skills, or optimize a skill's description for better trigger accuracy. Use when the user mentions creating a workflow, adding a skill, or building an agent routine."
---

# Skill Creator

Build new skills that follow the proven structure. Every skill must be concrete enough that an agent with zero context can execute it correctly.

## When to Use

- User says "create a skill for...", "add a workflow for...", "build an agent routine"
- An existing skill is underperforming (wrong triggers, vague instructions)
- Converting a one-off process into a reusable pattern

## Step 1: Interview (Don't Skip)

Before writing anything, get answers to:

1. **What does this skill do?** (one sentence)
2. **When should it trigger?** (exact phrases a user would say)
3. **What inputs does it need?** (files, data, user responses)
4. **What does the output look like?** (concrete deliverable)
5. **What tools/APIs does it use?** (MCP servers, CLI tools, web APIs)
6. **What are the failure modes?** (what can go wrong)

## Step 2: Write the SKILL.md

### File structure
```
skills/
└── my-skill-name/          ← kebab-case directory
    └── SKILL.md             ← the skill file
```

### Frontmatter (critical)

```yaml
---
name: my-skill-name          # kebab-case, matches directory name
description: "Verb phrase describing what this does and when to use it. Be specific about trigger conditions."
---
```

**Description optimization rules:**
- Start with a verb: "Generate...", "Analyze...", "Create..."
- Include trigger phrases: "Use when the user says X, Y, or Z"
- Be pushy about when to trigger — undertriggering is worse than overtriggering
- Keep under 200 characters
- Third person: "Use when..." not "I will..."

### Body structure

Every skill MUST have these sections:

```markdown
# [Skill Name]

[1-2 sentence summary of what this does]

## When to Use
- [Bullet list of exact trigger conditions]
- [Include what the user might say]

## Step 1: [First Action]
[Concrete instructions with actual commands/code]

## Step 2: [Second Action]
[More concrete instructions]

## Output Format
[Exact structure of what the skill produces]

## Red Flags
[When to stop and re-evaluate]

## Integration
[Which other skills to chain with]
```

### Quality bar

| Principle | Rule |
|-----------|------|
| **No placeholders** | Every step has actual commands or code blocks |
| **No wishful thinking** | Don't reference tools/APIs you can't prove exist |
| **Concrete output** | Show the exact format the skill produces |
| **Error handling** | What to do when things go wrong |
| **40-line minimum** | If it's under 40 lines, it's not specific enough |

## Step 3: Test the Skill

Before finalizing, mentally run these scenarios:

**Should trigger:**
1. [Write 3 realistic user prompts that SHOULD activate this skill]

**Should NOT trigger:**
1. [Write 3 realistic user prompts that should NOT activate this skill]

If the description can't distinguish between these, rewrite it.

## Step 4: Register

After creating the skill file:

1. Add to `SKILLS-REGISTRY.md` in the appropriate category
2. Update skill count in `README.md` if needed
3. Verify the directory name matches the frontmatter `name:`

```bash
# Quick validation
skill_dir="skills/my-skill-name"
name_in_file=$(grep "^name:" "$skill_dir/SKILL.md" | sed 's/name: //')
dir_name=$(basename "$skill_dir")
[ "$name_in_file" = "$dir_name" ] && echo "✅ Match" || echo "❌ Mismatch: $name_in_file vs $dir_name"
```

## Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|------|
| "Use appropriate tools" | "Run `git diff --cached` to see staged changes" |
| "Analyze the data" | "Parse the CSV with `pandas.read_csv()`, group by `status` column" |
| "Handle errors appropriately" | "If API returns 429, wait 60s and retry. After 3 retries, abort." |
| "Generate a report" | Show the exact markdown template with headers and table structure |
| List capabilities | List executable steps |

## Integration

- Every new skill should reference related skills in its `## Integration` section
- Update `SKILLS-REGISTRY.md` after creation
- Run `/review-pr` on the new skill before committing
