---
name: analyze-issue
description: Analyze a GitHub or Linear issue and generate a step-by-step implementation plan without writing code yet.
---

# Analyze Issue Skill

When the user runs this skill by typing `/analyze-issue <issue_url_or_id>`, you must follow these exact instructions to map out a solution without writing production code.

## 1. Fetch Context
- Use your web or API integration tools to read the content of the provided issue URL or ID.
- Extract the core problem, expected behavior, and any constraints mentioned.

## 2. Research Codebase
- Search the local repository using `grep_search` or `run_command` for relevant files, functions, and architectural patterns.
- Identify where the changes need to be made and trace dependencies to ensure no breaking side-effects.

## 3. Generate Implementation Plan
Create a highly structured markdown output (or artifact) detailing the plan:
1. **Summary of the Issue:** 1-2 sentence breakdown.
2. **Root Cause Analysis:** Why is the current behavior happening?
3. **Proposed Changes:** Grouped by file. List exact file paths.
4. **Step-by-Step Execution Plan:** A checklist of actions to be taken.
5. **Testing & Verification:** How will we ensure this works?

**WARNING:** DO NOT write or modify any application code while running this skill. Your only job is to analyze and plan. Wait for the user to approve the plan before proceeding.
