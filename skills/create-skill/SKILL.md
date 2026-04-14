---
name: create-skill
description: Create new skills, modify and improve existing skills, and optimize a skill's description for better triggering accuracy. Make sure to use this skill whenever the user mentions creating a new agent routine, adding a workflow, or building a skill.
---

# Skill Creator

A skill for creating new skills and iteratively improving them based on the Anthropic Official Plugins methodology.

## Skill Creation Paradigm

1. **Capture Intent**: Understand what the skill should do, when it should trigger, and expected outputs.
2. **Interview**: Ask about edge cases and dependencies. Don't write yet.
3. **Write the SKILL.md**:
   - Keep the YAML description "pushy" (e.g. "Make sure to use this skill whenever the user mentions X"). 
   - Ensure the description fully encapsulates when to trigger the skill to prevent undertriggering.
4. **Draft Test Cases**: Write a few realistic prompts a user would say and evaluate the outputs.

## Anatomy of a Skill
```
skill-name/
├── SKILL.md (required, keep under 500 lines)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks (e.g. Python CLI)
    ├── references/ - Docs loaded into context as needed
```

## Writing Principles
- **Explain the "Why"**: Don't just use MUST ALWAYS syntax. Explain the theory of mind behind the skill rules so the AI understands the rationale.
- **Leverage Bundled Scripts**: If a skill needs to do heavy mathematical work, data validation, or API fetching, instruct the AI to write a Python script inside `skills/<name>/scripts/` and invoke it via bash, rather than trying to do it natively.
- **Progressive Disclosure**: Keep SKILL.md under 500 lines. Reference markdown files in a `references/` directory if the ruleset is massive.

## Evaluation
Create a test prompt. Run the output. Work with the user to refine the `SKILL.md` until it yields the desired output consistently. If the description is failing to trigger, optimize it with diverse edge cases.
