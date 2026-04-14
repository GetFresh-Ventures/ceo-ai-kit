---
name: context-prime
description: Systematically scan the repository, read README and core architecture files, and build baseline context before starting work. Excellent for Monday mornings or entering new repositories.
---

# Context Prime Skill

When the user types `/context-prime`, your sole objective is to ingest the maximum amount of architectural and situational context about the current working directory so you can act as a fully informed engineering partner.

## Execution Sequence

1. **Repository Structure:**
   - Use your `list_dir` tool (or equivalent workspace reading tool) to understand the top-level directory structure.
   - Ignore `node_modules`, `.git`, `venv`, and compiled output folders.

2. **Core Documentation:**
   - Identify and read `README.md`, `CLAUDE.md`, `AGENT.md`, or `.cursorrules`.
   - Read any configuration files that define the stack (e.g., `package.json`, `requirements.txt`, `docker-compose.yml`, `go.mod`).

3. **Key Source Exploration:**
   - Identify the entry point of the application (e.g., `src/index.js`, `main.py`, `app.go`, `App.tsx`).
   - Use your file viewing tools to read the entry point and understand how the app bootstraps.

4. **Output Synthesis:**
   Generate a brief "Startup Diagnostics" report summarizing:
   - **Tech Stack Detected:** (e.g., Next.js with Tailwind and tRPC).
   - **Operational Directives:** Any strict rules found in `AGENT.md` or `.cursorrules`.
   - **Entry Point:** Where the application boots.
   - **Ready State:** "Context Primed. I am ready to begin. What is our first objective?"
